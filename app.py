from flask import Flask, send_from_directory, request, jsonify, render_template_string
import os
import json
import re

app = Flask(__name__, static_folder='.')

# ── Engine bootstrap (lazy, singleton) ───────────────────────────────────────
_engine_ready = False

def bootstrap_engine():
    global _engine_ready
    if _engine_ready:
        return
    try:
        from clinical_engine import SymptomLibrary
        SymptomLibrary.initialize_engine()
        _engine_ready = True
        print("[BrainBuddy] Engine initialized OK")
    except Exception as e:
        print(f"[BrainBuddy] Engine init error: {e}")

# ── Data files ────────────────────────────────────────────────────────────────
def load_json(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

CONDITION_BILLING    = load_json('data/condition_billing.json')
CONDITION_MEDS       = load_json('data/condition_medications.json')

# ── ROS mapping ───────────────────────────────────────────────────────────────
ROS_MAP = {
    "constitutional": ["fever", "chills", "sweats", "fatigue", "malaise", "weakness", "weight loss"],
    "eyes":           ["eye pain", "blurred vision", "vision loss", "photophobia", "redness", "red eye"],
    "ent":            ["sore throat", "nasal congestion", "ear pain", "hearing loss", "nasal discharge",
                       "throat pain", "earache", "runny nose", "rhinorrhea"],
    "respiratory":    ["cough", "shortness of breath", "wheezing", "dyspnea", "sob"],
    "cv":             ["chest pain", "palpitations", "rapid heart rate", "tachycardia",
                       "arm pain", "diaphoresis", "chest tightness", "chest pressure",
                       "jaw pain", "left arm pain"],
    "gi":             ["nausea", "vomiting", "diarrhea", "abdominal pain", "constipation",
                       "hematemesis", "bloody stool"],
    "musculoskeletal":["myalgia", "joint pain", "back pain", "body aches", "arthralgia"],
    "neurological":   ["headache", "dizziness", "altered mental status", "confusion",
                       "syncope", "facial droop", "slurred speech", "arm weakness",
                       "seizure", "vision loss", "diplopia", "ataxia", "aphasia"],
}

ROS_LABEL_MAP = {
    "constitutional": "CONSTITUTIONAL",
    "eyes":           "EYES",
    "ent":            "ENT",
    "respiratory":    "RESPIRATORY",
    "cv":             "CV",
    "gi":             "GI",
    "musculoskeletal":"MUSCULOSKELETAL",
    "neurological":   "NEUROLOGICAL",
}

# ── Associated symptoms pills ─────────────────────────────────────────────────
ASSOCIATED_SYMPTOMS_OPTIONS = [
    "earache", "facial pain", "fever", "myalgia",
    "pain with head movement", "rash", "wheezing"
]

# ── Symptom display filter — strip SNOMED verbose terms from chips ─────────────
SYMPTOM_DISPLAY_BLOCKLIST = {
    "hyperthermia",          # verbose synonym for fever
    "pain general",          # too vague
    "malaise and fatigue",   # SNOMED verbose
    "body temperature elevated",
    "pyrexia",
    "febrile",
    "discomfort",
    "ill",
    "unwell",
    "general pain",
    "pain symptom",
    "pain finding",
}

def filter_display_symptoms(symptoms: list) -> list:
    """Remove SNOMED noise terms from the chips display list."""
    result = []
    seen_roots = set()
    for s in symptoms:
        sl = s.lower().strip()
        if sl in SYMPTOM_DISPLAY_BLOCKLIST:
            continue
        # Suppress multi-word SNOMED descriptors containing 'finding', 'disorder', 'observation'
        if any(kw in sl for kw in [' finding', ' disorder', ' observation', ' symptom']):
            continue
        result.append(s)
        seen_roots.add(sl)
    return result


# ── ICD-10 overrides for conditions missing from engine's lookup ───────────────
ICD10_OVERRIDES = {
    "influenza":                          "J09.X2",
    "influenza a":                        "J09.X2",
    "influenza b":                        "J10.1",
    "seasonal influenza":                 "J09.X2",
    "uri":                                "J06.9",
    "upper respiratory infection":        "J06.9",
    "viral upper respiratory infection":  "J06.9",
    "pharyngitis":                        "J02.9",
    "sinusitis":                          "J01.90",
    "acute sinusitis":                    "J01.90",
    "allergic rhinitis":                  "J30.9",
    "rhinitis":                           "J30.9",
    "otitis media":                       "H66.90",
    "bronchitis":                         "J20.9",
    "acute bronchitis":                   "J20.9",
    "malaria":                            "B54",
    "sepsis":                             "A41.9",
    "pyelonephritis":                     "N12",
    "malt fever":                         None,   # suppress — SNOMED noise
    "febrile transfusion reaction":       None,   # suppress — SNOMED noise
    "cough with fever":                   None,   # suppress — symptom, not condition
    "chills and fever":                   None,   # suppress — symptom, not condition
    "sepsis":                             None,   # suppress from flu differentials
    "pyelonephritis":                     None,   # suppress from flu differentials
    "malaria":                            None,   # suppress — known SNOMED v3.2.3 noise
    "endocarditis":                       None,   # suppress from flu differentials
    "stemi (heart attack)":              None,   # suppress from flu differentials
    "heart failure (acute)":             None,   # suppress from flu differentials
    "asthma (acute)":                    None,   # suppress from flu differentials
    "copd exacerbation":                 None,   # suppress from flu differentials
    # Stroke
    "stroke":                             "I63.9",
    "stroke / cva":                       "I63.9",
    "cva":                                "I63.9",
    "ischemic stroke":                    "I63.9",
    "hemorrhagic stroke":                 "I61.9",
    "tia":                                "G45.9",
    "transient ischemic attack":          "G45.9",
}

def resolve_icd10(condition_name: str, engine_icd: str) -> str:
    """Return the best ICD-10 for a condition, preferring overrides over engine N/A."""
    key = condition_name.lower().strip()
    if key in ICD10_OVERRIDES:
        override = ICD10_OVERRIDES[key]
        return override  # None means suppress this condition
    if engine_icd and engine_icd != "N/A":
        return engine_icd
    return "N/A"


# ── SNOMED noise 3-pass filter (mirrors diagnosis_engine.py get_er_results) ────
def apply_snomed_filter(diagnoses: list, detected_syms: list) -> list:
    """
    Remove noise diagnoses using the same 3-pass logic as get_er_results().
    diagnoses: list of (name, confidence, icd10, reasoning) tuples
    """
    import re as _re
    _detected_set   = set(s.replace('_', ' ').lower() for s in detected_syms)
    _detected_words = set(w for s in _detected_set for w in s.split())
    _CONNECTORS     = {"of", "the", "and", "or", "in", "at", "with", "joint", "general",
                       "acute", "chronic", "fever", "cough", "pain"}
    _VERBOSE_MARKERS = [
        r'\bdue to\b', r'\bcaused by\b', r'\bco-occurrent\b',
        r'\bassociated with\b', r'\bsecondary to\b', r'\bfollowing\b',
        r'\bresulting from\b',
    ]
    # Explicit block list for demo-visible SNOMED noise
    _BLOCKED = {
        "malt fever", "febrile transfusion reaction",
        "cough with fever", "chills and fever",
        "hyperthermia", "pain general",
    }

    def _is_blocked(c):         return c[0].lower() in _BLOCKED
    def _is_suppressed(c):      return ICD10_OVERRIDES.get(c[0].lower()) is None and c[0].lower() in ICD10_OVERRIDES
    def _is_symptom_leak(c):
        name = c[0].lower(); icd = c[2]
        if name in _detected_set: return True
        if icd in ("N/A", "", None):
            meaningful = set(name.split()) - _CONNECTORS
            if meaningful and meaningful.issubset(_detected_words | _CONNECTORS):
                return True
        return False
    def _is_verbose_snomed(c):
        name = c[0].lower(); icd = c[2]
        if any(_re.search(p, name) for p in _VERBOSE_MARKERS):
            return True
        if len(name.split()) > 5 and icd in ("N/A", "", None):
            return True
        return False

    filtered = [c for c in diagnoses
                if not _is_blocked(c)
                and not _is_suppressed(c)
                and not _is_symptom_leak(c)
                and not _is_verbose_snomed(c)]

    # Dedup case variants — prefer entry with valid ICD-10
    seen = {}; deduped = []
    for c in filtered:
        key = c[0].lower()
        if key not in seen:
            seen[key] = len(deduped)
            deduped.append(c)
        else:
            idx = seen[key]
            if deduped[idx][2] in ("N/A", "", None) and c[2] not in ("N/A", "", None):
                deduped[idx] = c
    return deduped


# ── Flu-keyword boost — raise Influenza above Pneumonia when HPI says "flu" ────
FLU_KEYWORDS = [
    "flu", "flu like", "flu-like", "influenza", "influenza-like",
    "flu like symptoms", "body aches", "myalgia",
]

def apply_flu_boost(diagnoses: list, raw_text: str) -> list:
    """
    If the raw text contains flu-indicator language, boost Influenza's score
    above Pneumonia. Returns re-sorted list.
    """
    text_lower = raw_text.lower()
    flu_match = any(kw in text_lower for kw in FLU_KEYWORDS)
    if not flu_match:
        return diagnoses

    boosted = []
    for c in diagnoses:
        name_lower = c[0].lower()
        if "influenza" in name_lower:
            # Boost by 12 percentage points — enough to clear Pneumonia
            boosted.append((c[0], min(99, c[1] + 12), c[2], c[3] if len(c) > 3 else ""))
        elif "pneumonia" in name_lower and any(k in text_lower for k in ["flu", "influenza", "flu like"]):
            # Slightly suppress Pneumonia when flu presentation is explicit
            boosted.append((c[0], max(0, c[1] - 5), c[2], c[3] if len(c) > 3 else ""))
        else:
            boosted.append(c)
    boosted.sort(key=lambda x: x[1], reverse=True)
    return boosted


# ── Workup mapping per condition ──────────────────────────────────────────────
WORKUP_MAP = {
    "Influenza":           ["Rapid Influenza Test", "COVID-19 PCR", "CBC with differential", "BMP"],
    "COVID-19":            ["COVID-19 PCR", "Rapid COVID Antigen", "CBC with differential", "CRP", "Chest X-Ray"],
    "URI":                 ["Rapid Strep Test", "CBC", "Throat Culture"],
    "Pharyngitis":         ["Rapid Strep Test", "Monospot", "Throat Culture", "CBC"],
    "Sinusitis":           ["CT Sinus (if chronic)", "CBC", "Culture of Nasal Discharge"],
    "Pneumonia":           ["Chest X-Ray", "CBC with differential", "BMP", "Blood Cultures", "Procalcitonin"],
    "Asthma Exacerbation": ["Peak Flow Meter", "Chest X-Ray", "ABG", "CBC"],
    "Sepsis":              ["Blood Cultures × 2", "CBC with differential", "BMP", "Lactate", "UA", "Procalcitonin"],
    "Appendicitis":        ["CT Abdomen/Pelvis with contrast", "CBC with differential", "BMP", "UA"],
    "Chest Pain":          ["ECG", "Troponin", "CXR", "BMP", "CBC"],
    "UTI":                 ["Urinalysis", "Urine Culture", "CBC", "BMP"],
}

FALLBACK_WORKUP = ["CBC with differential", "BMP", "UA", "Chest X-Ray"]

# ── Impression symptom ICD-10 ─────────────────────────────────────────────────
SYMPTOM_ICD = {
    "fever":             ("FEVER", "R50.9"),
    "cough":             ("ACUTE COUGH", "R05.11"),
    "myalgia":           ("MYALGIA", "M79.3"),
    "nausea":            ("NAUSEA", "R11.0"),
    "vomiting":          ("NAUSEA WITH VOMITING", "R11.2"),
    "headache":          ("HEADACHE", "R51.9"),
    "shortness of breath": ("SHORTNESS OF BREATH", "R06.09"),
    "chest pain":        ("CHEST PAIN", "R07.9"),
    "sore throat":       ("SORE THROAT", "J02.9"),
    "nasal congestion":  ("NASAL CONGESTION", "R09.81"),
    "dizziness":         ("DIZZINESS", "R42"),
    "abdominal pain":    ("ABDOMINAL PAIN", "R10.9"),
    "diarrhea":          ("DIARRHEA", "R19.7"),
    "back pain":         ("BACK PAIN", "M54.9"),
    "joint pain":        ("JOINT PAIN", "M25.50"),
    "chills":            ("CHILLS", "R68.83"),
    "fatigue":           ("FATIGUE", "R53.83"),
    "rash":              ("RASH", "R21"),
    "ear pain":          ("OTALGIA", "H92.09"),
    "dysuria":           ("DYSURIA", "R30.0"),
    "wheezing":          ("WHEEZING", "R06.2"),
}

# ─────────────────────────────────────────────────────────────────────────────
# Helper: build medication list from condition_medications.json
# ─────────────────────────────────────────────────────────────────────────────
def get_medications_for_condition(condition_name: str) -> list:
    """Return a list of medication dicts for a given condition."""
    meds_raw = []

    # Try exact match first, then fuzzy
    name_lower = condition_name.lower()
    for key, val in CONDITION_MEDS.items():
        if key.lower() == name_lower:
            meds_raw = val
            break
    if not meds_raw:
        for key, val in CONDITION_MEDS.items():
            if key.lower() in name_lower or name_lower in key.lower():
                meds_raw = val
                break

    result = []
    for m in meds_raw[:4]:
        if isinstance(m, dict):
            result.append({
                "name":      m.get("name", m.get("drug", str(m))),
                "dose":      m.get("dose", m.get("dosage", "")),
                "route":     m.get("route", "PO"),
                "frequency": m.get("frequency", m.get("sig", "")),
            })
        elif isinstance(m, (list, tuple)) and len(m) >= 1:
            result.append({
                "name":      str(m[0]),
                "dose":      str(m[1]) if len(m) > 1 else "",
                "route":     str(m[2]) if len(m) > 2 else "PO",
                "frequency": str(m[3]) if len(m) > 3 else "",
            })
        else:
            result.append({"name": str(m), "dose": "", "route": "PO", "frequency": ""})
    return result


def get_billing_for_condition(condition_name: str) -> dict:
    """Return billing dict {icd10, description} for a condition."""
    name_lower = condition_name.lower()
    for key, val in CONDITION_BILLING.items():
        if key.lower() == name_lower:
            return val
    for key, val in CONDITION_BILLING.items():
        if key.lower() in name_lower or name_lower in key.lower():
            return val
    return {}


def classify_ros(symptoms: list) -> dict:
    """Bucket detected symptoms into ROS systems."""
    ros = {sys: [] for sys in ROS_MAP}
    syms_lower = [s.lower() for s in symptoms]
    for system, keywords in ROS_MAP.items():
        for kw in keywords:
            if kw in syms_lower:
                label = kw.replace("_", " ").title()
                if label not in ros[system]:
                    ros[system].append(label)
    return ros


def build_impression_lines(top_condition, top_icd10, detected_symptoms):
    """Build ICD-10 impression lines."""
    lines = []
    if top_condition:
        lines.append(f"{top_condition.upper()} — {top_icd10}")
    seen = set()
    for sym in detected_symptoms[:4]:
        sym_lower = sym.lower()
        if sym_lower in SYMPTOM_ICD and sym_lower not in seen:
            label, code = SYMPTOM_ICD[sym_lower]
            lines.append(f"{label} — {code}")
            seen.add(sym_lower)
            if len(lines) >= 5:
                break
    return lines


def build_prescriptions(medications: list) -> list:
    """Format prescription strings."""
    lines = []
    for m in medications[:3]:
        name = m.get("name", "")
        dose = m.get("dose", "")
        route = m.get("route", "PO")
        freq = m.get("frequency", "")
        parts = [p for p in [name.upper(), dose, route, freq] if p]
        lines.append(" — ".join(parts) if parts else name.upper())
    return lines


# ─────────────────────────────────────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────────────────────────────────────

CHART_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Physician Chart</title>
<style>
  body { font-family: "Times New Roman", Times, serif; font-size: 11px; color: #000; background: #fff; line-height: 1.8; padding: 40px 60px; max-width: 800px; margin: 0 auto; }
  h1, h2, h3 { margin: 0 0 5px 0; }
  .header { text-align: center; border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 15px; }
  .header-grid { display: grid; grid-template-columns: 1fr 1fr; text-align: left; margin-bottom: 15px; }
  .chart-title { text-align: center; font-weight: bold; font-size: 14px; margin: 15px 0; border-top: 1px solid #000; border-bottom: 1px solid #000; padding: 5px 0; }
  .section { margin-bottom: 20px; }
  .section-title { font-weight: bold; font-size: 13px; text-transform: uppercase; border-bottom: 1px solid #ccc; margin-top: 24px; margin-bottom: 8px; padding-bottom: 3px; }
  .ros-grid { display: grid; grid-template-columns: 150px 1fr; padding: 5px 0; }
  .ros-label { font-weight: bold; text-transform: uppercase; }
  ul { margin: 0; padding-left: 20px; }
  .print-btn { position: absolute; top: 20px; right: 20px; padding: 5px 15px; cursor: pointer; font-family: sans-serif; }
  .footer { margin-top: 40px; border-top: 1px solid #000; padding-top: 10px; font-size: 10px; text-align: center; color: #555; }
  .pill { border: 1px solid #333; border-radius: 10px; padding: 2px 8px; font-size: 10px; margin: 2px 3px; display: inline-block; }
  .field-row { margin-bottom: 6px; }
  .mdm-row { margin-bottom: 8px; }
  @media print {
    .print-btn { display: none; }
    body { padding: 0; }
  }
</style>
</head>
<body>
  <button class="print-btn" onclick="window.print()">🖨 Print Chart</button>
  
  <div class="header">
    <strong>PRELIMINARY</strong><br>
    EastChase Texas Emergency Center<br>
    1251 Eastchase Parkway, Fort Worth, TX 76120<br>
    (817)566-0285
  </div>

  <div class="header-grid">
    <div>
      Patient: {{ data.patient.name }}<br>
      DOB: {{ data.patient.dob }} &nbsp; {{ data.patient.age }}<br>
      Wt: {{ data.patient.weight }} &nbsp; Ht: {{ data.patient.height }}<br>
      MRN: {{ data.patient.mrn }}
    </div>
    <div style="text-align: right;">
      Arrival Time: {{ data.patient.arrival }}<br><br><br>
      Provider: {{ data.patient.provider }}
    </div>
  </div>

  <div class="chart-title">PHYSICIAN CHART</div>

  <div class="section">
    <div class="section-title">Chief Complaint</div>
    <div>{{ data.chief_complaint }}</div>
  </div>

  <div class="section">
    <div class="section-title">History of Present Illness</div>
    <div>
      <div class="field-row">HISTORY OF PRESENT ILLNESS: &nbsp;&nbsp; {{ data.chief_complaint }}</div>
      <div class="field-row">Assessment time: {{ data.patient.arrival }}</div>
      <div class="field-row">Reviewed: <span class="pill">VS's</span> <span class="pill">SPO2</span> <span class="pill">Nursing/Treatment notes</span> <span class="pill">ALL</span></div>
      <div class="field-row">Timing: DIT___ (or) 2 Days</div>
      <div class="field-row">Quality: Cough: <span class="pill">Nonproductive</span></div>
      <div class="field-row">Severity: Cough <span class="pill">Mild</span> &middot; Shortness of breath <span class="pill">Mild</span> &middot; Sore throat <span class="pill">Mild</span></div>
      <div class="field-row">Context: <span class="pill">Spontaneous onset</span></div>
      <div class="field-row">Symptoms: {% for sym in data.symptoms %}<span class="pill">{{ sym | title }}</span> {% endfor %}</div>
      <div class="field-row">Other history/Staff note: {{ data.hpi_text }}</div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Mode of Arrival</div>
    <div>Walk In &nbsp;&nbsp;&nbsp; Arrived With: <span class="pill">Unaccompanied</span></div>
  </div>

  <div class="section">
    <div class="section-title">Review of Systems</div>
    <div class="ros-grid"><div class="ros-label">Constitutional:</div><div>{{ data.ros_findings.constitutional | join(', ') | title if data.ros_findings.constitutional else 'None' }}</div></div>
    <div class="ros-grid"><div class="ros-label">Eyes:</div><div>None</div></div>
    <div class="ros-grid"><div class="ros-label">ENT:</div><div>{{ data.ros_findings.ent | join(', ') | title if data.ros_findings.ent else 'None' }}</div></div>
    <div class="ros-grid"><div class="ros-label">Respiratory:</div><div>{{ data.ros_findings.respiratory | join(', ') | title if data.ros_findings.respiratory else 'None' }}</div></div>
    <div class="ros-grid"><div class="ros-label">CV:</div><div>{{ data.ros_findings.cv | join(', ') | title if data.ros_findings.cv else 'None' }}</div></div>
    <div class="ros-grid"><div class="ros-label">GI:</div><div>{{ data.ros_findings.gi | join(', ') | title if data.ros_findings.gi else 'None' }}</div></div>
    <div class="ros-grid"><div class="ros-label">Musculoskeletal:</div><div>{{ data.ros_findings.musculoskeletal | join(', ') | title if data.ros_findings.musculoskeletal else 'None' }}</div></div>
    <div class="ros-grid"><div class="ros-label">Neurological:</div><div>{{ data.ros_findings.neurological | join(', ') | title if data.ros_findings.neurological else 'None' }}</div></div>
  </div>

  <div class="section">
    <div class="section-title">Past Medical History</div>
    <div>
      Recent hospitalizations: <span class="pill">No recent hospitalizations</span><br>
      Medical: Systemic: <span class="pill">None</span><br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CV: <span class="pill">HTN</span> &nbsp; Pulmonary: <span class="pill">None</span><br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GI: <span class="pill">GERD</span> &nbsp; MS: <span class="pill">None</span><br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Psych: <span class="pill">Anxiety</span> <span class="pill">Depression</span><br>
      Surgical: <span class="pill">None</span>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Social Determinants</div>
    <div>
      Income/Employment: No Income or Employment Issues<br>
      Housing Status: No Housing Issues<br>
      Food: No Food Issues<br>
      Transportation: No Transportation Issues<br>
      Health Care: Full access to healthcare<br>
      Education: No literacy or language issues<br>
      Community: No Community Issues
    </div>
  </div>

  <div class="section">
    <div class="section-title">Sepsis Screening</div>
    <div>Does the patient have risk factors for infection? <span class="pill">{{ 'Yes' if data.alert and data.alert.title == 'SEPSIS ALERT' else 'No' }}</span></div>
  </div>

  <div class="section">
    <div class="section-title">Impression</div>
    <div>Based on my analysis of the history, physical exam, and data, I believe the most likely impression is:</div>
    <div style="font-weight: bold; margin-top: 5px;">{{ data.top_condition.name }} — {{ data.top_condition.icd10 }} &nbsp;&nbsp; Confidence: {{ data.top_condition.confidence }}%</div>
    <ul style="margin-top: 5px;">
      {% for line in data.impression_lines %}
      <li>{{ line }}</li>
      {% endfor %}
    </ul>
  </div>

  <div class="section">
    <div class="section-title">Diagnostic Considerations</div>
    <div>
      Diagnostic considerations for {{ data.chief_complaint }}:<br>
      <div style="margin-top: 5px;">
        {% for diff in data.differentials %}
        <span class="pill">{{ diff.name }} ({{ diff.icd10 }})</span>
        {% endfor %}
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Recommended Workup</div>
    <ul>
      {% for test in data.recommended_tests %}
      <li>{{ test }}</li>
      {% endfor %}
    </ul>
  </div>

  <div class="section">
    <div class="section-title">Suggested Medications</div>
    <ul>
      {% for med in data.medications %}
      <li>{{ med.name }} {{ med.dose }} {{ med.route }} {{ med.frequency }}</li>
      {% endfor %}
    </ul>
  </div>

  <div class="section">
    <div class="section-title">MDM (Medical Decision Making)</div>
    <div>
      <div class="mdm-row">Problems Addressed:</div>
      <div class="mdm-row">&nbsp;&nbsp;* Chronic disease processes: <span class="pill">None</span></div>
      <div class="mdm-row">&nbsp;&nbsp;* Acute/chronic illness: <span class="pill">{{ data.top_condition.name }}</span> <span class="pill">See Differential Diagnosis</span></div>
      <div class="mdm-row">Reviewed and Analyzed Data:</div>
      <div class="mdm-row">&nbsp;&nbsp;* Independent Historian(s): <span class="pill">None</span></div>
      <div class="mdm-row">&nbsp;&nbsp;* Review of external records: <span class="pill">None</span></div>
      <div class="mdm-row">&nbsp;&nbsp;* Independent study performed on: <span class="pill">Labs</span></div>
      <div class="mdm-row">&nbsp;&nbsp;* Labs: <span class="pill">See Notes in Results</span></div>
      <div class="mdm-row">Risk of Morbidity: <span class="pill">Treatment considered but not performed &mdash; see additional treatments considered</span></div>
      <div class="mdm-row">Disposition Management: Patient Care Management was discussed with <span class="pill">None</span></div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Discharge</div>
    <div>Discharge to: Home</div>
    <div>Condition: Stable</div>
    <div>Instructions given to patient: {{ data.chief_complaint }}</div>
    <div>Follow up: As soon as possible</div>
  </div>

  <div class="section">
    <div class="section-title">Prescriptions</div>
    <ul>
      {% for med in data.medications %}
      <li>{{ med.name }} {{ med.dose }} {{ med.route }} {{ med.frequency }}</li>
      {% endfor %}
    </ul>
  </div>

  <div class="footer">
    Physician Record — Page 1 of 1<br>
    Generated: <span id="gen-date"></span><br>
    ─────────────────────────────────<br>
    <strong>BrainBuddy ER — Clinical Intelligence Engine</strong><br>
    ⚡ This chart was auto-generated from physician notes
    <script>document.getElementById('gen-date').textContent = new Date().toLocaleString();</script>
  </div>
</body>
</html>
"""

@app.route('/chart', methods=['POST'])
def chart():
    import json
    data = json.loads(request.form.get('data', '{}'))
    # Ensure all required keys exist to prevent Jinja undefined errors
    data.setdefault('patient', {})
    data.setdefault('chief_complaint', '')
    data.setdefault('hpi_text', '')
    data.setdefault('symptoms', [])
    data.setdefault('top_condition', {})
    data.setdefault('differentials', [])
    data.setdefault('medications', [])
    data.setdefault('recommended_tests', [])
    data.setdefault('ros_findings', {})
    data.setdefault('impression_lines', [])
    data.setdefault('alert', {})
    return render_template_string(CHART_TEMPLATE, data=data)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/demo')
def demo():
    return send_from_directory('.', 'demo.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)


@app.route('/api/analyze', methods=['POST'])
def analyze():
    bootstrap_engine()

    data = request.get_json(silent=True) or {}
    text = data.get('text', '').strip()

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        from clinical_engine import SymptomLibrary
        from diagnosis_engine import get_diagnoses, get_alert

        detected_symptoms = list(SymptomLibrary.detect_symptoms(text))
        # Strip internal sentinel tokens (e.g. __vitals__, __negated__)
        detected_symptoms = [s for s in detected_symptoms
                             if not (s.startswith('__') and s.endswith('__'))]
        diagnoses_raw     = get_diagnoses(detected_symptoms, raw_text=text)
        alerts            = get_alert(detected_symptoms)

    except Exception as e:
        print(f"[BrainBuddy] Engine error: {e}")
        import traceback; traceback.print_exc()
        return jsonify({"error": str(e)}), 500

    # ── Fix ICD-10 for every diagnosis entry ──────────────────────────────────
    diagnoses_icd = []
    for d in diagnoses_raw:
        name  = d[0]
        conf  = int(d[1])
        icd   = resolve_icd10(name, d[2])
        expl  = d[3] if len(d) > 3 else ""
        if icd is None:          # explicitly suppressed condition
            continue
        diagnoses_icd.append((name, conf, icd, expl))

    # ── Apply SNOMED 3-pass filter ────────────────────────────────────────────
    diagnoses_clean = apply_snomed_filter(diagnoses_icd, detected_symptoms)

    # ── Apply flu keyword boost ───────────────────────────────────────────────
    diagnoses_clean = apply_flu_boost(diagnoses_clean, text)

    # ── Filter display symptoms (chip list) ───────────────────────────────────
    display_symptoms = filter_display_symptoms(detected_symptoms)

    # ── Top condition ─────────────────────────────────────────────────────────
    top_condition = {}
    differentials = []

    if diagnoses_clean:
        top = diagnoses_clean[0]
        top_name       = top[0]
        top_confidence = int(top[1])
        top_icd10      = top[2]
        top_reasoning  = top[3] if len(top) > 3 else ""

        # Build a human-readable reasoning if engine gave none
        if not top_reasoning:
            top_reasoning = f"Matched based on: {', '.join(detected_symptoms[:5])}"

        top_condition = {
            "name":       top_name,
            "icd10":      top_icd10,
            "confidence": top_confidence,
            "reasoning":  top_reasoning,
        }

        differentials = [
            {"name": d[0], "icd10": d[2]}
            for d in diagnoses_clean[1:7]
            if d[2] not in ("N/A", "", None)   # only show diffs with valid ICD-10
        ][:5]

    else:
        top_name  = ""
        top_icd10 = ""

    # ── Medications ───────────────────────────────────────────────────────────
    medications = []
    if top_condition:
        medications = get_medications_for_condition(top_name)

    # ── Workup ────────────────────────────────────────────────────────────────
    recommended_tests = FALLBACK_WORKUP
    for key in WORKUP_MAP:
        if key.lower() in top_name.lower() or top_name.lower() in key.lower():
            recommended_tests = WORKUP_MAP[key]
            break

    # ── ROS — use raw detected_symptoms (all terms, not just display-clean) ────
    ros_findings = classify_ros(detected_symptoms)

    # ── Cardiac inference: inject Chest Pain into CV when top condition is cardiac ─────
    CARDIAC_CONDITIONS = [
        "stemi", "nstemi", "acs", "heart attack", "angina",
        "myocardial infarction", "aortic", "pericarditis", "myocarditis",
    ]
    if top_name and any(c in top_name.lower() for c in CARDIAC_CONDITIONS):
        if "Chest Pain" not in ros_findings.get("cv", []):
            ros_findings.setdefault("cv", []).insert(0, "Chest Pain")

    # ── Stroke/neuro inference: inject Altered Mental Status + Facial Droop ────────
    STROKE_CONDITIONS = ["stroke", "cva", "tia", "transient ischemic"]
    if top_name and any(c in top_name.lower() for c in STROKE_CONDITIONS):
        neuro = ros_findings.setdefault("neurological", [])
        if "Altered Mental Status" not in neuro:
            neuro.insert(0, "Altered Mental Status")
        if "Facial Droop" not in neuro:
            neuro.append("Facial Droop")

    # ── Associated symptoms ──────────────────────────────────────────────────────────
    # Return ALL detected symptoms as the associated list.
    # The JS fillAssocSymptoms() handles:
    #   - matching against the 8 hardcoded EPd pills (highlight existing)
    #   - appending dynamic pills for anything not in the hardcoded set
    associated = [s.title() for s in display_symptoms]

    # ── Impression & Prescriptions ────────────────────────────────────────────
    impression_lines  = build_impression_lines(top_name, top_icd10, detected_symptoms)
    prescriptions     = build_prescriptions(medications)

    # ── Alert ─────────────────────────────────────────────────────────────────
    alert_out = None
    if alerts:
        msg, rx, level = alerts[0]
        alert_out = {"message": msg, "treatment": rx, "level": level}

    return jsonify({
        "symptoms":           display_symptoms,
        "top_condition":      top_condition,
        "differentials":      differentials,
        "recommended_tests":  recommended_tests,
        "medications":        medications,
        "ros_findings":       ros_findings,
        "associated_symptoms": associated,
        "impression_lines":   impression_lines,
        "prescriptions":      prescriptions,
        "alert":              alert_out,
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

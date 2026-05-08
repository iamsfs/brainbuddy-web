import re
import math

# =========================================================
# diagnosis_engine.py — BrainBuddy Diagnosis Intelligence
# Contains: context modifiers, exclusion logic,
#           precision scoring, get_diagnoses(), get_alert()
# Edit this file to tune scoring behaviour.

def filter_workup(tests, top_condition):
    """Surgically remove low-yield tests to maintain physician trust."""
    if "STEMI" in top_condition or "ACS" in top_condition:
        return [
            t for t in tests
            if t not in ["ABG", "D-dimer"]
        ]
    return tests
# =========================================================

from clinical_engine import SymptomLibrary

# === RED FLAG OVERRIDE ===
RED_FLAG_RULES = {
    "Stroke": ["facial droop", "slurred speech", "arm weakness"],
    "STEMI": ["chest pain", "diaphoresis", "shortness of breath", "arm pain"],
    "Pulmonary Embolism": ["shortness of breath", "pleuritic chest pain"],
    "Sepsis": ["fever", "low blood pressure", "altered mental status"],
    "Diabetic Ketoacidosis": ["hyperglycemia signs", "metabolic acidosis"],
}

# === ADVANCED SCORING CONFIG ===
PATTERN_RULES = {
    "ACS": {
        "symptoms": ["chest pain", "diaphoresis", "shortness of breath", "arm pain", "nausea"],
        "boost": 1.5
    },
    "STROKE": {
        "symptoms": ["facial droop", "slurred speech", "unilateral weakness"],
        "boost": 1.7
    },
    "SEPSIS": {
        "symptoms": ["fever", "low blood pressure", "altered mental status", "tachycardia"],
        "boost": 1.6
    }
}
RISK_FACTORS = {
    "age>50": 0.2,
    "diabetes": 0.3,
    "hypertension": 0.2
}
SUPPRESSION_RULES = [
    ("STEMI", "Heartburn / Dyspepsia", 0.3),
    ("Stroke / CVA", "Migraine", 0.4),
    ("Pulmonary Embolism", "Anxiety", 0.3)
]

# === SURGICAL UPGRADES CONFIG ===
DISCRIMINATORS = {
    "Pulmonary Embolism": ["pleuritic", "recent travel", "immobility", "long flight", "postpartum", "surgery", "calf pain"],
    "STEMI (Heart Attack)": ["crushing", "radiating", "diaphoresis", "sweating", "left arm", "jaw pain"],
    "Pericarditis": ["leaning forward", "better when sitting", "worse lying down"],
    "Aortic Dissection": ["tearing", "radiating to back", "back pain", "hypertensive"],
    "Subarachnoid Hemorrhage": ["thunderclap", "worst headache", "worst of life"],
    "Anaphylaxis": ["bee sting", "peanut", "hives", "stridor", "throat tightness"],
    "Meningitis": ["neck stiffness", "photophobia", "stiff neck", "petechiae"],
    "Appendicitis": ["rlq", "rebound", "belly button", "right lower quadrant", "right lower"],
    "Gout": ["big toe", "drinking", "alcohol", "toe"],
    "Biliary Obstruction": ["pale stools", "dark urine", "painless jaundice"],
    "Cauda Equina Syndrome": ["saddle anesthesia", "incontinence", "bowel", "bladder"],
    "Opioid Overdose": ["pinpoint", "heroin", "fentanyl", "unconscious"],
    "Carbon Monoxide Poisoning": ["heater", "family", "winter", "co detector"],
    "Testicular Torsion": ["scrotal", "testicle", "testicular", "cremasteric"],
    "Ruptured Ectopic Pregnancy": ["pregnancy test", "ectopic", "positive pregnancy"],
    "Bowel Obstruction": ["distended", "no bowel movement", "multiple surgeries", "adhesions"],
    "DVT": ["calf pain", "unilateral", "recent surgery"],
    "Supraventricular Tachycardia": ["intermittent", "episodes", "racing", "sudden onset"],
    "Hypoglycemia": ["diabetic", "insulin", "skipped meal", "confusion"],
    "Pancreatitis": ["epigastric", "radiating to back", "alcohol"],
}

EXCLUSIONS = {
    "STEMI (Heart Attack)": ["pleuritic", "tender to touch", "chest wall pain", "lean forward"],
    "Pulmonary Embolism": ["reproducible on palpation", "chest wall pain", "trauma"],
    "Appendicitis": ["diarrhea", "intermittent"],
    "Panic Disorder": ["fever", "low blood pressure", "hypoxia"],
    "Migraine": ["fever", "neck stiffness", "altered mental status"],
}

CONTEXT_ANCHORS = {
    "Pulmonary Embolism": ["postpartum", "recent surgery", "long flight", "travel", "bed rest"],
    "Deep Vein Thrombosis": ["leg swelling", "recent surgery", "long flight"],
    "Septic Shock": ["confusion", "fever", "elderly", "nursing home", "urosepsis"],
    "Diabetic Ketoacidosis": ["diabetic", "type 1", "fruity", "ketones", "metabolic acidosis"],
    "Wernicke's Encephalopathy": ["alcoholic", "etoh", "malnourished"],
    "Aortic Dissection": ["hypertensive", "htn", "marfan"],
    "COPD Exacerbation": ["smoker", "smoking", "oxygen", "cpap", "bipap", "inhaler", "copd history"],
}

CLUSTERS = {
    "cardiac": ["STEMI (Heart Attack)", "NSTEMI / Unstable Angina"],
    "pulmonary": ["Pulmonary Embolism", "Pneumonia"],
    "neuro": ["Stroke / CVA", "TIA"],
    "tss": ["Toxic shock syndrome"],
}


# =========================================================
# CONTEXT PROFILES
# A profile fires when ALL required symptoms are present.
# It then:
#   boost  — multiplies the score of listed diagnoses
#   suppress — multiplies (reduces) the score of listed diagnoses
#   must_include — only these diagnoses are shown
#   min_threshold — override minimum confidence for display
# =========================================================
CONTEXT_PROFILES = [

	# ── PANIC / ANXIETY ──────────────────────────────────────────────
	{
		"name":        "Panic / Anxiety Pattern",
		"requires":    {"anxiety"},
		"also_has":    {"chest pain", "shortness of breath", "numbness", "tremor", "diaphoresis"},
		"min_also":    2,
		"boost":       {"Panic Disorder": 3.0, "Acute Anxiety / Panic Attack": 3.5,
		                "Hyperventilation Syndrome": 2.5},
		"suppress":    {"Asthma (Acute)": 0.3, "Simple Pneumothorax": 0.2,
		                "Tension Pneumothorax": 0.1, "Stimulant Toxicity": 0.4,
		                "STEMI (Heart Attack)": 0.5, "Traumatic Aortic Injury": 0.1,
		                "Rib Fractures": 0.2},
	},

	# ── GERD / REFLUX ────────────────────────────────────────────────
	{
		"name":        "GERD / Reflux Pattern",
		"requires":    {"regurgitation"},
		"also_has":    {"chest pain", "bloating", "abdominal pain", "nausea"},
		"min_also":    1,
		"boost":       {"GERD / Acid Reflux": 4.0, "Gastritis": 2.5,
		                "Peptic Ulcer Disease": 2.0, "Esophageal Spasm": 2.0},
		"suppress":    {"STEMI (Heart Attack)": 0.4, "Pulmonary Embolism": 0.3,
		                "Tension Pneumothorax": 0.2, "Asthma (Acute)": 0.4,
		                "Simple Pneumothorax": 0.3},
	},

	# ── MUSCULOSKELETAL CHEST ────────────────────────────────────────
	{
		"name":        "Musculoskeletal Chest Pattern",
		"requires":    {"chest wall pain"},
		"also_has":    {"chest pain", "back pain", "muscle pain"},
		"min_also":    0,
		"boost":       {"Costochondritis": 3.0, "Musculoskeletal Chest Pain": 3.0,
		                "Rib Fractures": 1.8},
		"suppress":    {"STEMI (Heart Attack)": 0.3, "NSTEMI / Unstable Angina": 0.3,
		                "Pulmonary Embolism": 0.4, "Aortic Dissection": 0.2,
		                "Tension Pneumothorax": 0.3},
	},

	# ── CLASSIC ACS ──────────────────────────────────────────────────
	{
		"name":        "ACS Pattern",
		"requires":    {"chest pain"},
		"also_has":    {"arm pain", "jaw pain", "diaphoresis", "shortness of breath"},
		"min_also":    2,
		"boost":       {"STEMI (Heart Attack)": 2.5, "NSTEMI / Unstable Angina": 2.5,
		                "Cardiogenic Shock": 1.5},
		"suppress":    {"Asthma (Acute)": 0.4, "Panic Disorder": 0.5,
		                "Costochondritis": 0.25, "Musculoskeletal Chest Pain": 0.25},
	},

	# ── PLEURITIC / RESPIRATORY CHEST ────────────────────────────────
	{
		"name":        "Pleuritic Chest Pattern",
		"requires":    {"pleuritic chest pain"},
		"also_has":    {"shortness of breath", "cough", "fever"},
		"min_also":    1,
		"boost":       {"Simple Pneumothorax": 2.5, "Pulmonary Embolism": 2.0,
		                "Pericarditis": 2.5, "Pneumonia": 1.8, "Pleural Effusion": 2.0},
		"suppress":    {"STEMI (Heart Attack)": 0.3, "Panic Disorder": 0.4,
		                "GERD / Acid Reflux": 0.2},
	},

	# ── SEPSIS ───────────────────────────────────────────────────────
	{
		"name":        "Sepsis Pattern",
		"requires":    {"fever"},
		"also_has":    {"low blood pressure", "rapid heart rate", "altered mental status"},
		"min_also":    2,
		"boost":       {"Sepsis": 3.0, "Septic Shock": 3.5, "Urosepsis": 2.0},
		"suppress":    {"Influenza": 0.5, "Panic Disorder": 0.1},
	},

	# ── STROKE ───────────────────────────────────────────────────────
	{
		"name":        "Stroke / TIA Pattern",
		"requires":    {"unilateral_weakness"},
		"also_has":    {"facial_droop", "slurred_speech", "vision change", "aphasia", "dizziness"},
		"min_also":    1,
		"boost":       {"Stroke": 3.5, "TIA": 3.5},
		"suppress":    {"Bell's Palsy": 0.2, "Panic Disorder": 0.1, "Hypoglycemia": 0.5},
	},

	# ── ANKLE TRAUMA ─────────────────────────────────────────────────
	{
		"name":        "Ankle Trauma Pattern",
		"requires":    {"ankle pain"},
		"also_has":    {"swelling", "twisted", "bone pain", "deformity"},
		"min_also":    1,
		"boost":       {"Ankle Sprain": 4.0, "Ankle Fracture": 2.5},
		"suppress":    {"DVT": 0.4, "Cellulitis": 0.3},
	},

	# ── AORTIC DISSECTION ────────────────────────────────────────────
	{
		"name":        "Aortic Dissection Pattern",
		"requires":    {"aortic pain"},
		"also_has":    {"chest pain", "back pain", "arm weakness"},
		"min_also":    1,
		"boost":       {"Aortic Dissection": 4.0, "Ruptured AAA": 3.0,
		                "Traumatic Aortic Injury": 2.0},
		"suppress":    {"Panic Disorder": 0.1, "GERD / Acid Reflux": 0.1},
	},

	# ── DKA ──────────────────────────────────────────────────────────
	{
		"name":        "DKA Metabolic Pattern",
		"requires":    {"hyperglycemia signs"},
		"also_has":    {"fruity breath", "vomiting", "tachypnea", "metabolic acidosis", "abdominal pain"},
		"min_also":    1,
		"boost":       {"Diabetic Ketoacidosis": 5.0, "Hyperosmolar Hyperglycemic State": 2.0},
		"suppress":    {"Asthma (Acute)": 0.3, "Panic Disorder": 0.2, "STEMI (Heart Attack)": 0.4},
	},

	# ── MENINGITIS ───────────────────────────────────────────────────
	{
		"name":        "Meningitis Pattern",
		"requires":    {"fever", "neck stiffness"},
		"also_has":    {"headache", "photophobia", "altered mental status"},
		"min_also":    1,
		"boost":       {"Meningitis (Bacterial)": 4.0, "Meningitis (Viral)": 3.0,
		                "Subarachnoid Hemorrhage": 2.0},
		"suppress":    {"Influenza": 0.4, "Tension Pneumothorax": 0.1},
	},
	{
		"name":        "Subarachnoid Hemorrhage Pattern",
		"requires":    {"thunderclap headache"},
		"boost":       {"Subarachnoid Hemorrhage": 10.0, "Headache due to spontaneous subarachnoid hemorrhage": 10.0},
	},

	{
		"name":        "Pediatric SVT Pattern",
		"requires":    {"__infant__", "rapid heart rate"},
		"boost":       {"Supraventricular Tachycardia": 5.0},
	},

	# ── PE ───────────────────────────────────────────────────────────
	{
		"name":        "Pulmonary Embolism Pattern",
		"requires":    {"shortness of breath"},
		"also_has":    {"deep vein thrombosis", "pleuritic chest pain", "hypoxia"},
		"min_also":    2,
		"boost":       {"Pulmonary Embolism": 4.0, "Saddle PE": 3.0},
		"suppress":    {"Asthma (Acute)": 0.5, "Panic Disorder": 0.4},
	},

	# ── ACUTE CHF / PULMONARY EDEMA ──────────────────────────────────
	{
		"name":        "Acute CHF Pattern",
		"requires":    {"leg swelling"},
		"also_has":    {"shortness of breath", "rapid heart rate", "orthopnea"},
		"min_also":    2,
		"boost":       {"Heart Failure (Acute)": 3.5, "Cardiogenic Shock": 2.0,
		                "Pulmonary Edema": 3.0},
		"suppress":    {"Pneumonia": 0.4, "Asthma (Acute)": 0.3},
	},

	# ── AFIB WITH RVR ────────────────────────────────────────────────
	{
		"name":        "Afib with RVR Pattern",
		"requires":    {"irregular heart rate"},
		"also_has":    {"rapid heart rate", "shortness of breath", "palpitations"},
		"min_also":    1,
		"boost":       {"Atrial Fibrillation": 4.0, "Supraventricular Tachycardia": 2.0},
		"suppress":    {"Ventricular Tachycardia": 0.4},
	},

	# ── HYPERTENSIVE EMERGENCY ───────────────────────────────────────
	{
		"name":        "Hypertensive Emergency Pattern",
		"requires":    {"hypertension signs"},
		"also_has":    {"headache", "vision loss", "altered mental status", "chest pain"},
		"min_also":    2,
		"boost":       {"Hypertensive Emergency": 4.0, "Hypertensive Encephalopathy": 3.0,
		                "Hemorrhagic Stroke": 2.0},
	},

	# ── COPD EXACERBATION ────────────────────────────────────────────
	{
		"name":        "COPD Exacerbation Pattern",
		"requires":    {"copd history"},
		"also_has":    {"shortness of breath", "cough", "wheezing", "hypoxia"},
		"min_also":    1,
		"boost":       {"COPD Exacerbation": 4.5, "Asthma (Acute)": 1.5},
		"suppress":    {"Heart Failure (Acute)": 0.5, "Pulmonary Embolism": 0.4, "Pneumonia": 0.7},
	},

	# ── ANAPHYLAXIS ──────────────────────────────────────────────────
	{
		"name":        "Anaphylaxis Pattern",
		"requires":    {"rash"},
		"also_has":    {"throat swelling", "low blood pressure", "shortness of breath", "rapid heart rate"},
		"min_also":    1,
		"boost":       {"Anaphylaxis": 5.0},
		"suppress":    {"Septic Shock": 0.3, "Panic Disorder": 0.2},
	},

	# ── ALCOHOL WITHDRAWAL ───────────────────────────────────────────
	{
		"name":        "Alcohol Withdrawal Pattern",
		"requires":    {"tremor"},
		"also_has":    {"diaphoresis", "altered mental status", "seizure", "rapid heart rate"},
		"min_also":    2,
		"boost":       {"Alcohol Withdrawal": 4.0, "Delirium Tremens": 3.5},
		"suppress":    {"Hypoglycemia": 0.5},
	},

	# ── HYPOGLYCEMIA ─────────────────────────────────────────────────
	{
		"name":        "Hypoglycemia Pattern",
		"requires":    {"altered mental status"},
		"also_has":    {"diaphoresis", "tremor", "rapid heart rate"},
		"min_also":    2,
		"boost":       {"Hypoglycemia": 4.0},
		"suppress":    {"Diabetic Ketoacidosis": 0.3, "Stroke": 0.4},
	},

	# ── THYROID STORM ────────────────────────────────────────────────
	{
		"name":        "Thyroid Storm Pattern",
		"requires":    {"rapid heart rate"},
		"also_has":    {"fever", "diaphoresis", "altered mental status", "tremor"},
		"min_also":    3,
		"boost":       {"Thyroid Storm": 4.0, "Stimulant Toxicity": 1.5},
		"suppress":    {"Sepsis": 0.5},
	},

	# ── OPIOID TOXIDROME ─────────────────────────────────────────────
	{
		"name":        "Opioid Toxidrome Pattern",
		"requires":    {"opioid signs"},
		"also_has":    {"respiratory failure", "altered mental status", "loss of consciousness"},
		"min_also":    1,
		"boost":       {"Opioid Overdose": 5.0},
		"suppress":    {"Alcohol Withdrawal": 0.2, "Sepsis": 0.3},
	},

	# ── TESTICULAR TORSION ───────────────────────────────────────────
	{
		"name":        "Testicular Torsion Pattern",
		"requires":    {"scrotal pain"},
		"also_has":    {"vomiting", "nausea"},
		"min_also":    1,
		"boost":       {"Testicular Torsion": 4.5},
		"suppress":    {"Epididymitis": 0.5},
	},

	# ── STIMULANT TOXICITY ───────────────────────────────────────────
	{
		"name":        "Stimulant Toxicity Pattern",
		"requires":    {"rapid heart rate"},
		"also_has":    {"agitation", "high blood pressure", "sweating", "dilated pupils"},
		"min_also":    2,
		"boost":       {"Stimulant Toxicity": 4.0},
		"suppress":    {"Panic Disorder": 0.3},
	},

	# ── NEW ER50 PROFILES ────────────────────────────────────────────
	{
		"name":        "Retinal Detachment Pattern",
		"requires":    {"vision loss"},
		"also_has":    {"vision loss"},
		"min_also":    1,
		"boost":       {"Retinal Detachment": 3.0, "Stroke": 2.0},
		"suppress":    {"TIA": 0.5, "Hypertensive": 0.5},
	},
	{
		"name":        "Heart Block Pattern",
		"requires":    {"slow heart rate"},
		"also_has":    {"low blood pressure", "fainting", "fatigue", "altered mental status"},
		"min_also":    1,
		"boost":       {"Heart Block": 4.0},
		"suppress":    {"Neurogenic Shock": 0.3},
	},
	{
		"name":        "Fever suppresses Anaphylaxis",
		"requires":    {"fever"},
		"also_has":    {"rash", "low blood pressure"},
		"min_also":    1,
		"boost":       {"Toxic shock syndrome": 10.0, "Staphylococcal toxic shock syndrome": 10.0, "Streptococcal toxic shock syndrome": 10.0},
		"suppress":    {"Anaphylaxis": 0.1},
	},
	{
		"name":        "Appendicitis Pattern",
		"requires":    {"right lower quadrant pain"},
		"also_has":    {"fever", "nausea", "vomiting"},
		"min_also":    1,
		"boost":       {"Appendicitis": 5.0},
		"suppress":    {"Pancreatitis": 0.1, "Gastritis": 0.1},
	},
	{
		"name":        "Pleuritis Pattern",
		"requires":    {"pleuritic chest pain"},
		"also_has":    {"chest pain"},
		"min_also":    1,
		"boost":       {"Pleuritis": 3.0, "Pulmonary Embolism": 2.5},
		"suppress":    {"Pericarditis": 0.3},
	},
	{
		"name":        "Drug Toxicity Pattern",
		"requires":    {"agitation"},
		"also_has":    {"fever", "rapid heart rate", "dilated pupils"},
		"min_also":    1,
		"boost":       {"Drug Toxicity": 5.0},
		"suppress":    {"Sepsis": 0.1, "Urosepsis": 0.1},
	},
	{
		"name":        "Pyloric Stenosis Pattern",
		"requires":    {"vomiting"},
		"also_has":    {"__infant__", "dehydration"},
		"min_also":    1,
		"boost":       {"Pyloric Stenosis": 20.0},
		"suppress":    {"Mesenteric Ischemia": 0.0, "Gastritis": 0.0, "STEMI": 0.0, "Subarachnoid Hemorrhage": 0.0, "Meningitis": 0.0},
	},
	{
		"name":        "Pancreatitis Pattern",
		"requires":    {"epigastric pain"},
		"also_has":    {"back pain", "aortic pain", "nausea", "vomiting"},
		"min_also":    1,
		"boost":       {"Pancreatitis": 6.0},
		"suppress":    {"Aortic Dissection": 0.2, "Ruptured AAA": 0.2},
	},
	{
		"name":        "Cholecystitis Pattern",
		"requires":    {"right upper quadrant pain"},
		"also_has":    {"nausea", "vomiting", "fever", "abdominal pain"},
		"min_also":    0,
		"boost":       {"Cholecystitis": 5.0},
		"suppress":    {"Ectopic Pregnancy": 0.1, "Ruptured Ectopic Pregnancy": 0.1, "Gastritis": 0.3},
	},

	# ── ECTOPIC PREGNANCY ────────────────────────────────────────────
	{
		"name":        "Ectopic Pregnancy Pattern",
		"requires":    {"ectopic pain"},
		"also_has":    {"vaginal bleeding", "low blood pressure", "pelvic pain"},
		"min_also":    1,
		"boost":       {"Ruptured Ectopic Pregnancy": 5.0, "Pelvic Inflammatory Disease": 1.5},
		"suppress":    {"Appendicitis": 0.4},
	},

	# ── BOWEL OBSTRUCTION ────────────────────────────────────────────
	{
		"name":        "Bowel Obstruction Pattern",
		"requires":    {"abdominal distension"},
		"also_has":    {"abdominal pain", "vomiting", "constipation"},
		"min_also":    2,
		"boost":       {"Bowel Obstruction": 4.0, "Paralytic Ileus": 2.5},
		"suppress":    {"Appendicitis": 0.4, "Pancreatitis": 0.3},
	},

	# ── VASCULAR EMERGENCY / PE ──────────────────────────────────────
	{
		"name":        "Must-Not-Miss: PE / Vascular Combo",
		"requires":    {"shortness of breath"},
		"also_has":    {"deep vein thrombosis", "leg swelling", "rapid heart rate", "chest pain"},
		"min_also":    2, 
		"boost":       {
			"Pulmonary Embolism": 6.0, 
			"DVT": 3.0,
			"Heart Failure (Acute)": 2.0
		},
	},

	{
		"name":        "Isolated DVT Pattern",
		"requires":    {"deep vein thrombosis"},
		"also_has":    {"leg swelling", "leg pain with walking", "pain general"},
		"min_also":    1,
		"boost":       {"DVT": 5.0},
	},
]

# =========================================================
# EXCLUSION RULES
# If a symptom is ABSENT, reduce listed diagnoses.
# Only applies when the diagnosis would otherwise score >30%.
# =========================================================
EXCLUSION_RULES = [
	# No fever → suppress infectious/inflammatory diagnoses
	{
		"absent":   "fever",
		"suppress": {
			"Sepsis": 0.3, "Septic Shock": 0.2, "Meningitis (Bacterial)": 0.3,
			"Meningitis (Viral)": 0.4, "Pneumonia": 0.5, "Endocarditis": 0.5,
			"Necrotizing Fasciitis": 0.4, "Cellulitis": 0.5,
		},
	},
	# No trauma → suppress trauma diagnoses
	{
		"absent":   "trauma",
		"suppress": {
			"Traumatic Brain Injury": 0.1, "Splenic Laceration": 0.1,
			"Traumatic Aortic Injury": 0.2, "Traumatic Pneumothorax": 0.2,
			"Pelvic Fracture": 0.1, "Rib Fractures": 0.4,
		},
	},
	# No pregnancy signs → suppress OB diagnoses
	{
		"absent":   "pregnancy signs",
		"suppress": {
			"Ruptured Ectopic Pregnancy": 0.1, "Eclampsia": 0.1,
			"Preeclampsia (Severe)": 0.1, "Placental Abruption": 0.1,
			"Hyperemesis Gravidarum": 0.1, "Postpartum Hemorrhage": 0.1,
		},
	},
	# No GI symptoms → suppress pure GI diagnoses when only chest pain present
	{
		"absent":   "regurgitation",
		"suppress": {
			"GERD / Acid Reflux": 0.3, "Esophageal Spasm": 0.4,
		},
	},
	# No aortic pain → suppress dissection
	{
		"absent":   "aortic pain",
		"suppress": {
			"Aortic Dissection": 0.3, "Ruptured AAA": 0.3,
		},
	},
	# No rapid heart rate absent
	{
		"absent":   "rapid heart rate",
		"suppress": {
			"Thyroid Storm": 0.3, "Stimulant Toxicity": 0.4, "Anaphylaxis": 0.4, "Delirium Tremens": 0.4
		},
	},
	# No altered mental status absent
	{
		"absent":   "altered mental status",
		"suppress": {
			"Hypertensive Encephalopathy": 0.2, "Meningitis (Bacterial)": 0.4, "Wernicke Encephalopathy": 0.2, "Hepatic Encephalopathy": 0.2, "Septic Shock": 0.4
		},
	},
	# No chest pain absent
	{
		"absent":   "chest pain",
		"suppress": {
			"STEMI (Heart Attack)": 0.2, "NSTEMI / Unstable Angina": 0.2, "Aortic Dissection": 0.3, "Pericarditis": 0.4, "Esophageal Rupture": 0.3
		},
	},
	# No shortness of breath absent
	{
		"absent":   "shortness of breath",
		"suppress": {
			"Pulmonary Embolism": 0.3, "Tension Pneumothorax": 0.2, "Asthma (Acute)": 0.2, "COPD Exacerbation": 0.2, "Pulmonary Edema": 0.3
		},
	},
	# No headache absent
	{
		"absent":   "headache",
		"suppress": {
			"Subarachnoid Hemorrhage": 0.2, "Meningitis (Bacterial)": 0.4, "Hypertensive Encephalopathy": 0.3, "Migraine": 0.1
		},
	},
	# No abdominal pain absent
	{
		"absent":   "abdominal pain",
		"suppress": {
			"Appendicitis": 0.2, "Pancreatitis": 0.2, "Bowel Obstruction": 0.3, "Ruptured Ectopic Pregnancy": 0.3, "Cholecystitis": 0.2, "Diverticulitis": 0.2
		},
	},
	# No low blood pressure absent
	{
		"absent":   "low blood pressure",
		"suppress": {
			"Septic Shock": 0.3, "Cardiogenic Shock": 0.3, "Anaphylaxis": 0.4, "Ruptured AAA": 0.3, "Neurogenic Shock": 0.3
		},
	},
	# No scrotal pain absent
	{
		"absent":   "scrotal pain",
		"suppress": {
			"Testicular Torsion": 0.1, "Epididymitis": 0.2
		},
	},
	# No vaginal bleeding absent
	{
		"absent":   "vaginal bleeding",
		"suppress": {
			"Ruptured Ectopic Pregnancy": 0.4, "Placental Abruption": 0.2, "Postpartum Hemorrhage": 0.1
		},
	},
	# No seizure absent
	{
		"absent":   "seizure",
		"suppress": {
			"Status Epilepticus": 0.1, "Eclampsia": 0.3, "Delirium Tremens": 0.4
		},
	},
]

# =========================================================
# MINIMUM CONFIDENCE THRESHOLD
# Diagnoses below this are hidden from display.
# =========================================================
MIN_CONFIDENCE = 35   # percent
MAX_RESULTS    = 8    # max diagnoses shown



# =========================================================
# PATIENT CONTEXT EXTRACTOR
# =========================================================


def extract_patient_context(text):
    text = text.lower()
    context = {
        "age": 0,
        "sex": "unknown",
        "pediatric_infant": False,
        "diabetes": False,
        "hypertension": False,
        "no_fever": False,
        "onset_minutes": 999,
        "worsening": False,
        "improving": False,
        "intermittent": False,
        "painless": any(p in text for p in ["painless", "no pain", "without pain"]),
        "chronic": any(x in text for x in ["weeks", "months", "chronic", "longstanding"]),
        "morning_stiffness": any(x in text for x in ["morning stiffness", "stiff in morning"]),
        "adhesions": any(x in text for x in ["surgery", "surgeries", "adhesions", "surgical", "scar"]),
        "flu_season": any(x in text for x in ["flu season", "outbreak", "epidemic"]),
        "tm_bulging": any(x in text for x in ["bulging", "tympanic", "tm"]),
        "periumbilical": any(x in text for x in ["periumbilical", "belly button", "around the navel"]),
        "curtain_veil": any(x in text for x in ["curtain", "veil", "shade"]),
        "travel_history": any(x in text for x in ["travel", "flight", "car ride", "long trip", "immobility"]),
        "heavy_lifting": any(x in text for x in ["lifting", "furniture", "heavy object"]),
        "cold_intolerance": any(x in text for x in ["cold intolerance", "feeling cold", "dry skin"]),
        "weight_gain": any(x in text for x in ["weight gain", "heavier"]),
        "nocturia": any(x in text for x in ["at night", "nocturia", "waking up to pee"]),
        "slow_movements": any(x in text for x in ["slow movements", "bradykinesia", "rigid", "stiff muscles"]),
        "raw_text": text
    }
    import re
    # Fix #4: Age regex with decimals and months
    age_match = re.search(r'(\d+\.?\d*)\s*[-]?\s*(yo|year|month)', text)
    if age_match:
        val = float(age_match.group(1))
        unit = age_match.group(2)
        if "month" in unit:
            context["age"] = val / 12
        else:
            context["age"] = val
        
        # Set pediatric_infant = True if age < 2
        if context["age"] < 2:
            context["pediatric_infant"] = True

    # Fix #5: Sex detection from M/F/male/female
    if re.search(r'\b(f|female|woman|lady)\b', text) or " f " in text or text.startswith("f "):
        context["sex"] = "female"
    elif re.search(r'\b(m|male|man|gentleman)\b', text) or " m " in text or text.startswith("m "):
        context["sex"] = "male"

    if "diabetic" in text or "dm" in text:
        context["diabetes"] = True
    if "htn" in text or "hypertension" in text:
        context["hypertension"] = True
    
    # Negative Evidence
    context["no_fever"] = "no fever" in text or "afebrile" in text

    # Time Awareness
    time_match = re.search(r'(\d+)\s?(min|minutes|hours)', text)
    if time_match:
        val = int(time_match.group(1))
        unit = time_match.group(2)
        if "hour" in unit:
            val *= 60
        context["onset_minutes"] = val
    
    # === PROGRESSION SIGNALS ===
    context["worsening"] = any(x in text for x in ["worsening", "getting worse", "progressively worse", "deteriorating"])
    context["improving"] = any(x in text for x in ["improving", "getting better", "better now", "resolved"])
    context["intermittent"] = any(x in text for x in ["intermittent", "comes and goes", "on and off"])
        
    return context


def normalize(score):
    return 1 / (1 + math.exp(-score))


def compute_scores(detected_symptoms, patient_context, raw_text=""):
    detected_symptoms = list(detected_symptoms)
    if any(k in detected_symptoms for k in ["right lower quadrant pain", "right upper quadrant pain", "epigastric pain", "pelvic pain"]):
        if "abdominal pain" not in detected_symptoms:
            detected_symptoms.append("abdominal pain")

    if any(k in detected_symptoms for k in ["pleuritic chest pain", "aortic pain"]):
        if "chest pain" not in detected_symptoms:
            detected_symptoms.append("chest pain")

    scores = {}
    explanations = {}
    LOW_SIGNAL_SYMPTOMS = ["fatigue", "nausea", "weakness"]

    # Base scoring with Tiering and Saturation
    for condition, symptoms in SymptomLibrary.DIAGNOSES.items():
        score = 0
        match_count = 0
        explanations[condition] = []
        for symptom in detected_symptoms:
            if symptom in symptoms:
                weight = 0.4
                if symptom in LOW_SIGNAL_SYMPTOMS:
                    weight *= 0.3
                score += weight
                match_count += 1
                explanations[condition].append(symptom)
        
        if score > 0:
            # Weight Saturation Curve
            score *= min(1.5, 1 + (match_count * 0.1))
            scores[condition] = score

    # === RED FLAG ENFORCEMENT ===
    red_flag_triggered = set()
    for condition_pattern, triggers in RED_FLAG_RULES.items():
        match_count = sum(1 for t in triggers if t in detected_symptoms)
        
        # Hard override boost
        if match_count >= 2:
            # Fix #2: Sepsis exception for meningitis signs
            if condition_pattern == "Sepsis":
                if any(s in detected_symptoms for s in ["neck stiffness", "photophobia", "petechiae", "rash"]):
                    continue

            for condition in SymptomLibrary.DIAGNOSES:
                if condition_pattern.lower() in condition.lower():
                    scores[condition] = max(scores.get(condition, 0), 2.5)
                    red_flag_triggered.add(condition)
                    explanations.setdefault(condition, []).append("RED FLAG PATTERN")
        # Soft boost for partial match
        elif match_count == 1:
            for condition in scores:
                if condition_pattern.lower() in condition.lower():
                    scores[condition] *= 1.3
                    explanations.setdefault(condition, []).append("possible red flag")

    # === Pattern Boosting ===
    for pattern, rule in PATTERN_RULES.items():
        match_count = sum(1 for s in rule["symptoms"] if s in detected_symptoms)
        if match_count >= 2:
            for condition in scores:
                if pattern.lower() in condition.lower():
                    scores[condition] *= rule["boost"]

    # === SURGICAL UPGRADE 1: DISCRIMINATORS ===
    raw_text_lower = raw_text.lower()
    for cond, keys in DISCRIMINATORS.items():
        matching_keys = [c for c in scores if cond.lower() in c.lower()]
        if matching_keys:
            actual_cond = matching_keys[0]
            match = sum(1 for k in keys if k.lower() in raw_text_lower)
            if match >= 1:
                scores[actual_cond] *= 1.4
                explanations.setdefault(actual_cond, []).append("discriminator match")

    # === Fix #1: Wire CONTEXT_PROFILES ===
    detected_set = set(detected_symptoms)
    if patient_context.get("pediatric_infant"):
        detected_set.add("__infant__")
    for profile in CONTEXT_PROFILES:
        # Check requires
        if all(s in detected_set for s in profile.get("requires", [])):
            # Check also_has/min_also
            also_count = sum(1 for s in profile.get("also_has", []) if s in detected_set)
            if also_count >= profile.get("min_also", 0):
                # Apply boosts
                for cond_pattern, multiplier in profile.get("boost", {}).items():
                    for condition in scores:
                        if cond_pattern.lower() in condition.lower():
                            scores[condition] *= multiplier
                            explanations.setdefault(condition, []).append(f"profile boost: {profile['name']}")
                # Apply suppressions
                for cond_pattern, multiplier in profile.get("suppress", {}).items():
                    for condition in scores:
                        if cond_pattern.lower() in condition.lower():
                            scores[condition] *= multiplier
                            explanations.setdefault(condition, []).append(f"profile suppression: {profile['name']}")

    # === Fix #5: Sex-based boosts ===
    if patient_context.get("sex") == "female":
        if "abdominal pain" in detected_set:
            for condition in scores:
                if "ectopic pregnancy" in condition.lower():
                    scores[condition] *= 2.0
                    explanations.setdefault(condition, []).append("female abdominal pain boost")
        if "pregnancy signs" in detected_set:
            for condition in scores:
                if "ectopic pregnancy" in condition.lower():
                    scores[condition] *= 3.0
                    explanations.setdefault(condition, []).append("female pregnancy boost")
    elif patient_context.get("sex") == "male":
        # Male + age < 30 + "groin pain" or "scrotal pain" -> boost Testicular Torsion 3.0x
        if patient_context.get("age", 0) < 30:
            if any(s in detected_set for s in ["scrotal pain", "hip pain"]): # hip pain often maps from groin pain
                for condition in scores:
                    if "testicular torsion" in condition.lower():
                        scores[condition] *= 3.0
                        explanations.setdefault(condition, []).append("male young groin pain boost")

    # === SURGICAL UPGRADE 2: MUTUAL EXCLUSION ===
    for cond, bad_signals in EXCLUSIONS.items():
        matching_keys = [c for c in scores if cond.lower() in c.lower()]
        if matching_keys:
            actual_cond = matching_keys[0]
            if any(sig.lower() in raw_text_lower for sig in bad_signals):
                scores[actual_cond] *= 0.6
                explanations.setdefault(actual_cond, []).append("contradictory signal")

    # === SURGICAL UPGRADE 3: CONTEXT ANCHORS ===
    for cond, triggers in CONTEXT_ANCHORS.items():
        matching_keys = [c for c in scores if cond.lower() in c.lower()]
        if matching_keys:
            actual_cond = matching_keys[0]
            if any(t.lower() in raw_text_lower for t in triggers):
                scores[actual_cond] *= 1.5
                explanations.setdefault(actual_cond, []).append("context anchor")

    # === Targeted Risk Multipliers ===
    CARDIAC = ["STEMI", "NSTEMI", "Heart Attack", "ACS"]
    STROKE = ["Stroke", "CVA", "TIA"]
    for condition in scores:
        if any(k.lower() in condition.lower() for k in CARDIAC):
            if patient_context["diabetes"]:
                scores[condition] *= 1.2
        if any(k.lower() in condition.lower() for k in STROKE):
            if patient_context["age"] > 50:
                scores[condition] *= 1.2

    if patient_context.get("onset_minutes", 999) < 60:
        for condition in scores:
            if any(k.lower() in condition.lower() for k in CARDIAC + STROKE):
                scores[condition] *= 1.3

    # === PROGRESSION MODIFIERS ===
    ACUTE_CRITICAL = ["stemi", "stroke", "sepsis", "embolism", "shock"]
    for condition in scores:
        # Worsening → boost acute / dangerous
        if patient_context.get("worsening"):
            if any(k in condition.lower() for k in ACUTE_CRITICAL):
                scores[condition] *= 1.2
                explanations.setdefault(condition, []).append("worsening symptoms")
        
        # Skip reduction if red flag is locked
        if condition in red_flag_triggered:
            continue
            
        # Improving → reduce acute criticals (Capped reduction for safety)
        if patient_context.get("improving"):
            if any(k in condition.lower() for k in ["stemi", "stroke", "sepsis"]):
                scores[condition] *= 0.85
                explanations.setdefault(condition, []).append("symptoms improving")
        # Intermittent → reduce catastrophic
        if patient_context.get("intermittent"):
            if any(k in condition.lower() for k in ["stroke", "stemi"]):
                scores[condition] *= 0.6

    # === CONTEXT CONTRADICTION FILTER ===
    for condition in scores:
        if condition in red_flag_triggered:
            continue
            
        # Chronic/intermittent kills acute neuro emergencies
        if patient_context.get("intermittent"):
            if any(k in condition.lower() for k in ["meningitis", "encephalitis", "hemorrhage", "hypertensive emergency", "stroke"]):
                scores[condition] *= 0.3
                explanations.setdefault(condition, []).append("contextual contradiction")

        # Improving strongly reduces catastrophic
        if patient_context.get("improving"):
            if any(k in condition.lower() for k in ["shock", "sepsis", "dissection"]):
                scores[condition] *= 0.5
                explanations.setdefault(condition, []).append("contextual contradiction")

    # === Negative Evidence Suppression ===
    if patient_context.get("no_fever"):
        for condition in scores:
            if "Sepsis" in condition or "Pneumonia" in condition:
                scores[condition] *= 0.5

    # === Suppression Rules ===
    for dominant, suppressed, factor in SUPPRESSION_RULES:
        if scores.get(dominant, 0) > 1.2:
            if suppressed in scores and suppressed not in red_flag_triggered:
                scores[suppressed] *= factor

    # === SURGICAL UPGRADE 5: COMPETING CLUSTER PENALTY ===
    for cluster, conds in CLUSTERS.items():
        # Find matches in current scores
        cluster_scores = []
        for c_pattern in conds:
            for actual_cond in scores:
                if c_pattern.lower() in actual_cond.lower():
                    cluster_scores.append((actual_cond, scores[actual_cond]))
        
        if cluster_scores:
            top_key, top_val = max(cluster_scores, key=lambda x: x[1])
            for actual_cond, val in cluster_scores:
                if actual_cond != top_key and actual_cond not in red_flag_triggered:
                    scores[actual_cond] *= 0.7
                    explanations.setdefault(actual_cond, []).append(f"cluster penalty ({cluster})")

    # --- Painless hematuria cancer boost ---
    if "hematuria" in detected_symptoms and patient_context.get("painless"):
        for cond in scores:
            if "cancer" in cond.lower() or "malignancy" in cond.lower():
                scores[cond] *= 1.6  # strong oncology signal
                explanations.setdefault(cond, []).append("painless hematuria boost")

    # --- Gout pattern boost ---
    if "joint pain" in detected_symptoms or "toe pain" in detected_symptoms:
        raw_txt = patient_context.get("raw_text", "")
        alcohol_trigger = any(x in raw_txt for x in ["alcohol", "drinking", "beer"])
        toe_trigger = any(x in raw_txt for x in ["big toe", "first toe", "1st toe"])
        if alcohol_trigger or toe_trigger:
            for cond in scores:
                if "gout" in cond.lower():
                    boost = 2.0 if (alcohol_trigger and toe_trigger) else 1.7
                    scores[cond] *= boost
                    explanations.setdefault(cond, []).append("gout pattern boost")

    # --- PE vs DVT Logic ---
    if "shortness of breath" not in detected_symptoms:
        if "Pulmonary Embolism" in scores:
            factor = 0.7 if "pleuritic chest pain" in detected_symptoms else 0.4
            scores["Pulmonary Embolism"] *= factor
            explanations.setdefault("Pulmonary Embolism", []).append("SOB absent suppression (partial)")

    # --- Rheumatoid Arthritis boost ---
    if "joint pain" in detected_symptoms or "stiffness" in detected_symptoms:
        if patient_context.get("chronic") or patient_context.get("morning_stiffness"):
            for cond in scores:
                if "rheumatoid" in cond.lower():
                    scores[cond] *= 1.4
                    explanations.setdefault(cond, []).append("RA clinical boost")

    # --- Allergic Rhinitis boost ---
    if "nasal congestion" in detected_symptoms:
        raw_txt = patient_context.get("raw_text", "")
        if any(x in raw_txt for x in ["sneeze", "sneezing", "itchy eyes", "watery eyes"]):
            for cond in scores:
                if "allergic rhinitis" in cond.lower():
                    scores[cond] *= 2.5
                    explanations.setdefault(cond, []).append("allergy pattern boost")

    # --- Parkinson's Disease boost ---
    if "tremor" in detected_symptoms and patient_context.get("slow_movements"):
        for cond in scores:
            if "parkinson" in cond.lower():
                scores[cond] *= 2.0
                explanations.setdefault(cond, []).append("parkinsonian pattern boost")

    # --- Hypothyroidism boost ---
    if "fatigue" in detected_symptoms:
        if patient_context.get("cold_intolerance") or patient_context.get("weight_gain"):
            for cond in scores:
                if "hypothyroidism" in cond.lower():
                    scores[cond] *= 2.0
                    explanations.setdefault(cond, []).append("hypothyroid signal boost")

    # --- Lumbar Strain boost ---
    if "back pain" in detected_symptoms and patient_context.get("heavy_lifting"):
        for cond in scores:
            if "lumbar strain" in cond.lower():
                scores[cond] *= 2.0
                explanations.setdefault(cond, []).append("mechanical lift boost")

    # --- Benign Prostatic Hyperplasia boost ---
    if "urinary frequency" in detected_symptoms and patient_context.get("nocturia"):
        for cond in scores:
            if "benign prostatic" in cond.lower() or "bph" in cond.lower():
                scores[cond] *= 2.0
                explanations.setdefault(cond, []).append("BPH clinical boost")
    # --- Appendicitis boost (Periumbilical migration) ---
    if "right lower quadrant pain" in detected_symptoms:
        if patient_context.get("periumbilical"):
            for cond in scores:
                if "appendicitis" in cond.lower():
                    scores[cond] *= 2.0
                    explanations.setdefault(cond, []).append("periumbilical migration boost")

    # --- Deep Vein Thrombosis boost ---
    if "leg swelling" in detected_symptoms or "leg pain" in detected_symptoms or "deep vein thrombosis" in detected_symptoms:
        if patient_context.get("travel_history") or any(x in patient_context.get("raw_text","").lower() for x in ["surgery", "post-op"]):
            for cond in scores:
                if "deep vein thrombosis" in cond.lower() or cond == "DVT":
                    factor = 2.5 if "shortness of breath" not in detected_symptoms else 1.8
                    scores[cond] *= factor
                    explanations.setdefault(cond, []).append("travel/post-op DVT boost")

    # --- Retinal Detachment boost (Curtain signal) ---
    if "vision loss" in detected_symptoms and patient_context.get("curtain_veil"):
        for cond in scores:
            if "retinal detachment" in cond.lower():
                scores[cond] *= 2.5
                explanations.setdefault(cond, []).append("visual curtain boost")

    # --- Bowel Obstruction boost (Adhesions) ---
    if ("abdominal pain" in detected_symptoms or "vomiting" in detected_symptoms) and patient_context.get("adhesions"):
        for cond in scores:
            if "bowel obstruction" in cond.lower():
                scores[cond] *= 1.8
                explanations.setdefault(cond, []).append("surgical adhesion boost")

    # --- Myasthenia Gravis boost ---
    if any(x in detected_symptoms for x in ["vision loss", "facial_droop"]):
        raw_txt = patient_context.get("raw_text", "")
        if any(x in raw_txt for x in ["drooping", "ptosis", "double vision", "diplopia"]):
            for cond in scores:
                if "myasthenia" in cond.lower():
                    scores[cond] *= 1.8
                    explanations.setdefault(cond, []).append("neuromuscular ptosis/diplopia boost")

    # --- Influenza boost ---
    if patient_context.get("flu_season") and "fever" in detected_symptoms:
        for cond in scores:
            if "influenza" in cond.lower():
                scores[cond] *= 1.6
                explanations.setdefault(cond, []).append("seasonal epidemic boost")

    # --- Retinal Detachment boost ---
    if "vision loss" in detected_symptoms:
        raw_txt = patient_context.get("raw_text", "")
        if any(x in raw_txt for x in ["floater", "flash", "photopsia"]):
            for cond in scores:
                if "retinal detachment" in cond.lower():
                    scores[cond] *= 2.0
                    explanations.setdefault(cond, []).append("floaters/flashes boost")

    # --- Otitis Media boost ---
    if "ear pain" in detected_symptoms and patient_context.get("tm_bulging"):
        for cond in scores:
            if "otitis media" in cond.lower():
                scores[cond] *= 2.0
                explanations.setdefault(cond, []).append("TM bulging boost")

    # --- Stable Angina boost ---
    if "chest pain" in detected_symptoms or any(x in patient_context.get("raw_text","").lower() for x in ["jaw pain", "arm pain"]):
        if any(x in patient_context.get("raw_text","").lower() for x in ["exertion", "stairs", "walking", "exercise"]):
            for cond in scores:
                if "stable angina" in cond.lower():
                    scores[cond] *= 2.5
                    explanations.setdefault(cond, []).append("exertional pattern boost")

    # --- Renal Cell Carcinoma boost ---
    if "hematuria" in detected_symptoms or "flank pain" in detected_symptoms:
        if any(x in patient_context.get("raw_text","").lower() for x in ["mass", "palpable", "smoker", "smoking"]):
            for cond in scores:
                if "renal cell carcinoma" in cond.lower():
                    scores[cond] *= 2.5
                    explanations.setdefault(cond, []).append("oncology risk boost")

    # === COPD History Override ===
    # When COPD is explicitly in the detected symptoms, suppress PE/vascular
    # and strongly boost COPD Exacerbation
    if "copd history" in detected_symptoms:
        for cond in scores:
            if "pulmonary embolism" in cond.lower() or "saddle pe" in cond.lower():
                scores[cond] *= 0.15
                explanations.setdefault(cond, []).append("copd history suppression")
            if "copd exacerbation" in cond.lower():
                scores[cond] *= 3.0
                explanations.setdefault(cond, []).append("copd history boost")

    # === Pediatric Safety Suppressions ===
    if patient_context.get("pediatric_infant") or (patient_context.get("age", 0) > 0 and patient_context.get("age") < 1):
        for cond in scores:
            if any(k in cond.lower() for k in ["stemi", "nstemi", "aortic dissection", "heart attack", "pulmonary embolism", "heart failure", "acute anxiety", "panic disorder", "hyperventilation", "peptic ulcer", "gastritis"]):
                scores[cond] *= 0.1
                explanations.setdefault(cond, []).append("pediatric age suppression")

    # === Baseline Threshold Filter ===
    scores = {k: v for k, v in scores.items() if v > 0.12}

    # === Normalize (Sigmoid) ===
    for condition in scores:
        scores[condition] = round(normalize(scores[condition]), 2)

    # === "Without" Condition Cap ===
    # SNOMED generates overly broad conditions like "Sepsis without septic shock".
    # These should never outscore a more specific diagnosis.
    for condition in list(scores.keys()):
        if "without" in condition.lower():
            scores[condition] = min(scores[condition], 0.80)

    return scores, explanations


# =========================================================
# MAIN SCORING FUNCTION
# =========================================================
def get_diagnoses(detected: list, raw_text: str = "") -> list:
	"""
	Returns list of (condition, confidence_pct, icd10) tuples,
	sorted by confidence descending, filtered by MIN_CONFIDENCE.
	Uses the advanced scoring pipeline.
	"""
	# Explicit condition name override — doctor typed it, engine respects it
	import re
	raw_lower = raw_text.lower()
	explicit_overrides = {
		r'\bsvt\b': ('Supraventricular Tachycardia', 99, 'I47.1', 'explicitly documented'),
		r'\bsupraventricular tachycardia\b': ('Supraventricular Tachycardia', 99, 'I47.1', 'explicitly documented'),
		r'\bwpw\b': ('Wolff-Parkinson-White Syndrome', 99, 'I45.6', 'explicitly documented'),
		r'\bcroup\b': ('Croup', 99, 'J05.0', 'explicitly documented'),
		r'\bbronchiolitis\b': ('Bronchiolitis', 99, 'J21.9', 'explicitly documented'),
		r'\bkawasaki\b': ('Kawasaki Disease', 99, 'M30.3', 'explicitly documented'),
		r'\bepiglottitis\b': ('Epiglottitis', 99, 'J05.10', 'explicitly documented'),
		r'\brsv\b': ('RSV Bronchiolitis', 99, 'J21.0', 'explicitly documented'),
	}
	for pattern, result in explicit_overrides.items():
		if re.search(pattern, raw_lower):
			_ctx = extract_patient_context(raw_text)
			_scores, _expl = compute_scores(detected, _ctx, raw_text)
			remaining = []
			for cond, score in _scores.items():
				confidence = int(score * 100)
				if confidence >= MIN_CONFIDENCE and cond != result[0]:
					icd10 = SymptomLibrary.DIAGNOSIS_ICD10.get(cond, "N/A")
					if isinstance(icd10, list): icd10 = icd10[0]
					remaining.append((cond, confidence, icd10, ", ".join(_expl.get(cond, []))))
			remaining.sort(key=lambda x: x[1], reverse=True)
			return [result] + remaining[:4]

	context = extract_patient_context(raw_text)
	scores_dict, explanations = compute_scores(detected, context, raw_text)
	
	results = []
	word_count = len(raw_text.split()) if raw_text else 0
	sparse_multiplier = 1.0
	if word_count < 5:
		sparse_multiplier = 0.60
	elif word_count < 10:
		sparse_multiplier = 0.80
	elif word_count < 15:
		sparse_multiplier = 0.90

	for cond, score in scores_dict.items():
		confidence = int(score * 100 * sparse_multiplier)
		if confidence >= MIN_CONFIDENCE:
			icd10 = SymptomLibrary.DIAGNOSIS_ICD10.get(cond, "N/A")
			if isinstance(icd10, list): icd10 = icd10[0]
			# Append explanation to condition name for now (or could be returned separately)
			explanation = ", ".join(explanations.get(cond, []))
			results.append((cond, confidence, icd10, explanation))
			
	results.sort(key=lambda x: x[1], reverse=True)
	return results[:MAX_RESULTS]


# =========================================================
# ALERT ENGINE
# =========================================================
ALERT_RULES = [
	# Cardiac
	{"symptoms": ["chest pain","shortness of breath","diaphoresis"],        "alert": "POSSIBLE STEMI / ACS — Activate Cath Lab",           "level": "critical"},
	{"symptoms": ["pleuritic chest pain","shortness of breath","diaphoresis"], "alert": "POSSIBLE STEMI / ACS — Activate Cath Lab",      "level": "critical"},
	{"symptoms": ["arm pain","diaphoresis","shortness of breath"],           "alert": "POSSIBLE STEMI / ACS — Activate Cath Lab",           "level": "critical"},
	{"symptoms": ["chest pain","arm pain"],                              "alert": "POSSIBLE ACS — ECG STAT",                            "level": "critical"},
	{"symptoms": ["pleuritic chest pain","arm pain"],                    "alert": "POSSIBLE ACS — ECG STAT",                            "level": "critical"},
	{"symptoms": ["aortic pain","chest pain"],                           "alert": "POSSIBLE AORTIC DISSECTION — CT Angio STAT",          "level": "critical"},
	{"symptoms": ["aortic pain","pleuritic chest pain"],                  "alert": "POSSIBLE AORTIC DISSECTION — CT Angio STAT",          "level": "critical"},
	{"symptoms": ["aortic pain","low blood pressure"],                   "alert": "RUPTURED AORTA — Surgical Emergency",                 "level": "critical"},
	{"symptoms": ["low blood pressure","rapid heart rate","chest pain"], "alert": "POSSIBLE CARDIOGENIC SHOCK",                         "level": "critical"},
	{"symptoms": ["cardiac arrest"],                                     "alert": "CARDIAC ARREST — Start CPR / ACLS",                   "level": "critical"},
	# Neuro
	{"symptoms": ["facial_droop","arm weakness","slurred_speech"],       "alert": "STROKE CODE — tPA Window Assessment",                "level": "critical"},
	{"symptoms": ["thunderclap headache","neck stiffness"],              "alert": "POSSIBLE SAH / MENINGITIS — LP + CT STAT",            "level": "critical"},
	{"symptoms": ["altered mental status","fever","neck stiffness"],     "alert": "POSSIBLE MENINGITIS — Antibiotics + LP STAT",         "level": "critical"},
	{"symptoms": ["seizure","altered mental status"],                    "alert": "POSSIBLE STATUS EPILEPTICUS — Benzodiazepines",       "level": "critical"},
	{"symptoms": ["head injury","loss of consciousness"],                "alert": "SIGNIFICANT HEAD TRAUMA — CT Head STAT",              "level": "critical"},
	# Respiratory
	{"symptoms": ["shortness of breath","low blood pressure","hypoxia"], "alert": "RESPIRATORY FAILURE / SHOCK — Airway Management",   "level": "critical"},
	{"symptoms": ["stridor","throat swelling"],                          "alert": "IMPENDING AIRWAY OBSTRUCTION — Prepare RSI",          "level": "critical"},
	{"symptoms": ["cyanosis","shortness of breath","low blood pressure"],"alert": "POSSIBLE TENSION PNEUMO — Needle Decompression",    "level": "critical"},
	{"symptoms": ["rash","throat swelling","low blood pressure"],        "alert": "ANAPHYLAXIS — Epinephrine IM STAT",                   "level": "critical"},
	{"symptoms": ["angioedema","low blood pressure"],                    "alert": "ANAPHYLAXIS — Epinephrine IM STAT",                   "level": "critical"},
	{"symptoms": ["stridor","low blood pressure"],                       "alert": "ANAPHYLAXIS — Epinephrine IM STAT",                   "level": "critical"},
	{"symptoms": ["angioedema","stridor"],                               "alert": "ANAPHYLAXIS — Epinephrine IM STAT",                   "level": "critical"},
	{"symptoms": ["copd history","shortness of breath","hypoxia"],       "alert": "COPD EXACERBATION — Bronchodilators + Steroids",      "level": "warning"},
	# Sepsis
	{"symptoms": ["fever","rapid heart rate","low blood pressure"],      "alert": "POSSIBLE SEPTIC SHOCK — Sepsis Bundle",               "level": "critical"},
	{"symptoms": ["fever","altered mental status","low blood pressure"],  "alert": "POSSIBLE SEPSIS / SEPTIC SHOCK",                    "level": "critical"},
	{"symptoms": ["fever","petechiae"],                                  "alert": "POSSIBLE MENINGOCOCCEMIA — Pen G + Ceftriaxone STAT", "level": "critical"},
	# Toxicology
	{"symptoms": ["opioid signs","respiratory failure"],                 "alert": "OPIOID OVERDOSE — Naloxone STAT",                     "level": "critical"},
	{"symptoms": ["altered mental status","respiratory failure"],        "alert": "POSSIBLE OVERDOSE / TOXIDROME — Secure ABCs",         "level": "critical"},
	{"symptoms": ["carbon monoxide","headache","altered mental status"], "alert": "CO POISONING — 100% O2 / HBO Therapy",               "level": "critical"},
	# Surgical
	{"symptoms": ["right lower quadrant pain","fever","rebound tenderness"], "alert": "POSSIBLE APPENDICITIS — Surgical Consult",       "level": "warning"},
	{"symptoms": ["abdominal pain","low blood pressure","vomiting"],     "alert": "POSSIBLE SURGICAL ABDOMEN — Urgent Assessment",       "level": "critical"},
	{"symptoms": ["vaginal bleeding","pregnancy signs","ectopic pain"],      "alert": "RUPTURED ECTOPIC — OB/GYN + OR STAT",               "level": "critical"},
	{"symptoms": ["pelvic pain","low blood pressure","pregnancy signs"],    "alert": "RUPTURED ECTOPIC — OB/GYN + OR STAT",               "level": "critical"},
	# OB
	{"symptoms": ["preeclampsia signs","seizure"],                       "alert": "ECLAMPSIA — MgSO4 + Deliver STAT",                    "level": "critical"},
	{"symptoms": ["labor signs","vaginal bleeding","low blood pressure"], "alert": "OBSTETRIC HEMORRHAGE — OB STAT",                    "level": "critical"},
	# Pediatric
	{"symptoms": ["fever","bulging fontanelle"],                         "alert": "POSSIBLE PEDIATRIC MENINGITIS — Antibiotics STAT",    "level": "critical"},
	{"symptoms": ["foreign body","stridor","cyanosis"],                  "alert": "FOREIGN BODY AIRWAY OBSTRUCTION — BLS/ALS",           "level": "critical"},
	# Vascular / Misc
	{"symptoms": ["shortness of breath","leg swelling","pleuritic chest pain"], "alert": "POSSIBLE PULMONARY EMBOLISM — CT Angio STAT",         "level": "critical"},
	{"symptoms": ["shortness of breath","pleuritic chest pain","hypoxia"],      "alert": "POSSIBLE PULMONARY EMBOLISM — CT Angio STAT",         "level": "critical"},
	{"symptoms": ["shortness of breath","pleuritic chest pain","rapid heart rate"], "alert": "POSSIBLE PULMONARY EMBOLISM — CT Angio STAT",      "level": "critical"},
	{"symptoms": ["swelling","pleuritic chest pain","hypoxia"],                 "alert": "POSSIBLE PULMONARY EMBOLISM — CT Angio STAT",         "level": "critical"},
	{"symptoms": ["bloody stool","hematemesis","low blood pressure"],    "alert": "GI BLEED — Urgent GI Consult / Resuscitation",        "level": "critical"},
	{"symptoms": ["peaked T waves","weakness","bradycardia"],            "alert": "HYPERKALEMIA — Calcium + Insulin/D50 STAT",           "level": "critical"},
	{"symptoms": ["hyperglycemia signs","metabolic acidosis"],              "alert": "DIABETIC KETOACIDOSIS — IV Fluids + Insulin",         "level": "critical"},
	{"symptoms": ["hyperglycemia signs","vomiting","abdominal pain"],       "alert": "DIABETIC KETOACIDOSIS — IV Fluids + Insulin",         "level": "critical"},
	{"symptoms": ["altered mental status","dry mucous membranes"],       "alert": "HYPEROSMOLAR HYPERGLYCEMIC STATE — IV Fluids",        "level": "critical"},
	{"symptoms": ["wheezing","shortness of breath","cyanosis"],          "alert": "SEVERE ASTHMA — Continuous Nebs / Steroids",          "level": "critical"},
	{"symptoms": ["jaundice","altered mental status"],                   "alert": "ACUTE LIVER FAILURE — Liver Transplant Consult",      "level": "critical"},
	{"symptoms": ["core temp < 30C","shivering absent"],                 "alert": "SEVERE HYPOTHERMIA — Active Rewarming",               "level": "critical"},
	{"symptoms": ["eye pain","vision loss","mid-dilated pupil"],         "alert": "ACUTE ANGLE CLOSURE GLAUCOMA — Ophthalmology STAT",   "level": "critical"},
	{"symptoms": ["abdominal pain","pain out of proportion"],            "alert": "ACUTE MESENTERIC ISCHEMIA — Vascular Surgery STAT",   "level": "critical"},
]

def get_alert(detected: list):
	"""
	Returns a list of matching (message, treatment, level) alerts,
	sorted so all 'critical' alerts come before 'warning' alerts.
	"""
	detected_set = set(detected)
	matches = []
	
	for rule in ALERT_RULES:
		if all(s in detected_set for s in rule["symptoms"]):
			# Split at " — " (em-dash U+2014 with spaces)
			parts = rule["alert"].split(" — ", 1)
			msg   = parts[0]
			rx    = parts[1] if len(parts) > 1 else ""
			matches.append((msg, rx, rule["level"]))
            
	# ── Stroke Red Flag Alert ──────────────────────────────────────
	if ("unilateral_weakness" in detected_set and 
	    ("slurred_speech" in detected_set or "facial_droop" in detected_set)):
		matches.append(("[!] CODE STROKE", "Patient presenting with unilateral weakness and facial/speech deficits. Expedite STAT CT Head.", "critical"))
            
	# Sort matches: critical first
	matches.sort(key=lambda x: 0 if x[2] == "critical" else 1)
	return matches

class DiagnosisEngine:
    def analyze(self, text):
        from clinical_engine import SymptomLibrary
        detected = SymptomLibrary.detect_symptoms(text)
        
        # New Scoring Pipeline
        context = extract_patient_context(text)
        scores_dict, explanations = compute_scores(detected, context, text)
        
        # Convert to the format expected by the UI (list of tuples)
        conditions = []
        for cond, score in scores_dict.items():
            confidence = int(score * 100)
            if confidence >= 35: # MIN_CONFIDENCE
                icd10 = SymptomLibrary.DIAGNOSIS_ICD10.get(cond, "N/A")
                if isinstance(icd10, list): icd10 = icd10[0]
                explanation = ", ".join(explanations.get(cond, []))
                conditions.append((cond, confidence, icd10, explanation))
        
        conditions.sort(key=lambda x: x[1], reverse=True)
        
        # ── Condition Quality Filter ────────────────────────────────
        # Three passes to remove noise before returning results:
        
        import re as _re
        _detected_set  = set(s.replace('_', ' ').lower() for s in detected if not s.startswith("__"))
        _detected_words = set(w for s in _detected_set for w in s.split())
        _CONNECTORS    = {"of", "the", "and", "or", "in", "at", "with", "joint", "general", "acute", "chronic"}
        _VERBOSE_MARKERS = [
            r'\bdue to\b', r'\bcaused by\b', r'\bco-occurrent\b',
            r'\bassociated with\b', r'\bsecondary to\b',
            r'\bfollowing\b', r'\bresulting from\b',
            r'\bof\b.{4,}',   # "rash of systemic..." but not "heart failure"
            r'\bmuscle fatigue\b', # "severe systemic illness respiratory muscle fatigue"
        ]

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
            # Rule A: Regex markers for clinical "narratives"
            if any(_re.search(p, name) for p in _VERBOSE_MARKERS):
                return True
            # Rule B: Word count guard for unlabeled or musculoskeletal noise
            if len(name.split()) > 5:
                if icd in ("N/A", "", None) or icd.startswith("M"):
                    return True
            return False

        # Pass 1 — Symptom leak
        conditions = [c for c in conditions if not _is_symptom_leak(c)]
        # Pass 2 — Verbose SNOMED
        conditions = [c for c in conditions if not _is_verbose_snomed(c)]
        # Pass 3 — Case-variant dedup
        _seen_lower = {}
        _deduped = []
        for c in conditions:
            _key = c[0].lower()
            if _key not in _seen_lower:
                _seen_lower[_key] = True
                _deduped.append(c)
            else:
                # Preference: keep whichever has a valid ICD-10 code
                existing_idx = next(i for i, x in enumerate(_deduped) if x[0].lower() == _key)
                if _deduped[existing_idx][2] in ("N/A", "", None) and c[2] not in ("N/A", "", None):
                    _deduped[existing_idx] = c
        conditions = _deduped

        return {
            "detected_symptoms": [s for s in detected if not s.startswith("__")],
            "possible_conditions": conditions[:8],
            "scores_dict": scores_dict,
            "explanations": explanations
        }

def triage_conditions(scores):
    triage = {
        "critical": [],
        "urgent": [],
        "consider": []
    }
    for condition, score in scores.items():
        if score >= 0.85:
            triage["critical"].append((condition, score))
        elif score >= 0.6:
            triage["urgent"].append((condition, score))
        else:
            triage["consider"].append((condition, score))
    # Sort each bucket
    for key in triage:
        triage[key].sort(key=lambda x: x[1], reverse=True)
    return triage

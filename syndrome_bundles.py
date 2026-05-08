# syndrome_bundles.py

SYNDROME_DOC_BUNDLES = {

    # ── 1. STEMI / ACS ───────────────────────────────────────────────────────
    "POSSIBLE STEMI / ACS": {
        "label": "STEMI / ACS — documentation ready",
        "abbr": "MI",
        "icd10": [
            ("I21.9",  "Acute MI, unspecified"),
            ("I21.0",  "Anterior wall STEMI"),
            ("I21.1",  "Inferior wall STEMI"),
            ("I24.0",  "Unstable angina"),
        ],
        "cpt": [
            ("93010",  "ECG interpretation"),
            ("92941",  "PCI — acute MI"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("ASA 325mg",     "Aspirin 325mg PO × 1 (loading dose)"),
            ("Ticagrelor",    "Ticagrelor 180mg PO × 1 (loading dose)"),
            ("Heparin UFH",   "Heparin 60 U/kg IV bolus (max 4,000 U), then 12 U/kg/hr infusion"),
            ("Nitroglycerin", "Nitroglycerin 0.4mg SL q5min PRN chest pain (hold if SBP < 90)"),
            ("Metoprolol",    "Metoprolol tartrate 5mg IV q5min × 3 doses if HR > 100 and SBP > 100"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with acute chest pain consistent with STEMI. 12-lead ECG demonstrated ST-elevation. Cath lab activated. Cardiology consulted and at bedside. Door-to-balloon time documented. Dual antiplatelet therapy and anticoagulation initiated."),
            ("Door-to-balloon",
             "Door-to-balloon time: __ minutes. First medical contact time: __. Cath lab activation time: __."),
            ("Reperfusion phrase",
             "Emergent coronary angiography performed. Culprit lesion identified and treated with percutaneous coronary intervention. TIMI flow post-intervention: __."),
        ],
    },
    "POSSIBLE ACS": {
        "label": "ACS — documentation ready",
        "abbr": "ACS",
        "icd10": [("I24.9", "Acute ischemic heart disease, unspecified")],
        "cpt": [("93010", "ECG interpretation")],
        "meds": [("ASA 325mg", "Aspirin 325mg PO")],
        "note": [("Primary note", "Patient presenting with symptoms concerning for acute coronary syndrome.")],
    },

    # ── 2. Aortic Dissection ─────────────────────────────────────────────────
    "POSSIBLE AORTIC DISSECTION": {
        "label": "Aortic dissection — documentation ready",
        "abbr": "AoD",
        "icd10": [
            ("I71.00", "Aortic dissection, unspecified"),
            ("I71.01", "Dissection of thoracic aorta"),
            ("I71.02", "Dissection of abdominal aorta"),
        ],
        "cpt": [
            ("71275",  "CT angiography, thoracic aorta"),
            ("75635",  "CT angiography, abdominal aorta"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("Esmolol",      "Esmolol 500 mcg/kg IV bolus, then 50–200 mcg/kg/min infusion (target HR < 60, SBP 100–120)"),
            ("Labetalol",    "Labetalol 20mg IV over 2 min, repeat q10min PRN (max 300mg cumulative)"),
            ("Nicardipine",  "Nicardipine 5mg/hr IV infusion, titrate to SBP 100–120 (if beta-blocker contraindicated)"),
            ("Morphine",     "Morphine 2–4mg IV q4h PRN pain (use cautiously)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with tearing/ripping chest pain radiating to the back. CT angiography confirmed aortic dissection. Cardiothoracic surgery and vascular surgery consulted. BP and HR managed with IV antihypertensives targeting SBP 100–120 mmHg and HR < 60 bpm."),
            ("Type classification",
             "Stanford Type __ (Type A — involves ascending aorta, surgical emergency / Type B — descending aorta, medical management)."),
        ],
    },

    # ── 3. Cardiac Arrest ────────────────────────────────────────────────────
    "CARDIAC ARREST": {
        "label": "Cardiac arrest — documentation ready",
        "abbr": "CA",
        "icd10": [
            ("I46.9",  "Cardiac arrest, cause unspecified"),
            ("I46.2",  "Cardiac arrest due to underlying cardiac condition"),
            ("I46.8",  "Cardiac arrest due to other underlying condition"),
        ],
        "cpt": [
            ("92950",  "Cardiopulmonary resuscitation (CPR)"),
            ("99291",  "Critical care, first 30–74 min"),
            ("93010",  "ECG interpretation"),
        ],
        "meds": [
            ("Epinephrine",   "Epinephrine 1mg IV/IO q3–5min during cardiac arrest"),
            ("Amiodarone",    "Amiodarone 300mg IV/IO × 1 (shockable rhythm), then 150mg IV × 1 if recurrence"),
            ("Lidocaine",     "Lidocaine 1–1.5 mg/kg IV/IO (alternative to amiodarone for VF/pVT)"),
            ("Sodium Bicarb", "Sodium bicarbonate 1 mEq/kg IV (if prolonged arrest or hyperkalemia suspected)"),
        ],
        "note": [
            ("Primary note",
             "Patient in cardiac arrest on arrival / developed cardiac arrest in ED. CPR initiated. Rhythm identified as __. Defibrillation delivered × __ shocks at __ J. ROSC achieved at __ minutes. Total downtime: __ minutes. Post-ROSC care initiated including targeted temperature management discussion."),
            ("Arrest timeline",
             "Time of arrest: __. CPR initiated: __. First rhythm check: __. First shock: __. ROSC: __. Total resuscitation duration: __ minutes."),
            ("Witnessed/unwitnessed",
             "Arrest was __ (witnessed / unwitnessed). Bystander CPR: __ (yes / no). EMS downtime prior to ED arrival: __ minutes."),
        ],
    },

    # ── 4. Stroke / CVA ──────────────────────────────────────────────────────
    "STROKE CODE": {
        "label": "Stroke / CVA — documentation ready",
        "abbr": "CVA",
        "icd10": [
            ("I63.9",  "Cerebral infarction, unspecified"),
            ("I63.0",  "Cerebral infarction due to thrombosis"),
            ("I61.9",  "Hemorrhagic stroke, unspecified"),
            ("G45.9",  "TIA, unspecified"),
        ],
        "cpt": [
            ("70553",  "MRI brain with contrast"),
            ("70450",  "CT head without contrast"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("tPA",          "Alteplase 0.9 mg/kg IV (max 90mg total): 10% of dose as bolus over 1 min, remainder over 60 min"),
            ("Labetalol",    "Labetalol 10mg IV over 1–2 min PRN SBP > 185 (pre-tPA threshold)"),
            ("Nicardipine",  "Nicardipine 5mg/hr IV infusion PRN BP management"),
            ("Aspirin",      "Aspirin 325mg PO (hold if tPA given — start 24h post-tPA)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with acute onset focal neurological deficits. NIHSS score: __. Last known well time: __. CT head obtained — hemorrhage excluded. Neurology consulted. tPA eligibility assessed and decision documented."),
            ("tPA administration",
             "tPA administered at __. Onset-to-needle time: __ minutes. Door-to-needle time: __ minutes. Patient/family consent obtained and documented."),
            ("tPA contraindication",
             "tPA not administered due to: __. Decision discussed with neurology attending. Alternative treatment plan: __."),
            ("NIHSS",
             "NIHSS documented: __. Deficits include: __. Baseline functional status per family: __."),
        ],
    },
    "[!] CODE STROKE": {
        "label": "Stroke / CVA — documentation ready",
        "abbr": "CVA",
        "icd10": [
            ("I63.9",  "Cerebral infarction, unspecified"),
        ],
        "cpt": [
            ("70450",  "CT head without contrast"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("tPA",          "Alteplase 0.9 mg/kg IV"),
            ("Aspirin",      "Aspirin 325mg PO"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with acute onset focal neurological deficits. NIHSS score: __. Last known well time: __. CT head obtained — hemorrhage excluded. Neurology consulted. tPA eligibility assessed and decision documented."),
        ],
    },

    # ── 5. Status Epilepticus ────────────────────────────────────────────────
    "POSSIBLE STATUS EPILEPTICUS": {
        "label": "Status epilepticus — documentation ready",
        "abbr": "SzE",
        "icd10": [
            ("G41.9",  "Status epilepticus, unspecified"),
            ("G41.0",  "Grand mal status epilepticus"),
            ("G41.1",  "Petit mal status epilepticus"),
        ],
        "cpt": [
            ("95957",  "EEG monitoring"),
            ("70553",  "MRI brain with contrast"),
            ("99291",  "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("Lorazepam",    "Lorazepam 0.1 mg/kg IV (max 4mg/dose), may repeat × 1 after 5 min"),
            ("Diazepam",     "Diazepam 0.15–0.2 mg/kg IV (max 10mg) — alternative to lorazepam"),
            ("Midazolam IM", "Midazolam 10mg IM (> 40kg) — if no IV access"),
            ("Levetiracetam","Levetiracetam 60 mg/kg IV (max 4,500mg) over 10 min — second-line"),
            ("Fosphenytoin", "Fosphenytoin 20 mg PE/kg IV at max 150 mg PE/min — second-line alternative"),
            ("Propofol",     "Propofol infusion 1–2 mg/kg IV bolus, then 20 mcg/kg/min — refractory SE only"),
        ],
        "note": [
            ("Primary note",
             "Patient presented in status epilepticus with continuous seizure activity lasting > 5 minutes. Benzodiazepine therapy initiated. Seizure duration: __ minutes. Response to treatment: __. Neurology consulted. Labs including glucose, electrolytes, AED levels obtained."),
            ("Seizure timeline",
             "Seizure onset: __. Duration prior to treatment: __ minutes. First benzodiazepine given: __. Seizure cessation: __. Total seizure duration: __ minutes."),
        ],
    },

    # ── 6. Airway Obstruction ────────────────────────────────────────────────
    "IMPENDING AIRWAY OBSTRUCTION": {
        "label": "Airway obstruction — documentation ready",
        "abbr": "AWO",
        "icd10": [
            ("J98.01", "Acute bronchospasm"),
            ("J39.8",  "Upper airway obstruction"),
            ("T17.9",  "Foreign body in respiratory tract"),
        ],
        "cpt": [
            ("31500",  "Emergency intubation"),
            ("31515",  "Laryngoscopy with foreign body removal"),
            ("99291",  "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("Albuterol",    "Albuterol 2.5mg via nebulizer q20min × 3 doses, then q1–4h PRN"),
            ("Epinephrine",  "Epinephrine 0.3mg IM (1:1000) for angioedema/anaphylaxis-related obstruction"),
            ("Dexamethasone","Dexamethasone 10mg IV × 1 for airway edema/croup"),
            ("Racemic Epi",  "Racemic epinephrine 0.5mL of 2.25% solution via nebulizer for croup"),
            ("Heliox",       "Heliox 70:30 via non-rebreather mask for partial obstruction bridge"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with acute airway obstruction. Airway assessment performed. Oxygen saturation: __%. Intervention: __. Airway secured via __ (BVM / intubation / surgical airway). Anesthesia / ENT / Pulmonology consulted."),
            ("Intubation note",
             "Rapid sequence intubation (RSI) performed. Pre-oxygenation with __. Medications: __. Blade: __ / Video laryngoscopy used: __. Tube size: __ / Depth: __ cm at lip. EtCO2 confirmation: __. CXR ordered for tube placement confirmation."),
        ],
    },
    "FOREIGN BODY AIRWAY OBSTRUCTION": {
        "label": "Foreign Body Airway Obstruction — documentation ready",
        "abbr": "AWO",
        "icd10": [("T17.9", "Foreign body in respiratory tract")],
        "cpt": [("31515", "Laryngoscopy with FB removal")],
        "meds": [("Oxygen", "100% O2 via NRB")],
        "note": [("Primary note", "Patient presenting with acute foreign body airway obstruction.")],
    },

    # ── 7. Tension Pneumothorax ──────────────────────────────────────────────
    "POSSIBLE TENSION PNEUMO": {
        "label": "Tension pneumothorax — documentation ready",
        "abbr": "TPx",
        "icd10": [
            ("J93.0",  "Spontaneous tension pneumothorax"),
            ("S27.0",  "Traumatic pneumothorax"),
            ("J93.11", "Primary spontaneous pneumothorax"),
        ],
        "cpt": [
            ("32551",  "Tube thoracostomy — chest tube placement"),
            ("32557",  "Needle decompression / pleural drainage"),
            ("71046",  "Chest X-ray, 2 views"),
        ],
        "meds": [
            ("NS flush",  "Normal saline 500mL IV bolus for hemodynamic support post-decompression"),
            ("Morphine",  "Morphine 2–4mg IV q4h PRN post-procedure pain"),
            ("Fentanyl",  "Fentanyl 1 mcg/kg IV for procedural analgesia"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with respiratory distress and hemodynamic instability consistent with tension pneumothorax. Absent breath sounds on __ side. Needle decompression performed at 2nd intercostal space, midclavicular line with immediate improvement. Chest tube subsequently placed."),
            ("Chest tube note",
             "Chest tube placed — size: __ Fr / Site: __ ICS, MAL. Confirmation: CXR obtained. Output: __ mL. Air leak present: __. Placed to water seal / suction at -20 cmH2O."),
        ],
    },

    # ── 8. Anaphylaxis ───────────────────────────────────────────────────────
    "ANAPHYLAXIS": {
        "label": "Anaphylaxis — documentation ready",
        "abbr": "Ana",
        "icd10": [
            ("T78.2",  "Anaphylactic shock, unspecified"),
            ("T78.00", "Anaphylaxis due to unspecified food"),
            ("T88.6",  "Anaphylactic reaction due to drug"),
        ],
        "cpt": [
            ("99285",  "ED visit, high complexity"),
            ("96372",  "Therapeutic injection, subcutaneous/IM"),
        ],
        "meds": [
            ("Epinephrine IM", "Epinephrine 0.3–0.5mg IM (1:1000) into anterolateral thigh, repeat q5–15min PRN"),
            ("Diphenhydramine","Diphenhydramine 50mg IV/IM × 1"),
            ("Famotidine",     "Famotidine 20mg IV × 1 (H2 blocker adjunct)"),
            ("Methylpred",     "Methylprednisolone 125mg IV × 1"),
            ("Albuterol",      "Albuterol 2.5mg via nebulizer q20min PRN bronchospasm"),
            ("NS bolus",       "Normal saline 1–2L IV bolus for hypotension"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with anaphylaxis following exposure to __ (trigger identified / unknown). Symptoms included urticaria, angioedema, bronchospasm, and hemodynamic compromise. Epinephrine administered IM. Response to treatment: __. Monitored for biphasic reaction for minimum 4–6 hours."),
            ("Trigger documentation",
             "Suspected trigger: __. Time of exposure: __. Time of symptom onset: __. Patient counseled on avoidance and self-injectable epinephrine prescribed."),
        ],
    },

    # ── 9. Septic Shock ──────────────────────────────────────────────────────
    "POSSIBLE SEPTIC SHOCK": {
        "label": "Septic shock — documentation ready",
        "abbr": "SEP",
        "icd10": [
            ("A41.9",  "Sepsis, unspecified organism"),
            ("R65.21", "Severe sepsis with septic shock"),
            ("A41.51", "Sepsis due to E. coli"),
            ("A41.01", "Sepsis due to MRSA"),
        ],
        "cpt": [
            ("99291",  "Critical care, first 30–74 min"),
            ("36556",  "Central venous catheter placement"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("NS bolus",         "Normal saline 30 mL/kg IV bolus within 3 hours of sepsis recognition"),
            ("Pip-Tazo",         "Piperacillin-tazobactam 3.375g IV q6h (or 4.5g IV q8h extended infusion)"),
            ("Vancomycin",       "Vancomycin 25 mg/kg IV loading dose (round to nearest 250mg, max 3g)"),
            ("Norepinephrine",   "Norepinephrine 0.01–3 mcg/kg/min IV infusion (first-line vasopressor, target MAP ≥ 65)"),
            ("Hydrocortisone",   "Hydrocortisone 200mg/day IV continuous infusion (if refractory shock after adequate fluids + 2 vasopressors)"),
        ],
        "note": [
            ("Primary note",
             "Patient met Sepsis-3 criteria with suspected source: __. Blood cultures × 2 obtained prior to antibiotic administration. Lactate: __ mmol/L. Broad-spectrum antibiotics initiated within 1 hour. IV fluid resuscitation 30 mL/kg administered. Vasopressor support initiated for MAP < 65 despite fluids."),
            ("Bundle compliance",
             "SEP-1 bundle: Blood cultures before antibiotics — yes/no. Lactate measured — yes/no. 30mL/kg IV crystalloid — yes/no. Antibiotics within 1 hour — yes/no. Vasopressors for MAP < 65 — yes/no."),
            ("Source",
             "Suspected sepsis source: __ (pulmonary / urinary / abdominal / skin/soft tissue / line-related / unknown). Cultures sent: blood × 2, urine, __."),
        ],
    },
    "POSSIBLE SEPSIS / SEPTIC SHOCK": {
        "label": "Sepsis / Septic shock — documentation ready",
        "abbr": "SEP",
        "icd10": [("A41.9", "Sepsis, unspecified organism")],
        "cpt": [("99291", "Critical care")],
        "meds": [("NS bolus", "30 mL/kg IV bolus")],
        "note": [("Primary note", "Patient met Sepsis-3 criteria. SEP-1 bundle initiated.")],
    },

    # ── 10. Meningitis ───────────────────────────────────────────────────────
    "POSSIBLE MENINGITIS": {
        "label": "Meningitis — documentation ready",
        "abbr": "MEN",
        "icd10": [
            ("G03.9",  "Meningitis, unspecified"),
            ("G00.9",  "Bacterial meningitis, unspecified"),
            ("G02",    "Meningitis in viral diseases"),
        ],
        "cpt": [
            ("62270",  "Lumbar puncture, diagnostic"),
            ("70553",  "MRI brain with contrast"),
            ("99291",  "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("Ceftriaxone",    "Ceftriaxone 2g IV q12h"),
            ("Vancomycin",     "Vancomycin 25 mg/kg IV q8–12h (for PCN-resistant S. pneumoniae coverage)"),
            ("Dexamethasone",  "Dexamethasone 0.15 mg/kg IV q6h × 4 days (first dose before or with first antibiotic)"),
            ("Ampicillin",     "Ampicillin 2g IV q4h (if Listeria suspected: age > 50, immunocompromised, pregnancy)"),
            ("Acyclovir",      "Acyclovir 10 mg/kg IV q8h (if HSV encephalitis cannot be excluded)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with classic triad of fever, neck stiffness, and altered mental status. Kernig / Brudzinski signs: __. CT head performed prior to LP: __. Lumbar puncture performed — opening pressure: __ cmH2O, appearance: __. CSF sent for cell count, glucose, protein, culture, Gram stain. Empiric antibiotics and dexamethasone administered."),
            ("LP results placeholder",
             "CSF results: WBC __ (__ % PMN), RBC __, glucose __ (serum glucose __), protein __, Gram stain __, culture pending."),
        ],
    },
    "POSSIBLE SAH / MENINGITIS": {
        "label": "SAH / Meningitis — documentation ready",
        "abbr": "MEN",
        "icd10": [("I60.9", "Subarachnoid hemorrhage, unspecified"), ("G03.9", "Meningitis, unspecified")],
        "cpt": [("62270", "Lumbar puncture"), ("70450", "CT head")],
        "meds": [("Ceftriaxone", "2g IV"), ("Vancomycin", "25 mg/kg IV")],
        "note": [("Primary note", "Clinical concern for SAH or Meningitis. LP and CT head performed.")],
    },
    "POSSIBLE MENINGOCOCCEMIA": {
        "label": "Meningococcemia — documentation ready",
        "abbr": "MEN",
        "icd10": [("A39.0", "Meningococcal meningitis"), ("A39.2", "Acute meningococcemia")],
        "cpt": [("99291", "Critical care")],
        "meds": [("Pen G", "4 million units IV"), ("Ceftriaxone", "2g IV")],
        "note": [("Primary note", "Patient presenting with fever and petechial rash concerning for meningococcemia.")],
    },
    "POSSIBLE PEDIATRIC MENINGITIS": {
        "label": "Pediatric Meningitis — documentation ready",
        "abbr": "MEN",
        "icd10": [("G03.9", "Meningitis, unspecified")],
        "cpt": [("62270", "Lumbar puncture")],
        "meds": [("Ceftriaxone", "100 mg/kg IV"), ("Vancomycin", "15 mg/kg IV")],
        "note": [("Primary note", "Infant presenting with fever and bulging fontanelle concerning for meningitis.")],
    },

    # ── 11. Opioid Overdose ──────────────────────────────────────────────────
    "OPIOID OVERDOSE": {
        "label": "Opioid overdose — documentation ready",
        "abbr": "OD",
        "icd10": [
            ("T40.2X1", "Poisoning by heroin, accidental"),
            ("T40.601", "Poisoning by unspecified opioids, accidental"),
            ("T40.4X1", "Poisoning by synthetic opioids, accidental"),
        ],
        "cpt": [
            ("99285",   "ED visit, high complexity"),
            ("99291",   "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("Naloxone IV",   "Naloxone 0.4–2mg IV/IM/intranasal, repeat q2–3min PRN — titrate to adequate respirations (not full reversal to avoid withdrawal)"),
            ("Naloxone infusion", "Naloxone infusion: 2/3 of effective bolus dose per hour (for long-acting opioid overdose)"),
            ("O2",            "Supplemental oxygen titrated to SpO2 > 94%, BVM ventilation PRN"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with opioid toxidrome: altered mental status, respiratory depression, miosis. Naloxone administered with response: __. Suspected substance: __. Route of use: __. Social work consulted. Substance use resources and naloxone prescription discussed with patient."),
            ("Discharge planning",
             "Addiction medicine / substance use counseling referral: __. Take-home naloxone prescribed: yes/no. Follow-up arranged: __."),
        ],
    },

    # ── 12. Eclampsia ────────────────────────────────────────────────────────
    "ECLAMPSIA": {
        "label": "Eclampsia — documentation ready",
        "abbr": "ECL",
        "icd10": [
            ("O15.9",  "Eclampsia, unspecified as to time period"),
            ("O15.0",  "Eclampsia in pregnancy"),
            ("O15.1",  "Eclampsia in labor"),
            ("O14.10", "Severe pre-eclampsia, unspecified trimester"),
        ],
        "cpt": [
            ("99291",  "Critical care, first 30–74 min"),
            ("59410",  "Vaginal delivery"),
            ("76805",  "Obstetric ultrasound, > 14 weeks"),
        ],
        "meds": [
            ("Mag Sulfate",   "Magnesium sulfate 4–6g IV loading dose over 15–20 min, then 1–2g/hr maintenance infusion"),
            ("Labetalol",     "Labetalol 20mg IV over 2 min, repeat 40mg then 80mg q10min PRN SBP > 160 (max 300mg)"),
            ("Hydralazine",   "Hydralazine 5–10mg IV q20min PRN SBP > 160 (max 20mg per episode)"),
            ("Nifedipine",    "Nifedipine 10mg PO immediate-release q20min PRN (alternative antihypertensive)"),
        ],
        "note": [
            ("Primary note",
             "Patient at __ weeks gestation presented with new-onset seizure in the setting of hypertension. Eclampsia diagnosed. Magnesium sulfate loading dose administered. BP management initiated. OB and MFM (maternal-fetal medicine) consulted immediately. Fetal heart rate: __. Delivery plan discussed."),
            ("Mag toxicity monitoring",
             "Magnesium toxicity monitoring: DTRs checked q1h — present/absent. RR > 12: yes/no. UO > 25mL/hr: yes/no. Calcium gluconate 1g IV at bedside as antidote."),
        ],
    },

    # ── 13. Pulmonary Embolism ───────────────────────────────────────────────
    "POSSIBLE PULMONARY EMBOLISM": {
        "label": "Pulmonary embolism — documentation ready",
        "abbr": "PE",
        "icd10": [
            ("I26.99", "Other pulmonary embolism without acute cor pulmonale"),
            ("I26.09", "Massive PE with acute cor pulmonale"),
            ("I26.90", "Unspecified PE without acute cor pulmonale"),
        ],
        "cpt": [
            ("71275",  "CT pulmonary angiography (CTPA)"),
            ("78582",  "Ventilation-perfusion (V/Q) scan"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("Heparin UFH",    "Heparin 80 U/kg IV bolus, then 18 U/kg/hr infusion (massive PE / high-risk)"),
            ("Enoxaparin",     "Enoxaparin 1 mg/kg SQ q12h (intermediate-risk PE, normal renal function)"),
            ("tPA systemic",   "Alteplase 100mg IV over 2 hours (massive PE with hemodynamic compromise only)"),
            ("Rivaroxaban",    "Rivaroxaban 15mg PO BID × 21 days, then 20mg daily (low/intermediate risk, non-high bleeding risk)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with dyspnea, plexitic chest pain, and/or hypoxia. Wells score: __. CTPA confirmed pulmonary embolism — clot burden: __. RV strain: present/absent. Troponin: __, BNP: __. Risk stratification: low / intermediate-low / intermediate-high / massive. Anticoagulation initiated. Hematology/vascular surgery/IR consulted as appropriate."),
            ("Risk stratification",
             "PESI score: __. Simplified PESI: __. Classification: massive PE (hemodynamic instability) / submassive (RV strain, no instability) / low-risk."),
        ],
    },

    # ── 14. Hypertensive Emergency ───────────────────────────────────────────
    "HYPERTENSIVE EMERGENCY": {
        "label": "Hypertensive emergency — documentation ready",
        "abbr": "HTN",
        "icd10": [
            ("I16.1",  "Hypertensive emergency"),
            ("I16.0",  "Hypertensive urgency"),
            ("I12.9",  "Hypertensive chronic kidney disease"),
        ],
        "cpt": [
            ("99285",  "ED visit, high complexity"),
            ("93000",  "ECG, 12-lead"),
        ],
        "meds": [
            ("Nicardipine",  "Nicardipine 5mg/hr IV infusion, titrate by 2.5mg/hr q5–15min (max 15mg/hr)"),
            ("Labetalol",    "Labetalol 20mg IV over 2 min, may double q10min (max 300mg cumulative)"),
            ("Clevidipine",  "Clevidipine 1–2mg/hr IV, double q90sec (max 32mg/hr) — rapid titratable option"),
            ("Hydralazine",  "Hydralazine 10–20mg IV q4–6h (pregnancy-associated HTN emergency)"),
            ("Fenoldopam",   "Fenoldopam 0.1–0.3 mcg/kg/min IV (preferred if renal protection needed)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with BP __/__. End-organ damage identified: __ (neurological / renal / cardiac / retinal / aortic). Hypertensive emergency confirmed. IV antihypertensive therapy initiated with goal of 20–25% BP reduction in first hour. ICU admission arranged."),
            ("End-organ assessment",
             "End-organ assessment: Neuro exam — __. Fundoscopic exam — __. Creatinine — __. Troponin — __. ECG — __. UA — __."),
        ],
    },

    # ── 15. DKA ──────────────────────────────────────────────────────────────
    "DIABETIC KETOACIDOSIS": {
        "label": "DKA — documentation ready",
        "abbr": "DKA",
        "icd10": [
            ("E11.10", "DKA without coma, type 2"),
            ("E10.10", "DKA without coma, type 1"),
            ("E10.11", "DKA with coma, type 1"),
        ],
        "cpt": [
            ("99285",  "ED visit, high complexity"),
            ("99291",  "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("NS bolus",       "Normal saline 1L IV bolus over 1 hour (initial resuscitation)"),
            ("NS maintenance", "Normal saline 250–500mL/hr IV — adjust based on volume status"),
            ("Insulin drip",   "Regular insulin 0.1 U/kg/hr IV infusion (start after K+ > 3.5 mEq/L confirmed)"),
            ("KCl replacement","KCl 20–40 mEq/hr IV replacement if K+ < 3.5 (hold insulin until K+ > 3.5)"),
            ("D5 addition",    "Add dextrose to IV fluid when BG < 250 mg/dL (switch to D5-0.45%NS to allow continued insulin drip)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with DKA. Glucose: __ mg/dL, pH: __, bicarb: __ mEq/L, anion gap: __, ketones: __. Precipitating factor identified: __ (infection / insulin non-compliance / new diagnosis / other). IV fluids, insulin drip, and electrolyte replacement initiated per DKA protocol."),
            ("Resolution criteria",
             "DKA resolution criteria: glucose < 200 mg/dL AND two of: bicarb ≥ 15 mEq/L, pH ≥ 7.30, anion gap ≤ 12. Transition to SQ insulin when criteria met and patient tolerating PO."),
        ],
    },

    # ── 16. HHS (Hyperosmolar Hyperglycemic State) ───────────────────────────
    "HYPEROSMOLAR HYPERGLYCEMIC STATE": {
        "label": "HHS — documentation ready",
        "abbr": "HHS",
        "icd10": [
            ("E11.01", "Type 2 DM with hyperosmolarity with coma"),
            ("E11.00", "Type 2 DM with hyperosmolarity without coma"),
        ],
        "cpt": [
            ("99285",  "ED visit, high complexity"),
            ("99291",  "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("NS bolus",      "Normal saline 1L IV over 1 hour, then 500mL/hr × 4 hours, then reassess"),
            ("0.45% NS",      "Switch to 0.45% NaCl at 250–500mL/hr once hemodynamically stable"),
            ("Insulin",       "Regular insulin 0.1 U/kg/hr IV only after initial fluid resuscitation (fluid is primary treatment)"),
            ("KCl",           "Potassium replacement per sliding scale — monitor q2–4h"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with HHS. Glucose: __ mg/dL, serum osmolality: __ mOsm/kg, Na: __, BUN: __, Cr: __. Mental status: __. No significant acidosis. Aggressive IV hydration initiated as primary treatment. Insulin initiated after initial fluid bolus."),
        ],
    },

    # ── 17. Severe Asthma / Status Asthmaticus ───────────────────────────────
    "SEVERE ASTHMA": {
        "label": "Severe asthma — documentation ready",
        "abbr": "AST",
        "icd10": [
            ("J45.51", "Severe persistent asthma with acute exacerbation"),
            ("J45.901","Unspecified asthma with acute exacerbation"),
            ("J45.41", "Moderate persistent asthma with acute exacerbation"),
        ],
        "cpt": [
            ("94640",  "Inhalation treatment for acute airway obstruction"),
            ("71046",  "Chest X-ray, 2 views"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("Albuterol",      "Albuterol 2.5mg via nebulizer q20min × 3 doses, then q1–4h (or continuous 10–15mg/hr neb)"),
            ("Ipratropium",    "Ipratropium 0.5mg via nebulizer q20min × 3 doses"),
            ("Methylpred",     "Methylprednisolone 125mg IV × 1 (or prednisone 40–60mg PO if tolerating)"),
            ("Magnesium",      "Magnesium sulfate 2g IV over 20 min × 1 (for severe exacerbation not responding to bronchodilators)"),
            ("Heliox",         "Heliox 70:30 via NRB mask — reduces airway resistance, bridge to definitive treatment"),
            ("Ketamine",       "Ketamine 1–2 mg/kg IV (if intubation required — preferred induction for asthma)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with severe asthma exacerbation. Peak flow: __ L/min (__ % predicted). O2 sat: __% on __L. SpO2 post-treatment: __%. Speaks in __ (full sentences / phrases / words). Respiratory rate: __. Accessory muscle use: __. Serial bronchodilator therapy and systemic steroids administered."),
        ],
    },

    # ── 17.5. SVT ────────────────────────────────────────────────────────────
    "SVT": {
        "label": "Supraventricular tachycardia — documentation ready",
        "abbr": "SVT",
        "icd10": [
            ("I47.10", "Supraventricular tachycardia, unspecified"),
            ("I47.19", "Other supraventricular tachycardia"),
        ],
        "cpt": [
            ("99285",  "ED visit, high complexity"),
            ("93000",  "ECG, 12-lead"),
        ],
        "meds": [
            ("Adenosine",      "Adenosine 6mg rapid IV push, followed by 20mL saline flush (repeat 12mg if no effect)"),
            ("Vagal Maneuvers","Vagal maneuvers: Valsalva, carotid sinus massage, diving reflex (ice water to face)"),
            ("Diltiazem",      "Diltiazem 0.25 mg/kg IV over 2 min (alternative for rate control)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with narrow-complex tachycardia. HR: __. ECG: consistent with SVT. Vagal maneuvers attempted: __. Adenosine administered: __. Patient response: __. Current rhythm: __."),
        ],
    },

    # ── 18. COPD Exacerbation ────────────────────────────────────────────────
    "COPD EXACERBATION": {
        "label": "COPD exacerbation — documentation ready",
        "abbr": "COPD",
        "icd10": [
            ("J44.1",  "COPD with acute exacerbation"),
            ("J44.0",  "COPD with acute lower respiratory infection"),
        ],
        "cpt": [
            ("94640",  "Inhalation treatment for acute airway obstruction"),
            ("71046",  "Chest X-ray, 2 views"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("Albuterol",     "Albuterol 2.5mg via nebulizer q20min × 3 doses"),
            ("Ipratropium",   "Ipratropium 0.5mg via nebulizer q6–8h"),
            ("Prednisone",    "Prednisone 40mg PO daily × 5 days (or methylprednisolone 125mg IV if unable to take PO)"),
            ("Azithromycin",  "Azithromycin 500mg PO/IV × 1, then 250mg daily × 4 days (if infectious trigger)"),
            ("BiPAP",         "BiPAP initiated: IPAP __ / EPAP __ (for moderate-severe exacerbation with respiratory acidosis)"),
        ],
        "note": [
            ("Primary note",
             "Patient with known COPD presented with acute exacerbation — increased dyspnea, sputum production, and/or change in sputum color. Trigger: __ (infection / environmental / medication non-compliance / unknown). O2 saturation: __% on __L (target 88–92%). ABG: pH __, pCO2 __, pO2 __. Bronchodilators and steroids administered."),
        ],
    },

    # ── 19. GI Bleed ─────────────────────────────────────────────────────────
    "GI BLEED": {
        "label": "GI hemorrhage — documentation ready",
        "abbr": "GIB",
        "icd10": [
            ("K92.2",  "GI hemorrhage, unspecified"),
            ("K92.0",  "Hematemesis"),
            ("K92.1",  "Melena"),
            ("K57.31", "Diverticulosis of large intestine with bleeding"),
        ],
        "cpt": [
            ("43239",  "EGD with biopsy — upper GI"),
            ("45378",  "Colonoscopy, diagnostic"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("PPI",           "Pantoprazole 80mg IV bolus, then 8mg/hr continuous infusion (upper GI bleed)"),
            ("Octreotide",    "Octreotide 50 mcg IV bolus, then 50 mcg/hr infusion (variceal bleed suspected)"),
            ("Ceftriaxone",   "Ceftriaxone 1g IV q24h (cirrhotic patients with GI bleed — SBP prophylaxis)"),
            ("pRBC",          "Packed RBC transfusion — threshold Hgb < 7 g/dL (< 8 if ACS or hemodynamic instability)"),
            ("TXA",           "Tranexamic acid — NOT routinely recommended for GI bleed per current evidence"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with __ (hematemesis / melena / hematochezia). Hemodynamic status: HR __, BP __. Hgb: __ g/dL. GI consulted for urgent endoscopy. Resuscitation initiated with IV fluids and blood products. IV PPI initiated. Coagulopathy: INR __, platelets __."),
            ("Glasgow-Blatchford",
             "Glasgow-Blatchford score: __. High-risk features: __ (hemodynamic instability / Hgb < 8 / BUN > 18 / melena / syncope / liver disease / cardiac failure)."),
        ],
    },

    # ── 20. Ectopic Pregnancy ────────────────────────────────────────────────
    "RUPTURED ECTOPIC": {
        "label": "Ectopic pregnancy — documentation ready",
        "abbr": "EcP",
        "icd10": [
            ("O00.90", "Ectopic pregnancy, unspecified, without intrauterine pregnancy"),
            ("O00.10", "Tubal pregnancy, without intrauterine pregnancy"),
        ],
        "cpt": [
            ("76817",  "Transvaginal ultrasound, obstetric"),
            ("59121",  "Surgical treatment of ectopic pregnancy, without salpingectomy"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("NS bolus",    "Normal saline 1–2L IV bolus for hemodynamic stabilization"),
            ("pRBC",        "Type and crossmatch — transfuse as needed for hemorrhagic shock"),
            ("Methotrexate","Methotrexate 50 mg/m² IM single dose (medical management only if hemodynamically stable, no rupture, bhCG < 5,000)"),
            ("Rh immune",   "Rh immunoglobulin 300 mcg IM if Rh-negative"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with pelvic pain and vaginal bleeding. Beta-hCG: __ mIU/mL. Transvaginal ultrasound: no intrauterine pregnancy identified, __ (adnexal mass / free fluid / other). Ectopic pregnancy confirmed / suspected. OB/GYN consulted for emergent evaluation. Hemodynamic status: __."),
        ],
    },

    # ── 21. Stroke Hemorrhagic ───────────────────────────────────────────────
    "HEMORRHAGIC STROKE": {
        "label": "Hemorrhagic stroke / ICH — documentation ready",
        "abbr": "ICH",
        "icd10": [
            ("I61.9",  "Hemorrhagic stroke, unspecified"),
            ("I61.0",  "Intracerebral hemorrhage in hemisphere, subcortical"),
            ("I60.9",  "Subarachnoid hemorrhage, unspecified"),
        ],
        "cpt": [
            ("70450",  "CT head without contrast"),
            ("70496",  "CT angiography, head"),
            ("99291",  "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("Labetalol",    "Labetalol 10–20mg IV q10–15min PRN SBP > 180 (target SBP < 140–160)"),
            ("Nicardipine",  "Nicardipine 5mg/hr IV infusion, titrate to target BP"),
            ("Mannitol",     "Mannitol 1 g/kg IV over 20 min (for herniation / elevated ICP)"),
            ("Keppra",       "Levetiracetam 1,000mg IV load for seizure prophylaxis (lobar ICH)"),
            ("Reversal",     "Anticoagulation reversal per agent: Warfarin — Vit K 10mg IV + 4F-PCC; DOAC — specific reversal agent per formulary"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with acute neurological deficit. CT head demonstrated __ hemorrhage, volume approximately __ mL, location: __. Midline shift: __ mm. Intraventricular extension: __. Neurosurgery consulted. BP management initiated. Anticoagulation reversed if applicable. ICU admission arranged."),
            ("ICH score",
             "ICH score: GCS __ (__ pts) + ICH volume __ mL (__ pts) + IVH __ (__ pts) + infratentorial __ (__ pts) + age __ (__ pts) = Total __."),
        ],
    },

    # ── 22. Hyperkalemia ─────────────────────────────────────────────────────
    "HYPERKALEMIA": {
        "label": "Hyperkalemia — documentation ready",
        "abbr": "HiK",
        "icd10": [
            ("E87.5",  "Hyperkalemia"),
            ("E11.649","Type 2 DM with hypoglycemia without coma"),
        ],
        "cpt": [
            ("93010",  "ECG, 12-lead"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("Calcium gluconate", "Calcium gluconate 1g IV over 5–10 min (cardiac membrane stabilization — first line if ECG changes)"),
            ("Insulin + D50",     "Regular insulin 10 U IV + Dextrose 50% 50mL IV (onset 20–30 min, lasts 4–6h)"),
            ("Albuterol neb",     "Albuterol 10–20mg via nebulizer (adjunct — shifts K+ intracellularly)"),
            ("Sodium bicarb",     "Sodium bicarbonate 50–100 mEq IV (if metabolic acidosis present)"),
            ("Kayexalate",        "Sodium polystyrene sulfonate 15–30g PO (eliminates K+ — slow onset, not for acute management)"),
            ("Patiromer",         "Patiromer 8.4g PO daily (preferred outpatient K+ binder — not for acute use)"),
            ("Dialysis",          "Emergent hemodialysis — for refractory hyperkalemia, K+ > 6.5 with symptoms, or renal failure"),
        ],
        "note": [
            ("Primary note",
             "Patient found to have hyperkalemia — K+ __ mEq/L. ECG changes: __ (peaked T waves / PR prolongation / wide QRS / sine wave / other / none). Etiology: __ (AKI / CKD / medication-related / other). Cardiac membrane stabilization, transcellular shift, and elimination therapy initiated."),
        ],
    },

    # ── 23. Acute Liver Failure ──────────────────────────────────────────────
    "ACUTE LIVER FAILURE": {
        "label": "Acute liver failure — documentation ready",
        "abbr": "ALF",
        "icd10": [
            ("K72.00", "Acute and subacute hepatic failure without coma"),
            ("K72.01", "Acute and subacute hepatic failure with coma"),
            ("K71.10", "Toxic liver disease with hepatic necrosis, without coma"),
        ],
        "cpt": [
            ("99291",  "Critical care, first 30–74 min"),
            ("76700",  "Abdominal ultrasound"),
        ],
        "meds": [
            ("NAC",          "N-acetylcysteine 150 mg/kg IV over 60 min (load), then 12.5 mg/kg/hr × 4h, then 6.25 mg/kg/hr × 16h (acetaminophen toxicity — also beneficial in non-acetaminophen ALF)"),
            ("Lactulose",    "Lactulose 25mL PO/NG q1–2h (target 2–4 soft stools/day for hepatic encephalopathy)"),
            ("Rifaximin",    "Rifaximin 550mg PO BID (adjunct for hepatic encephalopathy)"),
            ("Vit K",        "Vitamin K 10mg IV × 1 (for coagulopathy)"),
            ("Dextrose",     "Dextrose 10% continuous infusion for hypoglycemia prevention"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with acute liver failure. INR: __, total bilirubin: __, AST: __, ALT: __, ammonia: __. Mental status: __. Etiology: __ (acetaminophen / viral / ischemic / autoimmune / unknown). Liver transplant team consulted. NAC infusion initiated. ICU admission arranged."),
        ],
    },

    # ── 24. Traumatic Brain Injury ───────────────────────────────────────────
    "SIGNIFICANT HEAD TRAUMA": {
        "label": "Traumatic brain injury — documentation ready",
        "abbr": "TBI",
        "icd10": [
            ("S09.90", "Unspecified injury of head"),
            ("S06.9",  "Unspecified intracranial injury"),
            ("S06.0X", "Concussion"),
        ],
        "cpt": [
            ("70450",  "CT head without contrast"),
            ("99285",  "ED visit, high complexity"),
            ("99291",  "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("Mannitol",      "Mannitol 0.5–1 g/kg IV over 20 min (for herniation signs / GCS < 8 with acute deterioration)"),
            ("Hypertonic NS",  "3% NaCl 250mL IV over 30 min (alternative to mannitol for ICP management)"),
            ("Levetiracetam", "Levetiracetam 1,000mg IV load (seizure prophylaxis for severe TBI × 7 days)"),
            ("TXA",           "Tranexamic acid 1g IV over 10 min within 3 hours of injury (for traumatic hemorrhage)"),
        ],
        "note": [
            ("Primary note",
             "Patient sustained TBI via mechanism: __. GCS on arrival: __ (E__ V__ M__). Pupils: __. CT head: __. Neurosurgery consulted. ICP management initiated. C-spine cleared / immobilized pending imaging. Secondary survey completed."),
            ("GCS documentation",
             "GCS: Eye opening __ / Verbal response __ / Motor response __ = Total __. Pupil response: Right __ mm __, Left __ mm __."),
        ],
    },

    # ── 25. Hypothermia ──────────────────────────────────────────────────────
    "SEVERE HYPOTHERMIA": {
        "label": "Severe hypothermia — documentation ready",
        "abbr": "HyP",
        "icd10": [
            ("T68",    "Hypothermia"),
            ("T69.01", "Immersion hand and foot"),
        ],
        "cpt": [
            ("99285",  "ED visit, high complexity"),
            ("93010",  "ECG, 12-lead"),
        ],
        "meds": [
            ("Warm NS",       "Warm normal saline (42°C) IV fluids — avoid rapid large volume in cardiac hypothermia"),
            ("Dextrose",      "Dextrose 50% 50mL IV if hypoglycemia confirmed"),
            ("Thiamine",      "Thiamine 100mg IV prior to dextrose if alcohol use or malnutrition suspected"),
            ("Epinephrine",   "Epinephrine — withhold until core temp > 30°C (refractory VF); double intervals if used below 30°C"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with core temperature: __°C (__ stage: mild 32–35 / moderate 28–32 / severe < 28). Mechanism of exposure: __. Cardiac rhythm: __. Active rewarming initiated. ECMO considered for cardiac arrest with hypothermia (rewarming at 1–2°C per hour with active internal rewarming)."),
            ("Rewarming method",
             "Rewarming method: passive (mild) / active external (moderate) / active internal — warm IV fluids, warm humidified O2, bladder irrigation / ECMO (cardiac arrest). Target rewarming rate: 1–2°C per hour."),
        ],
    },

    # ── 26. Acute Angle Closure Glaucoma ────────────────────────────────────
    "ACUTE ANGLE CLOSURE GLAUCOMA": {
        "label": "Acute angle closure glaucoma — documentation ready",
        "abbr": "AACG",
        "icd10": [
            ("H40.211", "Acute angle-closure glaucoma, right eye"),
            ("H40.212", "Acute angle-closure glaucoma, left eye"),
            ("H40.20",  "Unspecified primary angle-closure glaucoma"),
        ],
        "cpt": [
            ("92020",  "Gonioscopy"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("Timolol drops",   "Timolol 0.5% ophthalmic solution 1 drop affected eye × 1"),
            ("Brimonidine",     "Brimonidine 0.1–0.2% ophthalmic solution 1 drop affected eye × 1"),
            ("Acetazolamide",   "Acetazolamide 500mg IV/PO × 1 (reduces aqueous humor production)"),
            ("Pilocarpine",     "Pilocarpine 1–2% ophthalmic solution 1 drop q15min × 2 (miotic — pulls iris away from angle)"),
            ("Mannitol",        "Mannitol 1–2 g/kg IV over 45 min (if IOP not responding to topical/oral agents)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with acute eye pain, decreased vision, and headache in the setting of mid-dilated pupil. IOP measured: __ mmHg (affected eye) / __ mmHg (contralateral). Corneal edema: present/absent. Ophthalmology consulted urgently. IOP-lowering agents initiated. Laser iridotomy arranged."),
        ],
    },

    # ── 27. Acute Mesenteric Ischemia ────────────────────────────────────────
    "ACUTE MESENTERIC ISCHEMIA": {
        "label": "Mesenteric ischemia — documentation ready",
        "abbr": "AMI",
        "icd10": [
            ("K55.059", "Acute (reversible) ischemia of large intestine, extent unspecified"),
            ("K55.019", "Acute infarction of small intestine, extent unspecified"),
            ("K55.1",   "Chronic vascular disorders of intestine"),
        ],
        "cpt": [
            ("74175",  "CT angiography, abdomen"),
            ("99285",  "ED visit, high complexity"),
            ("99291",  "Critical care, first 30–74 min"),
        ],
        "meds": [
            ("NS bolus",     "Normal saline 1–2L IV bolus resuscitation"),
            ("Heparin UFH",  "Heparin 80 U/kg IV bolus, then 18 U/kg/hr infusion (for thromboembolic etiology)"),
            ("Pip-Tazo",     "Piperacillin-tazobactam 3.375g IV q6h (bowel ischemia — broad spectrum coverage)"),
            ("Metronidazole","Metronidazole 500mg IV q8h (anaerobic coverage if perforation suspected)"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with severe abdominal pain out of proportion to exam. CT angiography: __. Suspected etiology: __ (arterial embolism / arterial thrombosis / venous thrombosis / NOMI). Vascular surgery and GI surgery consulted immediately. Anticoagulation initiated. NPO, IV access, monitoring."),
        ],
    },

    # ── 28. Carbon Monoxide Poisoning ────────────────────────────────────────
    "CO POISONING": {
        "label": "Carbon monoxide poisoning — documentation ready",
        "abbr": "CO",
        "icd10": [
            ("T58.91", "Toxic effects of CO from unspecified source, accidental"),
            ("T58.01", "Toxic effects of CO from motor vehicle exhaust, accidental"),
        ],
        "cpt": [
            ("99285",  "ED visit, high complexity"),
            ("99183",  "Physician attendance for hyperbaric oxygen therapy"),
        ],
        "meds": [
            ("100% O2",      "100% oxygen via non-rebreather mask at 15L/min (or intubation with FiO2 1.0 if altered) — continue until COHgb < 5% and asymptomatic"),
            ("HBO therapy",  "Hyperbaric oxygen therapy — indicated for: COHgb > 25%, loss of consciousness, neurological symptoms, cardiac involvement, or pregnancy. Contact HBO center: __."),
        ],
        "note": [
            ("Primary note",
             "Patient presented with CO poisoning. Source: __. COHgb level: __%. Symptoms: headache / nausea / confusion / syncope / chest pain. ECG: __. Troponin: __. All household members / co-exposed persons notified. 100% O2 initiated. HBO therapy evaluated — indicated: yes / no — reason: __."),
        ],
    },

    # ── 29. POSSIBLE APPENDICITIS (Warning level) ────────────────────────────
    "POSSIBLE APPENDICITIS": {
        "label": "Appendicitis — documentation ready",
        "abbr": "App",
        "icd10": [
            ("K37",    "Unspecified appendicitis"),
            ("K35.80", "Acute appendicitis without abscess"),
            ("K35.20", "Acute appendicitis with generalized peritonitis"),
        ],
        "cpt": [
            ("74177",  "CT abdomen and pelvis with contrast"),
            ("76705",  "Ultrasound, abdominal limited"),
            ("99285",  "ED visit, high complexity"),
        ],
        "meds": [
            ("NPO",          "Patient made NPO — IV access established, IV fluids initiated"),
            ("Ceftriaxone",  "Ceftriaxone 2g IV q24h (pre-op coverage or non-operative management)"),
            ("Metronidazole","Metronidazole 500mg IV q8h (anaerobic coverage)"),
            ("Ketorolac",    "Ketorolac 30mg IV × 1 (adequate analgesia — does not mask diagnosis or delay care)"),
            ("Morphine",     "Morphine 0.1 mg/kg IV q4h PRN — analgesia does not worsen outcomes and should not be withheld"),
        ],
        "note": [
            ("Primary note",
             "Patient presented with RLQ pain, fever, and elevated WBC consistent with acute appendicitis. Alvarado score: __. CT abdomen/pelvis: __. Surgery consulted. Patient made NPO. IV antibiotics initiated. Operative versus non-operative management discussed."),
            ("Alvarado score",
             "Alvarado score: migratory pain to RLQ __ + anorexia __ + nausea/vomiting __ + RLQ tenderness __ + rebound tenderness __ + elevated temp __ + leukocytosis __ + shift to left __ = Total __ / 10."),
        ],
    },
}

def get_doc_bundle(syndrome_name: str) -> dict | None:
    if not syndrome_name: return None
    return SYNDROME_DOC_BUNDLES.get(syndrome_name.upper().strip())

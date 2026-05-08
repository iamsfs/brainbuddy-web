# =========================================================
# clinical_engine.py — BrainBuddy Medical Data Layer
# Contains: SymptomLibrary (ontology, synonyms, weights,
#           DIAGNOSES, SYNDROMES)
# Edit this file to add/remove symptoms and conditions.
# =========================================================

import re

class SymptomLibrary:

	ONTOLOGY = {

		# ── CARDIOVASCULAR ───────────────────────────────────────────
		"cardiovascular": {
			"chest pain":              ["chest pain", "cp", "chest pressure", "tight chest", "angina", "chest tightness", "chest discomfort", "sternal pain", "precordial pain", "chest pain (finding)", "pressure in chest", "tight chest (finding)", "chest discomfort (finding)", "precordial pain (finding)", "centipoise", "centipoise (qualifier value)", "cp - centipoise", "angina (disorder)", "angina pectoris", "anginal syndrome", "ap - angina pectoris", "cardiac angina", "ischemic heart disease - angina", "stenocardia", "acute chest pain", "anterior chest wall pain", "atypical chest pain", "burning chest pain", "cardiac chest pain", "central chest pain", "central crushing chest pain", "chest pain at rest", "chest pain not present", "chest pain on breathing", "chest pain on exertion", "chest wall pain", "chronic chest pain", "chronic primary chest pain syndrome", "costal margin chest pain", "crushing chest pain", "dull chest pain", "esophageal chest pain", "ischemic chest pain", "left sided chest pain", "localized chest pain", "musculoskeletal chest pain", "non-cardiac chest pain", "pain radiating to center of chest", "pleuropericardial chest pain", "radiating chest pain", "right sided chest pain", "squeezing chest pain", "upper chest pain", "acute chest pain (finding)", "anterior chest wall pain (finding)", "atypical chest pain (finding)", "burning chest pain (finding)", "cardiac chest pain (finding)", "central chest pain (finding)", "central crushing chest pain (finding)", "chest pain at rest (finding)", "chest pain not present (situation)", "chest pain on breathing (finding)", "chest pain on exertion (finding)", "chest wall pain (finding)", "chronic chest pain (finding)", "chronic noncardiac chest pain", "chronic primary chest pain syndrome (disorder)", "chronic primary visceral pain in thoracic region", "costal margin chest pain (finding)", "crushing chest pain (finding)", "dull chest pain (finding)", "esophageal chest pain (finding)", "ischemic chest pain (finding)", "left sided chest pain (finding)", "localized chest pain (finding)", "musculoskeletal chest pain (finding)", "non-cardiac chest pain (finding)", "noncardiac chest pain", "pain radiating to center of chest (finding)", "pleuropericardial chest pain (finding)", "radiating chest pain (finding)", "right sided chest pain (finding)", "squeezing chest pain (finding)", "upper chest pain (finding)"],
			"palpitations":            ["palpitations", "heart fluttering", "heart pounding", "heart racing", "irregular heartbeat", "skipping beats", "palpitations (finding)", "intermittent palpitations", "palpitations - rapid", "palpitations with regular rhythm", "intermittent palpitations (finding)", "palpitations - rapid (finding)", "palpitations with regular rhythm (finding)"],
			"rapid heart rate":        ["rapid heart rate", "tachycardia", "racing heart", "fast pulse", "heart rate high", "hr elevated", "fast heart", "svt", "heart rate fast", "increased heart rate", "rapid heart beat", "tachycardia (finding)"],
			"slow heart rate":         ["slow heart rate", "bradycardia", "low pulse", "slow pulse", "heart rate low", "hr low", "bradycardia (finding)", "decreased heart rate", "heart rate slow", "slow heart beat"],
			"irregular heart rate":    ["irregular heart rate", "arrhythmia", "afib", "atrial fibrillation", "irregular pulse", "uneven heartbeat", "af - atrial fibrillation", "atrial fibrillation (disorder)", "cardiac arrhythmia", "cardiac arrhythmia (disorder)", "cardiac dysrhythmia", "disorder of heart rhythm", "pulse irregular", "pulse irregular (finding)"],
			"fainting":                ["fainting", "syncope", "passed out", "blacked out", "fainted", "collapsed", "pre-syncope", "near faint", "blackout", "faint", "syncope (finding)", "syncope attack", "collapsed (qualifier value)", "fear of fainting", "fear of fainting (finding)"],
			"leg swelling":            ["leg swelling", "edema", "swollen legs", "ankle swelling", "lower extremity edema", "pitting edema", "swollen ankles", "edema (finding)", "edema (morphologic abnormality)", "edema - lesion", "edematous", "interstitial edema", "swollen ankle", "swollen ankle (finding)", "swollen ankle region", "pitting edema (finding)", "pitting edema (morphologic abnormality)", "leg swelling symptom", "localized swelling of left lower leg", "localized swelling of right lower leg", "swelling of lower leg", "leg swelling symptom (finding)", "localized swelling of left lower leg (finding)", "localized swelling of right lower leg (finding)", "swelling of lower leg (finding)"],
			"jaw pain":                ["jaw pain", "jaw tightness", "pain radiating to jaw", "jaw ache", "jaw pain (finding)", "pain of jaw", "pain radiating to jaw (finding)"],
			"arm pain":                ["arm pain", "left arm pain", "pain radiating to arm", "left arm ache", "arm numbness", "pain in left arm", "pain in muscle of upper arm", "pain in right arm", "pain in upper arm", "pain of left upper arm", "pain of right upper arm", "pain radiating to left arm", "pain radiating to right arm", "pain in left arm (finding)", "pain in left upper limb", "myalgia of upper arm", "pain in muscle of upper arm (finding)", "pain in right arm (finding)", "pain in right upper limb", "pain in upper arm (finding)", "pain of left upper arm (finding)", "pain of right upper arm (finding)", "pain radiating to left arm (finding)", "pain radiating to right arm (finding)"],
			"heart murmur":            ["heart murmur", "murmur", "finding of heart murmur", "heart murmur (finding)", "heart murmur (observable entity)", "observation of heart murmur", "murmur (finding)", "diastolic murmur at apex of heart", "functional heart murmur", "heart murmur absent", "heart murmur configuration, crescendo-decrescendo", "heart murmur configuration, variable (uneven)", "heart murmur duration, long", "heart murmur duration, short", "heart murmur during pregnancy", "heart murmur in mother in childbirth", "heart murmur pitch, high", "heart murmur pitch, impure (mixed) frequency", "heart murmur pitch, low", "heart murmur pitch, medium", "heart murmur pitch, pure frequency", "heart murmur quality, blowing", "heart murmur quality, buzzing", "heart murmur quality, grating", "heart murmur quality, harsh", "heart murmur quality, humming", "heart murmur quality, musical", "heart murmur quality, rasping", "heart murmur quality, roaring", "heart murmur quality, rumbling", "heart murmur quality, scratchy", "heart murmur quality, squeaking", "heart murmur quality, twanging", "heart murmur quality, vibratory", "organic heart murmur", "postpartum heart murmur", "systolic murmur at apex of heart", "diastolic murmur at apex of heart (finding)", "functional cardiac murmur", "functional flow murmur", "functional heart murmur (finding)", "innocent heart murmur", "heart murmur absent (situation)", "crescendo-decrescendo cardiac murmur", "crescendo-decrescendo cardiac murmur (finding)", "heart murmur configuration, variable (uneven) (finding)", "heart murmur duration, long (finding)", "heart murmur duration, short (finding)", "heart murmur during pregnancy (finding)", "heart murmur in pregnancy", "heart murmur in childbirth", "heart murmur in mother in childbirth (finding)", "heart murmur pitch, high (finding)", "heart murmur pitch, impure (mixed) frequency (finding)", "heart murmur pitch, low (finding)", "heart murmur pitch, medium (finding)", "heart murmur pitch, pure frequency (finding)", "heart murmur quality, blowing (finding)", "heart murmur quality, buzzing (finding)", "heart murmur quality, grating (finding)", "heart murmur quality, harsh (finding)", "heart murmur quality, humming (finding)", "heart murmur quality, musical (finding)", "heart murmur quality, rasping (finding)", "heart murmur quality, roaring (finding)", "heart murmur quality, rumbling (finding)", "heart murmur quality, scratchy (finding)", "heart murmur quality, squeaking (finding)", "squeaking heart murmur quality", "heart murmur quality, twanging (finding)", "heart murmur quality, vibratory (finding)", "organic heart murmur (finding)", "postpartum heart murmur (finding)", "systolic murmur at apex of heart (finding)"],
			"cardiac arrest":          ["cardiac arrest", "no pulse", "pulseless", "no heartbeat", "asystole", "vfib", "ventricular fibrillation", "cardiac arrest (disorder)", "asystole (disorder)", "cardiac standstill", "cardiac arrest - ventricular fibrillation", "ventricular fibrillation (disorder)", "vf - ventricular fibrillation", "absent pulse", "absent pulse (finding)", "can't feel pulse", "cannot feel pulse", "pulselessness", "bradycardic cardiac arrest", "cardiac arrest during cardiac surgery", "cardiac arrest during procedure", "cardiac arrest during surgery", "cardiac arrest location", "cardiac arrest rhythm", "cardiac arrest with successful resuscitation", "fetal cardiac arrest", "in-hospital cardiac arrest", "neonatal cardiac arrest", "out-of-hospital cardiac arrest", "respiratory arrest preceding cardiac arrest", "bradycardic cardiac arrest (disorder)", "cardiac arrest during cardiac surgery (disorder)", "cardiac arrest during procedure (disorder)", "cardiac arrest during surgery (disorder)", "cardiac arrest location (observable entity)", "cardiac arrest rhythm (observable entity)", "cardiac arrest with successful resuscitation (disorder)", "fetal cardiac arrest (disorder)", "neonatal cardiac arrest (disorder)", "respiratory arrest preceding cardiac arrest (disorder)"],
			"orthopnea":               ["orthopnea", "breathless lying flat", "shortness of breath when lying flat", "need to prop up with pillows", "orthopnea (finding)"],
			"hypertension signs":      ["hypertension signs", "elevated blood pressure", "high bp", "systolic high", "pressure elevated", "finding of blood pressure"]
		},

		# ── RESPIRATORY ──────────────────────────────────────────────
		"respiratory": {
			"shortness of breath":     ["shortness of breath", "sob", "breathless", "dyspnea", "cant breathe", "difficulty breathing", "labored breathing", "air hunger", "winded", "short of breath", "breathlessness", "dyspnea (finding)", "sob - shortness of breath", "dib - difficulty in breathing", "difficulty breathing (finding)", "respiration difficult", "labored breathing (finding)", "labored respiration", "air hunger (finding)", "winded (finding)"],
			"cough":                   ["cough", "coughing", "persistent cough", "chronic cough", "dry cough", "productive cough", "hacking cough", "cough (finding)", "observation of cough", "coughing (observable entity)", "persistent cough (finding)", "chronic cough (finding)", "dry cough (finding)", "non-productive cough", "unproductive cough", "bronchial cough", "chesty cough", "loose cough", "moist cough", "producing sputum", "productive cough (finding)", "hacking cough (finding)", "ability to cough", "ability to cough up sputum", "ability to cough voluntarily", "acute cough", "allergic cough", "arnold's nerve reflex cough syndrome", "barking cough", "bovine cough", "brassy cough", "character of cough", "chronic refractory cough", "cough - urge incontinence of urine", "cough after eating", "cough aggravates symptom", "cough at rest", "cough fracture of ribs", "cough headache syndrome", "cough impulse impaired", "cough impulse in inguinal canal", "cough impulse of lump", "cough impulse of mass absent", "cough impulse of mass present", "cough on exercise", "cough reflex", "cough reflex absent", "cough reflex finding", "cough reflex present", "cough strength", "cough suppressant adverse reaction", "cough suppression", "cough variant asthma", "cough when swallowing", "cough with fever", "croupy cough", "does cough", "does cough up sputum", "does not cough", "does not cough up sputum", "dry tickly cough", "early morning cough", "effective cough", "evening cough", "finding related to ability to cough", "increasing frequency of cough", "morning cough", "night cough absent", "night cough present", "nocturnal cough", "nocturnal cough and wheeze", "painful cough", "paroxysmal cough", "postural cough", "postviral cough", "primary cough headache", "productive cough -clear sputum", "productive cough -green sputum", "psychogenic cough", "respiratory tract congestion and cough", "smokers' cough", "spasmodic cough", "subacute cough", "tracheal esophageal fistula cough", "unable to cough", "unable to cough up sputum", "unable to cough voluntarily", "unexplained chronic cough", "unexplained cough", "weavers' cough", "ability to cough (observable entity)", "ability to cough up sputum (observable entity)", "ability to cough voluntarily (observable entity)", "acute cough (finding)", "allergic cough (finding)", "arnold nerve reflex cough syndrome", "arnold's nerve reflex cough syndrome (disorder)", "barking cough (finding)", "bovine cough (finding)", "brassy cough (finding)"],
			"wheezing":                ["wheezing", "whistling breath", "wheeze", "bronchospasm", "asthmatic breath sounds", "asthmatic breathing", "wheezing (finding)", "wheezy", "bronchial spasm", "bronchospasm (finding)", "expiratory wheezing", "inspiratory wheezing", "wheezing stridor", "wheezing symptom", "expiratory wheeze", "expiratory wheezing (finding)", "inspiratory wheeze", "inspiratory wheezing (finding)", "wheezing stridor (finding)", "wheezing symptom (finding)"],
			"hemoptysis":              ["hemoptysis", "coughing blood", "blood in sputum", "bloody cough", "coughing up blood", "hemoptysis (finding)", "perinatal hemoptysis of fetus and/or neonate", "perinatal hemoptysis", "perinatal hemoptysis of fetus and/or neonate (finding)"],
			"stridor":                 ["stridor", "high pitched breathing", "noisy breathing", "inspiratory stridor", "crowing sound", "stridor (finding)", "stridulous breathing", "inspiratory stridor (finding)", "noisy respiration", "noisy respiration (finding)", "biphasic stridor", "congenital laryngeal stridor", "expiratory stridor", "intermittent stridor", "laryngeal stridor", "wheezing stridor", "biphasic stridor (finding)", "congenital laryngeal stridor (disorder)", "expiratory stridor (finding)", "intermittent stridor (finding)", "laryngeal stridor (finding)", "wheezing stridor (finding)"],
			"pleuritic chest pain":    ["pleuritic chest pain", "sharp chest pain", "pain with breathing", "chest pain on inspiration", "worse with breathing", "pain worse on breathing", "pain on deep breath"],
			"respiratory failure":     ["respiratory failure", "not breathing", "apnea", "respiratory arrest", "agonal breathing", "respiratory failure (disorder)", "apnea (finding)", "apneic", "has stopped breathing", "respiratory arrest (disorder)", "acute hypercapnic respiratory failure", "acute hypoxemic respiratory failure", "acute on chronic hypercapnic respiratory failure", "acute on chronic hypoxemic respiratory failure", "acute respiratory failure", "acute respiratory failure requiring reintubation", "acute-on-chronic respiratory failure", "chronic hypercapnic respiratory failure", "chronic hypoxemic respiratory failure", "chronic respiratory failure", "hereditary myopathy with early respiratory failure", "hypercapnic respiratory failure", "hypoxemic respiratory failure", "neonatal respiratory failure", "postprocedural respiratory failure", "respiratory failure in early neonatal period", "sleep-related respiratory failure", "acute hypercapnic respiratory failure (disorder)", "acute type 2 respiratory failure", "acute type ii respiratory failure", "acute hypoxemic respiratory failure (disorder)", "acute type 1 respiratory failure", "acute type i respiratory failure", "acute-on-chronic hypercapnic respiratory failure", "acute-on-chronic hypercapnic respiratory failure (disorder)", "acute-on-chronic hypoxemic respiratory failure", "acute-on-chronic hypoxemic respiratory failure (disorder)", "acute respiratory failure (disorder)", "arf - acute respiratory failure", "acute respiratory failure requiring reintubation (disorder)", "acute on chronic respiratory failure", "acute-on-chronic respiratory failure (disorder)", "chronic hypercapnic respiratory failure (disorder)", "chronic type 2 respiratory failure", "chronic type ii respiratory failure", "chronic hypoxemic respiratory failure (disorder)", "chronic type 1 respiratory failure", "chronic type i respiratory failure", "chronic respiratory failure (disorder)", "edstrom myopathy", "hereditary myopathy with early respiratory failure (disorder)", "hereditary proximal myopathy with early respiratory failure", "hmerf - hereditary myopathy with early respiratory failure", "mprm - myopathy, proximal, with early respiratory muscle involvement", "hypercapnic respiratory failure (disorder)", "type 2 respiratory failure", "type ii respiratory failure", "hypoxemic respiratory failure (disorder)", "type 1 respiratory failure", "type i respiratory failure", "neonatal respiratory failure (disorder)", "postprocedural respiratory failure (disorder)", "early neonatal respiratory failure", "respiratory failure in early neonatal period (disorder)", "sleep-related respiratory failure (disorder)"],
			"hypoxia":                 ["hypoxia", "low oxygen", "low o2 sat", "oxygen saturation low", "spo2 low", "desaturation", "decreased oxygen supply", "hypoxia (disorder)", "hypoxic", "antepartum fetal hypoxia", "corneal hypoxia", "dialysis-associated hypoxia", "fetal hypoxia", "hypoxia of brain", "hypoxia with feeding in newborn", "intrapartum fetal hypoxia", "intrauterine hypoxia", "liveborn with labor hypoxia", "liveborn with prelabor hypoxia", "perinatal hypoxia", "antepartum fetal hypoxia (disorder)", "antepartum foetal hypoxia", "corneal hypoxia (disorder)", "dialysis-associated hypoxia (disorder)", "fetal hypoxia (disorder)", "cerebral hypoxia", "hypoxia of brain (disorder)", "hypoxia with feeding in newborn (finding)", "birth hypoxia", "intrapartum fetal hypoxia (disorder)", "intrapartum foetal hypoxia", "intrauterine hypoxia (disorder)", "liveborn with labor hypoxia (finding)", "liveborn with prelabor hypoxia (finding)", "perinatal hypoxia (disorder)"],
			"tachypnea":               ["tachypnea", "rapid breathing", "fast breathing", "increased respiratory rate", "breathing fast", "rapid respiration", "tachypnea (finding)", "tachypneic", "mild neonatal transient tachypnea", "neonatal transitory tachypnea", "severe neonatal transient tachypnea", "sleep-related neurogenic tachypnea", "sleep-related neurogenic tachypnea (disorder)"],
			"cyanosis":                ["cyanosis", "blue lips", "bluish skin", "blue fingertips", "perioral cyanosis", "cyanosis (finding)", "blue lips (finding)", "central cyanosis", "cyanosis of skin", "cyanosis of skin over lesion", "hemoglobinopathy with cyanosis", "local cyanosis", "neonatal cyanosis", "peripheral cyanosis", "pulmonary cyanosis", "toxic methemoglobinemia with cyanosis", "central cyanosis (disorder)", "cyanosed", "cyanosis of skin (finding)", "cyanosis of skin over lesion (finding)", "hemoglobinopathy with cyanosis (disorder)", "local cyanosis (finding)", "neonatal cyanosis (disorder)", "peripheral cyanosis (finding)", "pulmonary cyanosis (disorder)", "toxic methemoglobinemia with cyanosis (disorder)"],
		},

		# ── NEUROLOGICAL ─────────────────────────────────────────────
		"neurological": {
			"headache":                ["headache", "migraine", "head pain", "cephalalgia", "head ache", "skull pain", "cranial pain", "cephalgia", "cephalodynia", "ha - headache", "headache (finding)", "pain in head", "migraine (disorder)", "aching headache", "acute headache", "acute posttraumatic headache", "allergic headache", "analgesic overuse headache", "atypical cluster headache", "aural headache", "benign coital headache", "bilateral headache", "cervicogenic headache", "chronic cluster headache", "chronic cluster headache unremitting from onset", "chronic headache disorder", "chronic mixed headache syndrome", "chronic post-concussion headache", "chronic post-traumatic headache", "chronic primary headache", "chronic tension-type headache", "cluster headache", "cough headache syndrome", "daily headache", "dental headache", "drug withdrawal headache", "episodic cluster headache", "episodic tension-type headache", "frequent episodic tension-type headache", "frequent headache", "frontal headache", "generalized headache", "headache character", "headache character - finding", "headache disorder", "hindbrain hernia headache", "hypnic headache", "idiopathic stabbing headache", "infrequent episodic tension-type headache", "intermittent headache", "intractable chronic tension headache", "low pressure headache", "medication overuse headache", "menopausal headache", "migraine aura without headache", "migraine variant with headache", "morning headache", "muscular headache", "nasal headache", "new daily persistent headache", "nummular headache", "occipital headache", "ocular headache", "orthostatic headache", "parietal headache", "post dural puncture headache", "postpartum headache", "postseizure headache", "posttraumatic headache", "primary cough headache", "primary exercise headache", "primary thunderclap headache", "psychogenic headache", "recurrent thunderclap headache", "shooting headache", "sick headache", "sinus headache", "temporal headache", "tension-type headache", "throbbing headache", "thunderclap headache", "unilateral headache", "unilateral left sided headache", "unilateral right sided headache", "vascular headache", "viral headache", "aching headache (finding)", "acute headache (finding)", "acute posttraumatic headache (finding)", "allergic headache (disorder)", "analgesic overuse headache (finding)", "atypical cluster headache (disorder)", "aural headache (finding)", "benign coital headache (finding)", "bilateral headache (finding)", "cervicogenic headache (finding)", "chronic cluster headache (disorder)", "chronic cluster headache unremitting from onset (disorder)", "chronic headache disorder (disorder)", "chronic mixed headache syndrome (disorder)"],
			"thunderclap headache":    ["thunderclap headache", "worst headache of life", "sudden severe headache", "explosive headache", "10/10 headache", "thunderclap headache (disorder)", "primary thunderclap headache", "recurrent thunderclap headache", "primary thunderclap headache (disorder)"],
			"dizziness":               ["dizziness", "dizzy", "lightheaded", "vertigo", "room spinning", "spinning", "giddiness", "off balance", "dizziness (finding)", "rotary vertigo", "rotatory vertigo", "vertigo (finding)", "vertigo (spinning sensation)", "giddiness (finding)", "feels light headed", "light-headedness", "lightheadedness", "lightheadedness (finding)", "wooziness", "dizziness and giddiness", "dizziness of unknown cause", "dizziness on standing up", "dizziness present", "exertional dizziness", "multisensory dizziness", "persistent postural perceptual dizziness", "postural dizziness", "dizziness - giddy", "dizziness and giddiness (finding)", "dizziness of unknown cause (finding)", "dizziness on standing up (finding)", "dizziness present (situation)", "exertional dizziness (finding)", "multisensory dizziness (disorder)", "chronic subjective dizziness", "persistent postural perceptual dizziness (finding)", "phobic postural vertigo", "pppd - persistent postural perceptual dizziness", "visual vertigo", "visually-induced vertigo", "postural dizziness (finding)"],
			"facial_droop":            ["facial droop", "drooping face", "face drooping", "uneven smile", "crooked mouth", "facial asymmetry", "drooping eyelid", "ptosis"],
			"unilateral_weakness":     ["unilateral weakness", "right sided weakness", "left sided weakness"],
			"slurred_speech":          ["slurred speech", "trouble speaking", "dysarthria", "cant speak clearly", "speech difficulty", "speech slurred", "garbled speech", "clipped speech", "scamping speech", "slurred speech (finding)", "slurring", "dysarthria (finding)", "episodic ataxia with slurred speech", "episodic ataxia type 8", "episodic ataxia with slurred speech (disorder)"],
			"aphasia":                 ["aphasia", "cant find words", "word finding difficulty", "not making sense", "incoherent speech", "confused speech", "aphasia (finding)", "aphasic disturbance", "loss of power of expression or comprehension", "incoherent articulation", "incoherent speech (finding)", "lexical retrieval deficit", "word finding difficulty (disorder)", "alzheimer's disease with progressive aphasia", "anomic aphasia", "associative aphasia", "auditory discrimination aphasia", "combined aphasia", "complete aphasia", "conduction aphasia", "developmental aphasia", "fluent aphasia", "functional aphasia", "gibberish aphasia", "global aphasia", "graphomotor aphasia", "intellectual aphasia", "logopenic progressive aphasia", "motor aphasia", "parieto-occipital aphasia", "pathematic aphasia", "posttraumatic aphasia", "primary progressive non fluent aphasia", "progressive aphasia", "semantic aphasia", "subcortical aphasia", "syntactical aphasia", "temporal lobe aphasia", "transcortical aphasia", "alzheimer's disease with progressive aphasia (disorder)", "progressive aphasia in alzheimer disease", "progressive aphasia in alzheimer's disease", "amnesic aphasia", "amnestic aphasia", "anomia", "anomic aphasia (finding)", "anomic dysphasia", "dysnomia", "nominal aphasia", "nominal dysphasia", "associative aphasia (finding)", "aphememesthesia", "auditory aphasia", "auditory discrimination aphasia (disorder)", "logokophosis", "word deafness", "combined aphasia (finding)", "complete aphasia (finding)", "conduction aphasia (finding)", "conduction dysphasia", "developmental aphasia (disorder)", "fluent aphasia (finding)", "fluent dysphasia", "functional aphasia (finding)", "gibberish aphasia (finding)", "jargon aphasia", "central aphasia", "cortical aphasia", "expressive-receptive aphasia", "global aphasia (finding)", "global dysphasia", "pictorial aphasia", "graphomotor aphasia (finding)", "intellectual aphasia (finding)", "true aphasia", "logopenic progressive aphasia (disorder)", "frontocortical aphasia", "motor aphasia (finding)", "alexia plus apraxia", "parieto-occipital aphasia (finding)", "pathematic aphasia (finding)", "posttraumatic aphasia (finding)", "primary progressive non fluent aphasia (disorder)", "progressive non-fluent aphasia", "progressive aphasia (disorder)", "semantic aphasia (finding)", "subcortical aphasia (finding)", "syntactic difficulties", "syntactic impairment", "syntactical aphasia (finding)", "temporal lobe aphasia (finding)", "transcortical aphasia (finding)"],
			"vision loss":             ["vision loss", "blurry vision", "vision blurred", "cant see", "loss of vision", "visual disturbance", "double vision", "diplopia", "amaurosis", "floaters", "flashes of light", "photopsia", "curtain", "veil", "vision curtain", "visual disturbance (disorder)", "diplopia (disorder)", "seeing double", "amaurosis (disorder)", "blurred vision", "blurring of visual image", "blurring of visual image (finding)"],
			"arm weakness":            ["arm weakness", "weak arm", "arm paralysis", "hemiparesis", "one sided weakness", "arm giving out", "hand weakness", "hemiparesis (disorder)", "hemiparesis (weakness on one side)", "weakness of one side of body", "muscle weakness of upper arm", "muscle weakness of upper arm (finding)"],
			"leg weakness":            ["leg weakness", "weak leg", "leg paralysis", "cant walk", "lower extremity weakness", "legs giving out", "weakness of muscle of lower leg", "weakness of muscle of lower leg (finding)"],
			"seizure":                 ["seizure", "convulsion", "shaking", "fitting", "epilepsy", "tonic clonic", "grand mal", "absence seizure", "postictal", "fit", "fit - convulsion", "seizure (finding)", "fitting procedure", "fitting procedure (procedure)", "epilepsy (disorder)", "absence seizure (finding)", "gas - generalized absence seizure", "generalized non-motor seizure", "generalized onset non-motor seizure", "generalized-onset non-motor seizure", "has a tremor", "involuntary quiver", "involuntary trembling", "quivering", "shakes", "shaking all over", "the shakes", "trembling", "tremor", "tremor (finding)", "absence seizure with eyelid myoclonia", "acute symptomatic epileptic seizure", "anoxic seizure", "atonic epileptic seizure", "atypical absence seizure", "behavior arrest epileptic seizure", "benign focal seizure of adolescence", "clonic epileptic seizure", "complex febrile seizure", "date of last seizure", "duration of seizure", "eeg abnormality with seizure", "eeg abnormality without seizure", "epileptic seizure", "epileptic seizure witnessed by history provider", "focal onset atonic epileptic seizure", "focal onset automatism epileptic seizure", "focal onset autonomic epileptic seizure", "focal onset aware atonic epileptic seizure", "focal onset aware automatism epileptic seizure", "focal onset aware autonomic epileptic seizure", "focal onset aware clonic epileptic seizure", "focal onset aware cognitive epileptic seizure", "focal onset aware emotional epileptic seizure", "focal onset aware epileptic seizure", "focal onset aware hyperkinetic epileptic seizure", "focal onset aware myoclonic epileptic seizure", "focal onset aware sensory epileptic seizure", "focal onset aware tonic epileptic seizure", "focal onset behavior arrest epileptic seizure", "focal onset clonic epileptic seizure", "focal onset cognitive epileptic seizure", "focal onset emotional epileptic seizure", "focal onset epileptic seizure", "focal onset hyperkinetic epileptic seizure", "focal onset impaired awareness epileptic seizure", "focal onset motor onset epileptic seizure", "focal onset myoclonic epileptic seizure", "focal onset nonmotor onset epileptic seizure", "focal onset sensory epileptic seizure", "focal onset somatosensory epileptic seizure", "focal onset tonic epileptic seizure", "focal to bilateral tonic-clonic epileptic seizure", "frontal lobe epileptic seizure", "generalized onset atonic epileptic seizure", "generalized onset clonic epileptic seizure", "generalized onset epileptic seizure", "generalized onset motor epileptic seizure", "generalized onset myoclonic epileptic seizure", "generalized onset tonic epileptic seizure", "generalized onset tonic-clonic epileptic seizure", "impaired awareness epileptic seizure", "lateral temporal lobe epileptic seizure", "measure of seizure", "mesial temporal lobe epileptic seizure", "motor epileptic seizure", "myoclonic absence seizure", "myoclonic epileptic seizure", "neonatal focal automatism epileptic seizure", "neonatal focal autonomic epileptic seizure", "neonatal focal behavior arrest epileptic seizure", "neonatal focal clonic epileptic seizure", "neonatal focal electro-clinical epileptic seizure", "neonatal focal epileptic seizure", "neonatal focal myoclonic epileptic seizure", "neonatal focal tonic epileptic seizure", "neonatal seizure", "non-motor epileptic seizure", "nonconvulsive seizure", "occipital lobe epileptic seizure"],
			"altered mental status":   ["altered mental status", "ams", "confused", "confusion", "disoriented", "not acting right", "behavior change", "encephalopathy", "altered mental status (finding)", "bewilderment", "clouded consciousness", "clouded consciousness (finding)", "dazed", "dazed state", "dullness of senses", "foggy mind", "muddled", "muzzy headed", "disorder of brain", "disorder of brain (disorder)"],
			"loss of consciousness":   ["loss of consciousness", "unconscious", "unresponsive", "not waking up", "unrousable", "loss of consciousness (finding)", "mental status, unconsciousness", "unconscious (finding)", "unconsciousness", "unresponsive (finding)", "brief loss of consciousness", "concussion with loss of consciousness", "incomplete loss of consciousness without amnesia", "intracranial injury with loss of consciousness", "moderate loss of consciousness", "prolonged loss of consciousness", "brief loss of consciousness (finding)", "concussion with loss of consciousness (disorder)", "incomplete loss of consciousness without amnesia (finding)", "intracranial injury with loss of consciousness (disorder)", "moderate duration loss of consciousness", "moderate duration loss of consciousness (finding)", "prolonged loss of consciousness (finding)"],
			"numbness":                ["numbness", "tingling", "paresthesia", "pins and needles", "loss of sensation", "sensory loss", "numb", "deadness - numbness", "numbness (finding)", "paresthesia (finding)", "paresthesia (numbness/tingling)", "pins and needles (finding)", "pins and needles sensation", "absence of sensation", "absence of sensation (finding)", "anesthesia", "sensory anesthesia", "mucosal numbness", "numbness and tingling sensation of skin", "numbness of face", "numbness of finger", "numbness of foot", "numbness of hand", "numbness of limbs", "numbness of lower limb", "numbness of pinna", "numbness of saddle area", "numbness of skin", "numbness of toe", "numbness of tongue", "numbness of upper limb", "numbness of vulva", "perioral numbness", "mucosal numbness (finding)", "numbness and tingling of skin", "numbness and tingling sensation of skin (finding)", "numbness of face (finding)", "numbness of finger (finding)", "numbness of foot (finding)", "numbness of hand (finding)", "numbness of limbs (finding)", "numbness of lower limb (finding)", "numbness of pinna (finding)", "numbness of saddle area (finding)", "saddle anesthesia", "loss of sensation of skin", "numbness of skin (finding)", "numbness of toe (finding)", "numbness of tongue (finding)", "numbness of upper limb (finding)", "numbness of vulva (finding)", "perioral numbness (finding)"],
			"neck stiffness":          ["neck stiffness", "stiff neck", "nuchal rigidity", "neck pain", "meningismus", "crick in neck", "ns - neck stiffness", "stiff neck (finding)", "nuchal rigidity (finding)", "cervical pain", "cervicalgia", "neck ache", "neck pain (finding)", "nonspecific pain in the neck region", "painful neck", "dupr\u00e9s's syndrome", "meningeal irritation", "meningeal irritation (disorder)", "acute muscle stiffness of neck", "acute muscle stiffness of neck (finding)"],
			"ataxia":                  ["ataxia", "unsteady gait", "difficulty walking", "stumbling", "coordination problems", "cant walk straight", "ataxia (finding)", "ataxia (loss of muscle coordination)", "disequilibrium when walking", "instability of gait", "unstable when walking", "unsteady when walking", "unsteady when walking (finding)", "difficulty walking (finding)", "stumbling (event)", "acquired ataxia", "adult-onset autosomal recessive cerebellar ataxia", "alcohol-induced cerebellar ataxia", "ataxia as sequela of cerebrovascular accident", "ataxia as sequela of cerebrovascular disease", "ataxia of bilateral upper limbs", "ataxia pancytopenia syndrome", "ataxia telangiectasia variant", "ataxia with tapetoretinal degeneration syndrome", "ataxia with vitamin e deficiency", "autosomal dominant cerebellar ataxia type 2", "autosomal dominant spastic ataxia type 1", "autosomal recessive cerebellar ataxia beauce type", "bedouin spastic ataxia syndrome", "bilateral lower limb ataxia", "cardiomyopathy in friedreich's ataxia", "carrier of spinocerebellar ataxia", "cerebellar ataxia", "cerebellar ataxia and ectodermal dysplasia", "cerebellar ataxia cayman type", "cerebellar ataxia with quadrupedal gait", "cerebral ataxia", "cerebral paralysis with homolateral ataxia", "cerebral paresis with homolateral ataxia", "congenital non-progressive ataxia", "drug-induced cerebellar ataxia", "early onset cerebellar ataxia", "early onset cerebellar ataxia with hypogonadism", "early onset cerebellar ataxia with myoclonus", "episodic ataxia", "episodic ataxia type 1", "episodic ataxia type 2", "episodic ataxia type 3", "episodic ataxia type 4", "episodic ataxia type 5", "episodic ataxia type 6", "episodic ataxia type 7", "episodic ataxia with slurred speech", "fragile x associated tremor ataxia syndrome", "friedreich ataxia", "frontal ataxia", "hereditary ataxia", "infantile onset spinocerebellar ataxia", "late onset cerebellar ataxia", "marie's cerebellar ataxia", "motor ataxia", "myoclonic epilepsy myopathy sensory ataxia", "neuropathy in association with hereditary ataxia", "non-progressive cerebellar ataxia", "optic ataxia", "oral motor ataxia", "parkinsonian ataxia", "periodic ataxia", "posthemiplegic ataxia", "postinfectious ataxia", "progressive cerebellar ataxia", "progressive cerebellar ataxia with hypogonadism", "progressive locomotor ataxia", "progressive myoclonus epilepsy with ataxia", "progressive spinal ataxia", "progressive truncal ataxia", "pum1-related cerebellar ataxia", "recessive mitochondrial ataxia syndrome", "sanger-brown cerebellar ataxia", "sensory ataxia", "single limb ataxia", "spastic ataxia", "spastic ataxia with congenital miosis", "spinal ataxia", "spinocerebellar ataxia", "spinocerebellar ataxia dysmorphism syndrome", "spinocerebellar ataxia type 1", "spinocerebellar ataxia type 10", "spinocerebellar ataxia type 11", "spinocerebellar ataxia type 12", "spinocerebellar ataxia type 13", "spinocerebellar ataxia type 14", "spinocerebellar ataxia type 15/16", "spinocerebellar ataxia type 17", "spinocerebellar ataxia type 18", "spinocerebellar ataxia type 19", "spinocerebellar ataxia type 2", "spinocerebellar ataxia type 20", "spinocerebellar ataxia type 21", "spinocerebellar ataxia type 23"],
			"tremor":                  ["tremor", "shaking hands", "hand tremor", "involuntary shaking", "resting tremor", "has a tremor", "involuntary quiver", "involuntary trembling", "quivering", "shakes", "shaking", "shaking all over", "the shakes", "trembling", "tremor (finding)", "hand tremor (finding)", "resting tremor (finding)", "arsenical tremor", "bilateral outstretched hands tremor", "chronic tremor", "coarse tremor", "continuous tremor", "dysphonia of organic tremor", "dystonic tremor", "enhanced physiological tremor", "essential tremor", "fine tremor", "fragile x associated tremor ataxia syndrome", "hereditary essential tremor", "intention tremor", "intermittent tremor", "isolated facial tremor", "isolated head tremor", "isolated vocal tremor", "lip tremor", "massive tremor", "medication-induced postural tremor", "mercurial tremor", "metallic tremor", "organic voice tremor", "orthostatic tremor", "parkinsonian tremor", "passive tremor", "persistent tremor", "physiological tremor", "post-hemiplegic tremor", "postural tremor of upper limb", "primary orthostatic tremor", "progressive cerebellar tremor", "psychogenic tremor", "rubral tremor", "saturnine tremor", "senile tremor", "static tremor", "thyrotoxic tremor", "toxic tremor", "tremor of limb", "tremor of palate", "tremor of tongue", "tremor opiophagorum", "voice tremor", "arsenical tremor (finding)", "tremor in bilateral outstretched hands", "tremor in bilateral outstretched hands (finding)", "tremor in both outstretched hands", "chronic tremor (finding)", "coarse tremor (finding)", "continuous tremor (finding)", "dysphonia of essential tremor", "dysphonia of organic tremor (disorder)", "dystonic tremor (finding)", "enhanced physiological tremor (finding)", "essential tremor (disorder)", "fine tremor (finding)", "fragile x associated tremor ataxia syndrome (disorder)", "hereditary essential tremor (disorder)", "action tremor", "cerebellar tremor", "intention tremor (finding)", "kinetic tremor", "volitional tremor", "intermittent tremor (finding)", "isolated facial tremor (finding)", "isolated head tremor (finding)", "isolated vocal tremor (finding)", "lip tremor (finding)", "massive tremor (finding)", "drug-induced tremor", "medication-induced postural tremor (disorder)", "mercurial tremor (finding)", "metallic tremor (finding)", "essential voice tremor", "organic voice tremor (finding)", "orthostatic tremor (finding)", "parkinsonian tremor (finding)", "passive tremor (finding)", "persistent tremor (finding)", "physiological tremor (finding)", "post-hemiplegic tremor (finding)", "postural tremor of upper limb (finding)"],
			"papilledema":             ["papilledema", "blurred disc margins", "raised icp signs"],
			"photophobia":             ["photophobia", "light sensitivity", "sensitive to light", "cant tolerate light", "photophobia (finding)"],
			"phonophobia":             ["phonophobia", "noise sensitivity", "sensitive to sound", "phonophobia (finding)"],
		},

		# ── GASTROINTESTINAL ─────────────────────────────────────────
		"gastrointestinal": {
			"abdominal pain":          ["abdominal pain", "stomach ache", "belly pain", "stomach pain", "tummy ache", "epigastric pain", "periumbilical pain", "periumbilical", "belly button pain", "lower abdominal pain", "upper abdominal pain", "cramping", "abd pain", "abdo pain", "abdominal pain (finding)", "ap - abdominal pain", "belly ache", "sore tummy", "stomach ache (finding)", "stomach discomfort", "stomach upset", "epigastric pain (finding)", "periumbilical abdominal pain", "periumbilical pain (finding)", "lower abdominal pain (finding)", "upper abdominal pain (finding)", "cramping sensation quality", "cramping sensation quality (qualifier value)", "crampy", "abdominal muscle pain", "abdominal pain - cause unknown", "abdominal pain in early pregnancy", "abdominal pain in pregnancy", "abdominal pain through to back", "abdominal pain worse on motion", "abdominal wall pain", "abdominal wind pain", "acute abdominal pain", "acute exacerbation of chronic abdominal pain", "central abdominal pain", "chronic abdominal pain", "chronic nonspecific abdominal pain", "functional abdominal pain of childhood", "functional abdominal pain syndrome", "generalized abdominal pain", "generalized colicky abdominal pain", "left sided abdominal pain", "localized abdominal pain", "non-colicky abdominal pain", "nonspecific abdominal pain", "pain in abdominal region on palpation", "pain in left abdominal lumbar region", "pain in right abdominal lumbar region", "pain on abdominal wall movement", "psychosomatic abdominal pain", "recurrent abdominal pain", "recurrent acute abdominal pain", "right sided abdominal pain", "site of abdominal pain", "type of abdominal pain", "visceral abdominal pain", "abdominal muscle pain (finding)", "abdominal pain - cause unknown (finding)", "unexplained abdominal pain", "abdominal pain in early pregnancy (finding)", "abdominal pain in pregnancy (finding)", "abdominal pain through to back (finding)", "abdominal pain worse on motion (finding)", "abdominal wall pain (finding)", "anterior abdominal wall pain", "abdominal wind pain (finding)", "gas pain - abdominal", "acute abdominal pain (finding)", "acute exacerbation of chronic abdominal pain (finding)", "central abdominal pain (finding)", "chronic abdominal pain (finding)", "chronic nonspecific abdominal pain (finding)", "caps (centrally mediated abdominal pain syndrome) of childhood", "centrally mediated abdominal pain syndrome of childhood", "functional abdominal pain of childhood (disorder)", "caps - centrally mediated abdominal pain syndrome", "centrally mediated abdominal pain syndrome", "functional abdominal pain syndrome (disorder)", "generalized abdominal pain (finding)", "generalized colicky abdominal pain (finding)", "left sided abdominal pain (finding)", "localized abdominal pain (finding)", "non-colicky abdominal pain (finding)", "idiopathic abdominal pain", "nonspecific abdominal pain (finding)", "pain in abdominal region on palpation (finding)", "pain in left abdominal lumbar region (finding)", "pain in left lumbar region of abdomen", "pain in right abdominal lumbar region (finding)", "pain in right lumbar region of abdomen", "pain on abdominal wall movement (finding)", "psychosomatic abdominal pain (disorder)", "recurrent abdominal pain (finding)", "recurrent acute abdominal pain (finding)", "right sided abdominal pain (finding)", "site of abdominal pain (observable entity)", "abdominal pain type"],
			"nausea":                  ["nausea", "queasy", "nauseated", "feel like vomiting", "sick to stomach", "upset stomach", "nausea (finding)", "nauseous", "observation of nausea", "upset stomach (finding)", "upset tummy", "functional nausea", "intractable nausea and vomiting", "nausea and vomiting", "nausea and vomiting in pregnancy", "nausea present", "tendency to nausea and vomiting", "vomiting without nausea", "functional nausea (disorder)", "intractable nausea and vomiting (disorder)", "refractory nausea and vomiting", "n&v - nausea and vomiting", "n+v - nausea and vomiting", "nausea and vomiting (disorder)", "nausea and vomiting in pregnancy (disorder)", "nausea present (situation)", "prone to nausea and vomiting", "tendency to nausea and vomiting (finding)", "vomiting without nausea (disorder)"],
			"vomiting":                ["vomiting", "vomit", "throwing up", "emesis", "puking", "retching", "projectile vomiting", "vomiting (disorder)", "dry heaves", "heaving", "retching (finding)", "projectile vomiting (disorder)", "vomitus", "vomitus (substance)", "acute vomiting", "bilious vomiting", "chronic vomiting", "coffee ground vomiting", "concealed vomiting", "cyclical vomiting syndrome", "diarrhea and vomiting", "effortless vomiting", "epidemic vomiting syndrome", "erotic vomiting", "fear of vomiting in public", "functional vomiting in childhood", "habit vomiting", "intermittent vomiting", "intractable cyclical vomiting syndrome", "intractable nausea and vomiting", "jamaican vomiting sickness", "nausea and vomiting", "nausea and vomiting in pregnancy", "nausea, vomiting and diarrhea", "neonatal bilious vomiting", "pattern of overeating and vomiting", "persistent vomiting", "post-tussive vomiting", "psychogenic cyclical vomiting", "psychogenic vomiting", "repeated self-induced vomiting", "self-induced vomiting", "self-induced vomiting to lose weight", "tendency to nausea and vomiting", "uncontrollable vomiting", "vomiting after gastrointestinal tract surgery", "vomiting blood - fresh", "vomiting during third trimester of pregnancy", "vomiting fecal matter", "vomiting food", "vomiting in infants and/or children", "vomiting in newborn", "vomiting of pregnancy", "vomiting symptom", "vomiting without nausea", "acute vomiting (disorder)", "bilious emesis", "bilious vomiting (disorder)", "vomiting bile", "chronic vomiting (disorder)", "coffee ground emesis", "coffee ground vomiting (disorder)", "vomiting blood - coffee ground", "vomiting old blood", "concealed vomiting (disorder)", "surreptitious vomiting", "cyclical vomiting", "cyclical vomiting syndrome (disorder)", "periodic vomiting", "periodic vomiting syndrome", "diarrhea and vomiting (finding)", "effortless vomiting (finding)", "epidemic vomiting syndrome (disorder)", "winter vomiting disease", "erotic vomiting (disorder)", "fear of vomiting in public (finding)", "functional vomiting in childhood (disorder)", "habit vomiting (disorder)", "intermittent vomiting (disorder)", "intractable cyclical vomiting syndrome (disorder)", "intractable nausea and vomiting (disorder)", "refractory nausea and vomiting", "ackee poisoning", "akee poisoning", "jamaican vomiting sickness (disorder)", "n&v - nausea and vomiting", "n+v - nausea and vomiting", "nausea and vomiting (disorder)", "nausea and vomiting in pregnancy (disorder)", "nausea, vomiting and diarrhea (disorder)", "pattern of overeating and vomiting (finding)", "emesis - persistent", "persistent vomiting (disorder)", "post-tussive vomiting (disorder)", "vomiting after coughing", "psychogenic cyclical vomiting (disorder)", "functional vomiting", "psychogenic vomiting (disorder)", "repeated self-induced vomiting (situation)", "making self sick"],
			"hematemesis":             ["hematemesis", "vomiting blood", "bloody vomit", "coffee ground emesis", "blood in vomit", "hematemesis (disorder)", "vomiting of blood", "coffee ground vomiting", "coffee ground vomiting (disorder)", "vomiting blood - coffee ground", "vomiting old blood", "vomit contains blood", "vomit contains blood (finding)", "hematemesis of unknown cause", "neonatal hematemesis", "perinatal hematemesis", "hematemesis of unknown cause (disorder)", "neonatal hematemesis (disorder)", "perinatal hematemesis (disorder)"],
			"diarrhea":                ["diarrhea", "watery stool", "loose stool", "frequent stools", "liquid stool", "loose bowels", "the runs", "explosive diarrhea", "d - diarrhea", "diarrhea (finding)", "observation of diarrhea", "fluid stool", "liquid feces", "liquid stool (finding)", "loose bowel motions", "loose bowel movement", "loose feces", "loose motion", "loose stool (finding)", "loose stools", "ls - loose stools", "acute diarrhea", "allergic diarrhea", "alteration in bowel elimination: diarrhea", "antibiotic-associated diarrhea", "brainerd diarrhea", "carcinoid syndrome diarrhea", "chronic diarrhea", "chronic diarrhea of unknown origin", "chronic diarrhea with villous atrophy syndrome", "clostridium difficile diarrhea", "congenital secretory diarrhea", "constipation alternates with diarrhea", "defecation reflex - spurious diarrhea", "diarrhea after gastrointestinal tract surgery", "diarrhea and vomiting", "diarrhea in pregnancy", "diarrhea not present", "diarrhea of presumed infectious origin", "diarrhea symptom", "dietetic diarrhea", "dysenteric diarrhea", "epidemic diarrhea", "functional diarrhea", "hemorrhagic diarrhea", "hyperalimentation formula for severe diarrhea", "inflammatory diarrhea", "irritable bowel syndrome with diarrhea", "nausea, vomiting and diarrhea", "neonatal diarrhea", "nervous diarrhea", "non-infective diarrhea", "non-infective neonatal diarrhea", "osmotic diarrhea", "post-vagotomy diarrhea", "postcholecystectomy diarrhea", "postprandial diarrhea", "prototheca diarrhea", "protracted diarrhea", "psychogenic diarrhea", "raw-milk associated diarrhea", "secretory diarrhea", "sensation as if diarrhea will start", "severe diarrhea", "spurious diarrhea - overflow", "syndromic congenital sodium diarrhea", "toddler diarrhea", "traveler's diarrhea", "acute diarrhea (disorder)", "allergic diarrhea (disorder)", "alteration in bowel elimination: diarrhea (finding)", "antibiotic-associated diarrhea (disorder)", "brainerd diarrhea (disorder)", "diarrhea co-occurrent and due to carcinoid syndrome", "diarrhea co-occurrent and due to carcinoid syndrome (disorder)", "chronic diarrhea (disorder)", "chronic diarrhea of unknown origin (disorder)", "chronic diarrhea with villous atrophy syndrome (disorder)", "clostridium difficile diarrhea (disorder)", "congenital secretory diarrhea (disorder)", "constipation alternates with diarrhea (finding)", "defecation reflex - spurious diarrhea (finding)", "diarrhea after gastrointestinal tract surgery (disorder)", "diarrhea following gastrointestinal surgery", "diarrhea and vomiting (finding)", "diarrhea in pregnancy (finding)", "diarrhea not present (situation)", "diarrhea of presumed infectious origin (disorder)", "diarrhea symptom (finding)", "dietetic diarrhea (disorder)", "dysenteric diarrhea (disorder)", "dysentery", "epidemic diarrhea (disorder)", "functional diarrhea (disorder)", "bloody diarrhea", "hemorrhagic diarrhea (disorder)", "hyperalimentation formula for severe diarrhea (finding)", "inflammatory diarrhea (disorder)", "irritable bowel syndrome with diarrhea (disorder)", "nausea, vomiting and diarrhea (disorder)"],
			"bloody stool":            ["bloody stool", "blood in stool", "rectal bleeding", "hematochezia", "melena", "black stool", "tarry stool", "red stool", "blood in feces", "brbpr - bright red blood per rectum", "bright red blood in stool", "bright red blood per rectum", "feces: blood", "fresh blood passed per rectum", "hematochezia (finding)", "passage of bloody stools", "altered blood in stool", "altered blood passed per rectum", "black, tarry stool", "melena (disorder)", "tarry stools", "bleeding per rectum", "blood per rectum", "pr - bleeding per rectum", "pr - blood per rectum", "prb - rectal bleeding", "proctorrhagia", "rb - rectal bleeding", "rectal hemorrhage", "rectal hemorrhage (disorder)", "rectorrhagia"],
			"constipation":            ["constipation", "no bowel movement", "obstipation", "no stool", "adhesions", "abdominal surgery", "multiple surgeries", "cn - constipation", "constipated", "constipation (finding)", "costiveness", "difficult passing motion", "difficulty defecating", "difficulty opening bowels", "difficulty passing stool", "intractable constipation", "obstipation (disorder)", "acute constipation", "acute constipation in childhood", "acute constipation in infancy", "alteration in bowel elimination: constipation", "atonic constipation", "chronic constipation", "chronic constipation with overflow", "chronic constipation without overflow", "chronic idiopathic constipation", "constipation alternates with diarrhea", "constipation by outlet obstruction", "constipation during pregnancy", "drug-induced constipation", "functional constipation", "functional constipation of infant", "perceived constipation", "psychogenic constipation", "simple constipation", "slow transit constipation", "therapeutic opioid induced constipation", "acute constipation (finding)", "acute constipation in childhood (finding)", "acute constipation in infancy (finding)", "alteration in bowel elimination: constipation (finding)", "intermittent constipation pattern", "constipation due to atony of colon", "constipation due to atony of colon (disorder)", "chronic constipation (disorder)", "chronic constipation with overflow (disorder)", "overflow diarrhea", "overflow incontinence due to constipation", "spurious diarrhea", "chronic constipation without overflow (disorder)", "chronic idiopathic constipation (disorder)", "constipation alternates with diarrhea (finding)", "constipation due to outlet obstruction", "constipation due to outlet obstruction (disorder)", "constipation during pregnancy (finding)", "constipation in pregnancy", "drug-induced constipation (disorder)", "functional constipation (disorder)", "functional constipation of infant (disorder)", "perceived constipation (finding)", "psychogenic constipation (disorder)", "simple constipation (finding)", "colonic constipation", "constipation by delayed colonic transit", "slow transit constipation (disorder)", "therapeutic opioid induced constipation (disorder)"],
			"jaundice":                ["jaundice", "yellow skin", "yellow eyes", "icterus", "yellowing", "scleral icterus", "icteric", "jaundice (finding)", "jaundiced", "scleral icterus (finding)", "yellow sclera", "yellow complexion", "yellow skin (finding)", "acute cholestatic jaundice syndrome", "cholestatic jaundice syndrome", "chronic cholestatic jaundice syndrome", "hemolytic jaundice", "hepatocellular jaundice", "maternal perinatal jaundice", "neonatal jaundice", "neonatal jaundice after preterm delivery", "neonatal jaundice with congenital hypothyroidism", "neonatal jaundice with porphyria", "neonatal physiological jaundice", "prolonged neonatal physiological jaundice", "transient neonatal physiological jaundice", "acute cholestatic jaundice syndrome (disorder)", "cholestatic jaundice", "cholestatic jaundice syndrome (disorder)", "chronic cholestatic jaundice syndrome (disorder)", "hemolytic jaundice (disorder)", "hepatocellular jaundice (disorder)", "maternal perinatal jaundice (finding)", "icterus neonatorum", "neonatal jaundice (finding)", "hyperbilirubinemia of prematurity", "neonatal jaundice associated with preterm delivery", "neonatal jaundice associated with preterm delivery (finding)", "preterm delivery-associated jaundice", "neonatal jaundice with congenital hypothyroidism (disorder)", "neonatal jaundice with porphyria (disorder)"],
			"abdominal distension":    ["abdominal distension", "bloated", "belly bloated", "distended abdomen", "swollen belly", "ascites", "ascites (disorder)", "hydroperitoneum", "hydroperitonia", "hydrops abdominis", "distension of abdomen", "distension of abdomen (finding)", "abdominal distension symptom", "abdominal distension symptom (finding)"],
			"rebound tenderness":      ["rebound tenderness", "guarding", "peritonitis", "board-like abdomen", "rigid abdomen", "abdominal rebound pain", "rebound tenderness (finding)", "peritonitis (disorder)", "rebound tenderness absent", "rebound tenderness of central region", "rebound tenderness of epigastrium", "rebound tenderness of hypogastrium", "rebound tenderness of left hypochondrium", "rebound tenderness of left iliac fossa", "rebound tenderness of left lumbar", "rebound tenderness of right hypochondrium", "rebound tenderness of right iliac fossa", "rebound tenderness of right lumbar", "rebound tenderness of umbilical region", "rebound tenderness absent (situation)", "rebound tenderness of central region (finding)", "rebound tenderness of epigastrium (finding)", "rebound tenderness of hypogastrium (finding)", "rebound tenderness of left hypochondrium (finding)", "lif - rebound tenderness of left iliac fossa", "rebound tenderness of left iliac fossa (finding)", "rebound tenderness of left lumbar (finding)", "rebound tenderness of right hypochondrium (finding)", "rebound tenderness of right iliac fossa (finding)", "rebound tenderness of right lumbar (finding)", "rebound tenderness of umbilical region (finding)"],
			"right lower quadrant pain": ["right lower quadrant pain", "rlq pain", "rlq", "right side pain", "appendix pain", "appendicitis pain", "right lower quadrant pain (finding)"],
			"right upper quadrant pain": ["right upper quadrant pain", "ruq pain", "ruq", "right upper pain", "gallbladder pain", "biliary pain", "right upper quadrant pain (finding)", "gallbladder pain (finding)"],
			"dysphagia":               ["dysphagia", "difficulty swallowing", "trouble swallowing", "cant swallow", "food gets stuck", "dysphagia (disorder)", "difficulty in swallowing", "difficulty swallowing (finding)", "swallowing difficult", "constant low-grade dysphagia", "dysphagia lusoria", "esophageal dysphagia", "functional dysphagia", "intermittent dysphagia", "oral phase dysphagia", "oropharyngeal dysphagia", "pharyngeal dysphagia", "post-vagotomy dysphagia", "screening for dysphagia performed", "constant low-grade dysphagia (disorder)", "dysphagia lusoria (disorder)", "esophageal dysphagia (disorder)", "functional dysphagia (disorder)", "functional swallowing disorder", "intermittent dysphagia (disorder)", "oral phase dysphagia (disorder)", "oropharyngeal dysphagia (disorder)", "transfer dysphagia", "pharyngeal dysphagia (disorder)", "post-vagotomy dysphagia (disorder)", "screening for dysphagia performed (situation)"],
			"rectal pain":             ["rectal pain", "anal pain", "perianal pain", "pain with defecation", "pain in rectum", "proctalgia", "rectal pain (finding)", "rectalgia", "anal pain (finding)", "perianal pain (finding)"],
			"regurgitation":           ["regurgitation", "acid reflux", "heartburn", "sour taste", "bitter taste", "food coming back up", "acid coming up", "reflux", "gerd", "burning throat", "acid reflux (finding)", "burning reflux", "heartburn (finding)", "pyrosis", "regurgitation - mechanism", "regurgitation - mechanism (qualifier value)", "acute mitral regurgitation", "acute mitral regurgitation from chordal rupture", "acute prosthetic aortic valve regurgitation", "acute prosthetic mitral valve regurgitation", "acute prosthetic tricuspid valve regurgitation", "aortic cusp regurgitation", "aortic valve regurgitation", "bile pigment regurgitation", "chronic regurgitation", "congenital regurgitation of truncal valve", "end-diastolic pulmonary regurgitation velocity", "functional mitral regurgitation", "functional pulmonary regurgitation", "functional tricuspid regurgitation", "heart valve regurgitation", "heart valve stenosis and regurgitation", "infant gastrointestinal regurgitation", "lacrimal regurgitation", "late syphilitic pulmonary regurgitation", "mild aortic valve regurgitation", "mild mitral valve regurgitation", "mild pulmonary valve regurgitation", "mild tricuspid valve regurgitation", "mitral valve regurgitation", "moderate aortic valve regurgitation", "moderate mitral valve regurgitation", "moderate pulmonary valve regurgitation", "moderate tricuspid valve regurgitation", "mucoid lacrimal regurgitation", "mucopurulent lacrimal regurgitation", "nasal regurgitation", "neoaortic valve regurgitation", "neonatal regurgitation of food", "neopulmonary valve regurgitation", "non-rheumatic mitral regurgitation", "paraprosthetic aortic regurgitation", "paraprosthetic mitral regurgitation", "paraprosthetic pulmonary regurgitation", "paraprosthetic tricuspid regurgitation", "peak velocity of tricuspid regurgitation", "periprosthetic aortic valve regurgitation", "postprocedural aortic valve regurgitation", "postprocedural mitral valve regurgitation", "postprocedural pulmonary valve regurgitation", "postprocedural regurgitation of tricuspid valve", "prosthetic aortic valve regurgitation", "prosthetic aortic valve stenosis and regurgitation", "prosthetic cardiac valve regurgitation", "prosthetic mitral valve regurgitation", "prosthetic mitral valve stenosis and regurgitation", "prosthetic pulmonary valve regurgitation", "prosthetic tricuspid valve regurgitation", "pulmonic valve regurgitation", "regurgitation - no aspiration detected", "regurgitation of common atrioventricular valve", "regurgitation of fetal aortic valve", "regurgitation of fetal mitral valve", "regurgitation of fetal pulmonary valve", "regurgitation of fetal tricuspid valve", "regurgitation of fetal truncal valve", "regurgitation of food", "regurgitation of gastric content", "rheumatic aortic regurgitation", "rheumatic aortic stenosis with regurgitation", "rheumatic heart valve regurgitation", "rheumatic mitral and aortic valve regurgitation", "rheumatic mitral regurgitation", "rheumatic mitral stenosis with regurgitation", "rheumatic tricuspid valve regurgitation", "right ventricular regurgitation velocity", "severe aortic valve regurgitation", "severe mitral valve regurgitation", "severe pulmonary valve regurgitation", "severe tricuspid valve regurgitation", "transient neonatal mitral regurgitation", "transient neonatal tricuspid regurgitation", "tricuspid valve regurgitation", "truncal valve regurgitation", "valvular regurgitation", "valvular regurgitation features", "watery lacrimal regurgitation", "acute mitral regurgitation (disorder)", "acute mitral regurgitation from chordal rupture (disorder)", "acute prosthetic aortic valve regurgitation (disorder)"],
			"bloating":                ["bloating", "bloated feeling", "gas", "flatulence", "feeling full", "abdominal bloating", "distended", "gas (basic dose form)", "gas (state of matter)", "gaseous substance", "gaseous substance (substance)", "flatus", "passing flatus", "passing flatus (finding)", "wind - flatus", "abdominal bloating (finding)", "bloated abdomen", "flatus, function", "flatus, function (observable entity)", "intestinal gas excretion", "passage of gas by anus", "functional bloating", "functional bloating after eating certain foods", "functional bloating (disorder)", "functional abdominal bloating after eating certain foods", "functional abdominal bloating after eating certain foods (disorder)"],
		},

		# ── GENITOURINARY / RENAL ────────────────────────────────────
		"genitourinary": {
			"dysuria":                 ["dysuria", "painful urination", "burning urination", "burning when urinating", "pain with urination", "burning pee", "dysuria (finding)", "pain emptying bladder", "pain on micturition", "pain on voiding", "pain passing urine", "pain passing water", "painful micturition", "passing water hurts", "urination painful", "psychogenic dysuria", "psychic dysuria", "psychogenic dysuria (disorder)"],
			"hematuria":               ["hematuria", "blood in urine", "bloody urine", "pink urine", "red urine", "blood in urine (finding)", "asymptomatic microscopic hematuria", "benign essential microscopic hematuria", "benign hematuria", "chemical hematuria", "clot hematuria", "familial hematuria", "frank hematuria", "glomerular hematuria", "hematuria of undiagnosed cause", "hematuria syndrome", "intermittent frank hematuria", "intermittent microscopic hematuria", "microscopic hematuria", "painful hematuria", "painless hematuria", "persistent frank hematuria", "persistent hematuria", "persistent microscopic hematuria", "recurrent benign hematuria syndrome", "recurrent frank hematuria", "recurrent hematuria", "recurrent microscopic hematuria", "renal hematuria", "traumatic hematuria", "upper urinary tract hematuria", "asymptomatic microscopic hematuria (disorder)", "benign essential microscopic hematuria (disorder)", "benign hematuria (disorder)", "chemical hematuria (disorder)", "dipstick hematuria", "clot hematuria (disorder)", "familial hematuria (disorder)", "frank hematuria (disorder)", "gross hematuria", "macroscopic hematuria", "essential hematuria", "hematuria - cause not known", "hematuria of undiagnosed cause (disorder)", "blood in urine - hematuria", "hematuria syndrome (disorder)", "intermittent frank hematuria (disorder)", "intermittent macroscopic hematuria", "intermittent microscopic hematuria (disorder)", "microscopic hematuria (disorder)", "painful hematuria (disorder)", "painless hematuria (disorder)", "persistent frank hematuria (disorder)", "persistent hematuria (disorder)", "persistent microscopic hematuria (disorder)", "recurrent benign hematuria syndrome (disorder)", "recurrent frank hematuria (disorder)", "recurrent hematuria (disorder)", "recurrent microscopic hematuria (disorder)", "renal hematuria (disorder)", "traumatic hematuria (disorder)", "upper urinary tract hematuria (disorder)"],
			"flank pain":              ["flank pain", "kidney pain", "costovertebral angle pain", "cva tenderness", "loin pain", "side pain", "flank pain (finding)", "loin pain (finding)", "renal pain", "renal pain (finding)", "left flank pain", "pain radiating to left flank", "pain radiating to right flank", "right flank pain", "left flank pain (finding)", "pain radiating to left flank (finding)", "pain radiating to right flank (finding)", "right flank pain (finding)"],
			"urinary frequency":       ["urinary frequency", "frequent urination", "urinating often", "overactive bladder", "going to bathroom often", "bladder instability", "hyperactive bladder", "instability of bladder", "overactive urinary bladder", "overactive urinary bladder (disorder)", "increased frequency of micturition", "increased frequency of urination", "increased frequency of urination (finding)", "passes water too often", "pollakisuria", "pollakiuria", "urinary frequency during pregnancy", "urinary frequency volume chart completed", "urinary frequency during pregnancy (finding)", "urinary frequency in pregnancy", "bladder diary completed", "urinary frequency volume chart completed (situation)"],
			"urinary retention":       ["urinary retention", "cant urinate", "unable to pee", "no urine output", "oliguria", "anuria", "cannot pass urine - retention", "not passing urine", "retention of urine", "retention of urine (disorder)", "unable to empty bladder", "oligouria", "oliguria (finding)", "passes too little urine", "anuria (finding)", "passes no urine", "bladder retention of urine", "urinary bladder retention of urine", "urinary bladder retention of urine (observable entity)"],
			"scrotal pain":            ["scrotal pain", "testicular pain", "testicle pain", "scrotal swelling", "groin pain male", "pain in scrotum", "pain in scrotum (finding)", "pain of scrotum"],
			"vaginal bleeding":        ["vaginal bleeding", "abnormal vaginal bleeding", "heavy period", "menorrhagia", "spotting", "intermenstrual bleeding", "bleeding from vagina", "bleeding from vagina (finding)", "observations of vaginal bleeding", "abnormal vaginal bleeding (finding)", "flooding during periods", "heavy menstrual bleeding", "heavy periods", "hypermenorrhea", "menorrhagia (finding)", "profuse menstrual flow", "bleeding between periods", "bleeding between periods (finding)", "imb - intermenstrual bleeding", "mid-cycle bleeding", "spotting between periods", "menstrual spotting", "menstrual spotting (finding)", "heavy episode of vaginal bleeding", "moderate vaginal bleeding", "non-menstrual vaginal bleeding", "perinatal transient vaginal bleeding", "profuse vaginal bleeding", "scanty vaginal bleeding", "vaginal bleeding complicating early pregnancy", "vaginal introitus bleeding", "vaginal vault bleeding", "heavy episode of vaginal bleeding (finding)", "moderate vaginal bleeding (finding)", "non-menstrual vaginal bleeding (disorder)", "perinatal pseudomenses", "perinatal transient vaginal bleeding (disorder)", "transient vaginal bleeding in newborn", "profuse vaginal bleeding (finding)", "scanty vaginal bleeding (finding)", "vaginal bleeding complicating early pregnancy (disorder)", "vaginal introitus bleeding (finding)", "vaginal vault bleeding (finding)"],
			"pelvic pain":             ["pelvic pain", "lower pelvic pain", "suprapubic pain", "ovarian pain", "pelvic pressure", "hypogastric pain", "pain of hypogastrium", "suprapubic pain (finding)", "ovarian pain (finding)", "pain of ovary", "acute pelvic pain", "bony pelvic pain", "chronic female pelvic pain syndrome", "chronic male primary pelvic pain syndrome", "chronic pelvic pain of female", "chronic pelvic pain without obvious pathology", "chronic primary pelvic pain syndrome", "cyclic pelvic pain", "joint pain of pelvic region", "pelvic and perineal pain", "pelvic girdle pain", "pelvic girdle pain during pregnancy", "acute pelvic pain (finding)", "bony pelvic pain (finding)", "chronic female pelvic pain syndrome (disorder)", "chronic male primary pelvic pain syndrome (disorder)", "chronic primary pelvic pain syndrome of male", "chronic primary visceral pain in male pelvic region", "chronic pain in female pelvis", "chronic pain in female pelvis (finding)", "chronic pelvic pain without obvious pathology (finding)", "chronic pelvic pain syndrome", "chronic primary pelvic pain syndrome (disorder)", "chronic primary visceral pain in pelvic region", "cyclic pelvic pain (finding)", "joint pain of pelvic region (finding)", "pelvic and perineal pain (finding)", "pelvic girdle pain (disorder)", "symphysis pubis dysfunction", "pelvic girdle pain during pregnancy (disorder)"],
			"penile discharge":        ["penile discharge", "urethral discharge", "discharge from penis", "discharge from penis (finding)", "observation of urethral discharge", "ud - urethral discharge", "urethral discharge (finding)", "urethrorrhea"],
			"vaginal discharge":       ["vaginal discharge", "abnormal discharge", "fishy discharge", "observation of vaginal discharge", "vaginal discharge (finding)", "bloodstained vaginal discharge", "brown vaginal discharge", "color of vaginal discharge", "consistency of vaginal discharge", "creamy vaginal discharge", "fishy vaginal discharge", "frothy vaginal discharge", "green vaginal discharge", "moderate vaginal discharge", "mucoid vaginal discharge", "odor of vaginal discharge", "odorless vaginal discharge", "offensive vaginal discharge", "profuse vaginal discharge", "purulent vaginal discharge", "quantity of vaginal discharge", "scanty vaginal discharge", "urinous vaginal discharge", "vaginal discharge absent", "vaginal discharge feature", "vaginal discharge present", "vaginal discharge problem", "vaginal discharge symptom", "watery vaginal discharge", "white vaginal discharge", "yellow vaginal discharge", "bloodstained vaginal discharge (finding)", "brown vaginal discharge (finding)", "color of vaginal discharge (observable entity)", "consistency of vaginal discharge (observable entity)", "creamy vaginal discharge (finding)", "fishy vaginal discharge (finding)", "frothy vaginal discharge (finding)", "green vaginal discharge (finding)", "moderate vaginal discharge (finding)", "mucoid vaginal discharge (finding)", "finding of odor of vaginal discharge", "finding of odor of vaginal discharge (finding)", "odor of vaginal discharge (observable entity)", "odorless vaginal discharge (finding)", "offensive vaginal discharge (finding)", "profuse vaginal discharge (finding)", "purulent vaginal discharge (finding)", "quantity of vaginal discharge (observable entity)", "scanty vaginal discharge (finding)", "urinous vaginal discharge (finding)", "vaginal discharge absent (situation)", "vaginal discharge feature (observable entity)", "vaginal discharge present (situation)", "abnormal vaginal discharge", "vaginal discharge problem (finding)", "vaginal discharge symptom (finding)", "watery vaginal discharge (finding)", "white vaginal discharge (finding)", "yellow vaginal discharge (finding)"],
		},

		# ── MUSCULOSKELETAL / TRAUMA ─────────────────────────────────
		"musculoskeletal": {
			"back pain":               ["back pain", "low back pain", "lumbar pain", "spine pain", "backache", "lbp", "thoracic pain", "back ache", "backache (finding)", "pain in back", "lbp - low back pain", "low back pain (finding)", "low back syndrome", "lumbago", "lumbalgia", "nonspecific pain in the lumbar region", "abdominal pain through to back", "acute back pain with sciatica", "acute low back pain", "acute thoracic back pain", "back pain complicating pregnancy", "back pain worse on sneezing", "chronic back pain", "chronic low back pain", "chronic primary low back pain", "chronic thoracic back pain", "disorder characterized by back pain", "intractable low back pain", "low back pain in pregnancy", "mechanical low back pain", "myofascial low back pain", "myofascial pain syndrome of lower back", "posterior compartment low back pain", "postural low back pain", "sacral back pain", "thoracic back pain", "vertebrogenic low back pain", "abdominal pain through to back (finding)", "acute back pain with sciatica (finding)", "acute back pain - lumbar", "acute low back pain (finding)", "acute thoracic back pain (finding)", "back pain complicating pregnancy (disorder)", "back pain worse on sneezing (finding)", "chronic back pain (finding)", "chronic low back pain (finding)", "clbp - chronic low back pain", "chronic primary low back pain (disorder)", "chronic thoracic back pain (finding)", "disorder characterized by back pain (disorder)", "intractable low back pain (finding)", "low back pain in pregnancy (finding)", "mechanical low back pain (finding)", "myofascial low back pain (finding)", "lumbar myofascial pain syndrome", "lumbar trigger point syndrome", "myofascial pain syndrome of lower back (disorder)", "posterior compartment low back pain (finding)", "postural low back pain (finding)", "hieralgia", "sacral back pain (finding)", "sacrodynia", "thoracic back pain (finding)", "vertebrogenic low back pain (finding)", "vertebrogenic pain of lumbar region of back"],
			"joint pain":              ["joint pain", "arthralgia", "joint swelling", "joint stiffness", "arthritis", "swollen joint", "painful joint", "articular pain", "pain of joint", "pain of joint (finding)", "joint swelling (finding)", "observation of joint swelling", "joint stiffness (finding)", "stiff joint", "arthritis (disorder)", "inflammatory arthritis", "acute pain of joint of knee", "arc of pain in joint", "bilateral acromioclavicular joint pain", "bilateral foot joint pain", "bilateral pain of joint of hands", "bilateral temporomandibular joint pain", "cervical facet joint pain", "chronic sacroiliac joint pain", "distal interphalangeal joint of finger pain", "first metatarsophalangeal joint pain", "joint pain in left hand", "joint pain in right hand", "joint pain of pelvic region", "lesser metatarsophalangeal joint pain", "lumbar facet joint pain", "metacarpophalangeal joint pain", "metatarsophalangeal joint pain", "pain in muscle of ankle joint", "pain of acromioclavicular joint", "pain of distal radioulnar joint", "pain of facet joint", "pain of hip joint", "pain of interphalangeal joint of toe", "pain of joint of ankle", "pain of joint of elbow", "pain of joint of foot", "pain of joint of hand", "pain of joint of knee", "pain of joint of wrist", "pain of left acromioclavicular joint", "pain of left hip joint", "pain of left sternoclavicular joint", "pain of right acromioclavicular joint", "pain of right hip joint", "pain of right sternoclavicular joint", "pain of sacroiliac joint", "pain of sternoclavicular joint", "pain of temporomandibular joint", "pain of tibiofibular joint", "pain of vertebral joint", "pain on joint movement", "pain on passive stretch of joint", "persistent prosthetic joint pain", "shoulder joint pain", "subtalar joint pain", "talonavicular joint pain", "thoracic facet joint pain", "acute arthralgia of knee", "acute knee joint pain", "acute pain of joint of knee (finding)", "arc of pain in joint (observable entity)", "pain of bilateral acromioclavicular joints", "pain of bilateral acromioclavicular joints (finding)", "pain of both acromioclavicular joints", "arthralgia of both feet", "bilateral foot joint pain (finding)", "pain of joint of both feet", "pain of joint of bilateral hands", "pain of joint of bilateral hands (finding)", "pain of joint of both hands", "bilateral tmj (temporomandibular joint) pain", "pain in bilateral temporomandibular joints", "pain in bilateral temporomandibular joints (finding)", "pain in both temporomandibular joints", "cervical facet joint pain (finding)", "facet syndrome of cervical spine", "chronic sacroiliac joint pain (finding)", "arthralgia of distal interphalangeal joint of finger", "distal interphalangeal joint of finger pain (finding)", "arthralgia of 1st metatarsophalangeal joint", "first metatarsophalangeal joint pain (finding)", "joint pain in left hand (finding)", "joint pain in right hand (finding)", "joint pain of pelvic region (finding)", "arthralgia of lesser metatarsophalangeal joint", "lesser metatarsophalangeal joint pain (finding)", "facet syndrome of lumbar spine", "lumbar facet joint pain (finding)", "lumbar facet syndrome", "lumbar zygapophysial joint pain", "arthralgia of metacarpophalangeal joint", "metacarpophalangeal joint pain (finding)", "metatarsophalangeal joint pain (finding)", "myalgia of ankle joint", "hand pain", "finger pain"],
			"joint stiffness":          ["joint stiffness", "stiffness", "morning stiffness", "stiff hands", "hand stiffness", "finger stiffness", "stiff joints", "joint stiffness (finding)"],
			"toe pain":                ["toe pain", "painful toe", "big toe", "first toe", "1st toe", "pain in toe", "pain of toe", "toe ache"],
			"joint swelling":          ["joint swelling", "swollen joint", "effusion", "swelling in joint", "joint effusion"],
			"bone pain":               ["bone pain", "fracture", "broken bone", "bony tenderness", "skeletal pain", "bone pain (finding)", "osteodynia", "fracture (morphologic abnormality)", "fracture of bone", "fracture of bone (disorder)", "malignant bone pain", "malignant bone pain (finding)"],
			"muscle pain":             ["muscle pain", "myalgia", "muscle ache", "muscle cramps", "muscle weakness", "myopathy", "aching muscles", "muscle pain (finding)", "myodynia", "myoneuralgia", "myosalgia", "decreased muscle strength", "muscle strength reduced", "muscle weakness (finding)", "disorder of muscle", "disorder of skeletal and/or smooth muscle", "disorder of skeletal and/or smooth muscle (disorder)", "myopathic disease", "cramp", "cramp (finding)", "cramp in muscle", "muscle cramp", "abdominal muscle pain", "delayed onset muscle pain", "muscle tension pain", "pain in muscle of ankle joint", "pain in muscle of foot", "pain in muscle of forearm", "pain in muscle of hand", "pain in muscle of lower leg", "pain in muscle of lower limb", "pain in muscle of pelvis", "pain in muscle of shoulder", "pain in muscle of thigh", "pain in muscle of upper arm", "pain on movement of skeletal muscle", "abdominal muscle pain (finding)", "delayed onset muscle pain (finding)", "delayed onset myalgia", "doms - delayed onset muscle soreness", "muscle tension pain (finding)", "myalgia of ankle joint", "pain in muscle of ankle joint (finding)", "myalgia of foot", "pain in muscle of foot (finding)", "myalgia of forearm", "pain in muscle of forearm (finding)", "myalgia of hand", "pain in muscle of hand (finding)", "myalgia of lower leg", "pain in muscle of lower leg (finding)", "myalgia of pelvis", "pain in muscle of pelvis (finding)", "myalgia of shoulder", "pain in muscle of shoulder (finding)", "myalgia of thigh", "pain in muscle of thigh (finding)", "myalgia of upper arm", "pain in muscle of upper arm (finding)", "pain on movement of skeletal muscle (finding)"],
			"trauma":                  ["trauma", "injury", "accident", "fell", "fall", "mvc", "motor vehicle collision", "car accident", "hit head", "blunt trauma", "fall (event)", "injury - disorder", "traumatic injury", "traumatic injury (disorder)", "traumatic or non-traumatic injury", "traumatic or non-traumatic injury (disorder)", "accidental event", "accidental event (event)", "automobile accident", "automobile accident (event)", "car crash", "blunt injury", "blunt injury (disorder)", "blunt force injury", "blunt injury (morphologic abnormality)", "airway trauma", "antepartum hemorrhage with trauma", "bilateral explosive acoustic trauma of ears", "bilateral ocular trauma", "birth trauma deafness", "cerebral trauma", "cochlear trauma", "concussive cochlear trauma", "dental trauma", "education of parent about trauma therapy", "erb-duchenne palsy as birth trauma", "explosive acoustic trauma to ear", "facial nerve injury as birth trauma", "facial palsy as birth trauma", "fetal birth trauma", "fetal trauma", "industrial trauma", "klumpke-d\u00e9jerine paralysis as birth trauma", "left ear explosive acoustic trauma", "localized secondary occlusal trauma", "obstetric trauma causing pelvic hematoma", "occlusal trauma", "pain provoked by trauma", "paralysis from birth trauma", "perinatal trauma", "phrenic nerve paralysis as birth trauma", "primary occlusal trauma", "right ear explosive acoustic trauma", "secondary occlusal trauma", "seen by trauma service", "seen by trauma surgeon", "self-inflicted trauma involving penis", "trauma from instrument during delivery", "trauma to aortic valve", "trauma to mitral valve", "trauma to perineum during delivery", "trauma to pulmonary valve", "trauma to tricuspid valve", "trauma to vagina during delivery", "trauma to vulva during delivery", "under care of trauma surgeon", "vestibular trauma", "victim of psychological trauma", "victim of trauma", "victim of trauma with multiple injuries", "vocal cord trauma", "airway trauma (disorder)", "antepartum hemorrhage with trauma (disorder)", "explosive acoustic trauma of bilateral ears", "explosive acoustic trauma of bilateral ears (finding)", "explosive acoustic trauma of both ears", "traumatic injury of both eyes", "traumatic injury of globe of bilateral eyes", "traumatic injury of globe of bilateral eyes (disorder)", "birth trauma deafness (disorder)", "cerebral trauma (disorder)", "cochlear trauma (disorder)", "cochlear trauma due to head injury", "concussive cochlear trauma (disorder)", "dental trauma (disorder)", "education of parent about trauma therapy (situation)", "erb's palsy as birth trauma", "erb-duchenne palsy as birth trauma (disorder)", "acoustic explosive ear trauma", "explosive acoustic trauma to ear (finding)", "impulsive acoustic trauma", "otitic blast injury", "facial nerve injury as birth trauma (disorder)", "facial nerve palsy due to birth trauma", "facial palsy as birth trauma (disorder)", "birth injury", "birth trauma", "birth trauma of fetus", "birth trauma of foetus", "fetal birth trauma (disorder)"],
			"head injury":             ["head injury", "head trauma", "hit head", "skull fracture", "concussion", "traumatic brain injury", "tbi", "hi - head injury", "injury of head", "injury of head (disorder)", "injury of head region", "traumatic brain injury (disorder)", "closed injury of head", "crush injury of head and neck", "degloving injury of head", "degloving injury of head and neck", "head and neck injury", "head and neck superficial nerve injury", "head injury advice given", "injury of back of head", "injury of extracranial vessel of head", "injury of fascia of head", "injury of head and/or neck", "injury of head with otorrhagia", "injury of head with rhinorrhagia", "injury of intracranial vessel of head", "injury of muscle of head", "injury of tendon of head", "injury to superficial nerves of head", "major head injury", "minor head injury", "moderate head injury", "needle stick injury of head", "non-accidental traumatic head injury to child", "pressure injury of head", "pressure injury of head stage i", "pressure injury of head stage ii", "pressure injury of head stage iii", "pressure injury of head stage iv", "sequelae of superficial injury of head", "superficial injury of head", "superficial injury of head and neck", "traumatic injury of head of pancreas", "unstageable pressure injury of head", "vertigo preceded by head injury", "closed head injury", "closed injury of head (disorder)", "crush injury of head and neck (disorder)", "degloving injury of head (disorder)", "degloving injury of head and neck (disorder)", "head and neck injury (disorder)", "head and neck superficial nerve injury (disorder)", "head injury advice given (situation)", "injury of back of head (disorder)", "injury of extracranial vessel of head (disorder)", "injury of fascia of head (disorder)", "injury of head and/or neck (disorder)", "head injury with hemorrhage from ear", "injury of head with otorrhagia (disorder)", "head injury with hemorrhage from nose", "injury of head with rhinorrhagia (disorder)", "injury of intracranial vessel of head (disorder)", "injury of muscle of head (disorder)", "injury of tendon of head (disorder)", "injury to superficial nerves of head (disorder)", "major head injury (disorder)", "minor head injury (disorder)", "moderate head injury (disorder)", "needle stick injury of head (disorder)", "non-accidental traumatic head injury to child (disorder)", "pressure injury of head (disorder)", "pressure injury of head stage 1", "pressure injury of head stage i (disorder)", "pressure injury of head stage 2", "pressure injury of head stage ii (disorder)", "pressure ulcer of head stage 2", "pressure injury of head stage 3", "pressure injury of head stage iii (disorder)", "pressure ulcer of head stage 3", "pressure injury of head stage 4", "pressure injury of head stage iv (disorder)", "pressure ulcer of head stage 4", "sequelae of superficial injury of head (disorder)", "superficial injury of head (disorder)", "superficial injury of head and neck (disorder)", "traumatic injury of head of pancreas (disorder)", "unstageable pressure injury of head (disorder)", "vertigo after head injury", "vertigo preceded by head injury (disorder)"],
			"neck injury":             ["neck injury", "cervical spine injury", "c-spine injury", "whiplash", "injury of neck", "injury of neck (disorder)", "crush injury of head and neck", "crushing injury of anterior neck", "crushing injury of neck", "degloving injury of head and neck", "degloving injury of neck", "head and neck injury", "head and neck superficial nerve injury", "hyperextension injury of neck", "injury of anterior neck", "injury of back of neck", "injury of face and neck", "injury of fascia of neck", "injury of head and/or neck", "injury of muscle of neck", "injury of neck of urinary bladder", "injury of peripheral nerves of neck", "injury of superficial nerves of neck", "injury of tendon of neck", "injury to blood vessel of neck", "needle stick injury of neck", "superficial injury of head and neck", "superficial injury of neck", "superficial injury of neck with infection", "whiplash injury to neck", "crush injury of head and neck (disorder)", "crush injury, throat", "crush injury, throat (disorder)", "crushing injury of throat", "crush injury, neck", "crushing injury of neck (disorder)", "degloving injury of head and neck (disorder)", "degloving injury of neck (disorder)", "head and neck injury (disorder)", "head and neck superficial nerve injury (disorder)", "hyperextension injury of neck (disorder)", "injury of anterior neck (disorder)", "injury of throat", "throat injury", "injury of back of neck (disorder)", "injury of face and neck (disorder)", "injury of fascia of neck (disorder)", "injury of head and/or neck (disorder)", "injury of muscle of neck (disorder)", "injury of bladder neck", "injury of neck of urinary bladder (disorder)", "injury of peripheral nerves of neck (disorder)", "injury of superficial nerves of neck (disorder)", "injury of tendon of neck (disorder)", "injury to blood vessel of neck (disorder)", "needle stick injury of neck (disorder)", "superficial injury of head and neck (disorder)", "superficial injury of neck (disorder)", "superficial injury of neck with infection (disorder)", "acceleration-deceleration injury of neck", "whiplash injury", "whiplash injury to neck (disorder)"],
			"laceration":              ["laceration", "cut", "wound", "gash", "skin tear", "bleeding wound", "laceration (morphologic abnormality)", "laceration - injury", "laceration - injury (disorder)", "tear - wound", "wound, lacerated", "incised wound - morphology", "incised wound - morphology (morphologic abnormality)", "wound (disorder)", "wound (morphologic abnormality)", "tear of skin", "traumatic tear of skin", "traumatic tear of skin (disorder)", "incised wound", "incised wound (disorder)", "accidental laceration during a procedure", "arterial laceration", "brain stem laceration", "brain stem laceration with concussion", "broad ligament laceration syndrome", "central laceration during delivery", "cerebellar laceration", "cerebellar laceration and contusion", "cerebellar laceration with concussion", "cerebellar laceration with open intracranial wound", "cerebral cortex laceration with concussion", "cervical laceration", "complex laceration of auricle of ear", "complex laceration of buccal mucosa", "complex laceration of cheek", "complex laceration of chin", "complex laceration of floor of mouth", "complex laceration of forehead", "complex laceration of hard palate", "complex laceration of labial mucosa", "complex laceration of left periorbital region", "complex laceration of left pinna", "complex laceration of mandibular attached gingiva", "complex laceration of mandibular vestibule", "complex laceration of maxillary attached gingiva", "complex laceration of maxillary vestibule", "complex laceration of neck", "complex laceration of nose", "complex laceration of oropharynx", "complex laceration of right periorbital region", "complex laceration of right pinna", "complex laceration of scalp", "complex laceration of soft palate", "complex laceration of tongue", "complex laceration of tonsil", "complex periorbital laceration", "conjunctival laceration", "contaminated complex laceration of buccal mucosa", "contaminated complex laceration of cheek", "contaminated complex laceration of chin", "contaminated complex laceration of forehead", "contaminated complex laceration of hard palate", "contaminated complex laceration of labial mucosa", "contaminated complex laceration of neck", "contaminated complex laceration of nose", "contaminated complex laceration of oropharynx", "contaminated complex laceration of scalp", "contaminated complex laceration of soft palate", "contaminated complex laceration of tongue", "contaminated complex laceration of tonsil", "contaminated complex periorbital laceration", "contaminated simple laceration of buccal mucosa", "contaminated simple laceration of cheek", "contaminated simple laceration of chin", "contaminated simple laceration of forehead", "contaminated simple laceration of hard palate", "contaminated simple laceration of labial mucosa", "contaminated simple laceration of neck", "contaminated simple laceration of nose", "contaminated simple laceration of oropharynx", "contaminated simple laceration of scalp", "contaminated simple laceration of soft palate", "contaminated simple laceration of tongue", "contaminated simple laceration of tonsil", "contaminated simple periorbital laceration", "contusion and laceration of cerebrum", "corneal laceration", "corneoscleral laceration", "cortex laceration", "cortex laceration and contusion", "cortex laceration with open intracranial wound", "deep laceration", "deep laceration of ankle", "deep laceration of finger", "deep laceration of foot", "deep laceration of hip", "deep laceration of knee", "deep laceration of lower limb", "deep laceration of nail of finger", "deep laceration of nail of thumb"],
			"burn":                    ["burn", "burning injury", "thermal burn", "chemical burn", "scald", "flame burn", "burn (disorder)", "thermal burn (disorder)", "thermal burn (morphologic abnormality)", "thermal burn - disorder", "caustic burn", "chemical burn (disorder)", "chemical burn (morphologic abnormality)", "burn - lesion", "burn injury", "burn injury (morphologic abnormality)", "scald of skin", "scalding injury", "scalding injury (morphologic abnormality)", "scald of skin (disorder)", "abrasion and/or friction burn", "abrasion and/or friction burn of skin", "abrasion and/or friction burn with infection", "abrasion and/or friction burn without infection", "acid burn of skin", "acid chemical burn of conjunctival sac", "acid chemical burn of cornea", "alkali burn of skin", "alkaline chemical burn of conjunctival sac", "alkaline chemical burn of cornea", "application site burn", "aspirin burn of oral mucosa", "bleach burn of skin", "burn by hot liquid", "burn by hot object", "burn confined to eye and adnexa", "burn contracture of skin", "burn erythema of abdominal wall", "burn erythema of buccal mucosa", "burn erythema of chest wall", "burn erythema of floor of mouth", "burn erythema of hard palate", "burn erythema of labial mucosa", "burn erythema of mandibular attached gingiva", "burn erythema of mandibular vestibule", "burn erythema of maxillary attached gingiva", "burn erythema of maxillary vestibule", "burn erythema of oropharynx", "burn erythema of soft palate", "burn erythema of tongue", "burn erythema of tonsillar area", "burn injury of skin of finger", "burn of abdominal wall", "burn of ankle", "burn of ankle and foot", "burn of anterior eyeball segment", "burn of anus", "burn of appendix", "burn of axilla", "burn of back", "burn of back of hand", "burn of bilateral wrists and hands", "burn of breast", "burn of bronchus", "burn of buccal mucosa", "burn of buttock", "burn of cardiovascular structure", "burn of cecum", "burn of cervix", "burn of cheek", "burn of chest wall", "burn of chin", "burn of circumoral region", "burn of clavicular region", "burn of coccygeal region", "burn of colon", "burn of conjunctiva", "burn of conjunctival sac", "burn of cornea and conjunctival sac", "burn of cornea of left eye", "burn of cornea of right eye", "burn of digit of hand", "burn of digits of hand", "burn of dorsum of left hand", "burn of dorsum of right hand", "burn of duodenum", "burn of ear", "burn of elbow", "burn of endocrine structure", "burn of esophagus", "burn of eye proper", "burn of eye region", "burn of face", "burn of fallopian tube", "burn of female genitalia", "burn of female perineum", "burn of finger", "burn of floor of mouth", "burn of foot", "burn of forearm"],
			"dislocation":             ["dislocation", "dislocated shoulder", "dislocated hip", "joint out of place", "dislocation (morphologic abnormality)", "ankle - recurrent dislocation", "anterior dislocation of left shoulder joint", "anterior dislocation of lens", "anterior dislocation of right shoulder joint", "anterior dislocation of shoulder joint", "anterior dislocation of sternoclavicular joint", "bilateral congenital dislocation of hip", "bilateral congenital knee dislocation", "bilateral congenital patella dislocation", "bilateral dislocation of lacrimal glands", "bilateral posterior lens dislocation", "central dislocation of tooth", "central fracture dislocation acetabulum", "central traumatic dislocation of hip", "closed anterior dislocation of elbow", "closed anterior dislocation of glenohumeral joint", "closed anterior dislocation of hip", "closed dislocation atlanto-occipital joint", "closed dislocation atlantoaxial joint", "closed dislocation c2/c3", "closed dislocation c3/c4", "closed dislocation c4/c5", "closed dislocation c5/c6", "closed dislocation c6/c7", "closed dislocation c7/t1", "closed dislocation cervical spine", "closed dislocation lumbar spine", "closed dislocation of left temporomandibular joint", "closed dislocation of manubriosternal joint", "closed dislocation of perilunate joint", "closed dislocation of radiocarpal joint", "closed dislocation of sacrum", "closed dislocation of talus", "closed dislocation thoracic spine", "closed fracture dislocation digit", "closed fracture dislocation elbow joint", "closed fracture dislocation foot", "closed fracture dislocation lunate (volar)", "closed fracture dislocation midcarpal", "closed fracture dislocation multiple digits", "closed fracture dislocation of ankle joint", "closed fracture dislocation of hip joint", "closed fracture dislocation of knee joint", "closed fracture dislocation of midtarsal joint", "closed fracture dislocation of pelvis", "closed fracture dislocation of sacroiliac joint", "closed fracture dislocation of sternum", "closed fracture dislocation of subtalar joint", "closed fracture dislocation of wrist", "closed fracture dislocation perilunate (dorsal)", "closed fracture dislocation radiocarpal joint", "closed fracture dislocation shoulder joint", "closed inferior dislocation of glenohumeral joint", "closed lateral dislocation of elbow", "closed lateral dislocation of subtalar joint", "closed left elbow dislocation", "closed left finger dislocation", "closed left patella dislocation", "closed left shoulder dislocation", "closed medial dislocation of elbow", "closed medial dislocation of subtalar joint", "closed obturator dislocation of hip", "closed posterior dislocation of elbow", "closed posterior dislocation of glenohumeral joint", "closed posterior dislocation of hip", "closed right elbow dislocation", "closed right finger dislocation", "closed right patella dislocation", "closed right shoulder dislocation", "closed traumatic dislocation ankle joint", "closed traumatic dislocation costovertebral joint", "closed traumatic dislocation digit", "closed traumatic dislocation elbow joint, anterior", "closed traumatic dislocation elbow joint, lateral", "closed traumatic dislocation elbow joint, medial", "closed traumatic dislocation hip joint, anterior", "closed traumatic dislocation hip joint, posterior", "closed traumatic dislocation knee joint, anterior", "closed traumatic dislocation knee joint, lateral", "closed traumatic dislocation knee joint, medial", "closed traumatic dislocation knee joint, posterior", "closed traumatic dislocation knee joint, rotatory", "closed traumatic dislocation laryngeal cartilage", "closed traumatic dislocation lunate (volar)", "closed traumatic dislocation midcarpal joint", "closed traumatic dislocation multiple digits", "closed traumatic dislocation of cervical vertebra", "closed traumatic dislocation of coccyx", "closed traumatic dislocation of elbow joint", "closed traumatic dislocation of glenohumeral joint", "closed traumatic dislocation of hip", "closed traumatic dislocation of joint", "closed traumatic dislocation of knee joint", "closed traumatic dislocation of lumbar vertebra", "closed traumatic dislocation of lumbosacral joint"],
			"hip pain":                ["hip pain", "hip fracture", "hip injury", "groin pain", "hip tenderness", "pain of hip region", "pain of hip region (finding)", "fracture of proximal end of femur", "fracture of proximal end of femur (disorder)", "injury of hip region", "injury of hip region (disorder)", "inguinal pain", "inguinal pain (finding)", "pain of bilateral hip joints", "pain of hip joint", "pain of left hip joint", "pain of right hip joint", "bilateral hip joint pain", "pain in both hip joints", "pain of bilateral hip joints (finding)", "arthralgia of hip", "hip joint pain", "pain of hip joint (finding)", "pain of left hip joint (finding)", "pain of right hip joint (finding)"],
			"knee pain":               ["knee pain", "knee injury", "knee swelling", "knee locking", "knee giving way", "pain of knee region", "pain of knee region (finding)", "injury of knee", "injury of knee (disorder)", "knee locking (finding)", "acute pain of joint of knee", "anterior knee pain", "complex regional pain syndrome of knee", "pain of joint of knee", "acute arthralgia of knee", "acute knee joint pain", "acute pain of joint of knee (finding)", "akp - anterior knee pain", "anterior knee pain (finding)", "algodystrophy of knee", "complex regional pain syndrome of knee (disorder)", "arthralgia of knee", "pain of joint of knee (finding)"],
			"ankle pain":              ["ankle pain", "twisted ankle", "ankle injury", "ankle swelling", "pain in ankle", "sprained ankle", "twisted", "swollen ankle"],
			"swelling":                ["swelling", "edema", "swollen", "distension", "puffiness"],
			"chest wall pain":         ["chest wall pain", "costochondritis", "musculoskeletal chest", "reproducible chest pain", "tender chest wall", "chest tender on palpation", "localized chest pain", "chest wall pain (finding)", "localized chest pain (finding)", "costal chondritis", "costal chondritis (disorder)", "anterior chest wall pain", "anterior chest wall pain (finding)"],
		},

		# ── DERMATOLOGICAL ───────────────────────────────────────────
		"dermatological": {
			"rash":                    ["rash", "skin rash", "erythema", "hives", "urticaria", "eruption", "skin lesion", "redness", "red", "flushing", "erythema (finding)", "erythema (morphologic abnormality)", "erythema - observation", "nettle rash", "urticarial rash", "weal", "welt", "wheal", "wheal (finding)", "urticaria (disorder)", "urticaria (morphologic abnormality)", "eruption (morphologic abnormality)", "exanthem", "exanthema", "skin lesion (disorder)", "flushing (disorder)", "breaking out - eruption", "eruption of skin", "eruption of skin (disorder)", "skin eruption", "blush", "blushing", "blushing, function", "blushing, function (observable entity)", "flush", "application site rash", "bacteremic skin rash", "blanching rash", "butterfly rash", "centrifugal rash", "centripetal rash", "diaper rash", "erythematous rash", "generalized rash", "grade of skin rash", "gravel rash", "introduction procedure site rash", "leptospiral rash", "meningococcal rash", "multimorphic rash", "mycoplasma pneumoniae induced rash and mucositis", "non-blanching rash", "phototherapy skin rash", "pruritic rash", "purpuric rash", "rash absent", "rash of genitalia", "rash of mouth", "rash of scalp", "rash of secondary syphilis", "rash of systemic lupus erythematosus", "serum rash", "smallpox without rash", "southern tick-associated rash illness", "synchronous rash", "vaccination site rash", "administration site rash", "application site rash (disorder)", "rash of skin due to bacteremia", "rash of skin due to bacteremia (disorder)", "blanching rash (disorder)", "butterfly rash (disorder)", "malar rash", "centrifugal rash (finding)", "centripetal rash (finding)", "ammonia dermatitis", "diaper dermatitis", "diaper erythema", "diaper rash (disorder)", "jacquet's dermatitis", "jacquet's erythema", "urine-induced contact dermatitis", "erythematous rash (disorder)", "diffuse rash", "generalized rash (disorder)", "grade of skin rash (observable entity)", "gravel rash (disorder)", "superficial gravel rash", "leptospiral rash (disorder)", "meningococcal rash (disorder)", "multimorphic rash (disorder)", "mirm - mycoplasma-induced rash and mucositis", "mycoplasma pneumoniae induced rash and mucositis (disorder)", "mycoplasma-induced rash and mucositis", "non-blanching rash (disorder)", "phototherapy skin rash (disorder)", "itchy skin eruption", "prurigo", "pruritic rash (disorder)", "purpuric rash (disorder)", "rash absent (situation)"],
			"petechiae":               ["petechiae", "pinpoint red spots", "non-blanching rash", "purpura", "petechia", "petechia (morphologic abnormality)", "petechiae (disorder)", "petechial hemorrhage", "non-blanching rash (disorder)", "disorder characterized by purpura", "purpura (morphologic abnormality)", "purpuric disorder", "purpuric disorder (disorder)", "calcaneal petechiae", "calcaneal petechiae of left foot", "calcaneal petechiae of right foot", "neonatal facial petechiae", "perifollicular petechiae of skin", "perinatal cutaneous petechiae", "petechiae of skin", "petechiae of tracheobronchial mucosa", "traumatic petechiae", "black heel", "black heel disease", "calcaneal petechiae (disorder)", "talon noir", "neonatal facial petechiae (disorder)", "perifollicular hemorrhage", "perifollicular petechiae of skin (disorder)", "perinatal cutaneous petechiae (disorder)", "petechiae of skin (disorder)", "petechial eruption", "petechial rash", "petechiae of tracheobronchial mucosa (disorder)", "tracheobronchial mucosal petechiae", "traumatic petechiae (disorder)"],
			"cellulitis":              ["cellulitis", "skin infection", "red warm skin", "spreading redness", "erythema with warmth", "cellulitis (disorder)", "cellulitis (morphologic abnormality)", "infection of skin and/or subcutaneous tissue", "infection of skin and/or subcutaneous tissue (disorder)", "infective dermatological disorders", "skin and subcutaneous tissue infection", "acute cellulitis", "acute female pelvic cellulitis", "anaerobic cellulitis", "anal cellulitis", "anorectal cellulitis", "bacterial cellulitis", "cellulitis - anus or rectum", "cellulitis and abscess of abdominal wall", "cellulitis and abscess of ankle", "cellulitis and abscess of axilla", "cellulitis and abscess of back", "cellulitis and abscess of breast", "cellulitis and abscess of buttock", "cellulitis and abscess of cheek (external)", "cellulitis and abscess of chest wall", "cellulitis and abscess of chin", "cellulitis and abscess of elbow", "cellulitis and abscess of face", "cellulitis and abscess of finger", "cellulitis and abscess of flank", "cellulitis and abscess of forearm", "cellulitis and abscess of forehead", "cellulitis and abscess of groin", "cellulitis and abscess of hand", "cellulitis and abscess of heel", "cellulitis and abscess of hip", "cellulitis and abscess of knee", "cellulitis and abscess of lower leg", "cellulitis and abscess of lower limb", "cellulitis and abscess of neck", "cellulitis and abscess of nose (external)", "cellulitis and abscess of perineum", "cellulitis and abscess of shoulder", "cellulitis and abscess of submandibular region", "cellulitis and abscess of temple region", "cellulitis and abscess of thigh", "cellulitis and abscess of toe", "cellulitis and abscess of trunk", "cellulitis and abscess of umbilicus", "cellulitis and abscess of upper arm", "cellulitis and abscess of upper limb", "cellulitis and abscess of wrist", "cellulitis of abdominal wall", "cellulitis of ankle", "cellulitis of axilla", "cellulitis of breast", "cellulitis of buccal space of mouth", "cellulitis of buttock", "cellulitis of calf of leg", "cellulitis of canine space of mouth", "cellulitis of chest wall", "cellulitis of chin", "cellulitis of clavicular region", "cellulitis of corpus cavernosum", "cellulitis of digit", "cellulitis of dorsum of hand", "cellulitis of elbow", "cellulitis of external cheek", "cellulitis of external nose", "cellulitis of eyelid", "cellulitis of face", "cellulitis of finger", "cellulitis of flank", "cellulitis of floor of mouth", "cellulitis of foot", "cellulitis of foot excluding toe", "cellulitis of forearm", "cellulitis of forehead", "cellulitis of fourth toe", "cellulitis of gingiva", "cellulitis of great toe", "cellulitis of groin", "cellulitis of hand", "cellulitis of hand excluding finger", "cellulitis of head", "cellulitis of heel", "cellulitis of hip", "cellulitis of index finger", "cellulitis of infratemporal fossa", "cellulitis of knee", "cellulitis of larynx", "cellulitis of left ankle", "cellulitis of left axilla", "cellulitis of left buttock", "cellulitis of left calf", "cellulitis of left clavicular region", "cellulitis of left elbow", "cellulitis of left foot", "cellulitis of left forearm"],
			"abscess":                 ["abscess", "skin abscess", "boil", "furuncle", "carbuncle", "pus collection", "fluctuant mass", "abscess (disorder)", "abscess (morphologic abnormality)", "abscess morphology", "furuncle (disorder)", "furuncle (morphologic abnormality)", "furunculus", "carbuncle (disorder)", "carbuncle (morphologic abnormality)", "fluctuant mass (morphologic abnormality)", "abscess of skin and/or subcutaneous tissue", "abscess of skin and/or subcutaneous tissue (disorder)", "cutaneous abscess", "abdominal abscess", "abdominal visceral abscess", "abdominopelvic abscess", "abscess at site of aortic coarctation", "abscess at site of arterial duct", "abscess at site of interatrial communication", "abscess between intestinal loops", "abscess gonococcal", "abscess iliopsoas non-tuberculous", "abscess of abdominal wall", "abscess of adrenal gland", "abscess of ankle", "abscess of anorectal fissure", "abscess of aorta", "abscess of aortic root", "abscess of aortic valve", "abscess of appendix", "abscess of axilla", "abscess of back", "abscess of back, except buttock", "abscess of bartholin's gland", "abscess of big toe", "abscess of bone of accessory sinus", "abscess of bone of skull", "abscess of brain", "abscess of brainstem", "abscess of breast", "abscess of broad ligament", "abscess of buccal space of mouth", "abscess of bursa", "abscess of bursa of ankle", "abscess of bursa of bilateral hands", "abscess of bursa of bilateral hips", "abscess of bursa of bilateral knees", "abscess of bursa of elbow", "abscess of bursa of foot", "abscess of bursa of hand", "abscess of bursa of hip", "abscess of bursa of knee", "abscess of bursa of left hand", "abscess of bursa of left hip", "abscess of bursa of left knee", "abscess of bursa of left wrist", "abscess of bursa of right hand", "abscess of bursa of right hip", "abscess of bursa of right knee", "abscess of bursa of right wrist", "abscess of bursa of shoulder", "abscess of bursa of wrist", "abscess of buttock", "abscess of calf", "abscess of canine space of mouth", "abscess of cardiac septum", "abscess of cardiovascular heterograft", "abscess of cardiovascular homograft", "abscess of cardiovascular structure of trunk", "abscess of cerebral hemisphere lobe", "abscess of cheek", "abscess of chest wall", "abscess of chin", "abscess of common atrioventricular valve", "abscess of conjunctiva", "abscess of connective tissue", "abscess of corpus callosum", "abscess of corpus cavernosum", "abscess of cowper's gland", "abscess of digestive system", "abscess of digit", "abscess of dorsum of hand", "abscess of elbow", "abscess of epididymis", "abscess of esophagus", "abscess of external auditory canal", "abscess of external cheek", "abscess of external ear", "abscess of external nose", "abscess of eye", "abscess of eyelid", "abscess of face", "abscess of facial bone", "abscess of fallopian tube"],
			"angioedema":              ["angioedema", "lip swelling", "tongue swelling", "face swelling", "facial edema", "swollen lips", "swollen tongue", "angioedema (disorder)", "angioedema (morphologic abnormality)", "angioneurotic edema", "quincke's disease", "quincke's edema", "lip swelling (finding)", "tongue swelling (finding)", "ace inhibitor-aggravated angioedema", "acquired angioedema type i", "acquired angioedema type ii", "allergic angioedema", "allergic urticaria and/or angioedema", "angioedema and/or urticaria", "angioedema of eyelid", "angioedema of lip", "angioedema of tongue", "angioedema of uvula", "autoimmune angioedema", "autoimmune urticaria and/or angioedema", "cholinergic angioedema", "episodic angioedema with eosinophilia", "hereditary angioedema", "idiopathic angioedema", "idiopathic urticaria and/or angioedema", "physical angioedema", "respiratory angioedema", "vibratory angioedema", "ace inhibitor-induced angioedema", "angiotensin converting enzyme (ace) inhibitor-aggravated angioedema", "angiotensin converting enzyme inhibitor-aggravated angioedema", "angiotensin converting enzyme inhibitor-aggravated angioedema (disorder)", "acquired angioedema type 1", "acquired angioedema type i (disorder)", "acquired angioedema type 2", "acquired angioedema type ii (disorder)", "allergic angioedema (disorder)", "allergic urticaria and/or angioedema (disorder)", "angioedema and/or urticaria (disorder)", "angioedema of eyelid (disorder)", "angioedema of lip (disorder)", "angioedema of tongue (disorder)", "autoimmune angioedema (disorder)", "autoimmune urticaria and/or angioedema (disorder)", "cholinergic angioedema (disorder)", "episodic angioedema with eosinophilia (disorder)", "hae - hereditary angioedema", "hane - hereditary angioneurotic edema", "hereditary angioedema (disorder)", "hereditary angioneurotic edema", "hereditary quincke's edema", "idiopathic angioedema (disorder)", "idiopathic urticaria and/or angioedema (disorder)", "inducible angioedema", "physical angioedema (disorder)", "respiratory angioedema (disorder)", "vibratory angioedema (disorder)"],
			"pruritis":                ["pruritis", "itching", "itch", "itchy skin", "generalized itching", "itching (finding)", "itchy", "generalized pruritus", "generalized pruritus (finding)"],
			"pallor":                  ["pallor", "pale skin", "pale", "pallid", "ashen", "pasty skin", "pale color", "pale color saturation", "pale color saturation (qualifier value)", "pallor of liver", "pallor of lung", "pallor of neuroretinal rim", "pallor of optic disc", "pallor of spleen", "temporal pallor of optic disc", "pale liver", "pallor of liver (finding)", "pale lung", "pallor of lung (finding)", "pallor of neuroretinal rim (finding)", "optic disc pallor", "pale optic disc", "pallor of optic disc (finding)", "pale spleen", "pallor of spleen (finding)", "temporal pallor of optic disc (finding)"],
			"diaphoresis":             ["diaphoresis", "sweating", "profuse sweating", "cold sweats", "clammy skin", "soaking sweat", "excessive sweating", "sweating profusely", "hidrosis", "perspiration", "clamminess", "clammy", "sweating attack"],
		},

		# ── INFECTIOUS DISEASE ───────────────────────────────────────
		"infectious": {
			"fever":                   ["fever", "febrile", "high temp", "pyrexia", "temperature elevated", "temp high", "hyperthermia", "high temperature", "feverish", "fever (finding)", "pyrexial", "hyperthermia (disorder)", "body temperature above reference range", "body temperature above reference range (finding)", "has a temperature", "high body temperature", "increased body temperature", "temperature raised", "high temperature (physical force)", "acute q fever", "acute rheumatic fever", "acute rise of fever", "african tick bite fever", "alkhurma hemorrhagic fever", "arbovirus hemorrhagic fever", "arenaviral hemorrhagic fever", "argentinian hemorrhagic fever", "aseptic fever", "bancroftian filarial fever", "batai fever", "bebaru fever", "biphasic fever", "black water fever", "bolivian hemorrhagic fever", "boutonneuse fever", "brass-founders' fever", "brazilian hemorrhagic fever", "brazilian purpuric fever", "calchaqui fever", "candiru fever", "canicola fever", "cat-bite fever", "central fever", "chapare hemorrhagic fever", "chikungunya fever", "chronic fever", "chronic q fever", "colorado tick fever", "continuous fever", "copper fever", "cough with fever", "crimean-congo hemorrhagic fever", "dehydration fever in newborn", "dengue hemorrhagic fever", "disorder characterized by fever", "double quotidien fever", "eastern rocky mountain spotted fever", "enteroviral exanthematous fever", "erythema marginatum in acute rheumatic fever", "etiocholanolone fever", "factitious fever", "falling phase of fever", "familial mediterranean fever", "far eastern spotted fever", "fever defervescence", "fever greater than 100.4 fahrenheit", "fever of newborn", "fever with chills", "fh: hay fever", "filoviral hemorrhagic fever", "fort bragg fever", "glandular fever pharyngitis", "gradual fall of fever", "gradual rise of fever", "grain fever", "hay fever with asthma", "hazara hemorrhagic fever", "hemorrhagic fever with renal syndrome", "hepatitis in yellow fever", "hereditary periodic fever", "humidifier fever", "hyperimmunoglobulinemia d with periodic fever", "intermittent fever", "intermittent hepatic fever", "irregular fever", "isfahan fever", "izumi fever", "jungle yellow fever", "kunjin fever", "lassa fever", "lujo hemorrhagic fever", "maguari fever", "malarial fever", "malayan filarial fever", "malignant tertian fever", "manzanilla fever", "mayaro fever", "menstrual cycle dependent periodic fever", "metal fever", "mucambo fever"],
			"chills":                  ["chills", "rigors", "shivering", "shaking chills", "chills and rigors", "chill", "chill (finding)", "rigor", "rigor (finding)", "fever with chills", "chills and fever", "fever with chills (finding)", "fever with rigors"],
			"night sweats":            ["night sweats", "sweating at night", "waking up soaked", "nocturnal diaphoresis", "night sweats (finding)"],
			"lymphadenopathy":         ["lymphadenopathy", "swollen lymph nodes", "enlarged lymph nodes", "glands up", "lymph node swelling", "enlargement of lymph nodes", "la - lymphadenopathy", "ln - lymphadenopathy", "lymphadenopathy (disorder)", "lymphadenopathy - swelling", "swelling of lymph node", "swelling of lymph nodes", "swollen lymph glands", "anterior auricular lymphadenopathy", "anterior cervical lymphadenopathy", "anterior mediastinal lymphadenopathy", "anterior tibial lymphadenopathy", "aortic lymphadenopathy", "apical axillary lymphadenopathy", "appendicular lymphadenopathy", "axillary lymphadenopathy", "brachial lymphadenopathy", "celiac lymphadenopathy", "central axillary lymphadenopathy", "cervical lymphadenopathy", "colic lymphadenopathy", "common duct lymphadenopathy", "cubital lymphadenopathy", "cystic lymphadenopathy", "deep inguinal lymphadenopathy", "deep lymphadenopathy", "deep popliteal lymphadenopathy", "delphian lymphadenopathy", "diaphragmatic lymphadenopathy", "epigastric lymphadenopathy", "epitrochlear lymphadenopathy", "esophageal lymphadenopathy", "external iliac lymphadenopathy", "facial lymphadenopathy", "fibrotic lymphadenopathy", "fibular lymphadenopathy", "focal lymphadenopathy", "gastro-omental lymphadenopathy", "gluteal lymphadenopathy", "gut-associated lymphadenopathy", "head and neck lymphadenopathy", "hepatic lymphadenopathy", "hilar lymphadenopathy", "hypogastric lymphadenopathy", "ileocolic lymphadenopathy", "iliac lymphadenopathy", "inferior auricular lymphadenopathy", "inferior gluteal lymphadenopathy", "inferior inguinal lymphadenopathy", "inferior mesenteric lymphadenopathy", "inferior pancreatic lymphadenopathy", "inferior pancreaticoduodenal lymphadenopathy", "inferior tracheobronchial lymphadenopathy", "infraclavicular lymphadenopathy", "inguinal lymphadenopathy", "innominate lymphadenopathy", "intercostal lymphadenopathy", "interiliac lymphadenopathy", "intermediate common iliac lymphadenopathy", "intermediate external iliac lymphadenopathy", "intestinal lymphadenopathy", "jugular lymphadenopathy", "juxtaintestinal lymphadenopathy", "lateral axillary lymphadenopathy", "lateral cervical lymphadenopathy", "lateral common iliac lymphadenopathy", "lateral external iliac lymphadenopathy", "lateral pericardial lymphadenopathy", "lateral vesicular lymphadenopathy", "left colic lymphadenopathy", "left gastric lymphadenopathy", "loa loa lymphadenopathy", "lower extremity lymphadenopathy", "lumbar lymphadenopathy", "lymphadenopathy absent", "lymphadenopathy of epiploic foramen", "lymphadenopathy of greater curvature of stomach", "lymphadenopathy of head and/or neck", "lymphadenopathy of left axilla", "lymphadenopathy of lesser curvature of stomach", "lymphadenopathy of right axilla", "mandibular lymphadenopathy", "medial common iliac lymphadenopathy", "medial external iliac lymphadenopathy", "medial lacunar lymphadenopathy", "mediastinal lymphadenopathy", "mesenteric lymphadenopathy", "midcolic lymphadenopathy", "obturator lymphadenopathy", "occipital lymphadenopathy", "pancreatic lymphadenopathy", "pancreaticoduodenal lymphadenopathy", "pancreaticosplenic lymphadenopathy", "paramammary lymphadenopathy", "parametrial lymphadenopathy"],
			"sore throat":             ["sore throat", "pharyngitis", "throat pain", "painful swallowing", "throat soreness", "tonsillitis", "sore throat (finding)", "pharyngitis (disorder)", "angina tonsillaris", "tonsillitis (disorder)", "pain in throat", "pain in throat (finding)", "pharyngeal pain", "throat discomfort", "odynophagia", "pain on swallowing", "swallowing painful", "swallowing painful (finding)", "acute sore throat", "chronic sore throat", "has a sore throat", "streptococcal sore throat", "streptococcal sore throat with scarlatina", "chronic sore throat (finding)", "persistent sore throat", "has a sore throat (situation)", "sore throat present", "septic sore throat", "strep throat", "strept throat", "streptococcal angina", "streptococcal pharyngitis", "streptococcal sore throat (disorder)", "streptococcal sore throat with scarlatina (disorder)"],
			"ear pain":                ["ear pain", "otalgia", "earache", "ear infection", "ear drainage", "otitis", "ear ache", "pain of ear", "pain of ear (finding)", "tympanic membrane", "bulging", "red tympanic membrane", "bulging red tympanic membrane", "inflammatory disorder of ear", "otitis (disorder)", "infection of ear", "infection of ear (disorder)"],
			"nasal congestion":        ["nasal congestion", "stuffy nose", "runny nose", "rhinorrhea", "blocked nose", "sinus congestion", "discharge from nose", "nasal catarrh", "nasal discharge", "nasal discharge (finding)", "congested nose", "nasal congestion (finding)", "stuffed-up nose", "congestion of nasal sinus", "congestion of nasal sinus (disorder)", "sneezing", "sneeze", "itchy eyes", "watery eyes"],
			"productive cough":        ["productive cough", "coughing up phlegm", "coughing up mucus", "purulent sputum", "yellow sputum", "green sputum", "bronchial cough", "chesty cough", "loose cough", "moist cough", "producing sputum", "productive cough (finding)", "purulent sputum (finding)", "yellow sputum (finding)", "green sputum (finding)", "productive cough -clear sputum", "productive cough -green sputum", "productive cough -clear sputum (finding)", "productive cough -green sputum (finding)"],
			"sepsis signs":            ["hypotension", "altered mentation", "lactate elevated", "arterial hypotension", "hypopiesis", "low blood pressure", "low blood pressure (disorder)"],
			"meningeal signs":         ["kernig sign", "brudzinski", "jolt accentuation", "kernig's sign", "kernig's sign (finding)"],
		},

		# ── ENDOCRINE / METABOLIC ────────────────────────────────────
		"endocrine": {
			"polyuria":                ["polyuria", "urinating a lot", "excessive urination", "frequent urination excessive", "high urine output", "passes too much urine", "polyuria (finding)", "adipsic vasopressin-related polyuria", "familial vasopressin-related polyuria", "hereditary vasopressin-related polyuria", "idiopathic vasopressin-related polyuria", "micturition frequency and polyuria", "nocturnal polyuria", "partial vasopressin-related polyuria", "secondary vasopressin-related polyuria", "vasopressin-related polyuria", "adipsic arginine vasopressin-related polyuria", "adipsic arginine vasopressin-related polyuria (disorder)", "adipsic avp (arginine vasopressin)-related polyuria", "familial arginine vasopressin-related polyuria", "familial arginine vasopressin-related polyuria (disorder)", "familial avp (arginine vasopressin)-related polyuria", "familial diabetes insipidus", "hereditary arginine vasopressin-related polyuria", "hereditary arginine vasopressin-related polyuria (disorder)", "hereditary avp (arginine vasopressin)-related polyuria", "idiopathic arginine vasopressin-related polyuria", "idiopathic arginine vasopressin-related polyuria (disorder)", "idiopathic avp (arginine vasopressin)-related polyuria", "idiopathic diabetes insipidus", "micturition frequency and polyuria (finding)", "nocturnal polyuria (finding)", "partial arginine vasopressin-related polyuria", "partial arginine vasopressin-related polyuria (disorder)", "partial avp (arginine vasopressin)-related polyuria", "partial diabetes insipidus", "secondary arginine vasopressin-related polyuria", "secondary arginine vasopressin-related polyuria (disorder)", "secondary avp (arginine vasopressin)-related polyuria", "secondary diabetes insipidus", "arginine vasopressin-related polyuria", "arginine vasopressin-related polyuria (disorder)", "avp (arginine vasopressin)-related polyuria", "diabetes insipidus"],
			"polydipsia":              ["polydipsia", "excessive thirst", "very thirsty", "drinking a lot", "cant stop drinking water", "always thirsty", "desperate to drink", "excessive thirst (finding)", "keen for fluids", "organic primary polydipsia", "primary polydipsia", "psychogenic polydipsia", "organic primary polydipsia (disorder)", "dipsogenic diabetes insipidus", "primary polydipsia (disorder)", "psychogenic polydipsia (disorder)"],
			"polyphagia":              ["polyphagia", "excessive hunger", "always hungry", "increased appetite", "always hungry (finding)", "insatiable hunger", "excessive eating", "excessive eating (finding)", "gluttony", "hyperphagia", "increased appetite (finding)"],
			"weight loss":             ["weight loss", "unintentional weight loss", "losing weight", "unexplained weight loss", "weight decreased", "weight decreased (finding)", "involuntary weight loss", "unintentional weight loss (finding)", "unexplained weight loss (finding)", "measured weight loss", "measured weight loss (observable entity)", "behavior to promote weight loss", "difficulty maintaining weight loss", "excessive weight loss", "intentional weight loss", "measured gestational weight loss", "measured interdialytic weight loss", "percentage weight loss", "weight loss (amount)", "weight loss advised", "weight loss from baseline weight", "behavior to promote weight loss (observable entity)", "difficulty maintaining weight loss (finding)", "excessive weight loss (finding)", "intentional weight loss (finding)", "measured gestational weight loss (observable entity)", "measured interdialytic weight loss (observable entity)", "percentage weight loss (observable entity)", "weight loss (amount) (observable entity)", "weight loss advised (situation)", "weight loss from baseline weight (observable entity)"],
			"weight gain":             ["weight gain", "gaining weight", "unexplained weight gain", "measured weight gain", "measured weight gain (observable entity)", "weight increased", "weight increased (finding)", "behavior to promote weight gain", "childhood failure to gain weight", "excess interdialytic weight gain", "excessive weight gain", "excessive weight gain during pregnancy", "failure to gain weight", "high maternal weight gain", "insufficient weight gain of pregnancy", "low maternal weight gain", "measured gestational weight gain", "measured interdialytic weight gain", "pattern of weight gain", "percentage weight gain", "slow weight gain", "target weight gain per day", "unintentional weight gain", "weight gain (amount)", "weight gain advised", "weight gain diet", "behavior to promote weight gain (observable entity)", "childhood failure to gain weight (finding)", "excess interdialytic weight gain (finding)", "excessive weight gain (finding)", "excessive weight gain measured during pregnancy", "excessive weight gain measured during pregnancy (finding)", "failure to gain weight (finding)", "not gaining weight", "not putting on weight", "poor weight gain", "unable to gain weight", "high maternal weight gain (finding)", "insufficient weight gain of pregnancy (disorder)", "low weight gain in pregnancy", "low maternal weight gain (finding)", "measured gestational weight gain (observable entity)", "measured interdialytic weight gain (observable entity)", "pattern of weight gain (observable entity)", "percentage weight gain (observable entity)", "slow weight gain (finding)", "target weight gain per day (observable entity)", "involuntary weight gain", "unintentional weight gain (finding)", "weight gain (amount) (observable entity)", "weight gain advised (situation)", "weight gain diet (finding)"],
			"heat intolerance":        ["heat intolerance", "cant tolerate heat", "feeling hot", "overheating"],
			"cold intolerance":        ["cold intolerance", "always cold", "feeling cold all the time", "intolerance to cold"],
			"hypoglycemia signs":      ["hypoglycemia", "low blood sugar", "blood sugar low", "shakiness hunger sweat", "hypoglycemic", "sugar crash", "hypoglycemia (disorder)", "low glucose", "glucose low"],
			"hyperglycemia signs":     ["hyperglycemia", "high blood sugar", "blood sugar high", "elevated glucose", "diabetic ketoacidosis", "dka", "hyperglycemia (disorder)", "diabetes mellitus with ketoacidosis", "diabetic acidosis", "dka - diabetic ketoacidosis", "ketoacidosis due to diabetes mellitus", "ketoacidosis due to diabetes mellitus (disorder)", "ketoacidosis in diabetes mellitus"],
			"fruity breath":           ["fruity breath", "acetone breath", "keto breath", "sweet smelling breath", "acetone on breath", "breath smells ketotic", "ketotic breath", "ketotic breath (finding)"],
			"thyroid symptoms":        ["thyroid", "goiter", "neck lump", "thyroid swelling", "thyroid mass", "hyperthyroid", "hypothyroid", "enlargement of thyroid", "goiter (disorder)", "struma - goiter", "struma of thyroid", "swelling of thyroid gland", "thyroid enlargement", "thyroid goiter", "thyromegaly", "thyroid gland", "thyroid structure", "thyroid structure (body structure)", "mass of thyroid gland", "mass of thyroid gland (finding)", "thyroid lump", "hypothyroidism", "hypothyroidism (disorder)"],
			"adrenal symptoms":        ["adrenal crisis", "addisonian crisis", "low cortisol", "darkening skin hyperpigmentation", "acute adrenal failure", "acute adrenal insufficiency", "acute adrenal insufficiency (disorder)", "acute adrenocortical insufficiency", "adrenocortical crisis"],
		},

		# ── PSYCHIATRIC / BEHAVIORAL ─────────────────────────────────
		"psychiatric": {
			"agitation":               ["agitation", "aggressive", "combative", "violent", "restless", "extremely anxious", "uncooperative", "threatening", "agitated", "agitated behavior", "feeling agitated", "feeling agitated (finding)", "unable to keep still", "uncooperative behavior", "uncooperative behavior (finding)", "neonatal agitation", "psychomotor agitation", "restlessness and agitation", "stress reaction with psychomotor agitation", "verbal agitation", "neonatal agitation (disorder)", "neonatal hyperkinesia", "excessive overactivity", "increased purposeless goalless activity", "psychomotor agitation (finding)", "restlessness and agitation (finding)", "stress reaction with psychomotor agitation (disorder)", "verbal agitation (finding)"],
			"suicidal ideation":       ["suicidal ideation", "wants to die", "suicide attempt", "self harm", "overdose intentional", "thinking about suicide", "suicidal", "suicide attempt (event)", "suicidal (finding)", "suicidal thoughts", "suicidal thoughts (finding)"],
			"psychosis":               ["psychosis", "hallucinations", "hearing voices", "seeing things", "paranoia", "delusions", "psychotic", "bizarre behavior", "hallucinations (finding)", "paranoid disorder", "paranoid disorder (disorder)", "paranoid psychosis", "bizarre behavior (finding)", "psychotic disorder", "psychotic disorder (disorder)", "verbal auditory hallucinations", "verbal auditory hallucinations (finding)", "visual hallucinations", "visual hallucinations (finding)", "acute hysterical psychosis", "acute psychosis", "affective psychosis", "alzheimer's disease with psychosis", "atypical psychosis", "borderline psychosis of childhood", "brief reactive psychosis", "chronic paranoid psychosis", "cutaneous monosymptomatic delusional psychosis", "cycloid psychosis", "drug-induced psychosis", "epileptic psychosis", "factitious psychosis", "infantile psychosis", "korsakoff's psychosis", "mild postnatal psychosis", "non-alcoholic korsakoff's psychosis", "non-organic psychosis", "paranoid-hallucinatory epileptic psychosis", "past pregnancy history of postpartum psychosis", "postpartum psychosis", "postpartum psychosis in remission", "presbyophrenic psychosis", "psychogenic paranoid psychosis", "psychosis in early childhood", "psychosis with origin in childhood", "reactive depressive psychosis", "recurrent manic episodes, severe, with psychosis", "residual childhood psychosis", "senile dementia with psychosis", "severe postnatal psychosis", "single manic episode, severe, with psychosis", "symbiotic infantile psychosis", "acute hysterical psychosis (disorder)", "acute psychosis (disorder)", "affective psychosis (disorder)", "alzheimer disease with psychosis", "alzheimer's disease with psychosis (disorder)", "atypical psychosis (disorder)", "borderline psychosis of childhood (disorder)", "brief psychotic disorder", "brief reactive psychosis (disorder)", "chronic paranoid psychosis (disorder)", "cutaneous monosymptomatic delusional psychosis (disorder)", "cycloid psychosis (disorder)", "drug induced psychosis", "drug psychosis", "psychotic disorder caused by drug", "psychotic disorder caused by drug (disorder)", "epileptic psychosis (disorder)", "factitious psychosis (disorder)", "infantile psychosis (disorder)", "alcoholic amnestic syndrome", "amnesic syndrome due to alcohol", "amnestic syndrome of wernicke's disease", "korsakoff psychosis", "korsakoff's psychosis (disorder)", "korsakov alcoholic psychosis", "korsakov psychosis", "korsakov syndrome - alcoholic", "wernicke-korsakoff syndrome", "wernicke-korsakov syndrome", "mild postnatal psychosis (disorder)", "korsakoff's syndrome - non-alcoholic", "korsakov's syndrome - non-alcoholic", "non-alcoholic amnestic syndrome", "non-alcoholic korsakoff psychosis", "non-alcoholic korsakoff's psychosis (disorder)", "non-organic psychoses", "non-organic psychosis (disorder)", "paranoid-hallucinatory epileptic psychosis (disorder)", "history of postpartum psychosis", "past pregnancy history of postpartum psychosis (situation)", "postnatal psychosis", "postpartum psychosis (disorder)", "postpartum psychosis in remission (disorder)", "presbyophrenic psychosis (disorder)", "psychogenic paranoid psychosis (disorder)", "psychosis in early childhood (disorder)", "psychosis, early childhood", "childhood psychosis"],
			"anxiety":                 ["anxiety", "panic attack", "panic", "anxious", "extreme worry", "hyperventilating", "terror", "phobia", "intense fear", "fear of dying", "impending doom", "anxiety (finding)", "anxiety reaction", "anxiousness", "feeling anxious", "panic attack (finding)", "panic (finding)", "panic reaction", "panic state", "hv - hyperventilation", "hyperventilation", "hyperventilation (finding)", "overbreathing", "abnormal fear", "phobia (finding)", "fear of death", "fear of death (finding)", "adolescent social anxiety disorder", "amphetamine-induced anxiety disorder", "anticipatory anxiety", "anxiety and fear", "anxiety attack", "anxiety disorder", "anxiety disorder in mother complicating childbirth", "anxiety disorder in pregnancy", "anxiety disorder of adolescence", "anxiety disorder of childhood", "anxiety hyperventilation", "anxiety in pregnancy", "anxiety state", "caffeine-induced anxiety disorder", "cannabis-induced anxiety disorder", "castration anxiety", "childhood phobic anxiety disorder", "childhood social anxiety disorder", "chronic anxiety", "death anxiety", "fh: anxiety state", "free-floating anxiety", "generalized anxiety disorder", "hallucinogen-induced anxiety disorder", "illness anxiety disorder", "inhalant-induced anxiety disorder", "mild anxiety", "mixed anxiety and depressive disorder", "moderate anxiety", "organic anxiety disorder", "parental anxiety", "performance anxiety", "postpartum anxiety", "recurrent anxiety", "separation anxiety", "separation anxiety disorder of childhood", "severe anxiety (panic)", "amphetamine induced anxiety disorder", "anxiety disorder caused by amfetamine", "anxiety disorder caused by amfetamine (disorder)", "anxiety disorder caused by amphetamine", "anticipatory anxiety (finding)", "anxiety and fear (finding)", "anxiety attack (finding)", "anxiety disorder (disorder)", "anxiety disorder in mother complicating childbirth (disorder)", "anxiety in childbirth", "anxiety disorder in pregnancy (disorder)", "anxiety disorder of adolescence (disorder)", "anxiety disorder of childhood (disorder)", "anxiety hyperventilation (disorder)", "anxiety in pregnancy (finding)", "anxiety state (finding)", "caffeine induced anxiety disorder", "caffeine-induced anxiety disorder (disorder)", "cannabis induced anxiety disorder", "cannabis-induced anxiety disorder (disorder)", "childhood phobic anxiety disorder (disorder)", "avoidance disorder, childhood", "avoidant disorder of childhood", "avoidant disorder of childhood (disorder)", "childhood avoidant disorder", "withdrawing reaction of childhood", "chronic anxiety (finding)", "death anxiety (finding)", "family history of anxiety disorder", "family history: anxiety state", "family history: anxiety state (situation)", "free-floating anxiety (finding)", "gad - generalized anxiety disorder", "generalized anxiety disorder (disorder)", "hallucinogen induced anxiety disorder", "hallucinogen-induced anxiety disorder (disorder)"],
			"depression":              ["depression", "depressed", "hopeless", "low mood", "cant function", "anhedonia", "suicidal thoughts", "anhedonia (finding)", "suicidal ideation", "suicidal thoughts (finding)", "depression - motion", "depression - motion (qualifier value)", "depressive disorder", "depressive disorder (disorder)", "depressive illness", "mood disorder of depressed type", "acute depression", "agitated depression", "antenatal depression", "anterior st segment depression", "arteriosclerotic dementia with depression", "bipolar disorder, most recent episode depression", "bone marrow depression", "central nervous system depression", "chronic depression", "congenital depression in skull", "depression annual review", "depression follow-up declined", "depression in cranium along frontal suture", "depression interim review", "depression of left ventricular systolic function", "depression requiring intervention", "depression screening declined", "depression worse in morning", "depression worse later in day", "diffuse st segment depression", "drug-induced central nervous system depression", "endogenous depression", "endogenous depression - recurrent", "endogenous depression first episode", "fh: depression", "fh: puerperal depression", "inferior st segment depression", "involutional depression", "knowledge level about depression management", "major depression in full remission", "major depression in partial remission", "major depression in remission", "major depression with psychotic features", "masked depression", "menopausal depression", "mild depression", "mild major depression", "mild postnatal depression", "mild recurrent major depression", "minimal depression", "minimal major depression", "minimal major depression single episode", "minimal recurrent major depression", "moderate depression", "moderate major depression", "moderate recurrent major depression", "moderately severe depression", "moderately severe major depression", "moderately severe major depression single episode", "moderately severe recurrent major depression", "multi-infarct dementia with depression", "neonatal effect of maternal postpartum depression", "neonatal respiratory depression", "on depression register", "perinatal depression", "post-schizophrenic depression", "posterior st segment depression", "postmenopausal depression", "postnatal depression not discussed", "postpartum depression", "postpartum major depression in remission", "postviral depression", "pr depression", "presenile dementia with depression", "pseudo-cushing's syndrome of depression", "reactive depression (situational)", "recurrent depression", "recurrent major depression", "recurrent major depression in full remission", "recurrent major depression in partial remission", "recurrent major depression in remission", "removed from depression register", "senile dementia with depression", "severe depression", "severe major depression", "severe major depression with psychotic features", "severe major depression without psychotic features", "severe postnatal depression", "severe recurrent major depression", "single stimulus depression - finding", "st depression", "st segment depression", "stuporous depression", "symptoms of depression"],
			"mania":                   ["mania", "manic", "grandiosity", "no sleep needed", "racing thoughts", "hypomanic", "inflated self-esteem", "inflated self-opinion", "inflated self-opinion (finding)", "racing thoughts (finding)", "mania (disorder)", "manic psychosis"],
			"substance use":           ["intoxication", "drug use", "alcohol intoxication", "withdrawal", "detox", "substance abuse", "overdose", "poisoning", "high", "drunk", "intoxication (disorder)", "alcohol intoxication (disorder)", "drunkenness", "od - overdose", "overdose (disorder)", "poisoning (disorder)", "poisoning by", "toxic effect", "toxic effect of", "toxicity", "toxicosis", "elevated", "high (qualifier value)", "harmful pattern of substance use", "harmful pattern of substance use (disorder)", "chronic harmful pattern of substance use", "continuous harmful pattern of substance use", "episode of harmful substance use", "episodic harmful pattern of substance use", "finding related to substance use", "knowledge level: substance use control", "nondependent harmful pattern of substance use", "psychoactive substance use disorder", "substance use disorder", "substance use disorder suspected", "chronic harmful pattern of substance use (disorder)", "continuous harmful pattern of substance use (disorder)", "episode of harmful substance use (disorder)", "episodic harmful pattern of substance use (disorder)", "finding related to substance use (finding)", "knowledge level: substance use control (observable entity)", "knowledge: substance use control", "nondependent harmful pattern of substance use (disorder)", "psychoactive substance use disorder (disorder)", "substance use disorder (disorder)", "substance use disorder suspected (situation)"],
			"delirium":                ["delirium", "acute confusion", "waxing and waning", "sundowning", "acute ams", "abs - acute brain syndrome", "acute brain syndrome", "acute confusional state", "acute organic reaction", "acute psycho-organic syndrome", "delirium (disorder)", "obs - organic brain syndrome", "organic brain syndrome", "acute confusion (finding)", "sundown syndrome", "sundowning (finding)", "alcohol intoxication delirium", "alcohol withdrawal delirium", "alzheimer's disease with delirium", "amphetamine intoxication delirium", "arteriosclerotic dementia with delirium", "cannabis intoxication delirium", "cocaine intoxication delirium", "delirium co-occurrent with dementia", "delirium in remission", "delirium of mixed origin", "exhaustion delirium", "family education about delirium", "hallucinogen intoxication delirium", "inhalant intoxication delirium", "multi-infarct dementia with delirium", "opioid intoxication delirium", "pcp (phencyclidine) intoxication delirium", "post-injection delirium sedation syndrome", "postseizure delirium", "presenile dementia with delirium", "senile dementia with delirium", "subacute delirium", "alcohol intoxication delirium (disorder)", "alcohol withdrawal delirium (disorder)", "delirium tremens", "dts - delirium tremens", "alzheimer's disease with delirium (disorder)", "amphetamine intoxication delirium (disorder)", "arteriosclerotic dementia with delirium (disorder)", "cannabis intoxication delirium (disorder)", "cocaine intoxication delirium (disorder)", "delirium co-occurrent with dementia (disorder)", "delirium superimposed on dementia", "delirium in remission (disorder)", "delirium of mixed origin (disorder)", "exhaustion delirium (finding)", "family education about delirium (situation)", "hallucinogen intoxication delirium (disorder)", "inhalant delirium", "inhalant induced delirium", "inhalant intoxication delirium (disorder)", "multi infarct dementia with delirium", "multi-infarct dementia with delirium (disorder)", "vascular dementia, with delirium", "opioid intoxication delirium (disorder)", "phencyclidine delirium", "phencyclidine intoxication delirium", "phencyclidine intoxication delirium (disorder)", "pdss - post-injection delirium sedation syndrome", "post-injection delirium sedation syndrome (finding)", "postepileptic delirium", "postictal delirium", "postseizure delirium (disorder)", "presenile dementia with delirium (disorder)", "senile delirium", "senile dementia with delirium (disorder)", "subacute confusional state", "subacute delirium (disorder)"],
		},

		# ── TOXICOLOGY / OVERDOSE ────────────────────────────────────
		"toxicology": {
			"overdose":                ["overdose", "od", "drug overdose", "medication overdose", "pill overdose", "intentional ingestion", "accidental ingestion", "od - overdose", "overdose (disorder)", "accidental ingestion of potentially harmful entity", "accidental ingestion of potentially harmful entity (event)", "accidental 5-aminosalicylic acid overdose", "accidental 5-ht3-receptor antagonist overdose", "accidental acemetacin overdose", "accidental acetaminophen overdose", "accidental acetazolamide overdose", "accidental acetohexamide overdose", "accidental acetylcholine overdose", "accidental acetylcysteine overdose", "accidental acitretin overdose", "accidental aclarubicin overdose", "accidental alfentanil overdose", "accidental allopurinol overdose", "accidental alprazolam overdose", "accidental aluminum hydroxide overdose", "accidental amantadine overdose", "accidental aminoglutethimide overdose", "accidental aminophylline overdose", "accidental amiodarone overdose", "accidental amitriptyline overdose", "accidental amoxapine overdose", "accidental amphotericin b overdose", "accidental ampicillin overdose", "accidental amsacrine overdose", "accidental amylobarbitone overdose", "accidental anthraquinone laxative overdose", "accidental anticholinesterase overdose", "accidental antihypertensive overdose", "accidental antileprotic drug overdose", "accidental antimony compound overdose", "accidental antispasmodic overdose", "accidental aspirin overdose", "accidental atenolol overdose", "accidental atropine overdose", "accidental azapropazone overdose", "accidental azathioprine overdose", "accidental azithromycin overdose", "accidental baclofen overdose", "accidental beclamide overdose", "accidental bendroflumethiazide overdose", "accidental benperidol overdose", "accidental benzocaine overdose", "accidental bisacodyl overdose", "accidental bismuth compound overdose", "accidental bleomycin overdose", "accidental bretylium overdose", "accidental bromazepam overdose", "accidental bromocriptine overdose", "accidental bronchodilator preparations overdose", "accidental bulk-forming laxative overdose", "accidental bumetanide overdose", "accidental bupivacaine overdose", "accidental buprenorphine overdose", "accidental buspirone overdose", "accidental busulfan overdose", "accidental butabarbitone overdose", "accidental butriptyline overdose", "accidental caffeine overdose", "accidental cannabis overdose", "accidental carbenicillin overdose", "accidental carbenoxolone overdose", "accidental carbimazole overdose", "accidental carboplatin overdose", "accidental carmustine overdose", "accidental cascara overdose", "accidental castor oil overdose", "accidental cefaclor overdose", "accidental cefadroxil overdose", "accidental cefixime overdose", "accidental cefodizime overdose", "accidental cefotaxime overdose", "accidental cefpirome overdose", "accidental cefpodoxime overdose", "accidental cefsulodin overdose", "accidental ceftazidime overdose", "accidental ceftibuten overdose", "accidental ceftizoxime overdose", "accidental ceftriaxone overdose", "accidental cefuroxime overdose", "accidental central appetite depressant overdose", "accidental cephalexin overdose", "accidental cephalothin overdose", "accidental cephamandole overdose", "accidental cephazolin overdose", "accidental cephradine overdose", "accidental chloral hydrate overdose", "accidental chlorambucil overdose", "accidental chloramphenicol overdose", "accidental chlordiazepoxide overdose", "accidental chlormethiazole overdose"],
			"opioid signs":            ["opioid overdose", "pinpoint pupils", "heroin overdose", "narcotic overdose", "morphine overdose", "fentanyl overdose", "respiratory depression opioid", "diamorphine overdose", "heroin overdose (disorder)", "overdose of heroin", "morphine overdose (disorder)", "fentanyl overdose (disorder)", "overdose of opiate", "overdose of opiate (disorder)"],
			"stimulant signs":         ["stimulant overdose", "cocaine", "meth", "amphetamine", "crystal meth", "crack", "stimulant toxicity", "sympathomimetic", "benzoylmethylecgonine", "cocaine (substance)", "1-phenylpropan-2-amine", "amfetamine", "amfetamine (substance)", "dl-alpha-methylphenethylamine", "psychostimulant overdose", "psychostimulant overdose (disorder)"],
			"acetaminophen toxicity":  ["tylenol overdose", "acetaminophen overdose", "paracetamol overdose", "apap overdose", "acetaminophen overdose (disorder)"],
			"alcohol toxicity":        ["alcohol poisoning", "ethanol toxicity", "drunk", "alcohol overdose", "binge drinking collapse", "ethanol causing toxic effect", "ethanol poisoning", "ethyl alcohol poisoning", "toxic effect of ethanol", "toxic effect of ethyl alcohol", "toxic effect of ethyl alcohol (disorder)", "toxic effect of grain alcohol", "alcohol intoxication", "alcohol intoxication (disorder)", "drunkenness"],
			"organophosphate signs":   ["organophosphate", "pesticide poisoning", "insecticide exposure", "salivation lacrimation", "sludge", "pesticide poisoning (disorder)", "pesticide product poisoning", "pesticide toxicity", "sludge (morphologic abnormality)", "organic phosphate", "organic phosphorus compound", "organic phosphorus compound (substance)", "organophosphorus compound"],
			"carbon monoxide":         ["carbon monoxide", "co poisoning", "co exposure", "gas poisoning", "smoke inhalation", "headache nausea after fire", "carbon monoxide (substance)", "co - carbon monoxide", "accidental poisoning by carbon monoxide", "carbon monoxide detector present", "carbon monoxide encephalopathy", "carbon monoxide in residence", "carbon monoxide poisoning from fire", "carbon monoxide reading at 4 weeks", "carbon monoxide transfer factor", "chronic carbon monoxide poisoning", "expired carbon monoxide concentration", "functioning carbon monoxide detector in residence", "presence of carbon monoxide detector", "self poisoning by carbon monoxide", "single breath carbon monoxide diffusing capacity", "toxic effect of carbon monoxide", "accidental poisoning caused by carbon monoxide", "accidental poisoning caused by carbon monoxide (disorder)", "carbon monoxide detector present (finding)", "disorder of brain caused by carbon monoxide", "disorder of brain caused by carbon monoxide (disorder)", "encephalopathy caused by carbon monoxide", "carbon monoxide in living accommodation", "carbon monoxide in residence (finding)", "carbon monoxide poisoning from fire (disorder)", "carbon monoxide reading at 4 weeks (observable entity)", "carbon monoxide transfer factor (observable entity)", "tlco - carbon monoxide transfer factor", "chronic carbon monoxide poisoning (disorder)", "expired carbon monoxide concentration (observable entity)", "functioning carbon monoxide detector in living accommodation", "functioning carbon monoxide detector in residence (finding)", "presence of carbon monoxide detector (observable entity)", "self poisoning caused by carbon monoxide", "self poisoning caused by carbon monoxide (disorder)", "dlco (diffusing capacity of lung for carbon monoxide) by single breath technique", "single breath carbon monoxide diffusing capacity (observable entity)", "tlco (transfer factor for carbon monoxide) single breath technique", "carbon monoxide poisoning", "toxic effect of carbon monoxide (disorder)"],
			"caustic ingestion":       ["caustic ingestion", "bleach ingestion", "acid ingestion", "corrosive swallowed", "lye ingestion"],
			"envenomation":            ["snake bite", "spider bite", "bee sting anaphylaxis", "scorpion sting", "jellyfish sting", "envenomation", "snake bite (event)", "jellyfish sting (event)", "stung by jelly fish", "stung by jellyfish nematocyst"],
		},

		# ── VASCULAR ─────────────────────────────────────────────────
		"vascular": {
			"leg pain with walking":   ["leg pain with walking", "claudication", "calf pain walking", "intermittent claudication", "peripheral artery disease", "ic - intermittent claudication", "intermittent claudication (finding)", "myasthenia angiosclerotica", "peripheral arterial disease", "peripheral arterial disease (disorder)", "peripheral arterial vascular disease"],
			"sudden limb pallor":      ["sudden pale limb", "cold limb", "pulseless limb", "limb ischemia", "white leg", "white arm", "blue limb", "limb ischemia (disorder)", "cold extremity", "cold extremity (finding)", "milk leg syndrome", "phlegmasia alba dolens", "phlegmasia alba dolens (disorder)"],
			"aortic pain":             ["aortic pain", "tearing chest pain", "ripping pain", "pain radiating to back", "worst back pain ever", "interscapular pain"],
			"deep vein thrombosis":    ["dvt", "deep vein thrombosis", "leg clot", "calf pain", "leg pain", "calf swelling unilateral", "leg pain swelling", "unilateral leg swelling", "deep venous thrombosis", "deep venous thrombosis (disorder)", "dvt - deep vein thrombosis", "acute deep vein thrombosis during pregnancy", "antepartum deep vein thrombosis", "chronic deep vein thrombosis during pregnancy", "deep vein thrombosis suspected", "deep venous thrombosis of femoropopliteal vein", "deep venous thrombosis of pelvic vein", "deep venous thrombosis of peroneal vein", "deep venous thrombosis of tibial vein", "iliofemoral deep vein thrombosis", "postpartum acute deep vein thrombosis", "postpartum chronic deep vein thrombosis", "recurrent deep vein thrombosis", "acute deep vein thrombosis during pregnancy (disorder)", "acute deep vein thrombus during pregnancy", "antenatal deep vein thrombosis", "antenatal dvt (deep vein thrombosis)", "antepartum deep phlebothrombosis", "antepartum deep phlebothrombosis (disorder)", "chronic deep vein thrombosis during pregnancy (disorder)", "chronic deep vein thrombus during pregnancy", "deep vein thrombosis suspected (situation)", "deep venous thrombosis of femoropopliteal vein (disorder)", "deep venous thrombosis of pelvic vein (disorder)", "deep venous thrombosis of peroneal vein (disorder)", "deep venous thrombosis of tibial vein (disorder)", "ifvt - iliofemoral vein thrombosis", "ileofemoral deep vein thrombosis", "iliofemoral deep vein thrombosis (disorder)", "acute deep vein thrombus during postpartum period", "acute deep vein thrombus during postpartum period (disorder)", "chronic deep vein thrombosis during postpartum period", "chronic deep vein thrombosis during postpartum period (disorder)", "chronic deep vein thrombus during postpartum period", "recurrent deep vein thrombosis (disorder)"],
			"pulmonary embolism signs": ["pe", "pulmonary embolism", "sudden chest pain sob", "pleuritic pain dyspnea", "dvt with sob", "pe - pulmonary embolism", "pulmonary embolism (disorder)"],
			"hypertensive urgency":    ["hypertensive urgency", "high blood pressure", "very high bp", "bp elevated", "hypertension severe", "blood pressure very high", "hypertensive urgency (disorder)", "bp - high blood pressure", "bp+ - hypertension", "hbp - high blood pressure", "high blood pressure disorder", "ht - hypertension", "htn - hypertension", "hypertension", "hypertensive disorder", "hypertensive disorder, systemic arterial", "hypertensive disorder, systemic arterial (disorder)", "hypertensive vascular degeneration", "hypertensive vascular disease", "systemic arterial hypertension"],
		},

		# ── OBSTETRIC / GYNECOLOGIC ──────────────────────────────────
		"obgyn": {
			"pregnancy signs":         ["pregnant", "pregnancy", "positive pregnancy test", "gravid", "gestational", "obstetric", "pregnancy, function", "pregnancy, function (observable entity)", "gestation", "pregnancy (finding)", "pregnancy confirmed", "pregnancy not delivered"],
			"ectopic pain":            ["ectopic", "ectopic pregnancy", "one sided pelvic pain", "shoulder tip pain pregnant", "fallopian tube pain", "ectopic (qualifier value)", "ectopic pregnancy (disorder)", "ep - ectopic pregnancy"],
			"labor signs":             ["contractions", "labor", "giving birth", "water broke", "amniotic fluid", "preterm labor", "regular contractions", "labor, function", "labor, function (observable entity)", "af - amniotic fluid", "amniotic fluid (substance)", "liquor", "premature labor", "premature labor (finding)", "premature onset of labor"],
			"preeclampsia signs":      ["preeclampsia", "hypertension pregnancy", "headache in pregnancy", "visual changes pregnancy", "swelling pregnancy", "eph - edema, proteinuria and hypertension of pregnancy", "pe - pre-eclampsia", "pet - pre-eclamptic toxemia", "pre-eclampsia", "pre-eclampsia (disorder)", "pre-eclamptic toxemia", "proteinuric hypertension of pregnancy", "toxemia of pregnancy"],
			"placental abruption":     ["placental abruption", "vaginal bleeding pain pregnant", "abdominal pain pregnant bleeding", "ablatio placentae", "abruptio placentae", "placental abruption (disorder)", "premature detachment of normally implanted placenta", "premature detachment of placenta", "premature separation of placenta", "concealed placental abruption", "mixed placental abruption", "past pregnancy history of placental abruption", "revealed placental abruption", "concealed accidental hemorrhage", "concealed placental abruption (disorder)", "mixed accidental hemorrhage", "mixed placental abruption (disorder)", "history of placental abruption", "past pregnancy history of placental abruption (situation)", "revealed accidental hemorrhage", "revealed placental abruption (disorder)"],
			"miscarriage signs":       ["miscarriage", "vaginal bleeding pregnancy", "threatened abortion", "spontaneous abortion", "miscarriage (disorder)", "vaginal expulsion of fetus", "vaginal expulsion of foetus", "vaginal expulsion of product of conception", "threatened abortion (antepartum)", "threatened abortion (disorder)", "threatened miscarriage"],
			"ovarian cyst":            ["ovarian cyst", "ovarian torsion", "sudden pelvic pain female", "adnexal mass pain", "cyst of ovary", "cyst of ovary (disorder)", "ovarian cystic mass", "torsion of ovary", "torsion of ovary (disorder)", "bilateral complex ovarian cyst", "bilateral ovarian cyst during pregnancy", "complex ovarian cyst", "complex cyst of bilateral ovaries", "complex cyst of bilateral ovaries (disorder)", "complex cyst of both ovaries", "cyst of bilateral ovaries during pregnancy", "cyst of bilateral ovaries during pregnancy (disorder)", "cyst of both ovaries during pregnancy", "complex cyst of ovary", "complex ovarian cyst (disorder)"],
		},

		# ── OPHTHALMOLOGIC / ENT ─────────────────────────────────────
		"ent_eye": {
			"eye pain":                ["eye pain", "ocular pain", "painful eye", "eye ache", "sore eye", "pain in eye", "pain in eye (finding)", "sore eye (finding)", "pain around eye", "pain on eye movement", "periorbital pain of left eye", "periorbital pain of right eye", "pain around eye (finding)", "periorbital pain", "pain on movement of eye", "pain on movement of eye (finding)", "pain provoked by movement of eye", "left periorbital eye pain", "periorbital pain of left eye (finding)", "periorbital pain of right eye (finding)", "right periorbital eye pain"],
			"vision change":           ["vision change", "visual change", "sudden vision loss", "vision gone", "blurred vision", "blind spot", "flashing lights", "floaters", "blurring of visual image", "blurring of visual image (finding)", "blurry vision", "visual field scotoma", "visual field scotoma (finding)"],
			"red eye":                 ["red eye", "conjunctivitis", "pink eye", "eye redness", "bloodshot eye", "red eye (finding)", "conjunctivitis (disorder)", "inflammation of conjunctiva", "pink eye disease", "hyperemia of eye", "hyperemia of eye (finding)", "ocular hyperemia", "contact lens related red eye", "has a red eye", "contact lens related red eye (disorder)", "has a red eye (situation)"],
			"eye trauma":              ["eye trauma", "eye injury", "chemical in eye", "foreign body eye", "hit eye"],
			"epistaxis":               ["epistaxis", "nosebleed", "bleeding from nose", "bloody nose", "bleeding from nose (finding)", "finding of bleeding of nose", "nasal hemorrhage", "observation of bleeding of nose", "anterior epistaxis", "evidence of recent epistaxis", "fetal epistaxis", "maternal perinatal epistaxis", "neonatal epistaxis", "post-surgical epistaxis", "posterior epistaxis", "traumatic epistaxis", "anterior epistaxis (disorder)", "epistaxis from anterior nasal septum", "epistaxis from kiesselbach's plexus", "epistaxis from little's area", "evidence of recent epistaxis (finding)", "fetal epistaxis (disorder)", "maternal perinatal epistaxis (disorder)", "neonatal epistaxis (disorder)", "post-surgical epistaxis (disorder)", "posterior epistaxis (disorder)", "traumatic epistaxis (disorder)"],
			"dental pain":             ["dental pain", "toothache", "tooth pain", "dental abscess", "jaw abscess", "dental infection", "dentagra", "dentalgia", "odontalgia", "pain in tooth", "toothache (finding)", "dental abscess (disorder)", "dental sepsis", "tooth abscess", "infection of tooth", "infection of tooth (disorder)", "chronic dental pain", "chronic pain due to dental disorder", "chronic pain due to dental disorder (finding)"],
			"facial pain":             ["facial pain", "sinusitis", "sinus pain", "facial swelling", "periorbital swelling", "orbital cellulitis", "face ache", "face pain", "pain in face", "pain in face (finding)", "pain of face", "sinusitis (disorder)", "orbital cellulitis (disorder)", "postseptal orbital cellulitis", "facial swelling (finding)", "swollen face", "atypical facial pain", "chronic secondary facial pain", "persistent idiopathic facial pain", "atypical facial pain (finding)", "chronic secondary facial pain (finding)", "persistent idiopathic facial pain (disorder)"],
			"hoarseness":              ["hoarseness", "hoarse voice", "voice change", "voice loss", "laryngitis", "voice hoarse", "croaky voice", "hoarse", "hoarse (finding)", "husky voice", "voice hoarseness", "laryngitis (disorder)", "chronic hoarseness", "vagal hoarseness", "chronic hoarseness (finding)", "neurologic hoarseness", "vagal hoarseness (disorder)"],
			"throat swelling":         ["throat swelling", "uvula swelling", "peritonsillar abscess", "pta", "neck swelling", "ludwig angina", "airway swelling", "peritonsillar abscess (disorder)", "quinsy", "neck swelling (finding)", "antihemophilic factor c", "coagulation factor xi", "coagulation factor xi (substance)", "factor xi", "plasma thromboplastin antecedent", "ludwig's angina", "ludwig's angina (disorder)"],
		},

		# ── HEMATOLOGICAL ────────────────────────────────────────────
		"hematology": {
			"bleeding":                ["bleeding", "hemorrhage", "uncontrolled bleeding", "abnormal bleeding", "spontaneous bleeding", "oozing", "bleeding (finding)", "blood loss", "extravasation of blood", "hemorrhage (morphologic abnormality)", "anastomotic bleeding", "anticoagulant excess without bleeding", "anticoagulant-induced bleeding", "at high risk for bleeding", "bleeding cervix", "bleeding disorder of unknown cause", "bleeding during surgery requiring transfusion", "bleeding esophageal varices", "bleeding external hemorrhoids", "bleeding from anus", "bleeding from breast", "bleeding from ear", "bleeding from fauces", "bleeding from hymen", "bleeding from larynx", "bleeding from male urethra", "bleeding from nipple", "bleeding from nose", "bleeding from tonsillar bed", "bleeding from urethra", "bleeding gastric varices", "bleeding gums", "bleeding hemorrhoids", "bleeding internal hemorrhoid grade i", "bleeding internal hemorrhoid grade ii", "bleeding internal hemorrhoid grade iii", "bleeding internal hemorrhoid grade iv", "bleeding internal hemorrhoids", "bleeding meckel's diverticulitis", "bleeding meckel's diverticulum", "bleeding of ear canal", "bleeding of mouth", "bleeding of oral mucosa", "bleeding of soft tissue", "bleeding of surface of nipple", "bleeding of unknown origin", "bleeding on probing of gingivae", "bleeding pinna", "bleeding requiring transfusion", "bleeding skin", "bleeding stress ulcer of stomach", "bleeding tooth socket", "bleeding ulcer of esophagus", "bleeding ulcer of large intestine", "bleeding varices of prostate", "break-through bleeding", "contact bleeding from cervix", "east texas bleeding disorder", "esophageal bleeding", "esophageal varices without bleeding", "fibrinolytic bleeding syndrome", "first trimester bleeding", "fresh bleeding from vagina", "gastric varices without bleeding", "gingival bleeding index", "heavy episode of vaginal bleeding", "intermenstrual bleeding - regular", "intermenstrual heavy bleeding", "iris bleeding", "irregular intermenstrual bleeding", "menstrual bleeding character", "menstrual bleeding present", "mid-cycle bleeding", "miscarriage with heavy bleeding", "missed withdrawal bleeding", "moderate vaginal bleeding", "nipple bleeding", "non-menstrual vaginal bleeding", "number of bleeding points", "oligoovulatory dysfunctional uterine bleeding", "ovulation bleeding", "painful rectal bleeding", "painless rectal bleeding", "perinatal transient vaginal bleeding", "placental separation with bleeding", "postcoital bleeding", "postmenopausal bleeding", "postmenopausal postcoital bleeding", "prepubertal bleeding from vagina", "profuse vaginal bleeding", "recurrent bleeding of nose", "recurrent gastrointestinal bleeding", "scanty vaginal bleeding", "second trimester bleeding", "stomal bleeding", "third trimester bleeding", "thrombomodulin-related bleeding disorder", "upper gastrointestinal bleeding", "vaginal bleeding", "vaginal bleeding complicating early pregnancy"],
			"bruising":                ["bruising", "bruise", "easy bruising", "ecchymosis", "unexplained bruising", "ecchymoses", "ecchymosis (finding)", "ecchymosis (morphologic abnormality)", "bruise - lesion", "contusion", "contusion (disorder)", "contusion - lesion", "contusion - lesion (morphologic abnormality)", "easy bruising (finding)", "increased tendency to bruise", "bruising over mastoid", "confluent bruising", "finding related to bruising", "impact bruising", "injection site bruising", "multiple bruising", "neonatal bruising of scalp", "painful bruising syndrome", "pattern bruising", "post-traumatic bruising", "spontaneous bruising", "superficial bruising of head and neck", "bruising over mastoid (disorder)", "confluent bruising (disorder)", "finding related to bruising (finding)", "observation of bruising", "impact bruising (disorder)", "injection site bruising (disorder)", "multiple bruising (finding)", "neonatal bruising of scalp (disorder)", "auto-erythrocyte sensitization syndrome", "autoerythrocyte sensitivity disorder", "factitious purpura", "gardner-diamond syndrome", "gardner-diamond syndrome (disorder)", "psychogenic purpura", "pattern bruising (disorder)", "post-traumatic bruising (disorder)", "spontaneous bruising (disorder)", "superficial bruising of head and neck (disorder)"],
			"pallor anemia":           ["anemia", "low hemoglobin", "tired pale", "fatigue pallor", "absolute anemia", "anemia (disorder)"],
			"sickle cell pain":        ["sickle cell", "sickle crisis", "vaso-occlusive crisis", "sickle cell crisis", "sickling pain", "drepanocyte", "drepanocyte (cell)", "meniscocyte", "sickling", "hemoglobin ss disease with crisis", "hemoglobin ss disease with crisis (disorder)", "sickle cell anemia with crisis"],
			"thrombosis":              ["thrombosis", "blood clot", "clot", "thrombus", "thrombosis (disorder)", "thrombosis (qualifier value)", "blood clot (morphologic abnormality)", "blood coagulum", "thrombus (morphologic abnormality)", "acute deep vein thrombosis during pregnancy", "acute deep venous thrombosis", "acute deep venous thrombosis of calf", "acute deep venous thrombosis of thigh", "acute thrombosis of inferior vena cava", "acute thrombosis of mesenteric vein", "acute thrombosis of splenic vein", "acute thrombosis of subclavian vein", "acute thrombosis of superior vena cava", "antepartum deep vein thrombosis", "anterior choroidal artery thrombosis", "anterior spinal artery thrombosis", "aortic bifurcation thrombosis", "arterial embolus and thrombosis", "arterial graft thrombosis", "arterial thrombosis", "arterial thrombosis of flap", "arterial thrombosis of spinal cord", "arteriovenous fistula thrombosis", "arteriovenous graft thrombosis", "arteriovenous shunt thrombosis", "atrial thrombosis", "axillary vein thrombosis", "basilar artery thrombosis", "bilateral thrombosis of carotid arteries", "bilateral thrombosis of cerebellar arteries", "bilateral thrombosis of common femoral arteries", "bilateral thrombosis of femoral arteries", "bilateral thrombosis of ulnar arteries", "bilateral thrombosis of vertebral arteries", "brachial artery thrombosis", "brachiocephalic vein thrombosis", "capillary thrombosis", "carotid artery thrombosis", "celiac artery thrombosis", "cerebellar artery thrombosis", "cerebral venous sinus thrombosis", "cerebral venous sinus thrombosis in pregnancy", "cerebral venous sinus thrombosis in puerperium", "cerebral venous thrombosis in pregnancy", "cerebral venous thrombosis in puerperium", "cerebral venous thrombosis of cortical vein", "cerebral venous thrombosis of sigmoid sinus", "cerebral venous thrombosis of straight sinus", "chronic deep vein thrombosis during pregnancy", "chronic deep venous thrombosis", "chronic deep venous thrombosis of calf", "chronic deep venous thrombosis of thigh", "chronic thrombosis of inferior vena cava", "chronic thrombosis of mesenteric vein", "chronic thrombosis of splenic vein", "chronic thrombosis of subclavian vein", "chronic thrombosis of superior vena cava", "chronic venous thrombosis", "common femoral artery thrombosis", "common iliac artery thrombosis", "congenital arteriovenous fistula thrombosis", "coronary artery stent thrombosis", "coronary artery thrombosis", "crural artery thrombosis", "deep vein thrombosis suspected", "deep venous thrombosis", "deep venous thrombosis in puerperium", "deep venous thrombosis of calf", "deep venous thrombosis of femoropopliteal vein", "deep venous thrombosis of lower extremity", "deep venous thrombosis of pelvic vein", "deep venous thrombosis of peroneal vein", "deep venous thrombosis of tibial vein", "deep venous thrombosis of upper extremity", "dermatosis resulting from intravascular thrombosis", "digital arterial thrombosis", "embolism and thrombosis of hepatic artery", "external iliac artery thrombosis", "femoral artery thrombosis", "fh: coronary thrombosis", "fh: thrombosis", "head and neck arterial thrombosis", "heparin-induced thrombocytopenia with thrombosis", "hepatic artery thrombosis", "hepatic vein thrombosis", "iliofemoral deep vein thrombosis", "inferior mesenteric vein thrombosis", "injection site thrombosis", "internal iliac artery thrombosis", "intervillous thrombosis", "intracardiac thrombosis in low output state", "left cerebellar artery thrombosis", "left main coronary artery thrombosis", "left posterior cerebral artery thrombosis", "lvad (left ventricular assist device) thrombosis"],
			"splenomegaly":            ["splenomegaly", "enlarged spleen", "spleen pain", "left upper quadrant pain", "enlargement of spleen", "large spleen", "splenomegaly (disorder)", "left upper quadrant pain (finding)", "chronic congestive splenomegaly", "congenital splenomegaly", "congenital syphilitic splenomegaly", "congestive splenomegaly", "hyperreactive malarial splenomegaly syndrome", "optic nerve edema, splenomegaly syndrome", "schistosomal splenomegaly", "chronic congestive splenomegaly (disorder)", "congenital splenomegaly (disorder)", "congenital syphilitic splenomegaly (disorder)", "banti syndrome", "banti's spleen", "congestive splenomegaly (disorder)", "fibrocongestive splenomegaly", "hms - hyperreactive malarial splenomegaly", "hmss - hyperreactive malarial splenomegaly syndrome", "hyperimmune malarious splenomegaly", "hyperreactive malarial splenomegaly", "hyperreactive malarial splenomegaly syndrome (disorder)", "tropical splenomegaly syndrome", "optic nerve edema, splenomegaly syndrome (disorder)", "schistosomal splenomegaly (disorder)"],
		},

		# ── PEDIATRIC SPECIFIC ───────────────────────────────────────
		"pediatric": {
			"high pitched cry":        ["high pitched cry", "inconsolable crying", "irritable infant", "fussy baby", "wont stop crying", "high pitched cry (finding)", "fussy infant", "unsettled infant", "unsettled infant (finding)"],
			"bulging fontanelle":      ["bulging fontanelle", "bulging soft spot", "tense fontanelle", "bulging fontanelle (finding)"],
			"barking cough":           ["croup", "barking cough", "seal like cough", "stridor child", "croup cough", "croup (disorder)", "croup syndrome", "barking cough (finding)"],
			"rash child":              ["meningococcal rash", "rash with fever child", "non-blanching rash child", "petechiae fever", "meningococcal rash (disorder)"],
			"febrile seizure":         ["febrile seizure", "seizure with fever", "convulsion with fever", "child seizing fever", "febrile convulsion", "febrile convulsion (finding)", "febrile fit", "febrile seizure (from fever)", "fever seizure", "pyrexial convulsion", "complex febrile seizure", "simple febrile seizure", "complex febrile convulsion", "complex febrile seizure (finding)", "simple febrile convulsion", "simple febrile seizure (finding)"],
			"intussusception signs":   ["intussusception", "colicky abdominal pain child", "currant jelly stool", "episodic abdominal pain infant", "invagination", "invagination (morphologic abnormality)"],
			"pyloric stenosis":        ["projectile vomiting infant", "pyloric stenosis", "nonbilious vomiting newborn", "ps - pyloric stenosis", "pyloric stenosis (disorder)", "acquired hypertrophic pyloric stenosis", "adult hypertrophic pyloric stenosis", "congenital hypertrophic pyloric stenosis", "congenital pyloric stenosis", "pyloric antral stenosis", "acquired gastric outlet stenosis", "acquired hypertrophic pyloric stenosis (disorder)", "adult hypertrophic pyloric stenosis (disorder)", "congenital hypertrophic pyloric stenosis (disorder)", "congenital pyloric stenosis (disorder)", "pyloric antral stenosis (disorder)"],
			"foreign body":            ["foreign body", "swallowed object", "choked", "choking", "coin swallowed", "button battery", "disorder due to presence of foreign body", "exogenous material", "fb - foreign body", "fb - foreign body of body structure", "foreign body (disorder)", "foreign body (morphologic abnormality)", "foreign body of body structure", "foreign material", "choking (finding)", "button battery (physical object)", "foreign body (physical object)", "angle foreign body", "aspirated foreign body", "aspirated foreign body in bronchus", "aspirated foreign body in larynx", "aspirated foreign body in pharynx", "aspiration of foreign body into lung", "conjunctival foreign body", "corneal foreign body", "effect of foreign body", "extraperitoneal foreign body removed", "facial bone foreign body removed", "fishing hook foreign body", "foreign body - finger", "foreign body at cardia", "foreign body at terminal ileum", "foreign body chewing", "foreign body dermatosis", "foreign body gingivitis", "foreign body granuloma of colon", "foreign body granuloma of intestine", "foreign body granuloma of muscle", "foreign body granuloma of penis", "foreign body granuloma of skin", "foreign body granuloma of soft tissue", "foreign body granuloma of subcutaneous tissue", "foreign body in anterior abdominal wall", "foreign body in anterior chamber", "foreign body in anus", "foreign body in anus and rectum", "foreign body in appendix", "foreign body in ascending colon", "foreign body in auditory canal", "foreign body in auricle", "foreign body in bone", "foreign body in bronchioles", "foreign body in bronchus", "foreign body in cecum", "foreign body in cervical esophagus", "foreign body in cervix", "foreign body in ciliary body", "foreign body in colon", "foreign body in conjunctival sac", "foreign body in descending colon", "foreign body in digestive tract", "foreign body in duodenum", "foreign body in ear", "foreign body in esophagus", "foreign body in eye", "foreign body in fallopian tube", "foreign body in female perineum", "foreign body in female urethra", "foreign body in forearm", "foreign body in genitourinary tract", "foreign body in gingival mucous membrane", "foreign body in hand", "foreign body in hand with infection", "foreign body in head", "foreign body in heart", "foreign body in heel", "foreign body in hypopharynx", "foreign body in ileum", "foreign body in intestine", "foreign body in intestine and colon", "foreign body in iris", "foreign body in jaw bone", "foreign body in jejunum", "foreign body in kidney", "foreign body in lacrimal punctum", "foreign body in larynx", "foreign body in left auditory canal", "foreign body in left auricle", "foreign body in left cornea", "foreign body in left ear", "foreign body in left external ear", "foreign body in left forearm", "foreign body in left lower leg", "foreign body in left lower limb", "foreign body in left main bronchus", "foreign body in left thigh", "foreign body in left thumb", "foreign body in lens", "foreign body in lip", "foreign body in lower leg"],
		},

		# ── GENERAL / SYSTEMIC ───────────────────────────────────────
		"general": {
			"fatigue":                 ["fatigue", "tired", "exhausted", "weakness", "lethargy", "malaise", "weak", "no energy", "asthenia", "fatigue (finding)", "weariness", "lack of vitality", "lethargic", "lethargy (finding)", "does not feel right", "feels off-color", "feels poorly", "feels unwell", "malaise (finding)", "not feeling great", "not feeling well", "vague bodily discomfort", "weak (qualifier value)", "asthenia (finding)", "debility", "feeling weak", "general weakness", "lassitude", "weakness - general", "feeling tired", "tired (finding)", "accommodative fatigue", "cancer-related fatigue", "central muscle fatigue", "chronic fatigue syndrome", "combat fatigue", "exercise induced muscle fatigue", "fatigue during pregnancy", "fatigue fracture of vertebra", "high frequency muscle fatigue", "low frequency muscle fatigue", "malaise and fatigue", "muscle fatigue", "neuromuscular fatigue", "peripheral muscle fatigue", "postexertional fatigue", "postviral fatigue syndrome", "psychogenic fatigue", "rapid fatigue of gait", "severe systemic illness respiratory muscle fatigue", "transient heat fatigue", "vocal fatigue", "accommodative fatigue (disorder)", "fatigue associated with malignant neoplastic disease", "fatigue associated with malignant neoplastic disease (finding)", "central muscle fatigue (finding)", "benign myalgic encephalomyelitis", "cfs - chronic fatigue syndrome", "chronic fatigue syndrome (disorder)", "iceland disease", "me - myalgic encephalomyelitis", "me/cfs - myalgic encephalomyelitis/chronic fatigue syndrome", "myalgic encephalomyelitis", "myalgic encephalomyelitis syndrome", "combat fatigue (disorder)", "exercise induced muscle fatigue (finding)", "exertional muscle fatigue", "fatigue during pregnancy (finding)", "fatigue fracture of vertebra (disorder)", "stress fracture of vertebra", "high frequency muscle fatigue (finding)", "low frequency muscle fatigue (finding)", "malaise and fatigue (finding)", "muscle fatigue (finding)", "muscle tiredness", "muscles tire easily", "neuromuscular fatigue, function", "neuromuscular fatigue, function (observable entity)", "peripheral muscle fatigue (finding)", "excessive postexertional fatigue", "excessive postexertional fatigue (finding)", "postviral fatigue syndrome (disorder)", "psychogenic fatigue (disorder)", "rapid fatigue of gait (finding)", "severe systemic illness respiratory muscle fatigue (disorder)", "transient heat fatigue (finding)", "decreased vocal loudness", "vocal fatigue (finding)", "voice fatigue", "weakness of voice"],
			"swelling":                ["swelling", "edema", "swollen", "distension", "puffiness"],
			"pain general":            ["pain", "generalized pain", "body aches", "all over pain", "diffuse pain", "aches", "dolor", "pain (finding)", "pain observations", "painful", "part hurts", "diffuse pain (finding)", "generalized aches and pains", "generalized aches and pains (finding)", "generalized body aches"],
			"high blood pressure":     ["high blood pressure", "hypertension", "elevated bp", "blood pressure up", "htn", "bp - high blood pressure", "bp+ - hypertension", "hbp - high blood pressure", "high blood pressure disorder", "ht - hypertension", "htn - hypertension", "hypertensive disorder", "hypertensive disorder, systemic arterial", "hypertensive disorder, systemic arterial (disorder)", "hypertensive vascular degeneration", "hypertensive vascular disease", "systemic arterial hypertension"],
			"low blood pressure":      ["low blood pressure", "hypotension", "bp low", "blood pressure dropping", "shock", "hypotensive", "arterial hypotension", "hypopiesis", "low blood pressure (disorder)", "acute circulatory failure", "circulatory collapse", "peripheral circulatory failure", "peripheral vascular failure", "peripheral vascular shutdown", "shock (disorder)", "shock - physiological"],
			"hypothermia":             ["hypothermia", "cold exposure", "low body temperature", "temp low", "freezing", "cold patient", "freezing (physical force)", "body temperature below normal", "decreased body temperature", "hypothermia (finding)", "state of hypothermia", "temperature subnormal", "exposure to cold", "exposure to cold (event)", "accidental hypothermia in elderly person", "behavior to prevent hypothermia", "hypothermia - accidental", "hypothermia of newborn", "immersion hypothermia", "induced hypothermia", "neonatal environmental hypothermia", "unplanned perioperative hypothermia", "accidental hypothermia in elderly person (finding)", "behavior to prevent hypothermia (observable entity)", "hypothermia - accidental (finding)", "hypothermia of newborn (disorder)", "immersion hypothermia (disorder)", "induced hypothermia (finding)", "unplanned perioperative hypothermia (disorder)"],
			"hyperthermia":            ["hyperthermia", "heat stroke", "heat exhaustion", "overheating", "high body temperature", "heat prostration", "hyperthermia (disorder)", "heat apoplexy", "heat hyperpyrexia", "heat stroke (disorder)", "thermoplegia", "heat exhaustion (disorder)", "body temperature above reference range", "body temperature above reference range (finding)", "has a temperature", "increased body temperature", "temperature elevated", "temperature raised", "behavior to prevent hyperthermia", "endocrine hyperthermia", "exercise-induced malignant hyperthermia", "malignant hyperthermia", "malignant hyperthermia genetic susceptibility", "maternal hyperthermia induced birth defect", "neonatal environmental hyperthermia", "neonatal hyperthermia", "neurogenic hyperthermia", "risk of malignant hyperthermia", "behavior to prevent hyperthermia (observable entity)", "endocrine hyperthermia (finding)", "exercise-induced malignant hyperthermia (disorder)", "malignant hyperthermia (disorder)", "mh - malignant hyperpyrexia", "mhs - malignant hyperthermia susceptibility", "genetic susceptibility to malignant hyperthermia", "genetic susceptibility to malignant hyperthermia (finding)", "birth defect due to maternal hyperthermia", "birth defect due to maternal hyperthermia (disorder)", "neurogenic hyperthermia (finding)", "risk of malignant hyperthermia (observable entity)"],
		},
	}

	# ── SYMPTOM WEIGHTS — higher = more dangerous / discriminating ──
	SYMPTOM_WEIGHTS = {
		# Weight 10 — immediately life-threatening
		"cardiac arrest":10, "respiratory failure":10, "facial_droop":10,
		"slurred_speech":10, "thunderclap headache":10, "aortic pain":10,
		"hematemesis":10, "loss of consciousness":10, "opioid signs":10,
		"carbon monoxide":10, "throat swelling":10,
		# Weight 9 — very high acuity
		"chest pain":9, "shortness of breath":9, "seizure":9, "hypoxia":9,
		"altered mental status":9, "suicidal ideation":9, "sudden limb pallor":9,
		"pulmonary embolism signs":9, "overdose":9, "placental abruption":9,
		# Weight 8 — high acuity
		"rapid heart rate":8, "fainting":8, "arm weakness":8, "leg weakness":8,
		"aphasia":8, "vision loss":8, "rebound tenderness":8, "bloody stool":8,
		"hematuria":8, "scrotal pain":8, "hypertensive urgency":8,
		"preeclampsia signs":8, "ectopic pain":8, "psychosis":8,
		"agitation":8, "sepsis signs":8, "head injury":8, "meningeal signs":8,
		"organophosphate signs":8, "bulging fontanelle":8, "labor signs":8,
		# Weight 7 — moderate-high
		"fever":7, "neck stiffness":7, "stridor":7, "hemoptysis":7,
		"pleuritic chest pain":7, "right lower quadrant pain":7, "flank pain":7,
		"deep vein thrombosis":7, "pelvic pain":7, "abdominal distension":7,
		"petechiae":7, "angioedema":7, "cyanosis":7,
		"hypoglycemia signs":7, "hyperglycemia signs":7,
		"acetaminophen toxicity":7, "caustic ingestion":7,
		"febrile seizure":7, "vaginal bleeding":7, "intussusception signs":7,
		"eye pain":6, "cellulitis":6, "abscess":6,
		# Weight 5 — moderate
		"palpitations":5, "irregular heart rate":5, "slow heart rate":5,
		"jaw pain":5, "arm pain":5, "dizziness":5, "headache":5,
		"numbness":5, "ataxia":5, "abdominal pain":5, "jaundice":5,
		"dysphagia":5, "right upper quadrant pain":5, "urinary retention":5,
		"trauma":5, "burn":6, "dislocation":5, "mania":5, "delirium":6,
		"substance use":5, "bleeding":5, "high pitched cry":6,
		"barking cough":5, "foreign body":6,
		# Weight 4 — lower acuity
		"leg swelling":4, "tremor":4, "nausea":4, "vomiting":4, "diarrhea":4,
		"constipation":4, "dysuria":4, "urinary frequency":4,
		"back pain":4, "joint pain":4, "rash":4, "diaphoresis":4, "pallor":4,
		"chills":4, "night sweats":4, "lymphadenopathy":4, "sore throat":4,
		"productive cough":4, "ear pain":4, "polyuria":4, "polydipsia":4,
		"weight loss":4, "heat intolerance":4, "cold intolerance":4,
		"anxiety":4, "leg pain with walking":4, "epistaxis":4,
		"hoarseness":4, "bruising":4, "pallor anemia":4, "splenomegaly":4,
		"sickle cell pain":6, "regurgitation":4, "bloating":3,
		"chest wall pain":5, "ankle pain":4, "swelling":3,
		# Weight 2-3 — low acuity
		"fatigue":3, "diaphoresis":4, "cough":2, "wheezing":3,
		"nasal congestion":2, "weight gain":2, "polyphagia":3,
		"hip pain":4, "knee pain":3, "muscle pain":3,
		"laceration":3, "photophobia":3, "phonophobia":2,
		"thyroid symptoms":3, "adrenal symptoms":5, "depression":3,
		"pruritis":3, "dental pain":3, "facial pain":3,
	}

	# ── SYNDROMES — fire when ≥2 symptoms match ──────────────────────
	SYNDROMES = {
		# Cardiac
		"STEMI / ACS":                  ["chest pain","shortness of breath","diaphoresis","arm pain","jaw pain"],
		"Aortic Dissection":            ["aortic pain","chest pain","back pain","arm weakness","hypertensive urgency"],
		"Cardiac Tamponade":            ["chest pain","low blood pressure","leg swelling","fainting"],
		"Heart Failure Exacerbation":   ["shortness of breath","leg swelling","fatigue","rapid heart rate"],
		"Cardiogenic Shock":            ["chest pain","low blood pressure","rapid heart rate","altered mental status"],
		# Neuro
		"Acute Stroke (FAST)":          ["facial_droop","arm weakness","slurred_speech","aphasia","vision loss"],
		"SAH / Meningitis":             ["thunderclap headache","neck stiffness","photophobia","fever","altered mental status"],
		"Status Epilepticus":           ["seizure","loss of consciousness","altered mental status"],
		"Increased ICP":                ["headache","vomiting","papilledema","altered mental status"],
		"Hypertensive Encephalopathy":  ["headache","hypertensive urgency","altered mental status","vision change","seizure"],
		# Respiratory
		"Tension Pneumothorax":         ["shortness of breath","chest pain","low blood pressure","tachypnea","cyanosis"],
		"Pulmonary Embolism":           ["pulmonary embolism signs","shortness of breath","pleuritic chest pain","deep vein thrombosis"],
		"Severe Asthma":                ["wheezing","shortness of breath","tachypnea","cyanosis","hypoxia"],
		"Epiglottitis":                 ["stridor","throat swelling","fever","dysphagia"],
		# Abdominal
		"Appendicitis":                 ["right lower quadrant pain","fever","nausea","vomiting","rebound tenderness"],
		"Bowel Obstruction":            ["abdominal pain","constipation","vomiting","abdominal distension"],
		"Ruptured Ectopic Pregnancy":   ["ectopic pain","vaginal bleeding","low blood pressure","fainting"],
		"Liver Failure":                ["jaundice","abdominal distension","altered mental status","bleeding"],
		# Infectious
		"Sepsis":                       ["fever","rapid heart rate","altered mental status","low blood pressure","tachypnea"],
		"Meningococcal Septicemia":     ["fever","petechiae","neck stiffness","altered mental status","rapid heart rate"],
		"Toxic Shock Syndrome":         ["fever","rash","low blood pressure","altered mental status","vomiting"],
		# Endocrine
		"Diabetic Ketoacidosis":        ["hyperglycemia signs","fruity breath","vomiting","altered mental status","tachypnea"],
		"Hypoglycemia":                 ["hypoglycemia signs","altered mental status","diaphoresis","palpitations","seizure"],
		"Thyroid Storm":                ["fever","rapid heart rate","altered mental status","heat intolerance","vomiting"],
		# Toxicology
		"Opioid Toxidrome":             ["opioid signs","respiratory failure","loss of consciousness","slow heart rate"],
		"Sympathomimetic Toxidrome":    ["stimulant signs","rapid heart rate","agitation"],
		"Serotonin Syndrome":           ["altered mental status","tremor","rapid heart rate","diaphoresis"],
		"Cholinergic Toxidrome":        ["organophosphate signs","diaphoresis","vomiting","seizure"],
		# Vascular
		"Acute Limb Ischemia":          ["sudden limb pallor","leg pain with walking"],
		# Anaphylaxis
		"Anaphylaxis":                  ["rash","throat swelling","shortness of breath","low blood pressure","rapid heart rate"],
		# OB
		"Eclampsia":                    ["preeclampsia signs","seizure","headache","vision change","high blood pressure"],
		# Pediatric
		"Pediatric Meningitis":         ["fever","bulging fontanelle","high pitched cry","rash child","neck stiffness"],
		"Croup":                        ["barking cough","stridor","fever","hoarseness"],
		# Psychiatric
		"Excited Delirium":             ["agitation","rapid heart rate","altered mental status","psychosis"],
		# GI
		"GERD / Acid Reflux":           ["regurgitation","chest pain","bloating","abdominal pain"],
		# MSK
		"Musculoskeletal Chest Pain":   ["chest wall pain","chest pain"],
		# Panic
		"Panic Attack":                 ["anxiety","chest pain","shortness of breath","numbness","rapid heart rate"],
	}

	# ── FULL ER DIAGNOSES ────────────────────────────────────────────
	DIAGNOSES = {
		# CARDIAC
		"STEMI (Heart Attack)":             ["chest pain","shortness of breath","diaphoresis","arm pain","jaw pain","palpitations","nausea","vomiting"],
		"NSTEMI / Unstable Angina":         ["chest pain","shortness of breath","diaphoresis","palpitations","fatigue","nausea"],
		"Aortic Dissection":                ["aortic pain","chest pain","arm weakness","hypertensive urgency","back pain","fainting"],
		"Pulmonary Embolism":               ["shortness of breath","pleuritic chest pain","tachypnea","deep vein thrombosis","leg swelling","hypoxia","rapid heart rate"],
		"Cardiac Tamponade":                ["chest pain","shortness of breath","low blood pressure","fainting","leg swelling"],
		"Heart Failure (Acute)":            ["shortness of breath","leg swelling","fatigue","rapid heart rate","cough"],
		"Hypertensive Emergency":           ["hypertensive urgency","headache","vision change","altered mental status","chest pain","shortness of breath"],
		"Atrial Fibrillation":              ["palpitations","irregular heart rate","shortness of breath","fainting","chest pain","rapid heart rate"],
		"Ventricular Tachycardia":          ["rapid heart rate","palpitations","chest pain","fainting","shortness of breath","loss of consciousness"],
		"Complete Heart Block":             ["slow heart rate","fainting","chest pain","altered mental status","fatigue"],
		"Endocarditis":                     ["fever","chills","heart murmur","fatigue","joint pain","petechiae","night sweats"],
		"Pericarditis":                     ["chest pain","fever","pleuritic chest pain","shortness of breath"],
		"Myocarditis":                      ["chest pain","shortness of breath","fever","fatigue","palpitations","rapid heart rate"],
		"Cardiogenic Shock":                ["chest pain","low blood pressure","rapid heart rate","altered mental status","shortness of breath"],
		"Cardiac Arrest":                   ["syncope", "loss of consciousness", "cardiac arrest signs"],
		# GI — ADDED FOR PRECISION
		"GERD / Acid Reflux":               ["regurgitation","chest pain","bloating","abdominal pain","nausea"],
		"Peptic Ulcer Disease":             ["abdominal pain","nausea","hematemesis","bloody stool","regurgitation"],
		"Esophageal Spasm":                 ["chest pain","dysphagia","regurgitation"],
		"Gastritis":                        ["abdominal pain","nausea","vomiting","regurgitation","bloating"],
		# MSK / CHEST WALL — ADDED FOR PRECISION
		"Costochondritis":                  ["chest wall pain","chest pain","pleuritic chest pain"],
		"Musculoskeletal Chest Pain":       ["chest wall pain","chest pain","back pain","muscle pain"],
		"Rib Fractures":                    ["chest pain","pleuritic chest pain","trauma","shortness of breath"],
		# MSK TRAUMA
		"Ankle Sprain":                     ["ankle pain","swelling","twisted"],
		"Ankle Fracture":                   ["ankle pain","swelling","deformity","bone pain"],
		# PSYCHIATRIC — ADDED FOR PRECISION
		"Panic Disorder":                   ["anxiety","rapid heart rate","shortness of breath","chest pain","diaphoresis","tremor","numbness"],
		"Acute Anxiety / Panic Attack":     ["anxiety","shortness of breath","chest pain","numbness","rapid heart rate","diaphoresis","tremor"],
		"Hyperventilation Syndrome":        ["shortness of breath","numbness","anxiety","dizziness","chest pain"],
		# VASCULAR
		"DVT":                              ["deep vein thrombosis","leg swelling","leg pain with walking"],
		"Acute Limb Ischemia":              ["sudden limb pallor","leg pain with walking"],
		"Abdominal Aortic Aneurysm":        ["aortic pain","abdominal pain","back pain","low blood pressure"],
		"Ruptured AAA":                     ["aortic pain","abdominal pain","low blood pressure","back pain","fainting"],
		"Mesenteric Ischemia":              ["abdominal pain","vomiting","bloody stool","low blood pressure","rapid heart rate"],
		# RESPIRATORY
		"Tension Pneumothorax":             ["shortness of breath","chest pain","hypoxia","low blood pressure","tachypnea"],
		"Simple Pneumothorax":              ["chest pain","shortness of breath","pleuritic chest pain","tachypnea"],
		"Pneumonia":                        ["fever","cough","shortness of breath","productive cough","chills","chest pain","tachypnea"],
		"COVID-19":                         ["fever","cough","shortness of breath","fatigue","hypoxia"],
		"Asthma (Acute)":                   ["wheezing","shortness of breath","tachypnea","cough","chest pain"],
		"COPD Exacerbation":                ["shortness of breath","cough","wheezing","productive cough","hypoxia","tachypnea","copd history"],
		"Epiglottitis":                     ["stridor","sore throat","fever","dysphagia","throat swelling","hoarseness"],
		"Anaphylaxis":                      ["rash","throat swelling","shortness of breath","low blood pressure","rapid heart rate","angioedema"],
		"Hemothorax":                       ["shortness of breath","chest pain","trauma","hypoxia","low blood pressure"],
		"ARDS":                             ["shortness of breath","hypoxia","tachypnea","fever","altered mental status"],
		"Foreign Body Aspiration":          ["choking","stridor","foreign body","cyanosis","shortness of breath"],
		"Pulmonary Edema":                  ["shortness of breath","cough","leg swelling","hypoxia"],
		"Pleural Effusion":                 ["shortness of breath","pleuritic chest pain","fever"],
		"Respiratory Failure":              ["respiratory failure","shortness of breath","altered mental status","cyanosis","hypoxia"],
		# NEUROLOGICAL
		"Stroke / CVA":             ["facial_droop","unilateral_weakness","slurred_speech","aphasia","vision loss","dizziness"],
		"TIA":                      ["facial_droop","unilateral_weakness","slurred_speech","dizziness","vision change","aphasia"],
		"Subarachnoid Hemorrhage":          ["thunderclap headache","neck stiffness","vomiting","altered mental status","photophobia","loss of consciousness"],
		"Meningitis (Bacterial)":           ["fever","neck stiffness","headache","photophobia","altered mental status","vomiting","petechiae"],
		"Meningitis (Viral)":               ["fever","neck stiffness","headache","photophobia","nausea","vomiting"],
		"Encephalitis":                     ["fever","altered mental status","seizure","headache","neck stiffness"],
		"Epidural Hematoma":                ["head injury","loss of consciousness","headache","altered mental status"],
		"Subdural Hematoma":                ["head injury","headache","altered mental status","slurred speech","seizure"],
		"Status Epilepticus":               ["seizure","altered mental status","loss of consciousness"],
		"Hypertensive Encephalopathy":      ["headache","vision change","seizure","hypertensive urgency","altered mental status"],
		"Wernicke's Encephalopathy":        ["altered mental status","ataxia","alcohol toxicity"],
		"Guillan-Barre Syndrome":           ["leg weakness","arm weakness","facial_droop"],
		"Myasthenic Crisis":                ["respiratory failure","arm weakness","leg weakness","dysphagia"],
		"Cerebral Venous Thrombosis":       ["headache","vision change","seizure","papilledema"],
		# GASTROINTESTINAL
		"Appendicitis":                     ["right lower quadrant pain","fever","nausea","vomiting","rebound tenderness"],
		"Cholecystitis (Acute)":            ["right upper quadrant pain","fever","nausea","vomiting","jaundice"],
		"Cholelithiasis":                   ["right upper quadrant pain","nausea","vomiting"],
		"Pancreatitis (Acute)":             ["abdominal pain","nausea","vomiting","fever","jaundice","epigastric pain","back pain"],
		"Bowel Obstruction":                ["abdominal pain","vomiting","constipation","abdominal distension","nausea"],
		"Perforated Viscus":                ["abdominal pain","rebound tenderness","fever","low blood pressure","nausea"],
		"Ischemic Colitis":                 ["abdominal pain","bloody stool","nausea","diarrhea","low blood pressure"],
		"Diverticulitis":                   ["abdominal pain","fever","nausea"],
		"GI Bleed (Upper)":                 ["hematemesis","abdominal pain","low blood pressure","rapid heart rate","bloody stool"],
		"GI Bleed (Lower)":                 ["bloody stool","abdominal pain","low blood pressure","rapid heart rate","pallor"],
		"Gastroenteritis":                  ["nausea","vomiting","diarrhea","fever","abdominal pain"],
		"Liver Failure (Acute)":            ["jaundice","altered mental status","abdominal distension","bleeding","fever"],
		"Volvulus":                         ["abdominal pain","constipation","abdominal distension","vomiting"],
		"Heartburn / Dyspepsia":            ["regurgitation"],
		# GENITOURINARY
		"Kidney Stones":                   ["flank pain","hematuria","nausea","vomiting","dysuria"],
		"Cystitis / UTI":                  ["dysuria","urinary frequency","fever","hematuria"],
		"Pyelonephritis":                   ["fever","flank pain","dysuria","urinary frequency","chills","nausea"],
		"Urosepsis":                        ["fever","flank pain","altered mental status","low blood pressure","rapid heart rate"],
		"Testicular Torsion":               ["scrotal pain","vomiting","nausea"],
		"Epididymo-Orchitis":               ["scrotal pain","fever","dysuria","urinary frequency"],
		"Supraventricular Tachycardia":     ["rapid heart rate","palpitations","chest pain","faintness"],
		"Delirium Tremens":                 ["tremor","altered mental status","fever","rapid heart rate","hallucinations"],
		"Hypoglycemia":                     ["altered mental status","diaphoresis","tremor","rapid heart rate","loss of consciousness"],

		"Epididymitis":                     ["scrotal pain","scrotal swelling","fever","dysuria"],
		"Pelvic Inflammatory Disease":      ["pelvic pain","fever","vaginal discharge","nausea"],
		"Paralytic Ileus":                  ["abdominal distension","nausea","vomiting","constipation"],
		"Pancreatitis":                     ["abdominal pain","nausea","vomiting","fever","epigastric pain","back pain"],
		"Wernicke Encephalopathy":          ["altered mental status","ataxia","vision loss","tremor"],
		"Hepatic Encephalopathy":           ["altered mental status","jaundice","tremor","abdominal distension"],
		"Esophageal Rupture":               ["chest pain","vomiting","shortness of breath","fever"],
		"Migraine":                         ["headache","nausea","photophobia","phonophobia","vision loss"],
		"Cholecystitis":                    ["right upper quadrant pain","fever","nausea","vomiting"],
		"Neurogenic Shock":                 ["low blood pressure","slow heart rate","trauma","loss of sensation"],
		"Acute Urinary Retention":          ["urinary retention"],
		"Dysuria":                          ["dysuria"],
		"Ruptured Ectopic Pregnancy":       ["ectopic pain","vaginal bleeding","low blood pressure","fainting","pelvic pain","abdominal pain","pregnancy signs"],
		"PID":                              ["pelvic pain","fever","vaginal discharge","abdominal pain","dysuria"],
		"Ovarian Torsion":                  ["ovarian cyst","vomiting","nausea","pelvic pain"],
		# INFECTIOUS
		"Sepsis":                           ["fever","rapid heart rate","altered mental status","low blood pressure","tachypnea","chills"],
		"Meningococcemia":                  ["fever","petechiae","neck stiffness","altered mental status","rapid heart rate","rash"],
		"Cellulitis":                       ["cellulitis","fever","rash"],
		"Necrotizing Fasciitis":            ["fever","cellulitis","low blood pressure"],
		"Endocarditis (Infective)":         ["fever","chills","heart murmur","petechiae","fatigue","joint pain"],
		"Influenza":                        ["fever","fatigue","headache","cough","chills","muscle pain"],
		"Malaria":                          ["fever","chills","diaphoresis","headache","nausea","fatigue"],
		"Dengue Fever":                     ["fever","headache","muscle pain","joint pain","rash","petechiae"],
		"Tuberculosis":                     ["productive cough","cough","hemoptysis","night sweats","weight loss","fever","fatigue"],
		# ENDOCRINE
		"Diabetic Ketoacidosis":            ["hyperglycemia signs","fruity breath","vomiting","altered mental status","tachypnea","abdominal pain"],
		"Hyperosmolar Hyperglycemic State": ["hyperglycemia signs","altered mental status","polyuria","polydipsia","fatigue"],
		"Severe Hypoglycemia":              ["hypoglycemia signs","altered mental status","diaphoresis","seizure","palpitations"],
		"Thyroid Storm":                    ["fever","rapid heart rate","altered mental status","heat intolerance","vomiting","thyroid symptoms"],
		"Myxedema Coma":                    ["altered mental status","cold intolerance","fatigue","slow heart rate","hypothermia"],
		"Adrenal Crisis":                   ["adrenal symptoms","low blood pressure","vomiting","altered mental status","fever","abdominal pain"],
		"Hypercalcemia":                    ["fatigue","altered mental status","abdominal pain","constipation","polyuria","vomiting"],
		"Hyponatremia (Severe)":            ["altered mental status","headache","seizure","nausea","vomiting","fatigue"],
		"Hyperkalemia":                     ["muscle pain","palpitations","slow heart rate","fatigue","altered mental status"],
		# TOXICOLOGY
		"Opioid Overdose":                  ["opioid signs","respiratory failure","loss of consciousness","slow heart rate","cyanosis"],
		"Stimulant Toxicity":               ["stimulant signs","agitation","rapid heart rate","high blood pressure","chest pain"],
		"Acetaminophen Overdose":           ["acetaminophen toxicity","nausea","vomiting","abdominal pain","jaundice"],
		"Alcohol Poisoning":                ["alcohol toxicity","altered mental status","vomiting","respiratory failure","low blood pressure"],
		"Carbon Monoxide Poisoning":        ["carbon monoxide","headache","nausea","altered mental status"],
		"Organophosphate Poisoning":        ["organophosphate signs","vomiting","diaphoresis","seizure","respiratory failure"],
		"Benzodiazepine Overdose":          ["altered mental status","respiratory failure","ataxia","loss of consciousness","slow heart rate"],
		"Tricyclic Antidepressant OD":      ["altered mental status","rapid heart rate","seizure","low blood pressure"],
		"Serotonin Syndrome":               ["altered mental status","tremor","rapid heart rate","diaphoresis","agitation"],
		"Neuroleptic Malignant Syndrome":   ["hyperthermia","muscle pain","altered mental status","rapid heart rate","diaphoresis"],
		# PSYCHIATRIC
		"Acute Psychosis":                  ["psychosis","agitation","altered mental status"],
		"Manic Episode":                    ["mania","agitation"],
		"Suicidal Crisis":                  ["suicidal ideation","depression","overdose"],
		"Excited Delirium":                 ["agitation","rapid heart rate","altered mental status","psychosis"],
		"Alcohol Withdrawal":               ["tremor","agitation","seizure","diaphoresis","rapid heart rate","fever"],
		"Opioid Withdrawal":                ["agitation","nausea","vomiting","diarrhea","muscle pain","diaphoresis","rapid heart rate"],
		# TRAUMA
		"Traumatic Brain Injury":           ["head injury","altered mental status","vomiting","headache","loss of consciousness","seizure"],
		"Traumatic Pneumothorax":           ["chest pain","shortness of breath","trauma","hypoxia"],
		"Splenic Laceration":               ["trauma","abdominal pain","low blood pressure","tachypnea"],
		"Traumatic Aortic Injury":          ["trauma","chest pain","aortic pain","back pain","low blood pressure"],
		"Spinal Cord Injury":               ["trauma","neck injury","leg weakness","arm weakness","numbness","urinary retention"],
		"Pelvic Fracture":                  ["trauma","pelvic pain","low blood pressure","hip pain","hematuria"],
		"Major Burns":                      ["burn","shortness of breath","carbon monoxide","hypoxia"],
		# OB/GYN
		"Eclampsia":                        ["preeclampsia signs","seizure","headache","vision change","high blood pressure"],
		"Preeclampsia (Severe)":            ["preeclampsia signs","headache","vision change","high blood pressure","abdominal pain"],
		"Ectopic Pregnancy":                ["ectopic pain","vaginal bleeding","pelvic pain","low blood pressure","fainting","abdominal pain","pregnancy signs"],
		"Placental Abruption":              ["placental abruption","abdominal pain","vaginal bleeding","low blood pressure","rapid heart rate"],
		"Postpartum Hemorrhage":            ["vaginal bleeding","low blood pressure","rapid heart rate","pallor","labor signs"],
		"Hyperemesis Gravidarum":           ["vomiting","nausea","pregnancy signs","weight loss"],
		# HEMATOLOGY
		"Sickle Cell Crisis":               ["sickle cell pain","fever","pallor","shortness of breath"],
		"Massive Hemorrhage":               ["bleeding","low blood pressure","rapid heart rate","pallor","altered mental status"],
		"DIC":                              ["bleeding","petechiae","low blood pressure","fever","thrombosis"],
		"Thrombocytopenia":                 ["bleeding","petechiae","bruising","pallor"],
		"Saddle PE":                        ["shortness of breath","low blood pressure","rapid heart rate","cyanosis","hypoxia"],
		"Drug Toxicity":                    ["altered mental status", "fever", "rapid heart rate", "seizure", "agitation"],
		"Hemorrhagic Shock":                ["low blood pressure", "rapid heart rate", "altered mental status", "pallor", "trauma", "abdominal pain", "internal bleeding"],
		"Airway Obstruction":               ["shortness of breath", "stridor", "throat swelling", "neck swelling", "cyanosis"],
		"Pleuritis":                        ["chest pain", "pleuritic chest pain", "fever", "shortness of breath"],
		# ENT / OPHTHALMOLOGY
		"Acute Angle Closure Glaucoma":     ["eye pain","vision loss","headache","nausea","vomiting","red eye"],
		"Retinal Artery Occlusion":         ["sudden vision loss","vision change"],
		"Orbital Cellulitis":               ["facial pain","fever","eye pain","vision change"],
		"Peritonsillar Abscess":            ["throat swelling","sore throat","fever","dysphagia"],
		"Ludwig's Angina":                  ["throat swelling","dental pain","fever","dysphagia"],
		"Mastoiditis":                      ["ear pain","fever","headache"],
		# PEDIATRIC
		"Croup":                            ["barking cough","stridor","fever","hoarseness"],
		"Bacterial Tracheitis":             ["stridor","fever","barking cough","respiratory failure"],
		"Intussusception":                  ["intussusception signs","abdominal pain","vomiting","bloody stool","high pitched cry"],
		"Pyloric Stenosis":                 ["pyloric stenosis","vomiting"],
		"Kawasaki Disease":                 ["fever","rash child","red eye","lymphadenopathy"],
		"Meningitis (Pediatric)":           ["fever","bulging fontanelle","high pitched cry","rash child","neck stiffness","altered mental status"],
		"Febrile Seizure":                  ["febrile seizure","fever","seizure","altered mental status"],
		"Pediatric Foreign Body":           ["foreign body","choking","stridor"],
		"Epiglottitis (Pediatric)":         ["stridor","fever","dysphagia","throat swelling"],
		"Non-Accidental Trauma":            ["head injury","bruising","altered mental status"],
		# ADDITIONAL BENCHMARK CONDITIONS
		"Flail Chest":                      ["chest pain", "pleuritic chest pain", "trauma", "shortness of breath"],
		"Scarlet Fever":                    ["fever", "sore throat", "rash", "strawberry tongue"],
		"Meniere's Disease":                ["vertigo", "tinnitus", "hearing loss"],
		"Takotsubo Cardiomyopathy":         ["chest pain", "shortness of breath", "anxiety"],
		"SLE Flare":                        ["rash", "joint pain", "fever"],
		"Retinal Detachment":               ["vision loss", "vision change", "sudden vision loss"],
		"Bladder Cancer":                   ["hematuria"],
		"Gout":                             ["joint pain", "joint swelling", "toe pain", "swelling"],
		"Otitis Media":                     ["ear pain", "fever"],
		"Biliary Obstruction":              ["jaundice", "abdominal pain", "nausea"],
		"Cauda Equina Syndrome":            ["back pain", "leg weakness", "urinary retention", "numbness"],
		"Lung Cancer":                      ["cough", "weight loss", "hemoptysis"],
		"Dehydration":                      ["dizziness", "fatigue", "nausea"],
		"Ischemic Colitis":                 ["abdominal pain", "bloody stool", "diarrhea"],
		"Measles":                          ["rash", "fever", "cough"],
		"Mallory-Weiss Tear":               ["hematemesis", "vomiting"],
		"Subdural Hematoma":                ["head injury", "headache", "altered mental status", "slurred speech"],
		"Rheumatoid Arthritis":             ["joint pain", "joint stiffness"],
		"Myasthenia Gravis":                ["vision loss", "facial_droop", "fatigue"],
		"Allergic Rhinitis":                ["nasal congestion"],
		"Lumbar Strain":                    ["back pain"],
		"Parkinson's Disease":              ["tremor"],
		"Hypothyroidism":                   ["fatigue"],
		"Benign Prostatic Hyperplasia":     ["urinary frequency"],
		"Renal Cell Carcinoma":             ["flank pain", "hematuria"],
		"Stable Angina":                    ["chest pain"],
	}

	DIAGNOSIS_ICD10 = {
		# Cardiac
		"STEMI (Heart Attack)":             "I21.9",
		"NSTEMI / Unstable Angina":         "I20.0",
		"Aortic Dissection":                "I71.0",
		"Pulmonary Embolism":               "I26.99",
		"Cardiac Tamponade":                "I31.4",
		"Heart Failure (Acute)":            ["I50.9", "J81.0"],
		"Hypertensive Emergency":           "I16.1",
		"Atrial Fibrillation":              "I48.91",
		"Ventricular Tachycardia":          "I47.2",
		"Complete Heart Block":             "I44.2",
		"Endocarditis":                     "I33.0",
		"Pericarditis":                     "I30.9",
		"Myocarditis":                      "I40.9",
		"Cardiogenic Shock":                "R57.0",
		"Supraventricular Tachycardia":     "I47.1",
		# GI / MSK / Psych
		"GERD / Acid Reflux":               "K21.9", # Specifically requested for Epigastric Burning
		"Peptic Ulcer Disease":             "K27.9",
		"Esophageal Spasm":                 "K22.4",
		"Gastritis":                        "K29.70",
		"Costochondritis":                  "M71.9",
		"Musculoskeletal Chest Pain":       "R07.89", # Specifically requested for Burning Chest Pain
		"Rib Fractures":                    "S22.4",
		"Panic Disorder":                   "F41.0",
		"Acute Anxiety / Panic Attack":     "F41.1",
		"Hyperventilation Syndrome":        "R06.4",
		# Respiratory
		"Tension Pneumothorax":             "J93.0",
		"Simple Pneumothorax":              "J93.81",
		"Pneumonia":                        "J18.9",
		"COVID-19":                         "U07.1",
		"Asthma (Acute)":                   "J45.901",
		"COPD Exacerbation":                "J44.1",
		"Epiglottitis":                     "J05.10",
		"Anaphylaxis":                      "T78.2",
		"Cardiac Arrest":                   "I46.9",
		"Pulmonary Edema":                  "J81.0",
		"Pleural Effusion":                 "J90",
		"Respiratory Failure":              "J96.0",
		# Neuro
		"Ischemic Stroke":                  "I63.9",
		"Hemorrhagic Stroke":               "I61.9",
		"Cystitis / UTI":                  "N39.0",
		"TIA":                              "G45.9",
		"Subarachnoid Hemorrhage":          "I60.9",
		"Meningitis (Bacterial)":           "G00.9",
		"Meningitis (Viral)":               "G03.0",
		"Encephalitis":                     "G04.90",
		"Epidural Hematoma":                "S06.4",
		"Ankle Sprain":                     "S93.4",
		"Ankle Fracture":                   "S82.8",
		"Subdural Hematoma":                "S06.5",
		"Status Epilepticus":               "G41.9",
		"Stroke / CVA [I63.9]":             "I63.9",
		"TIA (Transient Ischemic Attack) [G45.9]": "G45.9",
		"Hypertensive Encephalopathy":      "I67.4",
		# GI
		"Appendicitis":                     "K35.80",
		"Cholecystitis (Acute)":            "K81.0",
		"Pancreatitis (Acute)":             "K85.90",
		"Bowel Obstruction":                "K56.60",
		"Perforated Viscus":                "K63.1",
		"GI Bleed (Upper)":                 "K92.2",
		"Gastroenteritis":                  "K52.9",
		# GU
		"Kidney Stones":                   "N20.0",
		"Urinary Tract Infection":          "N39.0",
		"Pyelonephritis":                   "N12",
		"Urosepsis":                        "N39.0",
		"Testicular Torsion":               "N44.0",
		"Dysuria":                          "R30.0",
		"Heartburn / Dyspepsia":            "K21.9",
		"Epididymitis":                     "N45.1",
		"Pelvic Inflammatory Disease":      "N73.9",
		"Ruptured Ectopic Pregnancy":       "O00.1",
		"Ectopic Pregnancy":                "O00.9",
		# Infectious / Endocrine / Tox
		"Sepsis":                           "A41.9",
		"Septic Shock":                     "R57.2",
		"Meningococcemia":                  "A39.2",
		"Diabetic Ketoacidosis":            "E11.10",
		"Hyperosmolar Hyperglycemic State": "E11.00",
		"Thyroid Storm":                    "E05.9",
		"Adrenal Crisis":                   "E27.40",
		"Opioid Overdose":                  "T40.1",
		"Carbon Monoxide Poisoning":        "T58",
		# Trauma / OB
		"Traumatic Brain Injury":           "S06.9",
		"Traumatic Pneumothorax":           "S27.0",
		"Splenic Laceration":               "S36.0",
		"Traumatic Aortic Injury":          "S21.3",
		"Major Burns":                      "T30.0",
		"Eclampsia":                        "O15.9",
		"Preeclampsia (Severe)":            "O14.10",
		"Placental Abruption":              "O45.9",
		"Postpartum Hemorrhage":            "O72.1",
		"Sickle Cell Crisis":               "D57.00",
		"Massive Hemorrhage":               "R58",
		"Acute Angle Closure Glaucoma":     "H40.20",
		"Retinal Artery Occlusion":         "H34.1",
	}

	@classmethod
	def load_snomed_diagnoses(cls):
		"""Load SNOMED-backed diagnoses and merge with hardcoded DIAGNOSES."""
		import json, os
		snomed_path = os.path.join(os.path.dirname(__file__), 'data', 'diagnoses_from_snomed.json')
		if not os.path.exists(snomed_path):
			return
		try:
			with open(snomed_path) as f:
				snomed_dx = json.load(f)
			added = 0
			for condition_name, data in snomed_dx.items():
				# Don't overwrite existing manually curated entries
				if condition_name not in cls.DIAGNOSES:
					cls.DIAGNOSES[condition_name] = data.get('symptom_keys', [])
					# Also store ICD-10
					if not hasattr(cls, 'DIAGNOSIS_ICD10'):
						cls.DIAGNOSIS_ICD10 = {}
					if condition_name not in cls.DIAGNOSIS_ICD10:
						cls.DIAGNOSIS_ICD10[condition_name] = data.get('icd10', 'N/A')
					added += 1
			print(f"[BrainBuddy] SNOMED diagnoses loaded: +{added} conditions (total: {len(cls.DIAGNOSES)})")
		except Exception as e:
			print(f"[BrainBuddy] SNOMED diagnoses load failed: {e}")


	SYMPTOMS_SYNONYMS = {}
	DRUG_REFERENCE = {
	    "Stroke": [
	        {
	            "name": "Alteplase / tPA",
	            "rxcui": "8410",
	            "type": "IN"
	        },
	        {
	            "name": "Aspirin",
	            "rxcui": "1191",
	            "type": "IN"
	        },
	        {
	            "name": "clopidogrel",
	            "rxcui": "32968",
	            "type": "IN"
	        },
	        {
	            "name": "heparin",
	            "rxcui": "5224",
	            "type": "IN"
	        },
	        {
	            "name": "warfarin",
	            "rxcui": "11289",
	            "type": "IN"
	        },
	        {
	            "name": "apixaban",
	            "rxcui": "1364430",
	            "type": "IN"
	        }
	    ],
	    "STEMI": [
	        {
	            "name": "aspirin",
	            "rxcui": "1191",
	            "type": "IN"
	        },
	        {
	            "name": "heparin",
	            "rxcui": "5224",
	            "type": "IN"
	        },
	        {
	            "name": "nitroglycerin",
	            "rxcui": "4917",
	            "type": "IN"
	        },
	        {
	            "name": "morphine",
	            "rxcui": "7052",
	            "type": "IN"
	        },
	        {
	            "name": "clopidogrel",
	            "rxcui": "32968",
	            "type": "IN"
	        },
	        {
	            "name": "ticagrelor",
	            "rxcui": "1116632",
	            "type": "IN"
	        },
	        {
	            "name": "metoprolol",
	            "rxcui": "6918",
	            "type": "IN"
	        }
	    ],
	    "Sepsis": [
	        {
	            "name": "piperacillin",
	            "rxcui": "8339",
	            "type": "IN"
	        },
	        {
	            "name": "vancomycin",
	            "rxcui": "11124",
	            "type": "IN"
	        },
	        {
	            "name": "norepinephrine",
	            "rxcui": "7512",
	            "type": "IN"
	        },
	        {
	            "name": "dopamine",
	            "rxcui": "3628",
	            "type": "IN"
	        },
	        {
	            "name": "hydrocortisone",
	            "rxcui": "5492",
	            "type": "IN"
	        },
	        {
	            "name": "meropenem",
	            "rxcui": "29561",
	            "type": "IN"
	        }
	    ],
	    "Pulmonary Embolism": [
	        {
	            "name": "heparin",
	            "rxcui": "5224",
	            "type": "IN"
	        },
	        {
	            "name": "enoxaparin",
	            "rxcui": "613391",
	            "type": "IN"
	        },
	        {
	            "name": "warfarin",
	            "rxcui": "11289",
	            "type": "IN"
	        },
	        {
	            "name": "rivaroxaban",
	            "rxcui": "1114195",
	            "type": "IN"
	        },
	        {
	            "name": "apixaban",
	            "rxcui": "1364430",
	            "type": "IN"
	        }
	    ],
	    "Pneumonia": [
	        {
	            "name": "amoxicillin",
	            "rxcui": "723",
	            "type": "IN"
	        },
	        {
	            "name": "azithromycin",
	            "rxcui": "18631",
	            "type": "IN"
	        },
	        {
	            "name": "levofloxacin",
	            "rxcui": "82122",
	            "type": "IN"
	        },
	        {
	            "name": "ceftriaxone",
	            "rxcui": "2193",
	            "type": "IN"
	        },
	        {
	            "name": "doxycycline",
	            "rxcui": "3640",
	            "type": "IN"
	        }
	    ],
	    "Anaphylaxis": [
	        {
	            "name": "epinephrine",
	            "rxcui": "3992",
	            "type": "IN"
	        },
	        {
	            "name": "diphenhydramine",
	            "rxcui": "3498",
	            "type": "IN"
	        },
	        {
	            "name": "methylprednisolone",
	            "rxcui": "6902",
	            "type": "IN"
	        },
	        {
	            "name": "ranitidine",
	            "rxcui": "9143",
	            "type": "IN"
	        },
	        {
	            "name": "albuterol",
	            "rxcui": "435",
	            "type": "IN"
	        }
	    ],
	    "Asthma": [
	        {
	            "name": "albuterol",
	            "rxcui": "435",
	            "type": "IN"
	        },
	        {
	            "name": "ipratropium",
	            "rxcui": "7213",
	            "type": "IN"
	        },
	        {
	            "name": "methylprednisolone",
	            "rxcui": "6902",
	            "type": "IN"
	        },
	        {
	            "name": "magnesium sulfate",
	            "rxcui": "6585",
	            "type": "IN"
	        },
	        {
	            "name": "salmeterol",
	            "rxcui": "36117",
	            "type": "IN"
	        }
	    ],
	    "COPD": [
	        {
	            "name": "albuterol",
	            "rxcui": "435",
	            "type": "IN"
	        },
	        {
	            "name": "ipratropium",
	            "rxcui": "7213",
	            "type": "IN"
	        },
	        {
	            "name": "prednisone",
	            "rxcui": "8640",
	            "type": "IN"
	        },
	        {
	            "name": "azithromycin",
	            "rxcui": "18631",
	            "type": "IN"
	        },
	        {
	            "name": "theophylline",
	            "rxcui": "10438",
	            "type": "IN"
	        }
	    ],
	    "PE": [
	        {
	            "name": "heparin",
	            "rxcui": "5224",
	            "type": "IN"
	        },
	        {
	            "name": "enoxaparin",
	            "rxcui": "67108",
	            "type": "IN"
	        },
	        {
	            "name": "alteplase",
	            "rxcui": "8410",
	            "type": "IN"
	        },
	        {
	            "name": "warfarin",
	            "rxcui": "11289",
	            "type": "IN"
	        },
	        {
	            "name": "apixaban",
	            "rxcui": "1364430",
	            "type": "IN"
	        },
	        {
	            "name": "rivaroxaban",
	            "rxcui": "1114195",
	            "type": "IN"
	        }
	    ],
	    "DVT": [
	        {
	            "name": "enoxaparin",
	            "rxcui": "67108",
	            "type": "IN"
	        },
	        {
	            "name": "heparin",
	            "rxcui": "5224",
	            "type": "IN"
	        },
	        {
	            "name": "warfarin",
	            "rxcui": "11289",
	            "type": "IN"
	        },
	        {
	            "name": "apixaban",
	            "rxcui": "1364430",
	            "type": "IN"
	        },
	        {
	            "name": "rivaroxaban",
	            "rxcui": "1114195",
	            "type": "IN"
	        },
	        {
	            "name": "dabigatran",
	            "rxcui": "1546356",
	            "type": "IN"
	        }
	    ],
	    "DKA": [
	        {
	            "name": "potassium chloride",
	            "rxcui": "8591",
	            "type": "IN"
	        },
	        {
	            "name": "sodium bicarbonate",
	            "rxcui": "36676",
	            "type": "IN"
	        }
	    ],
	    "Meningitis": [
	        {
	            "name": "ceftriaxone",
	            "rxcui": "2193",
	            "type": "IN"
	        },
	        {
	            "name": "vancomycin",
	            "rxcui": "11124",
	            "type": "IN"
	        },
	        {
	            "name": "ampicillin",
	            "rxcui": "733",
	            "type": "IN"
	        },
	        {
	            "name": "dexamethasone",
	            "rxcui": "3264",
	            "type": "IN"
	        },
	        {
	            "name": "acyclovir",
	            "rxcui": "281",
	            "type": "IN"
	        }
	    ],
	    "Hypertension": [
	        {
	            "name": "labetalol",
	            "rxcui": "6185",
	            "type": "IN"
	        },
	        {
	            "name": "nicardipine",
	            "rxcui": "7396",
	            "type": "IN"
	        },
	        {
	            "name": "hydralazine",
	            "rxcui": "5470",
	            "type": "IN"
	        },
	        {
	            "name": "enalapril",
	            "rxcui": "3827",
	            "type": "IN"
	        },
	        {
	            "name": "nitroprusside",
	            "rxcui": "7476",
	            "type": "IN"
	        }
	    ],
	    "Opioid Overdose": [
	        {
	            "name": "naloxone",
	            "rxcui": "7242",
	            "type": "IN"
	        }
	    ],
	    "Seizure": [
	        {
	            "name": "lorazepam",
	            "rxcui": "6470",
	            "type": "IN"
	        },
	        {
	            "name": "diazepam",
	            "rxcui": "3322",
	            "type": "IN"
	        },
	        {
	            "name": "levetiracetam",
	            "rxcui": "114477",
	            "type": "IN"
	        },
	        {
	            "name": "phenytoin",
	            "rxcui": "8183",
	            "type": "IN"
	        },
	        {
	            "name": "fosphenytoin",
	            "rxcui": "72236",
	            "type": "IN"
	        },
	        {
	            "name": "valproate",
	            "rxcui": "40254",
	            "type": "IN"
	        }
	    ],
	    "Heart Failure": [
	        {
	            "name": "furosemide",
	            "rxcui": "4603",
	            "type": "IN"
	        },
	        {
	            "name": "bumetanide",
	            "rxcui": "1808",
	            "type": "IN"
	        },
	        {
	            "name": "nitroglycerin",
	            "rxcui": "4917",
	            "type": "IN"
	        },
	        {
	            "name": "digoxin",
	            "rxcui": "3407",
	            "type": "IN"
	        },
	        {
	            "name": "carvedilol",
	            "rxcui": "20352",
	            "type": "IN"
	        },
	        {
	            "name": "lisinopril",
	            "rxcui": "29046",
	            "type": "IN"
	        }
	    ],
	    "Atrial Fib": [
	        {
	            "name": "metoprolol",
	            "rxcui": "6918",
	            "type": "IN"
	        },
	        {
	            "name": "diltiazem",
	            "rxcui": "3443",
	            "type": "IN"
	        },
	        {
	            "name": "amiodarone",
	            "rxcui": "703",
	            "type": "IN"
	        },
	        {
	            "name": "heparin",
	            "rxcui": "5224",
	            "type": "IN"
	        },
	        {
	            "name": "warfarin",
	            "rxcui": "11289",
	            "type": "IN"
	        },
	        {
	            "name": "apixaban",
	            "rxcui": "1364430",
	            "type": "IN"
	        }
	    ],
	    "Appendicitis": [
	        {
	            "name": "cefazolin",
	            "rxcui": "2180",
	            "type": "IN"
	        },
	        {
	            "name": "metronidazole",
	            "rxcui": "6922",
	            "type": "IN"
	        },
	        {
	            "name": "piperacillin",
	            "rxcui": "8339",
	            "type": "IN"
	        },
	        {
	            "name": "morphine",
	            "rxcui": "7052",
	            "type": "IN"
	        },
	        {
	            "name": "ketorolac",
	            "rxcui": "35827",
	            "type": "IN"
	        }
	    ],
	    "UTI": [
	        {
	            "name": "trimethoprim",
	            "rxcui": "10829",
	            "type": "IN"
	        },
	        {
	            "name": "nitrofurantoin",
	            "rxcui": "7454",
	            "type": "IN"
	        },
	        {
	            "name": "ciprofloxacin",
	            "rxcui": "2551",
	            "type": "IN"
	        },
	        {
	            "name": "cephalexin",
	            "rxcui": "2231",
	            "type": "IN"
	        },
	        {
	            "name": "fosfomycin",
	            "rxcui": "4550",
	            "type": "IN"
	        }
	    ],
	    "Pyelonephritis": [
	        {
	            "name": "ciprofloxacin",
	            "rxcui": "2551",
	            "type": "IN"
	        },
	        {
	            "name": "ceftriaxone",
	            "rxcui": "2193",
	            "type": "IN"
	        },
	        {
	            "name": "gentamicin",
	            "rxcui": "1596450",
	            "type": "IN"
	        },
	        {
	            "name": "ampicillin",
	            "rxcui": "733",
	            "type": "IN"
	        },
	        {
	        },
	        {
	            "name": "gentamicin",
	            "rxcui": "1596450",
	            "type": "IN"
	        },
	        {
	            "name": "ampicillin",
	            "rxcui": "733",
	            "type": "IN"
	        },
	        {
	            "name": "trimethoprim",
	            "rxcui": "10829",
	            "type": "IN"
	        }
	    ],
	    "Pancreatitis": [
	        {
	            "name": "morphine",
	            "rxcui": "7052",
	            "type": "IN"
	        },
	        {
	            "name": "hydromorphone",
	            "rxcui": "3423",
	            "type": "IN"
	        },
	        {
	            "name": "ondansetron",
	            "rxcui": "26225",
	            "type": "IN"
	        },
	        {
	            "name": "pantoprazole",
	            "rxcui": "40790",
	            "type": "IN"
	        }
	    ],
	    "default": [
	        {
	            "name": "morphine",
	            "rxcui": "7052",
	            "type": "IN"
	        },
	        {
	            "name": "ondansetron",
	            "rxcui": "26225",
	            "type": "IN"
	        },
	        {
	            "name": "acetaminophen",
	            "rxcui": "161",
	            "type": "IN"
	        },
	        {
	            "name": "ibuprofen",
	            "rxcui": "5640",
	            "type": "IN"
	        },
	        {
	            "name": "ketorolac",
	            "rxcui": "35827",
	            "type": "IN"
	        }
	    ],
	    "Ankle Sprain": [
	        {
	            "name": "ibuprofen",
	            "rxcui": "5640",
	            "type": "IN"
	        },
	        {
	            "name": "acetaminophen",
	            "rxcui": "161",
	            "type": "IN"
	        }
	    ],
	    "Ankle Fracture": [
	        {
	            "name": "ibuprofen",
	            "rxcui": "5640",
	            "type": "IN"
	        },
	        {
	            "name": "acetaminophen",
	            "rxcui": "161",
	            "type": "IN"
	        }
	    ]
	}











	@classmethod
	def build_symptom_map(cls):
		for system, symptoms in cls.ONTOLOGY.items():
			for symptom, synonyms in symptoms.items():
				cls.SYMPTOMS_SYNONYMS[symptom] = synonyms

	# Maps for O(N) detection
	_PHRASE_MAP = {}
	_ROOT_MAP = {}
	_CATEGORY_MAP = {}

	@classmethod
	def initialize_engine(cls):
		"""Pre-compute lookup maps for instantaneous O(N) matching."""
		cls._PHRASE_MAP = {}
		cls._ROOT_MAP = {}
		cls._CATEGORY_MAP = {}

		# 1. Base Ontology priority
		for category, symptoms in cls.ONTOLOGY.items():
			for symptom, synonyms in symptoms.items():
				cls._CATEGORY_MAP[symptom] = category
				# Root matchable if single word
				if " " not in symptom:
					cls._ROOT_MAP[symptom] = symptom
				for phrase in synonyms:
					p_low = phrase.lower()
					if p_low not in cls._PHRASE_MAP:
						cls._PHRASE_MAP[p_low] = []
					if symptom not in cls._PHRASE_MAP[p_low]:
						cls._PHRASE_MAP[p_low].append(symptom)

		# 1.5 Force specific mappings for Stroke Module
		stroke_fixes = {
			"right sided weakness": ["unilateral_weakness"],
			"left sided weakness":  ["unilateral_weakness"],
			"facial droop":         ["facial_droop"],
			"facial asymmetry":     ["facial_droop"],
			"slurred speech":       ["slurred_speech"]
		}
		for phrase, syms in stroke_fixes.items():
			cls._PHRASE_MAP[phrase] = syms

		# Fix #3: Additional Clinical Mappings
		clinical_fixes = {
			"allergic reaction": ["rash", "throat swelling"],
			"collapse":          ["syncope", "loss of consciousness"],
			"no pulse":           ["cardiac arrest signs"],
			"epigastric pain":   ["epigastric pain", "upper abdominal pain"],
			"missed period":     ["pregnancy signs", "amenorrhea"],
			"missed periods":    ["pregnancy signs", "amenorrhea"],
			# Coverage for automated tests
			"rapid heartbeat":   ["rapid heart rate"],
			"right lower abdominal pain": ["right lower quadrant pain", "abdominal pain"],
			"right lower quadrant abdominal pain": ["right lower quadrant pain", "abdominal pain"],
			"polyuria":          ["hyperglycemia signs", "polyuria"],
			"polydipsia":        ["hyperglycemia signs", "polydipsia"],
			"neck swelling":     ["throat swelling", "neck swelling"],
			"agitation":         ["altered mental status", "agitation"],
			"hyperthermia":      ["fever", "hyperthermia"],
			"radiating to back": ["back pain"],
			"worse on inspiration": ["pleuritic chest pain"],
			"sudden vision loss": ["vision loss", "sudden vision loss"],
			"epigastric pain radiating to back": ["epigastric pain", "back pain", "aortic pain"],
			"chest pain worse on inspiration": ["chest pain", "pleuritic chest pain"],
			"worst headache of life": ["thunderclap headache"],
			"worst headache": ["thunderclap headache"],
			"worst of life": ["thunderclap headache"],
			"thunderclap": ["thunderclap headache"],
			"sudden severe headache": ["thunderclap headache"],
		}
		for phrase, syms in clinical_fixes.items():
			cls._PHRASE_MAP[phrase] = syms

		# 2. Load and merge SNOMED synonyms
		try:
			with open(get_data_path('symptom_synonyms.json'), 'r') as f:
				enriched = json.load(f)
				for symptom, synonyms in enriched.items():
					for phrase in synonyms:
						p_low = phrase.lower()
						if p_low not in cls._PHRASE_MAP:
							cls._PHRASE_MAP[p_low] = []
						if symptom not in cls._PHRASE_MAP[p_low]:
							cls._PHRASE_MAP[p_low].append(symptom)
		except: pass

	@classmethod
	def parse_vitals(cls, text):
		"""Strict numeric parsing for vital signs to prevent NLP hallucinations."""
		text_raw = text.lower()
		detected_vitals = set()
		vital_boost = False

		# 1. BP check (flexible regex)
		bp_match = re.search(r'\b(?:bp\s*|blood pressure\s*)?([0-9]{2,3})\s*/\s*([0-9]{2,3})\b', text_raw)
		if bp_match:
			sys_val, dia_val = int(bp_match.group(1)), int(bp_match.group(2))
			if sys_val < 90 or dia_val < 60:
				vital_boost = True
				detected_vitals.add("low blood pressure")
			elif sys_val >= 180 or dia_val >= 110:
				detected_vitals.add("hypertensive urgency")

		# 2. HR check (Strict Integer Enforcement)
		# Matches 'HR: 115', 'HR 115', 'Pulse: 115', etc.
		hr_match = re.search(r'\bhr\s*[:=]?\s*(\d+)', text_raw, re.IGNORECASE)
		if not hr_match:
			hr_match = re.search(r'\b(?:pulse|heart rate|heartrate)\b\s*[:=]?\s*(\d+)', text_raw, re.IGNORECASE)
		
		if hr_match:
			hr_val = int(hr_match.group(1))
			if hr_val > 100:
				vital_boost = True
				detected_vitals.add("rapid heart rate")
			elif hr_val < 50:
				detected_vitals.add("slow heart rate")

		# 3. SpO2 check
		o2_match = re.search(r'\b(?:spo2|o2 sat|oxygen|o2|sat)\b\s*[:=]?\s*([0-9]{2,3})%?', text_raw)
		if o2_match:
			sat = int(o2_match.group(1))
			if sat < 92:
				vital_boost = True
				detected_vitals.add("hypoxia")

		return detected_vitals, vital_boost

	@classmethod
	def detect_symptoms(cls, text):
		analysis_text = text.lower()
		
		# The "Smart Sweeper" v2.0 (Eats through line breaks)
		# Wipes comma-separated lists until it hits a period or a positive clinical word
		# Updated pattern to be more aggressive with whitespace and multiple symptoms
		negation_pattern = r'\b(denies|denied|no|without|negative for)\b[\s\w,]*?(?=\b(?:endorses|reports|has|with|positive for|complains of)\b|\.|\n|$)'
		analysis_text = re.sub(negation_pattern, ' ', analysis_text, flags=re.IGNORECASE | re.DOTALL)

		if not cls._PHRASE_MAP:
			cls.initialize_engine()

		# ── 1. DEDICATED VITALS EXTRACTION ────────────────────────────
		# Operating strictly on analysis_text instead of the original text
		vitals_found, vital_boost = cls.parse_vitals(analysis_text)

		# ── 2. INPUT SANITIZATION (Strip Vitals Block from NLP) ───────
		# Forcefully sanitize input hyphens before tokenization
		analysis_text = analysis_text.replace('-', ' ')
		
		# Removes 'Vitals: ... .' to prevent 'HR' triggering NLP matches
		nlp_text = re.sub(r'\bvitals:.*?(?:\.|$)', '', analysis_text, flags=re.IGNORECASE | re.DOTALL)
		text_raw = nlp_text
		
		# Clean text for tokenization
		tokens = re.findall(r'\b[a-z0-9/.]+\b', text_raw)
		detected = set(vitals_found)
		consumed = [False] * len(tokens)

		# ── 2. LOGIC FILTERS ─────────────────────────────────────────
		negations = {"no", "denies", "negative", "without", "not", "none", "nontender"}
		anchors_gi = {"chest", "epigastric", "throat", "stomach", "belly", "esophagus", "heartburn", "reflux"}
		anchors_gu = {"urination", "pee", "voiding", "micturition", "urine"}
		anchors_pleuritic = {"inspiration", "breathing", "breath", "deep breath", "pleuritic", "pleurisy", "inhaling"}

		def check_filters(symptom, start_idx, end_idx, matched_text):
			"""Returns (bool accept, str remapped_symptom)"""
			# A. Negation Check (Lookbehind 3 words)
			for k in range(max(0, start_idx-3), start_idx):
				if tokens[k] in negations:
					return False, None
			
			# B. Anatomical Anchor Check (Disambiguation for 'burning')
			# Only remap if the detected symptom is 'burn'
			if symptom == "burn" and "burning" in matched_text:
				# Check +/- 5 words
				context = tokens[max(0, start_idx-5):min(len(tokens), end_idx+5)]
				if any(a in context for a in anchors_gi):
					return True, "regurgitation"
				if any(a in context for a in anchors_gu):
					return True, "dysuria"
			
			if symptom == "chest pain":
				context = tokens[max(0, start_idx-5):min(len(tokens), end_idx+5)]
				if any(a in context for a in anchors_pleuritic):
					return True, "pleuritic chest pain"
				
			return True, symptom

		# ── 3. SLIDING WINDOW MATCHING (N-GRAMS) ──────────────────────
		# Sort phrases by word count (longest first) to ensure greedy matching
		sorted_phrases = sorted(cls._PHRASE_MAP.keys(), key=lambda k: len(k.split()), reverse=True)
		
		for phrase in sorted_phrases:
			phrase_tokens = phrase.split()
			n = len(phrase_tokens)
			if n == 0: continue
			
			for i in range(len(tokens) - n + 1):
				# If any token in this window is already consumed, skip
				if any(consumed[i:i+n]): continue
				
				# Check if window tokens match phrase tokens
				window_phrase = " ".join(tokens[i:i+n])
				if window_phrase == phrase:
					# Match found!
					possible_symptoms = cls._PHRASE_MAP[phrase]
					for sym in possible_symptoms:
						accept, final_sym = check_filters(sym, i, i+n, phrase)
						if accept:
							detected.add(final_sym)
							for k in range(i, i+n): consumed[k] = True
					# Once phrase is matched and consumed, we can continue to next window
					# (or technically next phrase since we consumed)

		# ── 4. ROOT MATCHING (for unconsumed tokens) ─────────────────
		for i, token in enumerate(tokens):
			if consumed[i]: continue
			if len(token) < 4: continue
			
			for root, sym in cls._ROOT_MAP.items():
				# Extra rule: 'racing' maps to rapid heart rate
				if token == "racing":
					accept, final_sym = check_filters("rapid heart rate", i, i+1, token)
					if accept: detected.add(final_sym); consumed[i] = True; break
				
				if token.startswith(root):
					accept, final_sym = check_filters(sym, i, i+1, token)
					if accept:
						detected.add(final_sym)
						consumed[i] = True
					break

		if vital_boost:
			detected.add("__VITAL_BOOST__")

		# ── 5. HARDCODED INTERCEPT (Bypass N-gram logic) ─────────────
		# Ensures critical stroke symptoms are captured even if normalized/misparsed
		# Operating strictly on analysis_text
		if "right sided weakness" in analysis_text or "left sided weakness" in analysis_text or "right sided fatigue" in analysis_text or "left sided fatigue" in analysis_text:
			detected.add("unilateral_weakness")
			if "fatigue" in detected: detected.remove("fatigue")
		if "facial droop" in analysis_text or "facial asymmetry" in analysis_text:
			detected.add("facial_droop")
		if "slurred speech" in analysis_text:
			detected.add("slurred_speech")

		# ── LAB VALUE INTERCEPTS ──────────────────────────────────────
		text_for_labs = text.lower()

		# Blood glucose numeric parsing
		glucose_match = re.search(r'(?:blood\s+glucose|glucose|blood\s+sugar)\s*[:\s]*(\d{2,4})', text_for_labs)
		if glucose_match:
			glucose = int(glucose_match.group(1))
			if glucose >= 250:
				detected.add("hyperglycemia signs")
			if glucose < 70:
				detected.add("hypoglycemia signs")

		# pH / acidosis
		ph_match = re.search(r'\bph\s*[:\s=]*(\d+\.\d+)', text_for_labs)
		if ph_match:
			ph = float(ph_match.group(1))
			if ph < 7.35:
				detected.add("metabolic acidosis")

		# Bicarbonate
		bicarb_match = re.search(r'(?:bicarbonate|bicarb|hco3)\s*[:\s=]*(\d+)', text_for_labs)
		if bicarb_match:
			bicarb = int(bicarb_match.group(1))
			if bicarb < 18:
				detected.add("metabolic acidosis")
				detected.add("hyperglycemia signs")

		# Ketones positive
		if re.search(r'ketones?\s+(?:positive|\+|present|in urine)', text_for_labs):
			detected.add("hyperglycemia signs")

		# Kussmaul breathing
		if "kussmaul" in text_for_labs:
			detected.add("hyperglycemia signs")
			detected.add("tachypnea")

		# Ectopic / RLQ pregnancy pain
		if re.search(r'(?:ectopic|right\s+lower\s+quadrant\s+pain|rlq\s+pain|positive\s+pregnancy)', text_for_labs):
			detected.add("ectopic pain")
		if re.search(r'(?:vaginal\s+(?:bleeding|spotting)|vaginal\s+discharge\s+blood)', text_for_labs):
			detected.add("vaginal bleeding")
		if re.search(r'(?:pregnant|pregnancy|lmp|weeks\s+pregnant)', text_for_labs):
			detected.add("pregnancy signs")

		# COPD history
		if re.search(r'\bcopd\b', text_for_labs):
			detected.add("copd history")

		# Safety catch for negated trauma
		text_lower = text.lower()
		if "trauma" in detected and ("denies" in text_lower or "no trauma" in text_lower):
			detected.remove("trauma")

		return sorted(list(detected))

	@classmethod
	def detect_syndromes(cls, detected):
		found = []
		# Filter out the internal boost flag
		clean_detected = [s for s in detected if not s.startswith("__")]
		for syndrome, symptoms in cls.SYNDROMES.items():
			match = sum(1 for s in symptoms if s in clean_detected)
			if match >= 2:
				found.append(syndrome)
		return found

import os
import sys
import json

def get_data_path(filename):
    """Resolve a data-file path for both terminal and Mac bundle."""
    if hasattr(sys, "_MEIPASS"):
        base = sys._MEIPASS
    else:
        base = os.environ.get('RESOURCEPATH', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, "data", filename)

# Initialize on module load
SymptomLibrary.initialize_engine()

try:
    with open(get_data_path('rxnorm_medications.json'), 'r') as f:
        RXNORM_MEDICATIONS = json.load(f)
except FileNotFoundError:
    RXNORM_MEDICATIONS = {}

try:
    with open(get_data_path('snomed_icd10_map.json'), 'r') as f:
        SNOMED_ICD10_MAP = json.load(f)
except FileNotFoundError:
    SNOMED_ICD10_MAP = {}

# Load SNOMED diagnoses at module startup
SymptomLibrary.load_snomed_diagnoses()


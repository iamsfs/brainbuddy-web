import json
# ---------- CONFIG ----------
CONFIDENCE_CAP_LOW_DATA = 70  # adjust based on your system
# ---------- HELPERS ----------
def contains_any(text, keywords):
    text = text.lower()
    return any(k.lower() in text for k in keywords)
# ---------- SCORING ----------
def score_case(test, result):
    score = 0
    feedback = []
    # 1. Top Condition (40 pts)
    norm_top = result["top_condition"].lower()
    norm_acceptable = [x.lower() for x in test["acceptable_top"]]
    if norm_top in norm_acceptable:
        score += 40
    else:
        feedback.append("❌ Wrong top condition")
    # 2. Differential Quality (15 pts)
    if "differentials" in result:
        norm_diffs = [d.lower() for d in result["differentials"]]
        norm_acceptable = [x.lower() for x in test["acceptable_top"]]
        matches = sum(
            1 for d in norm_diffs
            if d in norm_acceptable
        )
        if matches > 0:
            score += 15
        else:
            feedback.append("⚠️ Weak differential")
    # 3. Must Include (15 pts)
    if test["must_include"]:
        hits = sum(
            1 for item in test["must_include"]
            if contains_any(result.get("full_text", ""), [item])
        )
        if hits == len(test["must_include"]):
            score += 15
        else:
            feedback.append("❌ Missing required actions/tests")
    else:
        score += 15  # no requirement = full points
    # 4. Safety (15 pts)
    violations = [
        item for item in test["must_not_include"]
        if contains_any(result.get("full_text", ""), [item])
    ]
    if not violations:
        score += 15
    else:
        feedback.append(f"🚨 Unsafe output: {violations}")
    # 5. Confidence Calibration (10 pts)
    confidence = result.get("confidence", 0)
    if confidence <= CONFIDENCE_CAP_LOW_DATA:
        score += 10
    else:
        feedback.append("⚠️ Overconfident")
    # 6. Hallucination Check (5 pts)
    hallucination_terms = ["history of", "known case of"]
    if not contains_any(result.get("full_text", ""), hallucination_terms):
        score += 5
    else:
        feedback.append("❌ Possible hallucinated history")

    # 7. Reasoning Reward (New! +5 pts)
    if "reasoning_trace" in result:
        factors = result["reasoning_trace"].get("key_factors", [])
        if len(factors) >= 2:
            score += 5
            feedback.append("✅ Strong reasoning trace surfaced")
        elif len(factors) == 1:
            score += 2
            feedback.append("⚠️ Partial reasoning trace")

    return score, feedback
# ---------- RUNNER ----------
def run_tests(engine_function, test_file="data/er_test_suite.json"):
    with open(test_file) as f:
        tests = json.load(f)["cases"]
    total_score = 0
    results_summary = []
    for test in tests:
        output = engine_function(test["input"])
        # Expected output format from your app:
        # {
        #   "top_condition": "...",
        #   "confidence": 75,
        #   "differentials": [...],
        #   "full_text": "full generated note"
        # }
        score, feedback = score_case(test, output)
        total_score += score
        results_summary.append({
            "id": test["id"],
            "score": score,
            "feedback": feedback
        })
        status = "PASS" if score >= 70 else "FAIL"
        print(f"[{status}] Case {test['id']} → {score}/100")
    avg_score = total_score / len(tests)
    print("\n======================")
    print(f"AVERAGE SCORE: {avg_score:.2f}/100")
    print("======================")
    return results_summary
# ---------- MOCK ENGINE (replace this) ----------
def dummy_engine(input_text):
    return {
        "top_condition": "Test",
        "confidence": 50,
        "differentials": [],
        "full_text": input_text
    }
# ---------- RUN ----------
if __name__ == "__main__":
    run_tests(dummy_engine)

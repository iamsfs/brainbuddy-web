from clinical_engine import SymptomLibrary

def apply_competition(scores, features):
    """
    scores = {"STEMI": 0.8, "PE": 0.6, ...}
    features = extracted signals
    """
    adjusted = scores.copy()
    
    # -------------------------
    # 1. Group Reinforcement
    # -------------------------
    group_strength = {}
    for group, conditions in SymptomLibrary.CONDITION_GROUPS.items():
        group_strength[group] = sum(
            scores.get(c, 0) for c in conditions
        )
    
    if not group_strength:
        return adjusted
        
    dominant_group = max(group_strength, key=group_strength.get)
    
    # boost dominant group slightly
    for c in SymptomLibrary.CONDITION_GROUPS.get(dominant_group, []):
        if c in adjusted:
            adjusted[c] *= 1.2
            
    # -------------------------
    # 2. Cross-Group Penalty
    # -------------------------
    for group, conditions in SymptomLibrary.CONDITION_GROUPS.items():
        if group != dominant_group:
            for c in conditions:
                if c in adjusted:
                    adjusted[c] *= 0.8
                    
    # -------------------------
    # 3. Conflict Logic (Anxiety vs Cardiac)
    # -------------------------
    if features.get("cardiac") and features.get("anxiety"):
        # Panic Attack often mimics STEMI
        for c in SymptomLibrary.CONDITION_GROUPS["psych"]:
            if c in adjusted:
                adjusted[c] += 0.20
        for c in ["STEMI", "NSTEMI", "Unstable Angina"]:
            if c in adjusted:
                adjusted[c] *= 0.85
                
    # -------------------------
    # 4. Must-Not-Miss Injection
    # -------------------------
    if features.get("chest_pain"):
        for c in ["STEMI", "PE", "Aortic Dissection"]:
            if c in adjusted:
                adjusted[c] = max(adjusted.get(c, 0), 0.40)
    
    # -------------------------
    # 5. Strong Lead Reinforcement
    # -------------------------
    sorted_adj = sorted(adjusted.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_adj) > 1 and sorted_adj[0][1] > 1.3 * sorted_adj[1][1]:
        adjusted[sorted_adj[0][0]] *= 1.25

    return adjusted

def normalize_scores(scores):
    """Normalize scores to 0-100 scale based on relative probability."""
    total = sum(scores.values())
    if total == 0:
        return {k: 0 for k in scores}
    return {
        k: round((v / total) * 100, 2)
        for k, v in scores.items()
    }

def sharpen(scores):
    """Sharpen top candidates by suppressing weak tails (softmax-like)."""
    if not scores:
        return scores
    max_score = max(scores.values())
    if max_score == 0:
        return scores
        
    sharpened = {}
    for k, v in scores.items():
        if v < max_score * 0.4: # Suppression threshold
            sharpened[k] = v * 0.6 # Push weak ones down
        else:
            sharpened[k] = v
            
    return sharpened

def reinforce_within_group(scores, conditions):
    """Sharpen the lead for the top candidate within a clinical group."""
    group_scores = {k: v for k, v in scores.items() if k in conditions}
    if not group_scores or len(group_scores) < 2:
        return scores
        
    winner = max(group_scores, key=group_scores.get)
    if group_scores[winner] > 0:
        scores[winner] *= 1.15 # 15% boost for the within-group leader
        
    return scores

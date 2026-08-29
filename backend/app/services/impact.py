"""Transparent deterministic prototype impact assessment; not a validated prediction."""
import re

# Prototype assumptions: all factors are 0-100, then combined by these weights.
FACTOR_WEIGHTS = {"communityReach": .30, "urgency": .25, "resourceSensitivity": .20, "domainImportance": .15, "problemSeverity": .10}
LEVEL_THRESHOLDS = {"high": 80, "medium": 60}
DOMAIN_IMPORTANCE = {"Healthcare": 90, "Water & Sanitation": 90, "Environment": 88, "Transportation": 85, "Energy": 85, "Agriculture": 78, "Education": 78, "Waste Management": 78}

def _clamp(value): return max(0, min(100, value))
def _keyword_score(text, keywords, base=45, increment=10): return _clamp(base + sum(word in text for word in keywords) * increment)
def _reach(value):
    digits = re.sub(r"[^0-9]", "", value or "")
    if digits:
        count = int(digits)
        if count >= 100000: return 100
        if count >= 10000: return 85
        if count >= 1000: return 70
        if count >= 100: return 55
        return 35
    return 70 if any(word in (value or "").lower() for word in ("city", "district", "large", "many", "community")) else 50

def assess_impact(challenge):
    """Score deterministic challenge signals; this is prototype guidance, not scientific forecasting."""
    text = f"{challenge['title']} {challenge['description']} {challenge.get('location', '')}".lower()
    factors = {
        "communityReach": _reach(challenge.get("affectedPeople", "")),
        "urgency": _keyword_score(text, ("urgent", "emergency", "risk", "unsafe", "critical", "shortage", "outbreak")),
        "resourceSensitivity": _keyword_score(text, ("water", "sanitation", "health", "energy", "waste", "food", "pollution", "safety"), 40, 9),
        "domainImportance": DOMAIN_IMPORTANCE.get(challenge.get("domain"), 65),
        "problemSeverity": _keyword_score(text, ("wastage", "wasted", "lack", "difficult", "failure", "overflow", "delay", "inequality"), 45, 8),
    }
    score = round(sum(factors[name] * weight for name, weight in FACTOR_WEIGHTS.items()))
    level = "High" if score >= LEVEL_THRESHOLDS["high"] else "Medium" if score >= LEVEL_THRESHOLDS["medium"] else "Low"
    return {"score": score, "level": level, "factors": factors}

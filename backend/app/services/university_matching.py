"""Transparent deterministic matching against fictional demo university data."""
from app.data.demo_universities import DEMO_UNIVERSITIES

# Scores are domain 50%, required-expertise overlap 30%, department overlap 20%.
REQUIREMENTS = {
 "Water & Sanitation": {"expertise":["IoT","Environmental Engineering","Data Analytics"], "departments":["Civil Engineering","Environmental Engineering","Electronics"]},
 "Waste Management": {"expertise":["IoT","Data Analytics","Environmental Engineering"], "departments":["Environmental Engineering","Computer Engineering"]},
 "Education": {"expertise":["EdTech","Web Development","AI/ML"], "departments":["Computer Engineering","Design"]},
 "Healthcare": {"expertise":["AI/ML","Mobile Development","Data Science"], "departments":["Biomedical Engineering","Computer Engineering"]},
 "Agriculture": {"expertise":["IoT","Data Science","Environmental Engineering"], "departments":["Agricultural Engineering","Environmental Engineering"]},
 "Environment": {"expertise":["Environmental Engineering","Data Analytics","IoT"], "departments":["Environmental Engineering","Civil Engineering"]},
}

def _shared(required, available): return [item for item in required if item in available]
def match_universities(challenge: dict) -> list[dict]:
    domain = challenge.get("domain", "")
    requirements = REQUIREMENTS.get(domain, {"expertise": [], "departments": []})
    matches = []
    for university in DEMO_UNIVERSITIES:
        expertise = _shared(requirements["expertise"], university["expertise"])
        departments = _shared(requirements["departments"], university["departments"])
        domain_points = 50 if domain in university["domains"] else 0
        expertise_points = round(30 * len(expertise) / len(requirements["expertise"])) if requirements["expertise"] else 0
        department_points = round(20 * len(departments) / len(requirements["departments"])) if requirements["departments"] else 0
        score = domain_points + expertise_points + department_points
        if score:
            matches.append({"id": university["id"], "name": university["name"], "match_score": score, "matching_expertise": expertise, "relevant_departments": departments, "score_breakdown": {"domain_match": domain_points, "expertise_match": expertise_points, "department_match": department_points}})
    return sorted(matches, key=lambda item: item["match_score"], reverse=True)[:4]

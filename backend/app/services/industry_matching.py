"""Transparent industry matching: domain 40%, capabilities 35%, support 25%."""
from app.data.demo_industries import DEMO_INDUSTRIES
CAPABILITY_MAP = {"Water & Sanitation":["IoT","Data Analytics","Smart Infrastructure","Cloud Systems"],"Waste Management":["IoT","Data Analytics","Smart Infrastructure"],"Education":["EdTech","Cloud Systems","Mobile Development","AI/ML"],"Healthcare":["AI/ML","Mobile Development","Cloud Systems","Data Analytics"],"Agriculture":["IoT","Data Analytics","Smart Infrastructure"],"Environment":["IoT","Data Analytics","Environmental Monitoring"]}
SUPPORT_TYPES = ["Technology", "Mentorship", "Infrastructure"]
def match_industries(challenge: dict) -> list[dict]:
    required = CAPABILITY_MAP.get(challenge.get("domain"), [])
    output = []
    for org in DEMO_INDUSTRIES:
        capabilities = [x for x in required if x in org["capabilities"]]
        support = [x for x in SUPPORT_TYPES if x in org["support_types"]]
        domain = 40 if challenge.get("domain") in org["domains"] else 0
        capability = round(35 * len(capabilities) / len(required)) if required else 0
        support_score = round(25 * len(support) / len(SUPPORT_TYPES))
        score = domain + capability + support_score
        if score: output.append({"id":org["id"],"name":org["name"],"match_score":score,"matching_capabilities":capabilities,"support_types":support,"demo":True,"score_breakdown":{"domain":domain,"capability":capability,"support":support_score}})
    return sorted(output, key=lambda item: (-item["match_score"], item["name"]))[:3]

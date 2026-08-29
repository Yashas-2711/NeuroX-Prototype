"""Curated deterministic solution directions for the local prototype."""

SOLUTION_LIBRARY = {
    "Water & Sanitation": [
        ("Smart Water Usage Monitoring", "Monitor public water usage and identify unnecessary wastage.", "Technology", "Medium", "High"),
        ("Community Water Leak Reporting", "Let residents report leaks and unattended public taps.", "Community", "Low", "Medium"),
        ("Automatic Tap Shut-off System", "Explore timed or sensor-based shut-off mechanisms for shared taps.", "Infrastructure", "Medium", "High"),
        ("Water Consumption Dashboard", "Make local water-use patterns visible to community coordinators.", "Data", "Medium", "Medium"),
    ],
    "Waste Management": [
        ("Smart Waste Collection Scheduling", "Prioritize collection schedules using area-level waste patterns.", "Technology", "Medium", "High"),
        ("Overflow Detection System", "Flag bins that need attention before they overflow.", "Technology", "Medium", "High"),
        ("Citizen Waste Reporting", "Enable residents to report missed collection and overflowing bins.", "Community", "Low", "Medium"),
        ("Collection Route Optimization", "Explore efficient routes for collection vehicles.", "Data", "High", "Medium"),
    ],
    "Healthcare": [
        ("Telemedicine Access Platform", "Connect remote residents with timely basic medical guidance.", "Technology", "Medium", "High"),
        ("Rural Health Camp Coordination", "Coordinate local health camps and resident outreach.", "Community", "Medium", "High"),
        ("Medicine Availability Monitoring", "Track essential medicine availability at nearby facilities.", "Data", "Medium", "High"),
    ],
    "Education": [
        ("Community Digital Learning Centers", "Create shared spaces for access to digital learning resources.", "Community", "Medium", "High"),
        ("Offline Learning Platform", "Provide curriculum materials that work with limited connectivity.", "Technology", "Medium", "High"),
        ("Teacher-Student Resource Sharing", "Make local teaching resources easier to share and reuse.", "Platform", "Low", "Medium"),
        ("Rural Internet Learning Kiosk", "Explore managed access points for online educational resources.", "Infrastructure", "High", "High"),
    ],
    "Agriculture": [
        ("Crop Advisory Platform", "Share localized crop guidance with smallholder farmers.", "Technology", "Medium", "High"),
        ("Local Weather Alert System", "Deliver timely local weather alerts for farm decisions.", "Technology", "Medium", "High"),
        ("Irrigation Monitoring", "Help identify opportunities to use irrigation resources efficiently.", "Technology", "Medium", "High"),
    ],
    "Environment": [
        ("Community Environmental Reporting", "Enable residents to report local environmental concerns.", "Community", "Low", "Medium"),
        ("Pollution Monitoring Dashboard", "Visualize local pollution observations and trends.", "Data", "Medium", "High"),
        ("Tree Plantation Tracking", "Track community plantation efforts and maintenance needs.", "Platform", "Low", "Medium"),
    ],
}
DEFAULT_SOLUTIONS = [("Community Problem Reporting", "Collect structured local reports to understand the issue and coordinate action.", "Community", "Low", "Medium"), ("Local Data Dashboard", "Make challenge signals visible for informed planning.", "Data", "Medium", "Medium"), ("Pilot Intervention", "Test a small, measurable intervention with community feedback.", "Program", "Medium", "Medium")]

def recommend_solutions(challenge: dict) -> list[dict]:
    """Return curated directions by domain; never calls an external service."""
    templates = SOLUTION_LIBRARY.get(challenge.get("domain"), DEFAULT_SOLUTIONS)
    return [{"id": f"SOL-{index:03d}", "title": title, "description": description, "type": kind, "estimated_complexity": complexity, "potential_impact": impact} for index, (title, description, kind, complexity, impact) in enumerate(templates, 1)]

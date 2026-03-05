import requests
import json
from datetime import datetime

class GovernanceAuditAgent:

    def __init__(self, model="llama3"):
        self.model = model
        self.ollama_url = "http://localhost:11434/api/generate"

    def monitor(
        self,
        candidate,
        role,
        decision,
        fairness_report,
        team_report,
        career_report,
        negotiation_report
    ):
        """
        Monitors all agents and performs governance level audit
        """

        alerts = []

        # -----------------------------
        # Rule Based Governance Checks
        # -----------------------------

        # Fairness Risk Check
        if fairness_report.get("risk_level") == "High":
            alerts.append("Fairness risk detected in hiring decision")

        # Team Compatibility Check
        team_score = team_report.get("team_compatibility_score", 1)

        if team_score < 0.4:
            alerts.append("Low team compatibility may impact team performance")

        # Career Path Check
        skill_gap = career_report.get("skill_gap", [])

        if len(skill_gap) > 5:
            alerts.append("Large skill gap for the role")

        # Negotiation Check
        negotiated_salary = negotiation_report.get("final_salary", 0)

        if negotiated_salary > negotiation_report.get("max_budget", negotiated_salary):
            alerts.append("Negotiated salary exceeds allowed budget")

        # Decision Consistency Check
        if decision["final_score"] > 0.75 and fairness_report.get("risk_level") == "High":
            alerts.append("High candidate score but fairness risk detected")

        # --------------------------------
        # LLM Governance Review (Ollama)
        # --------------------------------

        prompt = f"""
[SYSTEM: GOVERNANCE AUDIT AGENT]

Perform a governance level audit of an autonomous hiring system.

Candidate:
{candidate.candidate_id}

Role:
{role.role_id}

Evaluation Decision:
{json.dumps(decision, indent=2)}

Fairness Report:
{json.dumps(fairness_report, indent=2)}

Team Compatibility:
{json.dumps(team_report, indent=2)}

Career Path:
{json.dumps(career_report, indent=2)}

Negotiation Outcome:
{json.dumps(negotiation_report, indent=2)}

Task:
1. Identify governance risks
2. Detect ethical or fairness concerns
3. Provide overall governance score (0 to 1)
4. Suggest corrective actions

Return result strictly in JSON.
"""

        try:
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "format": "json"
                }
            )

            llm_review = json.loads(response.json()["response"])

        except Exception as e:

            llm_review = {
                "error": f"Ollama connection failed: {str(e)}"
            }

        # --------------------------------
        # Governance Verdict
        # --------------------------------

        compliant = len(alerts) == 0

        return {
            "system_compliant": compliant,
            "governance_risk": "Low" if compliant else "High",
            "alerts": alerts,
            "llm_governance_review": llm_review,
            "timestamp": str(datetime.now())
        }
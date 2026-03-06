import requests
import json

class ExplanationAgent:

    def explain(
        self,
        candidate,
        role,
        decision,
        audit,
        team_compatibility,
        career_growth,
        negotiation,
        governance_report
    ):

        prompt = f"""
You are an HR AI assistant.

Explain the hiring decision clearly and ethically.

Candidate:
Skills: {candidate.skills}
Experience: {candidate.experience_years}
Career Interests: {candidate.career_interests}

Role:
Required Skills: {role.required_skills}
Minimum Experience: {role.min_experience}

Evaluation Decision:
{json.dumps(decision, indent=2)}

Fairness Audit:
{json.dumps(audit, indent=2)}

Team Compatibility:
{json.dumps(team_compatibility, indent=2)}

Career Growth Analysis:
{json.dumps(career_growth, indent=2)}

Negotiation Outcome:
{json.dumps(negotiation, indent=2)}

Governance Report:
{json.dumps(governance_report, indent=2)}

Explain:
1. Why the candidate should or should not be hired
2. Key strengths and weaknesses
3. Any fairness or governance concerns
4. Final recommendation
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]
import requests
import json

class ExplanationAgent:
    def explain(self, candidate, role, decision, audit):
        prompt = f"""
You are an HR AI assistant.

Explain the hiring decision clearly and ethically.

Candidate:
- Skills: {candidate.skills}
- Experience: {candidate.experience_years}
- Career Interests: {candidate.career_interests}

Role:
- Required Skills: {role.required_skills}
- Minimum Experience: {role.min_experience}

Scores:
{json.dumps(decision, indent=2)}

# Fairness Audit:
# {json.dumps(audit, indent=2)}

Explain why this candidate should or should not be shortlisted.
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
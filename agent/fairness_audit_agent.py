import requests
import json
from datetime import datetime 
class FairnessGovernanceAgent:
    def __init__(self, model="llama3"):
        self.model = model
        self.ollama_url = "http://localhost:11434/api/generate"
        
        self.protected_attributes = ["gender", "college", "age", "ethnicity"]

    def audit(self, decision, candidate):
        
        score = decision.get("final_score", 0)
        demographics = candidate.demographics
        
        
        alerts = []
        
        
        if demographics.get("college") == "Tier 1" and decision['scores']['skill_fit'] < 0.5:
            alerts.append("Potential Prestige Bias: High score despite moderate skill fit.")

        
        audit_prompt = f"""
        [SYSTEM: AUDIT AGENT]
        Review the following hiring decision for bias:
        Candidate ID: {candidate.candidate_id}
        Demographics: {json.dumps(demographics)}
        Scores: {json.dumps(decision['scores'])}
        Final Score: {score}

        Task: Identify if any 'Protected Attributes' likely influenced this score. 
        Check if the 'Experience' vs 'Skill' ratio is fair.
        Provide a 'Fairness Rating' (0.0 to 1.0) and a brief 'Mitigation Suggestion'.
        Return strictly in JSON format.
        """

        try:
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model,
                    "prompt": audit_prompt,
                    "stream": False,
                    "format": "json"
                }
            )
            llm_analysis = json.loads(response.json()['response'])
        except Exception as e:
            llm_analysis = {"error": f"Ollama connection failed: {str(e)}"}

       
        is_fair = score >= 0.6 and len(alerts) == 0
        
        return {
            "is_compliant": is_fair,
            "risk_level": "Low" if is_fair else "High",
            "alerts": alerts,
            "llm_audit_summary": llm_analysis,
            "timestamp": str(datetime.now())
        }
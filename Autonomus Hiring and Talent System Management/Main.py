from models.candidate import Candidate
from models.role import Role
from agent.candidate_evaluation_agent import CandidateEvaluationAgent
from agent.fairness_audit_agent import FairnessGovernanceAgent
from agent.explanation_agent import ExplanationAgent


def list_input(msg):
    return [i.strip() for i in input(msg).split(",") if i.strip()]


def main():
    print("\n=== Autonomous Hiring System (Agentic + Ollama) ===\n")

    candidate = Candidate(
        candidate_id=input("Candidate ID: "),
        skills=list_input("Candidate skills: "),
        experience_years=float(input("Years of experience: ")),
        assessments={
            "coding": float(input("Coding score: ")),
            "aptitude": float(input("Aptitude score: "))
        },
        career_interests=list_input("Career interests: "),
        demographics={
            "gender": input("Gender: "),
            "college": input("College tier: ")
        }
    )

    role = Role(
        role_id=input("\nRole ID: "),
        required_skills=list_input("Required skills: "),
        min_experience=float(input("Min experience: ")),
        team_culture=list_input("Team culture: "),
        growth_path=list_input("Growth path: ")
    )

    eval_agent = CandidateEvaluationAgent()
    fairness_agent = FairnessGovernanceAgent()
    explanation_agent = ExplanationAgent()

    decision = eval_agent.evaluate(candidate, role)
    audit = fairness_agent.audit(decision, candidate)
    explanation = explanation_agent.explain(candidate, role, decision,audit)

    print("\n--- FINAL DECISION ---")
    print(decision)

    print("\n--- FAIRNESS AUDIT ---")
    print(audit)

    print("\n--- AI EXPLANATION (OLLAMA) ---")
    print(explanation)


if __name__ == "__main__":
    main()
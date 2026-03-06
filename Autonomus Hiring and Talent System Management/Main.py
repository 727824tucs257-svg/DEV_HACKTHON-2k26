from models.candidate import Candidate
from models.role import Role

from agent.candidate_evaluation_agent import CandidateEvaluationAgent
from agent.fairness_audit_agent import FairnessGovernanceAgent
from agent.explanation_agent import ExplanationAgent
from agent.team_compatibility_agent import TeamCompatibilityAgent
from agent.career_growth_agent import CareerGrowthAgent
from agent.negotiation_agent import NegotiationAgent
from agent.Governance_and_audit_agent import GovernanceAuditAgent
from agent.Orchestrator_agent import HiringOrchestratorAgent


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

    expected_salary = float(input("\nCandidate expected salary: "))
    budget_min = float(input("Role minimum budget: "))
    budget_max = float(input("Role maximum budget: "))

    eval_agent = CandidateEvaluationAgent()
    fairness_agent = FairnessGovernanceAgent()
    team_compatibility_agent = TeamCompatibilityAgent()
    career_growth_agent = CareerGrowthAgent()
    negotiation_agent = NegotiationAgent()
    governance_and_audit_agent = GovernanceAuditAgent()
    explanation_agent = ExplanationAgent()

    agents = {
        "evaluation": eval_agent,
        "fairness": fairness_agent,
        "team": team_compatibility_agent,
        "career": career_growth_agent,
        "negotiation": negotiation_agent,
        "governance": governance_and_audit_agent,
        "explanation": explanation_agent
    }

  
    orchestrator = HiringOrchestratorAgent(agents)

    result = orchestrator.run(
        candidate,
        role,
        expected_salary,
        budget_min,
        budget_max
    )

    print("\n=== AUTONOMOUS HIRING RESULT ===")

    for key, value in result.items():
        print(f"\n--- {key.upper()} ---")
        print(value)


if __name__ == "__main__":
    main()
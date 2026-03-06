from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from models.candidate import Candidate
from models.role import Role

from agent.candidate_evaluation_agent import CandidateEvaluationAgent
from agent.fairness_audit_agent import FairnessGovernanceAgent
from agent.team_compatibility_agent import TeamCompatibilityAgent
from agent.career_growth_agent import CareerGrowthAgent
from agent.negotiation_agent import NegotiationAgent
from agent.Governance_and_audit_agent import GovernanceAuditAgent
from agent.explanation_agent import ExplanationAgent
from agent.Orchestrator_agent import HiringOrchestratorAgent


app = FastAPI(title="Autonomous Hiring System API")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request Schema
class HiringRequest(BaseModel):

    candidate_id: str
    skills: List[str]
    experience_years: float
    coding: float
    aptitude: float
    career_interests: List[str]
    gender: str
    college: str

    role_id: str
    required_skills: List[str]
    min_experience: float
    team_culture: List[str]
    growth_path: List[str]

    expected_salary: float
    budget_min: float
    budget_max: float



eval_agent = CandidateEvaluationAgent()
fairness_agent = FairnessGovernanceAgent()
team_agent = TeamCompatibilityAgent()
career_agent = CareerGrowthAgent()
negotiation_agent = NegotiationAgent()
governance_agent = GovernanceAuditAgent()
explanation_agent = ExplanationAgent()



orchestrator = HiringOrchestratorAgent({
    "evaluation": eval_agent,
    "fairness": fairness_agent,
    "team": team_agent,
    "career": career_agent,
    "negotiation": negotiation_agent,
    "governance": governance_agent,
    "explanation": explanation_agent
})


@app.post("/run-hiring-agent")
def run_hiring_agent(data: HiringRequest):

    candidate = Candidate(
        candidate_id=data.candidate_id,
        skills=data.skills,
        experience_years=data.experience_years,
        assessments={
            "coding": data.coding,
            "aptitude": data.aptitude
        },
        career_interests=data.career_interests,
        demographics={
            "gender": data.gender,
            "college": data.college
        }
    )

    role = Role(
        role_id=data.role_id,
        required_skills=data.required_skills,
        min_experience=data.min_experience,
        team_culture=data.team_culture,
        growth_path=data.growth_path
    )

    result = orchestrator.run(
        candidate,
        role,
        data.expected_salary,
        data.budget_min,
        data.budget_max
    )

    return result
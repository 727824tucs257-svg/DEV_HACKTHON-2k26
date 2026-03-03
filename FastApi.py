from fastapi import APIRouter
from agent.candidate_evaluation_agent import CandidateEvaluationAgent
from models.candidate import Candidate
from models.role import Role

router = APIRouter()
eval_agent = CandidateEvaluationAgent()

@router.post("/evaluate")
def evaluate_candidate(candidate: Candidate, role: Role):
    result = eval_agent.evaluate(candidate, role)
    return result

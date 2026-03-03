from langchain.tools import tool
from agent.candidate_evaluation_agent import CandidateEvaluationAgent
from models.candidate import Candidate
from models.role import Role

@tool
def evaluate_candidate(candidate_data:dict,role_data:dict)->dict:
    """
    Evaluation candidate sustainbility for a role using a objective criteria.
    """
    candidate=Candidate(**candidate_data)
    role=Role(**role_data)
    agent= CandidateEvaluationAgent()
    decision=agent.evaluate(candidate,role)
    return decision
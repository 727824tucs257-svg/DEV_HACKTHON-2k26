import requests
import json

class HiringOrchestratorAgent:

    def __init__(self, agents):
        self.agents = agents
        self.completed = []

    def ask_llm_next_step(self, state):

        prompt = f"""
You are an AI orchestrator for an autonomous hiring system.

Agents available:
1. evaluation
2. fairness
3. team
4. career
5. negotiation
6. governance
7. explanation

Completed agents:
{self.completed}

Current state:
{json.dumps(state, indent=2)}

Which agent should run next?

Return ONLY the agent name.
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"].strip().lower()

    def run(self, candidate, role, expected_salary, budget_min, budget_max):

        state = {}
        finished = False

        while not finished:

            next_agent = self.ask_llm_next_step(state)

            print("\nOrchestrator chose:", next_agent)

            if next_agent == "evaluation":
                state["decision"] = self.agents["evaluation"].evaluate(candidate, role)

            elif next_agent == "fairness":
                state["audit"] = self.agents["fairness"].audit(state["decision"], candidate)

            elif next_agent == "team":
                state["team"] = self.agents["team"].evaluate(candidate, role)

            elif next_agent == "career":
                state["career"] = self.agents["career"].evaluate(candidate, role)

            elif next_agent == "negotiation":
                state["negotiation"] = self.agents["negotiation"].calculate_offer(
                    state["decision"], expected_salary, budget_min, budget_max
                )

            elif next_agent == "governance":
                state["governance"] = self.agents["governance"].monitor(
                    candidate,
                    role,
                    state.get("decision"),
                    state.get("audit"),
                    state.get("team"),
                    state.get("career"),
                    state.get("negotiation"),
                )

            elif next_agent == "explanation":
                state["explanation"] = self.agents["explanation"].explain(
                    candidate,
                    role,
                    state.get("decision"),
                    state.get("audit"),
                    state.get("team_compatibility"),
                    state.get("career_growth"),
                    state.get("negotiation"),
                    state.get("governance_report")
                )
                finished = True

            self.completed.append(next_agent)

        return state
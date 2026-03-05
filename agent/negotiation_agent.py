class NegotiationAgent:
    def __init__(self):
        # No LLM initialization needed here anymore
        pass

    def _calculate_base_offer(self, final_score, budget_min, budget_max):
        """
        Calculates an offer scaled by the candidate's evaluation score.
        """
        score = max(0.0, min(final_score, 1.0))
        offer = budget_min + (budget_max - budget_min) * score
        return round(offer, 2)

    def calculate_offer(self, decision, expected_salary, budget_min, budget_max):
        """
        Determines the approved offer amount and the internal negotiation stance.
        Does NOT generate text.
        """
        score = decision.get("final_score", 0)
        calculated_offer = self._calculate_base_offer(score, budget_min, budget_max)
        
        if calculated_offer >= expected_salary:
            stance = "Match or exceed expectation. Enthusiastic offer."
            final_offer = max(expected_salary, budget_min)
        else:
            stance = "Below expectation. Requires tactful negotiation and justification."
            final_offer = calculated_offer

        return {
            "expected_salary": expected_salary,
            "approved_offer": final_offer,
            "budget_min": budget_min,
            "budget_max": budget_max,
            "negotiation_stance": stance
        }
import numpy as np

class CandidateEvaluationAgent:
    def __init__(self):
        self.weights = {
            "skill_fit": 0.35,
            "experience": 0.25,
            "assessment": 0.20,
            "growth_alignment": 0.15,
            "team_compatibility": 0.05
        }

    def _normalize(self, items):
        return [i.lower().strip() for i in items]

    def skill_match_score(self, candidate, role):
        c = set(self._normalize(candidate.skills))
        r = set(self._normalize(role.required_skills))
        return len(c & r) / max(len(r), 1)

    def experience_score(self, candidate, role):
        return min(candidate.experience_years / role.min_experience, 1.0)

    def assessment_score(self, candidate):
        return np.mean(list(candidate.assessments.values())) / 100

    def growth_alignment_score(self, candidate, role):
        c = set(self._normalize(candidate.career_interests))
        r = set(self._normalize(role.growth_path))
        return len(c & r) / max(len(r), 1)

    def team_compatibility_score(self, candidate, role):
        return 0.8  # placeholder

    def evaluate(self, candidate, role):
        scores = {
            "skill_fit": float(self.skill_match_score(candidate, role)),
            "experience": float(self.experience_score(candidate, role)),
            "assessment": float(self.assessment_score(candidate)),
            "growth_alignment": float(self.growth_alignment_score(candidate, role)),
            "team_compatibility": float(self.team_compatibility_score(candidate, role))
        }

        final_score = float(
            sum(self.weights[k] * scores[k] for k in scores)
        )

        return {
            "final_score": round(final_score, 3),
            "scores": scores
        }
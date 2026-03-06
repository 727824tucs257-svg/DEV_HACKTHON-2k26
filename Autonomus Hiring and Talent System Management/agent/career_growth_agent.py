class CareerGrowthAgent:

    def evaluate(self, candidate, role):

        match = len(set(candidate.career_interests) & set(role.growth_path))
        total = len(role.growth_path)

        score = match / total if total > 0 else 0

        if score >= 0.7:
            alignment = "Strong"
        elif score >= 0.4:
            alignment = "Moderate"
        else:
            alignment = "Weak"

        return {
            "career_alignment_score": round(score, 2),
            "alignment_level": alignment,
            "matching_paths": list(set(candidate.career_interests) & set(role.growth_path))
        }
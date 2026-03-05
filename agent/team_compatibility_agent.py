class TeamCompatibilityAgent:

    def evaluate(self, candidate, role):

    
        match = len(set(candidate.career_interests) & set(role.team_culture))
        total = len(role.team_culture)

        score = match / total if total > 0 else 0

        if score >= 0.7:
            level = "High"
        elif score >= 0.4:
            level = "Moderate"
        else:
            level = "Low"

        return {
            "team_compatibility_score": round(score, 2),
            "team_fit_level": level,
            "matched_attributes": list(set(candidate.career_interests) & set(role.team_culture))
        }

import React, { useState } from "react";
import axios from "axios";
import "./CandidateForm.css";
import { TypeAnimation } from "react-type-animation";

function CandidateForm() {

  const [formData, setFormData] = useState({
    candidate_id: "",
    skills: "",
    experience_years: "",
    coding: "",
    aptitude: "",
    career_interests: "",
    gender: "",
    college: "",

    role_id: "",
    required_skills: "",
    min_experience: "",
    team_culture: "",
    growth_path: "",

    expected_salary: "",
    budget_min: "",
    budget_max: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      candidate_id: formData.candidate_id,
      skills: formData.skills.split(",").map(s => s.trim()),
      experience_years: Number(formData.experience_years),
      coding: Number(formData.coding),
      aptitude: Number(formData.aptitude),
      career_interests: formData.career_interests.split(",").map(s => s.trim()),
      gender: formData.gender,
      college: formData.college,

      role_id: formData.role_id,
      required_skills: formData.required_skills.split(",").map(s => s.trim()),
      min_experience: Number(formData.min_experience),
      team_culture: formData.team_culture.split(",").map(s => s.trim()),
      growth_path: formData.growth_path.split(",").map(s => s.trim()),

      expected_salary: Number(formData.expected_salary),
      budget_min: Number(formData.budget_min),
      budget_max: Number(formData.budget_max)
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/run-hiring-agent",
        payload
      );

      setResult(response.data);
    } catch (error) {
      console.error("API Error:", error);
    }
  };
  const parseAIResponse = (text) => {
    if (!text) return {};
  
    const sections = {};
    const regex = /\*\*(.*?)\*\*([\s\S]*?)(?=\*\*|$)/g;
    let match;
  
    while ((match = regex.exec(text)) !== null) {
      const title = match[1].trim();
      const content = match[2].trim();
      sections[title] = content;
    }
  
    return sections;
  };
  return (
    <div className="container">

      <h1>Autonomous Hiring System</h1>

      <form onSubmit={handleSubmit} className="form-card">

        <h2>Candidate Details</h2>

        <input name="candidate_id" placeholder="Candidate ID" onChange={handleChange} />
        <input name="skills" placeholder="Skills (comma separated)" onChange={handleChange} />
        <input name="experience_years" placeholder="Experience Years" onChange={handleChange} />
        <input name="coding" placeholder="Coding Score" onChange={handleChange} />
        <input name="aptitude" placeholder="Aptitude Score" onChange={handleChange} />
        <input name="career_interests" placeholder="Career Interests" onChange={handleChange} />
        <input name="gender" placeholder="Gender" onChange={handleChange} />
        <input name="college" placeholder="College Tier" onChange={handleChange} />

        <h2>Role Details</h2>

        <input name="role_id" placeholder="Role ID" onChange={handleChange} />
        <input name="required_skills" placeholder="Required Skills" onChange={handleChange} />
        <input name="min_experience" placeholder="Min Experience" onChange={handleChange} />
        <input name="team_culture" placeholder="Team Culture" onChange={handleChange} />
        <input name="growth_path" placeholder="Growth Path" onChange={handleChange} />

        <h2>Salary</h2>

        <input name="expected_salary" placeholder="Expected Salary" onChange={handleChange} />
        <input name="budget_min" placeholder="Budget Min" onChange={handleChange} />
        <input name="budget_max" placeholder="Budget Max" onChange={handleChange} />

        <button type="submit">Run Hiring Agent</button>

      </form>

      {result && (
  <div className="results">

    <h2>Hiring Analysis Result</h2>

    <div className="card">
      <h3>Final Hiring Score</h3>
      <h1>{(result.decision.final_score * 100).toFixed(1)}%</h1>
    </div>

    <div className="grid">

      <div className="card">
        <h3>Skill Fit</h3>
        <p>{(result.decision.scores.skill_fit * 100).toFixed(1)}%</p>
      </div>

      <div className="card">
        <h3>Experience</h3>
        <p>{(result.decision.scores.experience * 100).toFixed(1)}%</p>
      </div>

      <div className="card">
        <h3>Assessment Score</h3>
        <p>{(result.decision.scores.assessment * 100).toFixed(1)}%</p>
      </div>

      <div className="card">
        <h3>Career Alignment</h3>
        <p>{(result.career.career_alignment_score * 100).toFixed(1)}%</p>
      </div>

    </div>

    <div className="card">
      <h3>Fairness Audit</h3>
      <p><b>Risk Level:</b> {result.audit.risk_level}</p>
      <p><b>Fairness Rating:</b> {result.audit.llm_audit_summary.fairness_rating}</p>
      <p><b>Suggestion:</b> {result.audit.llm_audit_summary.mitigation_suggestion}</p>
    </div>

    <div className="card">
      <h3>Team Compatibility</h3>
      <p><b>Fit Level:</b> {result.team.team_fit_level}</p>
    </div>

    <div className="card">
      <h3>Career Growth Alignment</h3>
      <p>{result.career.matching_paths.join(", ")}</p>
    </div>

    <div className="card">
      <h3>Salary Negotiation</h3>
      <p><b>Expected:</b> ₹{result.negotiation.expected_salary}</p>
      <p><b>Approved Offer:</b> ₹{result.negotiation.approved_offer}</p>
      <p><b>Decision:</b> {result.negotiation.negotiation_stance}</p>
    </div>

    <div className="card explanation">
  <h3>AI Hiring Explanation</h3>

  {Object.entries(parseAIResponse(result.explanation)).map(
    ([title, content], index) => (
      <div key={index} style={{ marginBottom: "15px" }}>
        <h4>{title}</h4>
        <p style={{ whiteSpace: "pre-line" }}>{content}</p>
      </div>
    )
  )}
</div>
 

  </div>
)}

    </div>
  );
}

export default CandidateForm;
function ResultsPanel({results}){

    if(!results) return null
    
    return(
    
    <div>
    
    <h2>Decision</h2>
    <pre>{JSON.stringify(results.decision,null,2)}</pre>
    
    <h2>Fairness Audit</h2>
    <pre>{JSON.stringify(results.audit,null,2)}</pre>
    
    <h2>Team Compatibility</h2>
    <pre>{JSON.stringify(results.team_compatibility,null,2)}</pre>
    
    <h2>Career Growth</h2>
    <pre>{JSON.stringify(results.career_growth,null,2)}</pre>
    
    <h2>Negotiation</h2>
    <pre>{JSON.stringify(results.negotiation,null,2)}</pre>
    
    <h2>Governance</h2>
    <pre>{JSON.stringify(results.governance_report,null,2)}</pre>
    
    <h2>AI Explanation</h2>
    <p>{results.explanation}</p>
    
    </div>
    
    )
    
    }
    
    export default ResultsPanel
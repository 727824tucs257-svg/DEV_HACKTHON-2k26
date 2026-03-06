import CandidateForm from "./components/CandidateForm";
import ResultsPanel from "./components/ResultsPanel";
import { useState } from "react";

function App(){

const [results,setResults]=useState(null)

return(

<div className="container">
<div className="card">

  <h1 className="title">AI Hiring Agent-AETHER</h1>

  <CandidateForm />

</div>
</div>

)

}

export default App
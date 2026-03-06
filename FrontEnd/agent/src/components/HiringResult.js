import { parseAIResponse } from "../utils/parseAIResponse";

function HiringResult({ response }) {

  const sections = parseAIResponse(response);

  return (
    <div>

      {Object.entries(sections).map(([title, content], index) => (
        <div key={index} style={{marginBottom:"20px"}}>
          <h3>{title}</h3>
          <p>{content}</p>
        </div>
      ))}

    </div>
  );
}

export default HiringResult;
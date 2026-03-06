export function parseAIResponse(text) {
    const sections = {};
  
    const regex = /\*\*(.*?)\*\*([\s\S]*?)(?=\*\*|$)/g;
    let match;
  
    while ((match = regex.exec(text)) !== null) {
      const title = match[1].trim();
      const content = match[2].trim();
      sections[title] = content;
    }
  
    return sections;
  }
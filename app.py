import os
import gradio as gr
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

APP_TITLE = "AI-Powered Emergency Incident Reporting Assistant"

PROMPT = ChatPromptTemplate.from_template("""
You are an Industrial Safety Incident Analyst working for a large industrial facility.

Your task is to analyze the employee's incident description and convert it into a professional
and concise safety report.

INCIDENT DESCRIPTION:
{incident_description}

Analyze the incident using only the information provided.

Return the response using EXACTLY these six fields:

1. Incident Category:
   Identify the most appropriate category, such as Slip/Fall, Equipment Failure, Fire,
   Chemical Exposure, Electrical, Workplace Injury, Unsafe Condition, or Other.

2. Severity Level:
   Select exactly one:
   Low / Medium / High / Critical

3. Short Incident Summary:
   Provide a concise professional summary of what happened.

4. Possible Immediate Risk:
   Identify the immediate safety risk that may exist.

5. Recommended Immediate Action:
   Recommend practical immediate safety actions.

6. Management Note:
   Provide a brief professional note for management.

CONSTRAINTS:
- Do not invent facts that are not present in the incident description.
- Do not assume injuries, damage, causes, or circumstances that were not stated.
- If information is missing, explicitly state "Not specified in the report."
- Keep the response professional, factual and concise.
- Safety must be prioritized.
- Return all six fields even if some information is unavailable.
""")

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not configured. Add it as an environment variable "
            "or as a Hugging Face Space Secret."
        )

    return ChatGroq(
        model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
        temperature=0.1,
        max_tokens=1024,
        api_key=api_key,
    )

def analyze_incident(incident_description):
    if not incident_description or not incident_description.strip():
        return "Please enter an incident description."

    try:
        llm = get_llm()
        chain = PROMPT | llm
        response = chain.invoke({
            "incident_description": incident_description.strip()
        })
        return response.content
    except Exception as exc:
        return f"Unable to analyze the incident. Error: {exc}"

CUSTOM_CSS = """
body {
    background: #f4f7fb !important;
    color: #1f2937 !important;
    font-family: 'Inter', 'Segoe UI', Arial, sans-serif !important;
}

.gradio-container {
    max-width: 1200px !important;
    margin: 30px auto !important;
    background: #ffffff !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 18px !important;
    box-shadow: 0 10px 35px rgba(15, 23, 42, 0.08) !important;
    overflow: hidden !important;
}

h1.gradio-header {
    background: #ffffff !important;
    color: #163b65 !important;
    padding: 30px 25px 12px !important;
    font-size: 2.2rem !important;
    font-weight: 750 !important;
    text-align: center !important;
    border: none !important;
    margin: 0 !important;
}

p.gradio-description {
    background: #ffffff !important;
    color: #64748b !important;
    font-size: 1rem !important;
    line-height: 1.6 !important;
    text-align: center !important;
    padding: 5px 30px 30px !important;
    margin: 0 !important;
}

.gr-block {
    border: none !important;
}

.gr-box {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 14px !important;
}

.gr-label {
    color: #334155 !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
}

.gr-textbox textarea,
.gr-textarea textarea,
.gr-textbox input,
.gr-textarea input {
    background: #f8fafc !important;
    color: #1e293b !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 12px !important;
    padding: 15px !important;
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
    transition: all 0.25s ease !important;
}

.gr-textbox textarea:focus,
.gr-textarea textarea:focus,
.gr-textbox input:focus,
.gr-textarea input:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
    background: #ffffff !important;
}

.gr-textbox textarea::placeholder,
.gr-textarea textarea::placeholder {
    color: #94a3b8 !important;
}

.gr-button {
    background: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px 26px !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 10px rgba(37, 99, 235, 0.20) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease !important;
}

.gr-button:hover {
    background: #1d4ed8 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 7px 16px rgba(37, 99, 235, 0.25) !important;
}

.gr-button:active {
    transform: translateY(0) !important;
}

.gr-markdown,
.output-markdown {
    background: #ffffff !important;
    color: #334155 !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 14px !important;
    padding: 24px !important;
    line-height: 1.7 !important;
    font-size: 0.95rem !important;
}

.output-markdown h1,
.output-markdown h2,
.output-markdown h3 {
    color: #163b65 !important;
    font-weight: 750 !important;
    margin-top: 20px !important;
}

.output-markdown p,
.output-markdown li {
    color: #475569 !important;
}

.output-markdown li {
    margin-bottom: 6px !important;
}

@media (max-width: 768px) {
    .gradio-container {
        margin: 10px !important;
        border-radius: 12px !important;
    }

    h1.gradio-header {
        font-size: 1.65rem !important;
        padding: 22px 15px 10px !important;
    }

    p.gradio-description {
        font-size: 0.9rem !important;
        padding: 5px 20px 20px !important;
    }

    .gr-textbox textarea {
        min-height: 180px !important;
    }
}
"""

demo = gr.Interface(
    fn=analyze_incident,
    inputs=gr.Textbox(
        lines=8,
        placeholder=(
            "Describe the workplace incident here...\n\n"
            "Example: During the night shift, an employee observed smoke and sparks "
            "coming from an electrical control panel in the production area."
        ),
        label="Incident Description",
    ),
    outputs=gr.Markdown(label="Safety Incident Report"),
    title=APP_TITLE,
    description=(
        "Describe the workplace incident in your own words. "
        "The AI will analyze the event and generate a structured, "
        "professional safety incident report."
    ),
    submit_btn="Analyse Incident",
    clear_btn="Clear",
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="slate",
        neutral_hue="slate",
    ),
    css=CUSTOM_CSS,
)

if __name__ == "__main__":
    demo.launch()

# AI-Powered Emergency Incident Reporting Assistant

An AI-powered workplace safety assistant that converts an employee's free-text incident description into a concise, structured safety incident report.

## Features

- Industrial safety incident analysis
- Six-field structured report:
  1. Incident Category
  2. Severity Level
  3. Short Incident Summary
  4. Possible Immediate Risk
  5. Recommended Immediate Action
  6. Management Note
- LangChain `ChatPromptTemplate`
- Groq-hosted LLM
- Professional Gradio web interface
- Responsive light UI
- Designed for deployment on Hugging Face Spaces

## Architecture

Employee Incident Description
→ LangChain ChatPromptTemplate
→ Groq LLM
→ Structured Safety Report
→ Gradio Interface

## Local Setup

### 1. Clone/download the project

```bash
git clone <your-repository-url>
cd ai-emergency-incident-reporting-assistant
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API key

Windows PowerShell:

```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

macOS/Linux:

```bash
export GROQ_API_KEY="your_groq_api_key"
```

Optional model override:

```bash
export GROQ_MODEL="openai/gpt-oss-120b"
```

The application defaults to `openai/gpt-oss-120b`.

### 5. Run

```bash
python app.py
```

Then open the local Gradio URL shown in the terminal.

## Hugging Face Spaces Deployment

Create a new **Gradio Space** and upload:

- `app.py`
- `requirements.txt`
- `README.md`

Then add your API key under:

**Space Settings → Secrets and variables → Secrets**

Create:

```text
GROQ_API_KEY = your_groq_api_key
```

Do **not** hard-code the API key in `app.py`.

The optional model variable can also be added:

```text
GROQ_MODEL = openai/gpt-oss-120b
```

## Example Incident

Input:

> During the night shift, an employee reported seeing smoke coming from an electrical control panel in the production area. Sparks were visible and employees were working nearby. No injuries have been reported.

The application generates a professional safety assessment containing the incident category, severity, summary, immediate risk, recommended action, and management note.

## Safety Note

This application is an AI-assisted reporting tool. Its output should support—not replace—qualified safety personnel, emergency procedures, and organizational safety protocols.

## Project Files

```text
ai-emergency-incident-reporting-assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── emergency_incident_reporting_assistant.ipynb
```

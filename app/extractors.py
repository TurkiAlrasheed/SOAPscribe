import requests
import os

OLLAMA_URL = os.getenv("OLLAMA_HOST", "http://localhost:11434")


def extract_with_llama(transcript):
    prompt = f"""
You are a strict AI assistant helping doctors extract accurate SOAP notes from patient transcripts. You MUST follow the exact instructions below. If you break any rule, your output will be rejected.

---

📌 Format your output ONLY as JSON with these 4 fields:
{{
  "subjective": "...",
  "objective": "...",
  "assessment": "...",
  "plan": "..."
}}

---

🧠 STRICT EXTRACTION RULES — READ CAREFULLY:

• Subjective: Extract only what the PATIENT verbally says (e.g., symptoms, history, allergies, medications, social/family history). Do NOT invent or assume anything not said.

• Objective: Only extract what the DOCTOR says about exam findings, vital signs, labs, or imaging. If no exam or vitals are mentioned, write "not documented".

• Assessment: Only write diagnoses that the DOCTOR explicitly says. If no diagnosis is mentioned, write "not documented". NEVER write possible, likely, suggests, or any inference.

• Plan: Only write what the DOCTOR clearly says about medications, tests, instructions, follow-up, or education. If nothing is said, write "not documented". Do NOT generate a plan based on symptoms.

---

⚠️ If any section is not mentioned by the doctor, you MUST write exactly:
  "not documented"

❌ NEVER guess, infer, or write what you think should happen.
❌ NEVER write "may be", "suggests", or "recommend" unless those exact words are used by the doctor.
✅ You are doing strict extraction, NOT diagnosis.

---

✅ Example output (for a transcript with no doctor info):

Transcript:
\"\"\"
Doctor: What brings you in today?  
Patient: I've had a sore throat and cough for 3 days.  
Doctor: Any fever?  
Patient: Just a mild one.
\"\"\"

Correct output:
{{
  "subjective": "Patient reports sore throat, cough, and mild fever for 3 days.",
  "objective": "not documented",
  "assessment": "not documented",
  "plan": "not documented"
}}

---

📤 Begin your output below as valid JSON only. Do not include any other text.

Transcript:
\"\"\"
{transcript}
\"\"\"
"""

    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "llama3:8b",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        content = response.json().get("response", "")

        # Extract dictionary from text (you can make this safer with regex or ast)
        if "{" in content:
            result = content[content.index("{") : content.rindex("}") + 1]
            return eval(result)  # replace with ast.literal_eval() if security matters

    except Exception as e:
        print("❌ llama failed:", e)

    return None
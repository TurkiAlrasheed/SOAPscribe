import requests

def extract_with_mistral(transcript):
    prompt = f"""You are a medical assistant. Extract a SOAP note from this transcript.

Transcript:
{transcript}

Return the output as a Python dictionary like this:
{{
  "subjective": "...",
  "objective": "...",
  "assessment": "...",
  "plan": "..."
}}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
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
        print("❌ Mistral failed:", e)

    return None
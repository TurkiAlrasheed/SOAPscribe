import yagmail
from dotenv import load_dotenv
import os

load_dotenv()

sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
receiver = os.getenv("EMAIL_RECEIVER")


yag = None
if sender and password:
    yag = yagmail.SMTP(sender, password)

def notify_doctor(patient_id, soap):
    if not yag:
        return
    missing_sections = []

    for section in ['subjective', 'objective', 'assessment', 'plan']:
        value = soap.get(section, "").strip().lower()
        if not value or "not documented" in value or "missing" in value:
            missing_sections.append(section.capitalize())

    if not missing_sections:
        return  # nothing to notify

    msg_lines = [f"Note for patient ID {patient_id} has missing sections:"]
    for section in missing_sections:
        msg_lines.append(f"- {section}")
    msg_lines.append("\nPlease review the transcript or complete the SOAP note.")
    body = "\n".join(msg_lines)

    yag.send(
        to=receiver,
        subject=f"SOAPscribe Alert: Missing SOAP Fields for Patient {patient_id}",
        contents=body
    )

def generate_soap_note(info):
    return f"""
S: {info['subjective']}

O: {info['objective']}

A: {info['assessment']}

P: {info['plan']}
""".strip()
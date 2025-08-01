import yagmail

def needs_clarification(soap):
    s = soap.get("subjective", "").strip().lower()
    o = soap.get("objective", "").strip().lower()

    return (
        not s or "not documented" in s or "missing" in s,
        not o or "not documented" in o or "missing" in o
    )

yag = yagmail.SMTP("your_email@gmail.com", "your_app_password")

def notify_doctor(patient_id, missing_subjective, missing_objective):
    msg_lines = [f"Note for patient ID {patient_id} has missing sections:"]
    if missing_subjective:
        msg_lines.append("- Subjective")
    if missing_objective:
        msg_lines.append("- Objective")
    msg_lines.append("\nPlease review the transcript or complete the SOAP note.")
    body = "\n".join(msg_lines)

    yag.send(
        to="doctor_email@example.com",
        subject=f"AutoNote Alert: Missing SOAP Fields for Patient {patient_id}",
        contents=body
    )
import os
from getpass import getpass

def prompt_env_var(var_name, prompt_text, hidden=False):
    return getpass(f"{prompt_text}: ") if hidden else input(f"{prompt_text}: ")

print("🛠️ First-time setup: Let's configure your email notification settings.")

email = prompt_env_var("EMAIL_ADDRESS", "Enter your Gmail address")
password = prompt_env_var("EMAIL_PASSWORD", "Enter your Gmail app password", hidden=True)
doctor_email = prompt_env_var("EMAIL_RECEIVER", "Enter the reciever's email")

with open(".env", "w") as f:
    f.write(f"EMAIL_ADDRESS={email}\n")
    f.write(f"EMAIL_PASSWORD={password}\n")
    f.write(f"DOCTOR_EMAIL={doctor_email}\n")

print("✅ Email credentials and doctor email saved to .env")
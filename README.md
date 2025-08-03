# SOAPscribe

SOAPscribe is an AI agent that monitors a folder for new patient-doctor transcript `.txt` files and automatically extracts a structured **SOAP note** using the `llama3:8b` language model via [Ollama](https://ollama.com/). If any essential sections like Subjective or \*\*Objective are missing, AutoNote sends an email alert to the doctor.

---

## First-Time Setup (One-Time Only)

> This will download the model (~4GB), install dependencies, and start watching for transcripts.

1. **Install Docker** (if not already):

   - [Mac & Windows (Docker Desktop)](https://www.docker.com/products/docker-desktop/)

2. **Clone the repo**:

   ```bash
   git clone https://github.com/TurkiAlrasheed/SOAPscribe.git

   ```

3. **(Optional) Enable Email Alerts**

   If you want the app to email you when a SOAP section is missing:

   - Enable 2-Step Verification on your Google account:  
     https://myaccount.google.com/security
   - Generate an App Password:  
     https://myaccount.google.com/apppasswords
   - From the same location where you cloned the repo (e.g., `~/Desktop`), run:

     ```bash
     python3 SOAPscribe/app/setup_email.py
     ```

   - Enter the requsted information

   This will securely save your email settings to a `.env` file.

4. docker compose up --build

---

## Running the App Again (After Setup)

Once the initial setup is complete, running the app is much faster:

```bash
docker compose up
```

---

## How to Use

1. Drop a `.txt` file inside the following folder:

   ```
   app/transcripts/
   ```

2. The app will automatically:

   - Parse the transcript
   - Generate a SOAP note in the generated_notes folder
   - Save it as JSON in notes_db folder:
   - Send an email to the doctor if any section is missing

---

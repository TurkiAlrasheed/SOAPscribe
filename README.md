# SOAPscribe

SOAPscribe is an AI agent that monitors a folder for new patient-doctor transcript `.txt` files and automatically extracts a structured **SOAP note** using the `llama3:8b` language model via [Ollama](https://ollama.com/). If any essential sections like Subjective or **Objective are missing, AutoNote sends an email alert to the doctor.

---

## Features

- Extracts structured SOAP notes from raw conversation text
- Sends email alerts for incomplete notes
- Saves both formatted note and structured JSON to disk
- Fully containerized with Docker Compose
- Also works from terminal using Python + Ollama CLI

---

## Setup
> This will download the model (~4GB), install dependencies, and start watching for transcripts.

1. **Install Docker** (if not already):

   - [Mac & Windows (Docker Desktop)](https://www.docker.com/products/docker-desktop/)
    
2. **Clone the repo**:

   ```bash
   git clone https://github.com/TurkiAlrasheed/SOAPscribe.git
   
3. docker compose up --build

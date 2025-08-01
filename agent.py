import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from note_templates import generate_soap_note
from extractors import extract_with_mistral
import json

TRANSCRIPTS_DIR = "transcripts"
NOTES_DIR = "generated_notes"
DB_DIR = "notes_db"

class TranscriptHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".txt"):
            return
        print(f"New transcript detected: {event.src_path}")
        process_transcript(event.src_path)

def process_transcript(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Simulated extraction
    extracted_info = extract_with_mistral(content)

    # Generate SOAP note text
    note_text = generate_soap_note(extracted_info)

    # Save to .txt
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    note_path = os.path.join(NOTES_DIR, f"{base_filename}_note.txt")
    with open(note_path, 'w') as f:
        f.write(note_text)
    print(f"SOAP note saved to: {note_path}")

    # Save structured JSON to mock EMR db
    db_record = extracted_info.copy()
    db_record["patient_id"] = base_filename
    db_record["flags"] = []
    if "No vitals" in extracted_info["objective"]:
        db_record["flags"].append("Vitals missing")

    db_path = os.path.join(DB_DIR, f"{base_filename}.json")
    with open(db_path, 'w') as f:
        json.dump(db_record, f, indent=2)
    print(f"Structured data saved to: {db_path}")

if __name__ == "__main__":
    print(f"Monitoring {TRANSCRIPTS_DIR} for new transcripts...")
    event_handler = TranscriptHandler()
    observer = Observer()
    observer.schedule(event_handler, TRANSCRIPTS_DIR, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
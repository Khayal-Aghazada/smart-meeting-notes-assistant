from dotenv import load_dotenv
load_dotenv()
import os, time, requests
import re

API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
if not API_KEY:
    raise RuntimeError("AssemblyAI API key not found. Please set ASSEMBLYAI_API_KEY.")

BASE_URL = "https://api.assemblyai.com/v2"
HEADERS = {
    "authorization": API_KEY,
    "content-type": "application/json"
}

def transcribe_and_summarize(audio_file):
    upload = requests.post(
        f"{BASE_URL}/upload",
        headers={"authorization": API_KEY},
        data=audio_file.read()
    )
    if not upload.ok:
        raise RuntimeError(f"Upload failed ({upload.status_code}): {upload.text}")
    audio_url = upload.json().get("upload_url")

    payload = {
    "audio_url": audio_url,
    "summarization": True,
    "summary_model": "informative",
    "summary_type": "bullets"
}
    req = requests.post(f"{BASE_URL}/transcript", json=payload, headers=HEADERS)
    if not req.ok:
        raise RuntimeError(f"Transcript request failed ({req.status_code}): {req.text}")
    transcript_id = req.json().get("id")

    while True:
        poll = requests.get(f"{BASE_URL}/transcript/{transcript_id}", headers=HEADERS)
        if not poll.ok:
            raise RuntimeError(f"Polling failed ({poll.status_code}): {poll.text}")
        data = poll.json()
        status = data.get("status")
        if status == "completed":
            break
        if status == "error":
            raise RuntimeError("Transcription error: " + data.get("error", "Unknown"))
        time.sleep(3)

    # 4) Return transcript + summary
    return {
        "text": data.get("text", ""),
        "summary": data.get("summary", "")
    }




def extract_action_items(transcript_text):
    sentences = re.split(r'(?<=[.!?]) +', transcript_text)
    items = []
    for s in sentences:
        if re.search(r"\b(will|should|need to|please|assign)\b", s, re.IGNORECASE):
            items.append("• " + s.strip())
    return "\n".join(items) or "• _No obvious action items found._"

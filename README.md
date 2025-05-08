# Smart Meeting Notes Assistant

A Streamlit app that converts meeting audio into a transcript, generates an informative bullet-point summary, and extracts action items—without large model downloads or OpenAI billing. It leverages AssemblyAI’s free-tier speech-to-text and built-in summarization.

---

## 🚀 Features

- **Audio Upload:** Accept MP3, WAV, or M4A files via a simple web interface  
- **Transcription:** Uses AssemblyAI API (5 hr free per month) to generate text  
- **Summarization:** AssemblyAI’s built-in “informative” bullet-point summaries  
- **Action-Item Extraction:** Local regex scans for task-like verbs (e.g. “will”, “need to”)  
- **Zero Large Downloads:** No local model weights; all processing via AssemblyAI  

---

## 📦 Technology Stack

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Transcription & Summaries:** [AssemblyAI API](https://www.assemblyai.com/)  
- **Backend Utilities:** `requests`, `python-dotenv`  
- **Language:** Python 3.8+  

---

## 🔧 Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Khayal-Aghazada/smart-meeting-notes-assistant.git
   cd smart-meeting-notes-assistant
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your AssemblyAI API key**  
   Create a file named `.env` in the project root with:  
   ```dotenv
   ASSEMBLYAI_API_KEY=sk-YourAssemblyAIKeyHere
   ```

---

## ▶️ Running the App Locally

```bash
streamlit run app.py
```

- After the server starts, open the URL printed in the console (typically [http://localhost:8501](http://localhost:8501)).  
- Upload your meeting audio file and view the transcript, summary, and action items.

---

## 📁 Project Structure

```
smart-meeting-notes-assistant/
├── app.py                  # Streamlit UI & orchestrator
├── ai_utils.py             # AssemblyAI transcription & summarization helpers
├── requirements.txt        # Python dependencies
└── .env                    # (not committed) AssemblyAI API key
```

---

## 🛠️ Customization

- **Summary Style:** In `ai_utils.py`, change `"summary_model": "informative"` to `"catchy"` or `"conversational"`.  
- **Action-Item Logic:** Edit the regex in `extract_action_items()` to recognize your preferred task indicators.  
- **Deployment:**  
  - **Streamlit Cloud:** Push to GitHub, connect your repository, add `ASSEMBLYAI_API_KEY` as a secret, and deploy.  
  - **Docker (optional):** Add a `Dockerfile` that copies code, installs dependencies, sets up `.env`, and exposes port 8501.

---

## 🤝 Contributing

1. Fork the repo  
2. Create a branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m "feat: describe your feature"`)  
4. Push to your branch (`git push origin feature/your-feature`)  
5. Open a Pull Request and describe your changes

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

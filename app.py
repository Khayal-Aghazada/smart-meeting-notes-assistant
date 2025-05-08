

import streamlit as st
from ai_utils import transcribe_and_summarize, extract_action_items

st.set_page_config(page_title="Smart Meeting Notes", layout="wide")
st.title("🧠 Smart Meeting Notes — AssemblyAI Summaries Only")

uploaded = st.file_uploader("Upload audio (MP3/WAV)", type=["mp3","wav","m4a"])
if uploaded:
    try:
        with st.spinner("Processing…"):
            result = transcribe_and_summarize(uploaded)
    except Exception as e:
        st.error(f"🚨 AssemblyAI error:\n{e}")
    else:
        st.subheader("📄 Transcript")
        st.write(result["text"])

        st.subheader("🧾 AI-Generated Summary")
        st.write(result["summary"])

        st.subheader("✅ Extracted Action Items")
        st.text(extract_action_items(result["text"]))

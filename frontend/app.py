import streamlit as st
import requests

# -----------------------------
# CONFIG
# -----------------------------
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="InsightTube", layout="wide")

# -----------------------------
# SESSION STATE
# -----------------------------
if "processed" not in st.session_state:
    st.session_state.processed = False

if "summary" not in st.session_state:
    st.session_state.summary = {}

if "notes" not in st.session_state:
    st.session_state.notes = {}

if "translation" not in st.session_state:
    st.session_state.translation = None

# -----------------------------
# HEADER
# -----------------------------
st.title("🎥 InsightTube")
st.write("AI-powered YouTube Video Intelligence")

# -----------------------------
# INPUT SECTION
# -----------------------------
url = st.text_input("🔗 Enter YouTube URL")

if st.button("🚀 Process Video"):
    if url:
        with st.spinner("Processing video..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/process-video",
                    json={"url": url}
                )
                if response.status_code == 200:
                    st.session_state.processed = True
                    st.success("✅ Video processed successfully!")
                else:
                    st.error("❌ Failed to process video")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a URL")

# -----------------------------
# MAIN FEATURES
# -----------------------------
if st.session_state.processed:
# if True:

    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Summary",
        "📝 Notes",
        "🌐 Translate",
        "📥 Export"
    ])

    # -------------------------
    # SUMMARY TAB
    # -------------------------
    with tab1:
        st.subheader("Generate Summary")

        option = st.selectbox(
            "Choose summary type",
            ["Short", "Detailed", "Key Takeaways"]
        )

        if st.button("Generate Summary"):
            with st.spinner("Generating summary..."):
                response = requests.post(
                    f"{BACKEND_URL}/summary",
                    json={"type": option}
                )
                if response.status_code == 200:
                    result = response.json().get("result")
                    st.session_state.summary[option] = result

        if option in st.session_state.summary:
            st.write(st.session_state.summary[option])

    # -------------------------
    # NOTES TAB
    # -------------------------
    with tab2:
        st.subheader("Generate Notes")

        note_type = st.selectbox(
            "Choose notes type",
            ["Study Notes", "Revision Notes", "Quiz", "Flashcards"]
        )

        if st.button("Generate Notes"):
            with st.spinner("Generating notes..."):
                response = requests.post(
                    f"{BACKEND_URL}/notes",
                    json={"type": note_type}
                )
                if response.status_code == 200:
                    result = response.json().get("result")
                    st.session_state.notes[note_type] = result

        if note_type in st.session_state.notes:
            st.write(st.session_state.notes[note_type])

    # -------------------------
    # TRANSLATE TAB
    # -------------------------
    with tab3:
        st.subheader("Translate Transcript")

        if st.button("Translate Hindi → English"):
            with st.spinner("Translating..."):
                response = requests.post(f"{BACKEND_URL}/translate")
                if response.status_code == 200:
                    st.session_state.translation = response.json().get("result")

        if st.session_state.translation:
            st.write(st.session_state.translation)

    # -------------------------
    # EXPORT TAB
    # -------------------------
    with tab4:
        st.subheader("Export PDF")

        if st.button("Generate PDF"):
            with st.spinner("Generating PDF..."):
                response = requests.post(f"{BACKEND_URL}/generate-pdf")
                if response.status_code == 200:
                    st.success("PDF generated!")

                    st.download_button(
                        label="📥 Download PDF",
                        data=response.content,
                        file_name="summary.pdf",
                        mime="application/pdf"
                    )

# -----------------------------
# SIDEBAR CHATBOT
# -----------------------------
st.sidebar.title("🤖 Chatbot")

query = st.sidebar.text_input("Ask about the video")

if st.sidebar.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={"query": query}
            )
            if response.status_code == 200:
                data = response.json()
                st.sidebar.write(f"📍 {data.get('timestamp')}")
                st.sidebar.write(data.get("answer"))
    else:
        st.sidebar.warning("Enter a question")
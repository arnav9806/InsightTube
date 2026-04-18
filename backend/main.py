from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.services.video_service import process_video_pipeline
# -----------------------------
# APP INIT
# -----------------------------
app = FastAPI(
    title="InsightTube API",
    description="Backend for InsightTube (RAG-based YouTube AI system)",
    version="1.0.0"
)

print("🚀 InsightTube Backend Starting...")

# -----------------------------
# CORS CONFIGURATION
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("✅ CORS Middleware Enabled")

# -----------------------------
# ROOT ROUTE
# -----------------------------
@app.get("/")
def root():
    print("📌 Root endpoint hit")
    return {
        "message": "InsightTube Backend is Running 🚀"
    }

# -----------------------------
# PROCESS VIDEO
# -----------------------------
@app.post("/process-video")
def process_video(request: dict):
    print("\n📥 /process-video API called")

    url = request.get("url")
    print(f"🔗 Received URL: {url}")

    # Validate input
    if not url:
        print("❌ No URL provided")
        return {
            "status": "error",
            "message": "URL is required"
        }

    try:
        print("⚙️ Starting full video processing pipeline...")

        # 🔥 Call actual pipeline
        process_video_pipeline(url)

        print("🎉 Video processed successfully")

        return {
            "status": "success",
            "message": "Video processed and stored in vector DB"
        }

    except Exception as e:
        print(f"❌ Error during processing: {e}")

        return {
            "status": "error",
            "message": str(e)
        }

# -----------------------------
# SUMMARY
# -----------------------------
@app.post("/summary")
def get_summary(request: dict):
    print("\n📥 /summary API called")

    summary_type = request.get("type")
    print(f"📝 Summary type: {summary_type}")

    result = f"{summary_type} summary will be generated here..."

    print("✅ Summary generated")

    return {
        "status": "success",
        "result": result
    }

# -----------------------------
# NOTES
# -----------------------------
@app.post("/notes")
def get_notes(request: dict):
    print("\n📥 /notes API called")

    note_type = request.get("type")
    print(f"🧠 Notes type: {note_type}")

    result = f"{note_type} notes will be generated here..."

    print("✅ Notes generated")

    return {
        "status": "success",
        "result": result
    }

# -----------------------------
# TRANSLATE
# -----------------------------
@app.post("/translate")
def translate():
    print("\n📥 /translate API called")

    print("🌐 Translating transcript...")

    result = "Translated transcript will appear here..."

    print("✅ Translation completed")

    return {
        "status": "success",
        "result": result
    }

# -----------------------------
# CHAT (RAG Placeholder)
# -----------------------------
@app.post("/chat")
def chat(request: dict):
    print("\n📥 /chat API called")

    query = request.get("query")
    print(f"💬 User query: {query}")

    answer = f"Answer for: {query}"
    timestamp = "02:15"

    print("🧠 Generating answer using RAG (dummy)")
    print(f"📍 Timestamp: {timestamp}")

    print("✅ Response sent")

    return {
        "status": "success",
        "answer": answer,
        "timestamp": timestamp
    }

# -----------------------------
# GENERATE PDF
# -----------------------------
@app.post("/generate-pdf")
def generate_pdf():
    print("\n📥 /generate-pdf API called")

    print("📄 Generating PDF...")

    print("✅ PDF generated")

    return {
        "status": "success",
        "message": "PDF generated successfully"
    }
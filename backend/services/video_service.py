from youtube_transcript_api import YouTubeTranscriptApi
from backend.rag.chunking import chunk_transcript
from backend.rag.vector_store import add_documents


def extract_video_id(url: str) -> str:
    """
    Extract video ID from YouTube URL
    """
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be" in url:
        return url.split("/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")


def get_transcript(url: str):
    print("\n🎥 Fetching transcript...")

    video_id = extract_video_id(url)
    print(f"📌 Video ID: {video_id}")

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Step 1: Try manually created transcript
        try:
            print("🔍 Trying manually created transcript...")
            transcript_obj = transcript_list.find_manually_created_transcript(['en', 'hi'])
            print(f"✅ Found manual transcript: {transcript_obj.language}")

        except:
            print("⚠️ No manual transcript, trying generated...")

            # Step 2: fallback to generated transcript
            transcript_obj = transcript_list.find_generated_transcript(['en', 'hi'])
            print(f"✅ Found generated transcript: {transcript_obj.language}")

        # Step 3: fetch transcript
        transcript = transcript_obj.fetch()

        # Format transcript
        formatted = [
            {
                "text": entry["text"],
                "start": entry["start"],
                "end": entry["start"] + entry["duration"],
            }
            for entry in transcript
        ]

        print(f"✅ Total entries: {len(formatted)}")

        return formatted

    except Exception as e:
        print(f"❌ Final error fetching transcript: {e}")

        raise Exception(
            "Transcript could not be fetched. Try another video with subtitles."
        )

def process_video_pipeline(url: str):
    print("\n🚀 Starting video processing pipeline...")

    transcript = get_transcript(url)

    chunks = chunk_transcript(transcript)

    add_documents(chunks)

    print("🎉 Video processing completed!")

    return True
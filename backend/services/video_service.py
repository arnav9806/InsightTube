from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
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
    
# def get_transcript(url: str):
#     print("\n Fetching transcript...")

#     video_id = extract_video_id(url)
#     print(f" Video ID: {video_id}")

#     try:
#         #  Create API instance (NEW WAY)
#         ytt_api = YouTubeTranscriptApi()

#         print(" Trying direct fetch (auto language)...")

#         fetched = ytt_api.fetch(video_id)

#         print(f" Transcript fetched: {fetched.language}")

#         transcript_data = fetched.to_raw_data()

#     except TranscriptsDisabled:
#         print(" Captions are disabled")
#         raise Exception("No captions available for this video")

#     except Exception as e:
#         print(f" Direct fetch failed: {e}")

#         #  FALLBACK METHOD
#         try:
#             print(" Trying fallback with language priority...")

#             ytt_api = YouTubeTranscriptApi()

#             fetched = ytt_api.fetch(video_id, languages=["en", "hi"])

#             print(f" Fallback worked: {fetched.language}")

#             transcript_data = fetched.to_raw_data()

#         except Exception as e2:
#             print(f" All transcript methods failed: {e2}")

#             raise Exception(
#                 "Transcript could not be fetched. Try another video with captions."
#             )

#     #  FORMAT (for your pipeline)
#     formatted = [
#         {
#             "text": entry["text"],
#             "start": entry["start"],
#             "end": entry["start"] + entry["duration"],
#         }
#         for entry in transcript_data
#     ]

#     print(f" Total entries: {len(formatted)}")

#     #  PRINT SAMPLE (clean)
#     print("\n SAMPLE TRANSCRIPT (first 10 lines):\n")
#     for entry in formatted[:10]:
#         print(f"{entry['start']:.2f}s → {entry['text']}")

#     #  SAVE FULL TRANSCRIPT TO FILE
#     print("\n Saving full transcript to file...")

#     with open("transcript.txt", "w", encoding="utf-8") as f:
#         for entry in formatted:
#             f.write(f"{entry['start']:.2f}s → {entry['text']}\n")

#     print(" Transcript saved as transcript.txt")

#     return formatted

def get_transcript(url: str):
    print("\n Fetching transcript...")

    video_id = extract_video_id(url)
    print(f" Video ID: {video_id}")

    try:
        #  Create API instance (NEW WAY)
        ytt_api = YouTubeTranscriptApi()

        print(" Trying direct fetch (auto language)...")

        #  BEST METHOD (auto-selects best transcript)
        fetched = ytt_api.fetch(video_id)

        print(f" Transcript fetched: {fetched.language}")

        # Convert to raw list
        transcript_data = fetched.to_raw_data()

    except TranscriptsDisabled:
        print(" Captions are disabled")
        raise Exception("No captions available for this video")

    except Exception as e:
        print(f" Direct fetch failed: {e}")

        #  FALLBACK METHOD
        try:
            print(" Trying fallback with language priority...")

            ytt_api = YouTubeTranscriptApi()

            # Try English → then Hindi
            fetched = ytt_api.fetch(video_id, languages=["en", "hi"])

            print(f" Fallback worked: {fetched.language}")

            transcript_data = fetched.to_raw_data()

        except Exception as e2:
            print(f" All transcript methods failed: {e2}")

            raise Exception(
                "Transcript could not be fetched. Try another video with captions."
            )

    #  FORMAT (for your pipeline)
    formatted = [
        {
            "text": entry["text"],
            "start": entry["start"],
            "end": entry["start"] + entry["duration"],
        }
        for entry in transcript_data
    ]

    print(f" Total entries: {len(formatted)}")

    return formatted

def process_video_pipeline(url: str):
    print("\n Starting video processing pipeline...")

    transcript = get_transcript(url)

    chunks = chunk_transcript(transcript)

    add_documents(chunks)

    print(" Video processing completed!")

    return True
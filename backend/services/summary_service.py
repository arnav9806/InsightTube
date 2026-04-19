from backend.chains.summary_chain import generate_summary
from backend.rag.vector_store import documents


def get_sorted_transcript():
    """
    Get full transcript in correct order
    """
    if not documents:
        raise Exception("No transcript found. Process a video first.")

    # Sort by timestamp (VERY IMPORTANT)
    sorted_docs = sorted(documents, key=lambda x: x["start"])

    return sorted_docs


def map_reduce_summary(chunks, summary_type):
    """
    Handle long transcripts safely
    """
    partial_summaries = []

    for chunk in chunks:
        summary = generate_summary(chunk["text"], summary_type)
        partial_summaries.append(summary)

    combined = " ".join(partial_summaries)

    # Final summary
    final_summary = generate_summary(combined, summary_type)

    return final_summary


def generate_video_summary(summary_type="short"):
    print("\n📝 Generating summary...")

    chunks = get_sorted_transcript()

    # If small transcript → direct
    if len(chunks) < 5:
        full_text = " ".join([c["text"] for c in chunks])
        return generate_summary(full_text, summary_type)

    # If large → map-reduce
    return map_reduce_summary(chunks, summary_type)
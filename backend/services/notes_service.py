from backend.chains.notes_chain import generate_notes
from backend.services.summary_service import get_sorted_transcript


def map_reduce_notes(chunks, notes_type):
    partial_notes = []

    for chunk in chunks:
        notes = generate_notes(chunk["text"], notes_type)
        partial_notes.append(notes)

    combined = " ".join(partial_notes)

    # Final refinement
    final_notes = generate_notes(combined, notes_type)

    return final_notes


def generate_video_notes(notes_type="study_notes"):
    print("\n📚 Generating notes...")

    chunks = get_sorted_transcript()

    # Small transcript → direct
    if len(chunks) < 5:
        full_text = " ".join([c["text"] for c in chunks])
        return generate_notes(full_text, notes_type)

    # Large transcript → map-reduce
    return map_reduce_notes(chunks, notes_type)
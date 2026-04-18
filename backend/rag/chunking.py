def chunk_transcript(transcript, chunk_size=500, overlap=100):
    """
    Break transcript into smaller pieces (chunks)

    transcript: list of {text, start, end}
    chunk_size: max length of text in one chunk
    overlap: how much text to repeat in next chunk
    """

    print("\n✂️ Chunking started...")

    chunks = []
    current_text = ""
    start_time = 0

    for entry in transcript:
        text = entry["text"]

        # If starting new chunk, save start time
        if current_text == "":
            start_time = entry["start"]

        # Add text to current chunk
        current_text += " " + text

        # If chunk is big enough → save it
        if len(current_text) >= chunk_size:
            chunk = {
                "text": current_text.strip(),
                "start": start_time,
                "end": entry["end"]
            }

            chunks.append(chunk)

            print(f"✅ Chunk added ({len(chunks)})")

            # Keep last part (overlap) for next chunk
            current_text = current_text[-overlap:]

    # Add last chunk if anything left
    if current_text.strip() != "":
        chunk = {
            "text": current_text.strip(),
            "start": start_time,
            "end": transcript[-1]["end"]
        }

        chunks.append(chunk)
        print("✅ Final chunk added")

    print(f"🎯 Total chunks: {len(chunks)}")

    return chunks
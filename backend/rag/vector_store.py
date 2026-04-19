import faiss
import numpy as np
from backend.rag.embeddings import get_embedding

print("🔄 Initializing vector database...")

# MiniLM embedding size = 384
dimension = 384

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Store actual text + metadata
documents = []

print("✅ Vector DB ready")


def add_documents(chunks):
    """
    Store chunks in vector DB
    """
    print("\n📦 Storing chunks in vector DB...")

    for chunk in chunks:
        text = chunk["text"]

        # Convert text → embedding
        embedding = get_embedding(text)

        # Convert to correct format
        embedding = np.array([embedding]).astype("float32")

        # Add to FAISS
        index.add(embedding)

        # Store text + timestamp
        documents.append({
            "text": text,
            "start": chunk["start"],
            "end": chunk["end"]
        })

    print(f"✅ Stored {len(chunks)} chunks")


def search(query, top_k=3):
    """
    Search similar chunks
    """
    print("\n🔍 Searching in vector DB...")

    # Convert query to embedding
    query_embedding = get_embedding(query)
    query_embedding = np.array([query_embedding]).astype("float32")

    # Search
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in indices[0]:
        results.append(documents[i])

    print(f"✅ Found {len(results)} results")

    return results
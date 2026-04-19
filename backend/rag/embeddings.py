from sentence_transformers import SentenceTransformer

print("🔄 Loading embedding model...")

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

print("✅ Embedding model loaded")


def get_embedding(text):
    """
    Convert text into vector (numbers)
    """
    print("🧠 Generating embedding...")

    embedding = model.encode(text)

    print("✅ Embedding created")

    return embedding
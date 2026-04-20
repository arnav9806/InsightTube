from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

NOTES_PROMPT = PromptTemplate(
    input_variables=["text", "notes_type"],
    template="""
You are an expert educational assistant.

Convert the transcript into {notes_type}.

Types:
- study_notes → detailed structured notes with headings
- revision_notes → concise quick revision points
- quiz → generate questions with answers
- flashcards → generate Q&A pairs for memorization

Transcript:
{text}

Output:
"""
)

def generate_notes(text, notes_type):
    prompt = NOTES_PROMPT.format(text=text, notes_type=notes_type)
    response = llm.invoke(prompt)
    return response.content
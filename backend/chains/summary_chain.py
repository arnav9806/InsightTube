
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")
# print("API KEY:", os.getenv("GROQ_API_KEY"))
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    # temperature=0.3
)

SUMMARY_PROMPT = PromptTemplate(
    input_variables=["text", "summary_type"],
    template="""
You are an expert video summarizer.

Generate a {summary_type} summary of the transcript.

Types:
- short → 5-6 lines
- detailed → full explanation
- key_takeaways → bullet points

Transcript:
{text}

Summary:
"""
)

def generate_summary(text, summary_type):
    prompt = SUMMARY_PROMPT.format(text=text, summary_type=summary_type)

    response = llm.invoke(prompt)

    return response.content
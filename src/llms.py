from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv(override= True)

client = Groq(api_key = os.environ.get("GROQ_API_KEY"))

def qwen_model():
    llm = ChatGroq(
        model="qwen/qwen3-32b",
        temperature=0.2,
        max_retries=3,)
    return llm

def gpt_model():
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.2,
        max_retries=3,)
    return llm

def llama_model():
    llm = ChatGroq(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0.2,
        max_retries=3,)
    return llm


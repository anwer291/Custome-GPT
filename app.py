from fastapi import FastAPI, HTTPException
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Initialize FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Math-Only GPT API!"}

@app.get("/ask")
def ask_math(question: str):
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    # Strict prompt to enforce math-only responses
    strict_prompt = f"""
    You are an AI specialized only in mathematics. You strictly answer only math-related questions, including algebra, calculus, trigonometry, probability, and other mathematical topics. 
    If the question is not related to mathematics, you must reply with exactly: "I only answer math questions."
    
    Question: {question}
    """

    response = model.generate_content(strict_prompt)
    answer = response.text.strip()

    return {"answer": answer}

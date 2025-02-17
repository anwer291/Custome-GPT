import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
st.title("Math-Only GPT")
question = st.text_input("Enter your math question:")

if st.button("Get Answer"):
    if question:
        # Strict prompt to enforce math-only responses
        strict_prompt = f"""
        You are an AI specialized only in mathematics. You strictly answer only math-related questions, including algebra, calculus, trigonometry, probability, and other mathematical topics. 
        If the question is not related to mathematics, you must reply with exactly: "I only answer math questions."
        
        Question: {question}
        """

        response = model.generate_content(strict_prompt)
        answer = response.text.strip()

        # Display the response
        st.success(answer)
    else:
        st.warning("Please enter a math question.")

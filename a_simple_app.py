import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Use the API key from .env

# Initialize the model
llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0, api_key=GROQ_API_KEY)

st.title("Open-Source LLM Demo")

# User input
query = st.text_input("Ask anything:")
if query:
    try:
        # Call the model with user input
        response = llm.invoke(f"User: {query}")
        
        # Access the content of the response
        st.write(response.content)  # Use the .content attribute for the response
    except Exception as e:
        st.error(f"An error occurred: {e}")

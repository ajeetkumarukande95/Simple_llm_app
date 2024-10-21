import streamlit as st
from langchain_groq import ChatGroq
import os
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Use the API key from .env

# Load models from config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Initialize sidebar for model selection
st.sidebar.title("Select Model")

# Create selectboxes for model categories
selected_llama_model = st.sidebar.selectbox("Select a Llama model:", [model['name'] for model in config['models']['llama']])
selected_mistral_model = st.sidebar.selectbox("Select a Mistral model:", [model['name'] for model in config['models']['mistral']])
selected_gemma_model = st.sidebar.selectbox("Select a Gemma model:", [model['name'] for model in config['models']['gemma']])
selected_distil_model = st.sidebar.selectbox("Select a Distil-Whisper model:", [model['name'] for model in config['models']['distil_whisper']])

# Get selected model IDs
selected_model = None
if selected_llama_model:
    selected_model = next(model['id'] for model in config['models']['llama'] if model['name'] == selected_llama_model)
elif selected_mistral_model:
    selected_model = next(model['id'] for model in config['models']['mistral'] if model['name'] == selected_mistral_model)
elif selected_gemma_model:
    selected_model = next(model['id'] for model in config['models']['gemma'] if model['name'] == selected_gemma_model)
elif selected_distil_model:
    selected_model = next(model['id'] for model in config['models']['distil_whisper'] if model['name'] == selected_distil_model)

# Initialize the model if a model is selected
if selected_model:
    llm = ChatGroq(model=selected_model, temperature=0, api_key=GROQ_API_KEY)
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
else:
    st.sidebar.warning("Please select a model to proceed.")

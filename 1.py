import streamlit as st
import requests
import json

# Your Gemini API key (hardcoded for now)
API_KEY = "AIzaSyBhqXGiQRyPPkcG2uL-zNdwNdTSGStonGo"  # Replace this with your actual API key
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Function to call the Gemini API
def generate_gemini_content(prompt):
    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    params = {
        "key": API_KEY  # Your Gemini API Key
    }

    try:
        response = requests.post(URL, headers=headers, params=params, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Print the full response for debugging purposes
        response_data = response.json()
        
        # Extract the generated text from the response
        generated_text = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", None)
        if generated_text:
            return generated_text
        else:
            return "No text returned from the API."
        
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit UI
st.title("New Skill Generator and Assistant")

# Input field for skill to learn
skill = st.text_input("Enter the skill you want to learn:")

# Button to trigger skill development path generation
if st.button("Generate Skill Development Path"):
    if skill:
        with st.spinner("Generating skill development path..."):
            generated_content = generate_gemini_content(skill)
            st.success(f"Skill: {skill}")
            st.write(f"Generated Skill Development Path: {generated_content}")
    else:
        st.error("Please enter a skill.")

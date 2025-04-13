import streamlit as st
import requests
import json

API_KEY = "AIzaSyBhqXGiQRyPPkcG2uL-zNdwNdTSGStonGo"
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

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
        "key": API_KEY
    }

    try:
        response = requests.post(URL, headers=headers, params=params, json=data)
        response.raise_for_status()
        response_data = response.json()
        generated_text = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", None)
        if generated_text:
            return generated_text
        else:
            return "No text returned from the API."
        
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

st.title("New Skill Generator and Assistant")

skill = st.text_input("Enter the skill you want to learn:")

if st.button("Generate Skill Development Path"):
    if skill:
        with st.spinner("Generating skill development path..."):
            generated_content = generate_gemini_content(skill)
            st.success(f"Skill: {skill}")
            st.write(f"Generated Skill Development Path: {generated_content}")
    else:
        st.error("Please enter a skill.")

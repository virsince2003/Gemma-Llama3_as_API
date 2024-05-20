import requests
import streamlit as st

def call_llama3(input: str) -> str:
    url = "http://localhost:8000/llama3/invoke"
    payload = {
        "input": {
            "topic": input
        }
    }
    print(payload)
    response = requests.post(url, json=payload)
    return response.json()["output"]


def call_gemma(input: str) -> str:
    url = "http://localhost:8000/gemma/invoke"
    payload = {
        "input": {
            "topic": input
        }
    }
    response = requests.post(url, json=payload)
    return response.json()["output"]


st.title("Langchain API")
llama3_input = st.text_input("Enter a topic and get a response from the llama3 API")
gemma_input = st.text_input("Enter a topic and get a response from the Gemma API")

if llama3_input:
    st.write(call_llama3(llama3_input))

if gemma_input:
    st.write(call_gemma(gemma_input))
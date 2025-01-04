import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from backend import ask
# from env import *
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("key")
sys_prompt = os.getenv("sys_prompt")
user_prompt = os.getenv("user_prompt")
model = os.getenv("model")

def load_image(image_url):
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

def generate_llm_response(input_text):
    # write actual code to generate a response
    return f"LLM response to your input: {input_text}"

st.title("AI-Powered Doctor Assistant")
image_url = st.text_input("Enter image URL:")

if image_url:
    img = load_image(image_url)
    if img:
        fixed_width = 200
        st.image(img,width=fixed_width)

    user_input = st.text_input("Ask something related to the image:")

    submit_button = st.button("Ask V-LLM")

    if submit_button:
        llm_response = ask(image_url, key, sys_prompt, user_prompt, model, user_input)
        st.write(llm_response)

    # if user_input:
    #     llm_response = generate_llm_response(user_input)
    #     st.write(llm_response)
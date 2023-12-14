
import streamlit as st
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
Imodel = genai.GenerativeModel('gemini-pro-vision')
model = genai.GenerativeModel('gemini-pro')

# Function to generate story and display image
def generate_story(prompt, image):
    if image is not None:
        response = Imodel.generate_content([prompt, image], stream=True)
        response_text = "\n".join(chunk.text for chunk in response)
        st.text(response_text)
    else:
        response = model.generate_content(prompt, stream=True)
        response_text = "\n".join(chunk.text for chunk in response)
        st.text(response_text)
# Streamlit app
def main():
    st.title("Magic Backpack Story Generator")

    prompt = st.text_input("Enter a prompt:")
    image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if image_file:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image.", width = 100)

    else:
        image = None
    if st.button("Generate"):
        generate_story(prompt, image)

if __name__ == "__main__":
    main()

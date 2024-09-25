import streamlit as st
import requests
import json
from PIL import Image
from io import BytesIO

# Set up the page configuration with custom background color
st.set_page_config(
    page_title="Text-to-Image Generator",
    page_icon=":art:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for background color and input box size
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .stTextInput > div > div > input {
            font-size: 18px;
            padding: 10px;
        }
        textarea {
            height: 150px !important;
            font-size: 16px !important;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: black;
            text-align: center;
            padding: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🖼️ Text-to-Image Generator")
st.write("Generate an image from your text description using AI.")

# Input for the text prompt with increased size
user_input = st.text_area("Enter a description for the image:", "", height=150)

# Button to generate image
if st.button("Generate Image"):
    with st.spinner('Generating...'):
        # Your API call
        url = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
        payload = json.dumps({
            "inputs": user_input
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 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'
        }

        response = requests.post(url, headers=headers, data=payload)

        # Check if the response is successful
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, caption=user_input, use_column_width=True)
        else:
            st.error(f"Failed to generate image. Status code: {response.status_code}")

# Footer
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ by Santosh</p>
    </div>
    """, unsafe_allow_html=True)

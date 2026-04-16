from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import streamlit as st
import io

# load env 
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def note_generate(images):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
           images,
           "Summarize the picture in note format at 100 words,make sure to add necessary markdown to differentiate section"
        ]
    )

    return response.text

def audio_transcription(text):
    speech = gTTS(text=text,lang="en",slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(images,difficulty):
    prompt = f"Generate 3 quizes based on the {difficulty} make sure to add markdown to differentiate the options"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
           images,
           prompt
        ]
    )  
    return response.text  
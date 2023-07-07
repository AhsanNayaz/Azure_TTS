import os

import azure.cognitiveservices.speech as speechsdk
import os
import streamlit as st

# Creates an instance of a speech config with specified subscription key and service region.

# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = os.environ["SPEECH_KEY"], os.environ["SPEECH_REGION"]
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.

speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"

# Creates a speech synthesizer using the default speaker as audio output.

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Receives a text from console input.

# print("Type some text that you want to speak...")

# text = input()


# result = speech_synthesizer.speak_text_async(text).get()


st.title("TTS demo")

input_text = st.text_input("enter your text here....")

button = st.button("submit")

if button and input_text:
    result = speech_synthesizer.speak_text_async(input_text).get()

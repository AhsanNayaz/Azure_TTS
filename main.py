import os
import azure.cognitiveservices.speech as speechsdk
import os
import streamlit as st

# Creates an instance of a speech config with specified subscription key and service region.

# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = st.secrets["SPEECH_KEY"], st.secrets["SPEECH_REGION"]
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"

# Creates a speech synthesizer using the default speaker as audio output.
file_name = "outputaudio.wav"
file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)

# Receives a text from console input.

# print("Type some text that you want to speak...")

# text = input()


# result = speech_synthesizer.speak_text_async(text).get()


st.title("TTS demo")

input_text = st.text_input("enter your text here....")

button = st.button("submit")

if button and input_text:
    speech_synthesis_result = speech_synthesizer.speak_text_async(input_text).get()
    #result = speech_synthesizer.speak_text_async(input_text).get()
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(input_text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

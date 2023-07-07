from flask import Flask, request, render_template
import azure.cognitiveservices.speech as speechsdk
import os
# from pydub import AudioSegment
# from pydub.playback import play

speech_key, service_region = os.environ["SPEECH_KEY"], os.environ["SPEECH_REGION"]
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    # If a form is submitted
    if request.method == "POST":
        # Unpickle classifier
        # Get values through input bars
        input_text = request.form.get("name")
        res = speech_synthesizer.speak_text_async(input_text)
        return render_template("index.html", output=res)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

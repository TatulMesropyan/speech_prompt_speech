import os
import platform

import helpers
import subprocess
import speech_to_text as stt
import text_to_speech as tts

client = helpers.get_client()


def open_audio_file(file_path):
    if platform.system() == "Darwin":
        subprocess.run(["open", file_path])
    elif platform.system() == "Windows":
        subprocess.run(["start", "", file_path], shell=True)
    elif platform.system() == "Linux":
        subprocess.run(["xdg-open", file_path])


root_dir = os.path.dirname(os.path.abspath(__file__))
file_name = None
for file in os.listdir(root_dir):
    if file.startswith("speech.") and os.path.isfile(os.path.join(root_dir, file)):
        file_name = file
        break
audio_file_path = os.path.join(root_dir, file_name)
text = stt.speech_to_text(audio_file_path, client)
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=text,
    temperature=1
)
tts.text_to_speech(response.choices[0].text, client)
open_audio_file(os.path.join(root_dir, "output.mp3"))

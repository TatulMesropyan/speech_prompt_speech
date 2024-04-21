import os

import helpers
import speech_to_text as stt
import text_to_speech as tts

client = helpers.get_client()


root_dir = os.path.dirname(os.path.abspath(__file__))
print(root_dir)
file_name = "speech.m4a"
audio_file_path = os.path.join(root_dir, file_name)

text = stt.speech_to_text(audio_file_path, client)

tts.text_to_speech(text, client)

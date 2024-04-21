import os

import helpers
import speech_to_text as stt
import text_to_speech as tts

client = helpers.get_client()


root_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "speech.m4a"
audio_file_path = os.path.join(root_dir, file_name)
text = stt.speech_to_text(audio_file_path, client)
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=text,
  temperature=1
)
tts.text_to_speech(response.choices[0].text, client)

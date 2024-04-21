from openai import OpenAI


def text_to_speech(text, client: OpenAI):
    speech = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )
    speech.stream_to_file("output.mp3")

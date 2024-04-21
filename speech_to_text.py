import io

from openai import OpenAI


def speech_to_text(audio_file_path, client: OpenAI):
    supported_formats = ('.mp3', '.wav', '.ogg', '.mp4', '.mpeg', '.mpga', '.m4a', '.webm')
    if not audio_file_path.endswith(supported_formats):
        return "Invalid format"

    with open(audio_file_path, 'rb') as audio_file:
        audio_content = audio_file.read()

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=io.BytesIO(audio_content),
        response_format="text"
    )
    print(transcription.text)
    return transcription.text

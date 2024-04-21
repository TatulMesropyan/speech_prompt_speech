import io

from openai import OpenAI


def speech_to_text(audio_file_path, client: OpenAI):
    supported_formats = ('flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm')
    if not audio_file_path.endswith(supported_formats):
        return "Invalid format"

    audio_file = open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    return transcription

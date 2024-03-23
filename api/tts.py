import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
organization = os.getenv("OPENAI_ORG_ID")

client = OpenAI(api_key=api_key, organization=organization)

response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input="Listo, he actualizado la lista con los nuevos elementos.",
)

response.stream_to_file("output.mp3")

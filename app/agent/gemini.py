import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("No se encontró GEMINI_API_KEY en el archivo .env")

    return genai.Client(api_key=api_key)


def ask_gemini(prompt):
    client = get_gemini_client()

    print("Enviando solicitud a Gemini...")

    stream = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
        stream=True
    )

    response = ""

    for event in stream:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
                response += event.delta.text

    print()

    return response
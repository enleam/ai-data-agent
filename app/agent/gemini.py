import os
import json

from dotenv import load_dotenv
from google import genai

from app.agent.tools import (
    SALES_SUMMARY_TOOL,
    get_sales_summary
)

load_dotenv()

MODEL = "gemini-3.8-flash"

TOOLS = [SALES_SUMMARY_TOOL]


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "No se encontró GEMINI_API_KEY en el archivo .env"
        )

    return genai.Client(api_key=api_key)


def execute_tool(name):
    if name == "get_sales_summary":
        return get_sales_summary()

    raise ValueError(f"Herramienta desconocida: {name}")


def ask_gemini(prompt):
    client = get_gemini_client()

    interaction = client.interactions.create(
        model=MODEL,
        input=prompt,
        tools=TOOLS
    )

    function_calls = [
        step for step in interaction.steps
        if step.type == "function_call"
    ]

    if not function_calls:
        return interaction.output_text

    function_results = []

    for call in function_calls:
        print(f"Ejecutando herramienta: {call.name}")

        result = execute_tool(call.name)

        function_results.append({
            "type": "function_result",
            "name": call.name,
            "call_id": call.id,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps(
                        result,
                        ensure_ascii=False
                    )
                }
            ]
        })

    final_interaction = client.interactions.create(
        model=MODEL,
        previous_interaction_id=interaction.id,
        input=function_results
    )

    return final_interaction.output_text
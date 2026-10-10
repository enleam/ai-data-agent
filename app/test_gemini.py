from app.agent.gemini import ask_gemini

prompt = "Explica brevemente qué es el análisis de datos."

response = ask_gemini(prompt)

print("\n=== RESPUESTA DE GEMINI ===")
print(response)
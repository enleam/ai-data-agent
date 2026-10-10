from app.agent.gemini import ask_gemini

prompt = """
Analiza las ventas de AdventureWorks.

Indica:
1. El total de órdenes.
2. Las ventas totales.
3. El ticket promedio.

Utiliza la herramienta de consulta de ventas para obtener
los datos reales. Explica brevemente qué significa cada indicador.
"""

response = ask_gemini(prompt)

print("\n=== RESPUESTA DEL AGENTE ===")
print(response)
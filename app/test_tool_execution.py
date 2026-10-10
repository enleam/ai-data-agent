
from app.agent.tools import get_sales_summary

result = get_sales_summary()

print("\n=== RESULTADO DE LA HERRAMIENTA ===")
print(f"Total de órdenes: {result['total_orders']}")
print(f"Ventas totales: ${result['total_sales']:,.2f}")
print(
    f"Ticket promedio: "
    f"${result['average_order_value']:,.2f}"
)
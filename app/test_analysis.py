from app.database import execute_query
from app.queries import GET_SALES_SUMMARY
from app.analysis.sales import calculate_sales_kpis


df = execute_query(GET_SALES_SUMMARY)

kpis = calculate_sales_kpis(df)

print("\n=== KPIs DE VENTAS ===")
print(f"Total de órdenes: {kpis['total_orders']}")
print(f"Ventas totales: ${kpis['total_sales']:,.2f}")
print(f"Ticket promedio: ${kpis['average_order_value']:,.2f}")
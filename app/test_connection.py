from app.database import execute_query
from app.queries import GET_PRODUCTS
from app.analysis.sales import calculate_average_price


df = execute_query(GET_PRODUCTS)

average_price = calculate_average_price(df)

print("\nProductos encontrados:")
print(df)

print(f"\nPrecio promedio: {average_price:.2f}")

from app.database import execute_query
from app.queries import GET_SALES_SUMMARY


SALES_SUMMARY_TOOL = {
    "type": "function",
    "name": "get_sales_summary",
    "description": (
        "Obtiene indicadores generales de ventas de AdventureWorks, "
        "incluyendo total de órdenes, ventas totales y ticket promedio."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}


def get_sales_summary():
    df = execute_query(GET_SALES_SUMMARY)

    if df.empty:
        return {"error": "No se encontraron datos de ventas."}

    row = df.iloc[0]

    return {
        "total_orders": int(row["TotalOrders"]),
        "total_sales": float(row["TotalSales"]),
        "average_order_value": float(row["AverageOrderValue"])
    }

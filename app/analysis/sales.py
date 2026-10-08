def calculate_sales_kpis(df):
    if df.empty:
        raise ValueError("No se encontraron datos para calcular los KPIs.")

    total_orders = int(df["TotalOrders"].iloc[0])
    total_sales = float(df["TotalSales"].iloc[0])
    average_order_value = float(df["AverageOrderValue"].iloc[0])

    return {
        "total_orders": total_orders,
        "total_sales": total_sales,
        "average_order_value": average_order_value
    }
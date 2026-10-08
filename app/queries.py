GET_PRODUCTS = """
SELECT TOP 10
    ProductID,
    Name,
    ListPrice
FROM Production.Product
ORDER BY ListPrice DESC;
"""


GET_CUSTOMERS = """
SELECT TOP 10
    CustomerID,
    PersonID,
    StoreID,
    TerritoryID
FROM Sales.Customer;
"""


GET_SALES_SUMMARY = """
SELECT
    COUNT(*) AS TotalOrders,
    SUM(TotalDue) AS TotalSales,
    AVG(TotalDue) AS AverageOrderValue
FROM Sales.SalesOrderHeader;
"""
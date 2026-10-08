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
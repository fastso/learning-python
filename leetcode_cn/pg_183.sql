SELECT name AS "Customers"
FROM customers
WHERE id not in (SELECT customerid FROM orders);

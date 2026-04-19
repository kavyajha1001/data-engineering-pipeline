-- Total revenue
SELECT SUM(amount) AS total_revenue FROM sales_data;

-- Revenue by city
SELECT city, SUM(amount) AS total
FROM sales_data
GROUP BY city;

-- Top customers
SELECT customer_id, SUM(amount) AS total_spent
FROM sales_data
GROUP BY customer_id
ORDER BY total_spent DESC;
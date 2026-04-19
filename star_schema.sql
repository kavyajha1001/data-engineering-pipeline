-- Fact table
CREATE TABLE sales_fact AS
SELECT order_id, customer_id, amount FROM sales_data;

-- Dimension table
CREATE TABLE customer_dim AS
SELECT DISTINCT customer_id, name, city FROM sales_data;
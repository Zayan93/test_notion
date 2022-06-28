CREATE SCHEMA content;
CREATE TABLE IF NOT EXISTS content.sheets_content (
    id uuid PRIMARY KEY,
    num INT,
    order_number INT,
    price_usd FLOAT,
    price_rub FLOAT,
    delivery_date DATE
);
"""
Loads amazon_sales_2025.csv into a SQLite database (amazon_sales.db)
so that 02_analysis_queries.sql can be run directly in DB Browser for SQLite,
or via this script for verification.
"""
import sqlite3
import pandas as pd

df = pd.read_csv('/home/claude/amazon_sales_project/data/amazon_sales_2025.csv')

conn = sqlite3.connect('/home/claude/amazon_sales_project/data/amazon_sales.db')
df.to_sql('sales', conn, if_exists='replace', index=False)

# quick verification - run query 2 (monthly trend) and query 3 (category revenue)
print("Monthly trend sample:")
print(pd.read_sql("""
    SELECT strftime('%Y-%m', Order_Date) AS year_month, COUNT(*) AS orders, SUM(Net_Amount) AS net_revenue
    FROM sales WHERE Order_Status != 'Cancelled'
    GROUP BY year_month ORDER BY year_month
""", conn))

print("\nCategory revenue:")
print(pd.read_sql("""
    SELECT Category, SUM(Net_Amount) AS net_revenue
    FROM sales WHERE Order_Status != 'Cancelled'
    GROUP BY Category ORDER BY net_revenue DESC
""", conn))

conn.close()
print("\nSaved: data/amazon_sales.db")

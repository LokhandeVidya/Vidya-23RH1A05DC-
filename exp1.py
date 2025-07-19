import pandas as pd
import mysql.connector

# Step 1: Extract
df = pd.read_csv("SuperMarket Analysis.csv")  # Fixed typo: 'read_cvs' ➜ 'read_csv'

# Step 2: Transform
df['Total_price'] = df['Quantity'] * df['Unit price']

# Step 3: Load to MySQL
conn = mysql.connector.connect(
    host="localhost",          # Fixed typo: 'loacalhost' ➜ 'localhost'
    user="root",
    password="",
    database="sales_db"
)
cursor = conn.cursor()

# Use backticks for column names with spaces
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO products (`Product line`, `Quantity`, `Unit price`, `Total_price`)
        VALUES (%s, %s, %s, %s)
    """, (
        row['Product line'],
        int(row['Quantity']),
        float(row['Unit price']),
        float(row['Total_price'])
    ))

conn.commit()
cursor.close()
conn.close()

print("ETL to MySQL completed successfully.")
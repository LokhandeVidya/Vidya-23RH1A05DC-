#Etl.py
import pandas as pd
import mysql.connector
from config import MYSQL_CONFIG 
import schedule
import time
def extract(path="SuperMarket Analysis.csv"):  
    print("Extracting data....")
    return pd.read_csv(path)
def transform(df):
    print("Transforming data....")
    #  Fix typos in column names: 'Quntity' ➜ 'Quantity'
    df['Total_price'] = df['Quantity'] * df['Unit price']
    return df
def load(df):
    print("Loading into MySQL....")
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()
    #  Fixed: cursor.execute should not use = (it was cursor.execute = "...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            `Product line` VARCHAR(255),
            Quantity INT,
            `Unit price` FLOAT,
            Total_price FLOAT
        )
    """)
    conn.commit()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO products(`Product line`, Quantity, `Unit price`, Total_price)
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
    print("Load complete.")
def run_pipeline():
    print("Running pipeline.....")
    df = extract()
    df = transform(df)  # Fix: function name was wrongly written as 'Transform'
    load(df)
#  Schedule section
if __name__ == "__main__":
    schedule.every().day.at("13:53").do(run_pipeline)
    print("Scheduler started. Waiting to run pipeline...")

    while True:
        schedule.run_pending()
        time.sleep(60)

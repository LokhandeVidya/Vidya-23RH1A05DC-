import pandas as pd
from pymongo import MongoClient
import schedule
import time

#mongodb connection setup
MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "sales.db"
COLLECTION_NAME = "products"

def extract(path='sales.csv'):
    print("Extracting data...")
    return pd.read_csv(path)
def trans(df):
    print("Transforming data...")
    df['total_price']=df['quality']*df['unit_price']
    return df
def load(df):
    print("Loading data...")
    client = MongoClient(MONGO_URL)
    db = client(DATABASE_NAME)
    collection = db[COLLECTION_NAME]

##Optional clear collection before insert
##collection.delete_many(())

#convert dataframe to list of dicts
records = df.to_dict(orient='records')

#insert records
    if records:
        collcetion.insert_many[records]
        print(f"inserted {len(records)} records")
    else:
        print("No records to insert.")

    client.close()
    print("Load complete")

def run_pipeline():
    print("Running ETL pipeline....")
    df = extract()
    df = transform()
    load(df)
# ---scheduling section 
if __name__ =="__main__":
    #run every day at 6:37 am
    schedule,every().day.at("06:41").do(run.pipeline)
    print("Scheduler started . Witing to run pipeline......")
    while True:
        schedule.run_pendng()
        time.sleep(60)


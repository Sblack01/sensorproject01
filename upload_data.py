from pymongo.mongo_client import MongoClient
import pandas as pd
import json
import warnings
warnings.filterwarnings("ignore")
#url
uri = "mongodb+srv://kumarsatyam0301_db_user:194700@cluster0.jgjpyyg.mongodb.net/?appName=Cluster0"

#create a new client and connect to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME = "faultdetection"
COLLECTION_NAME = "waferfault"

df = pd.read_csv(r"notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis=1)

json_record = json.loads(df.to_json(orient = "records"))


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

print("DATA is successfully uploaded")
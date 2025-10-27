from pymongo.mongo_client import MongoClient
import panda as pd
import json

#url
uri="mongodb+srv://chandalesaurabh6_db_user:bnZD1O1qLh5HKYra@cluster1.svcvr23.mongodb.net/?appName=Cluster1"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="sensor_fault"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\DELL\Documents\Project_Database\Project_Sensorefault\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
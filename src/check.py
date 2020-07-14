import pymongo
from src.config import DBURL
from src.config import DBURL, DB_NAME
from pymongo import MongoClient

#client = pymongo.MongoClient()
#db = client[ "Antoniopepiapi" ] # makes a test database called "testdb"
#col = db[ "users" ] #makes a collection called "testcol" in the "testdb"

client = pymongo.MongoClient("mongodb://localhost/Antoniopepiapi")
#db = client[ "Antoniopepiapi" ] # makes a test database called "testdb"
db= client.get_database()
col = db[ "users" ] #makes a collection called "testcol" in the "testdb"

#client_text= MongoClient(DBURL)
#print(f"connected to db {DBURL}")

def check_user(name):
    query = {"name":{"$eq":f"{name}"}}
    cur = db.col.find(query)
    data = list(cur)
    if len(data)==0:
        print(len(data))
        return True
    else:
        print(len(data))
        return False

#def messageCollectionExists():
#    return (True, False)["messages" in client.collection_names()]
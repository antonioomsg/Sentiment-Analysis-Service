from src.app import app
from flask import json
import pymongo 
from src.config import DBURL, DB_NAME
from flask import request
from pymongo import MongoClient

db_user = MongoClient(DBURL).get_database(DB_NAME).user

@app.route("/get/users")
def get_user():
    print("Request to get messages from a conversation")
    messagesDb = db_user.find({"name": {"$exits":True}})
    return messagesDb
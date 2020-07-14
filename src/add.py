from pymongo import MongoClient
from flask import request
from src.config import DBURL 
from bson.json_util import dumps
import re

client = MongoClient(DBURL)
db = client.get_database("Antoniopepiapi")#["Antoniopepiapi"]
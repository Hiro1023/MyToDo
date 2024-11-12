# app/db.py
from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://mongodb:27017/")
    return client["your_database_name"]
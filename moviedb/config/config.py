from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["movie_database"]
collection = db["movies"]
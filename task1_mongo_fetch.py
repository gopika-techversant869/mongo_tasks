from pymongo import MongoClient

MONGO_USERNAME = "test"
MONGO_PASSWORD = "Tech%4097"
MONGO_HOST = "localhost"
MONGO_DB = "task_db"

MONGO_URI =  f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONGO_DB}?authSource=admin"

client = MongoClient(MONGO_URI)

db = client["task_db"]
collection = db["tasks"]


doc_to_insert = {
    "name": "Gopika",
    "age": 27,
    "email": "gopika.na@techversantinfotech.com"
}

insert_result = collection.insert_one(doc_to_insert)
print("Inserted ID:", insert_result.inserted_id)

fetched_doc = collection.find_one({"_id": insert_result.inserted_id})
print("Fetched Document:", fetched_doc)

fetch_value = collection.find_one({"email":"gopika.na@techversantinfotech.com"})
print("fetch with emsil",fetch_value)

client.close()

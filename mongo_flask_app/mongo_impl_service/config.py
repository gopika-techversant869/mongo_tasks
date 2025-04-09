class Config:

        MONGO_USERNAME = "test"
        MONGO_PASSWORD = "Tech%4097"
        MONGO_HOST = "localhost"
        MONGO_DB = "task_db"

        MONGO_URI =  f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONGO_DB}?authSource=admin"
from mongo_impl_service.extensions import mongo

class Task(mongo.Document):
    title = mongo.StringField(required=True)
    description = mongo.StringField()
    status = mongo.StringField(choices=["pending", "in_progress", "completed"], default="pending")

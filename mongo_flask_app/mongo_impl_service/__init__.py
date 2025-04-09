import logging
from flask import Flask
from mongo_impl_service.config import Config
from mongo_impl_service.extensions import mongo


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    print("Config Loaded:", app.config["MONGO_URI"])

    
    mongo.init_app(app)

    with app.app_context():
        from mongo_impl_service.routes.task_routes import task_bp
        app.register_blueprint(task_bp, url_prefix="/api/tasks")

    return app

from flask import Blueprint, request, jsonify
from mongo_impl_service.models.task import Task


task_bp = Blueprint("task", __name__)

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    task = Task(
        title=data["title"],
        description=data.get("description", ""),
        status=data.get("status", "pending")
    )
    task.save()
    return jsonify({"message": "Task created", "id": str(task.id)}), 201

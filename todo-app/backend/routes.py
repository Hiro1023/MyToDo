import uuid

# from app import app
from flask import Flask, request, jsonify
from app.models.task_list import TaskList
from app.models.task import Task

from flask import Blueprint

routes = Blueprint("routes", __name__)
tasks = TaskList()


@routes.route("/")
def index():
    return "Hello, World!"


@routes.route("/todos", methods=["GET"])
def getTodos():
    return jsonify(tasks.get_all_tasks())


@routes.route("/todos", methods=["POST"])
def postTask():
    new_task = request.json.get("task")
    description = request.json.get("description")
    result = tasks.add_task(new_task, description)
    if result:
        return jsonify(tasks.get_task_by_taskname(new_task)), 201
    return jsonify({"error": "Task content is required"}), 400


@routes.route("/todos/<id>", methods=["PUT"])
def editTask(id):
    new_task = request.json.get("task")
    description = request.json.get("description")
    updated_task = tasks.edit_task(id, new_task, description)
    if updated_task:
        return jsonify(tasks.get_task(id)), 200
    return jsonify({"error": "Task not found"}), 404


@routes.route("/todos/<id>", methods=["PATCH"])
def updateTask(id):
    if tasks.toggle_task(id):
        return jsonify(tasks.get_task(id)), 201
    return jsonify({"error": "Task is not found"}), 404


@routes.route("/todos/<id>", methods=["DELETE"])
def deleteTask(id):
    if tasks.remove_task(id):
        return jsonify(tasks.get_all_tasks()), 201
    return jsonify({"error": "Task content is not exist"}), 404

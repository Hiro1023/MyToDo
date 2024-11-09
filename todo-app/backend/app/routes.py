import uuid
from app import app
from flask import Flask, request, jsonify
from app.models.task_list import TaskList 
from app.models.task import Task

tasks = TaskList()
tasks.add_task("test1","")
tasks.add_task("test2","Hello, I am test2")
tasks.add_task("test3","Hello, I am test3")


@app.route('/')
def hello():
    return "Hello! This is my first flask test"

@app.route('/todos',methods=['GET'])
def getTodos():
    return jsonify(tasks.get_all_tasks())


@app.route('/todos', methods=['POST'])
def postTask():
    new_task = request.json.get("task")
    description = request.json.get("description")
    if new_task:
        tasks.add_task(new_task, description)
        return jsonify(tasks.get_all_tasks()), 201
    return jsonify({"error": "Task content is required"}), 400

@app.route('/todos/<id>', methods=['PUT'])
def editTask(id):
    new_task = request.json.get("task")
    description = request.json.get("description")
    updated_task = tasks.edit_task(id, new_task, description)
    if updated_task:
        return jsonify(updated_task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404
 

@app.route('/todos/<id>', methods=['PATCH'])
def updateTask(id):
    if tasks.toggle_task(id):
        return jsonify(tasks.get_task(id)), 201
    return jsonify({"error": "Task is not found"}), 404


@app.route('/todos/<id>', methods=['DELETE'])
def deleteTask(id):
    if tasks.remove_task(id) :
        return jsonify(tasks.get_all_tasks()), 201
    return jsonify({"error": "Task content is not exist"}), 404




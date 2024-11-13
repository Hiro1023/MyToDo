from multiprocessing.resource_tracker import getfd
import os
import sys

import logging
from bson import ObjectId
from flask import jsonify
from pymongo import MongoClient
from app.models.task import Task
from app.db import get_db

logging.basicConfig(level=logging.DEBUG)


class TaskList:
    def __init__(self):
        self.db = get_db()
        self.tasks_collection = self.db["tasks"]

    def add_task(self, task, description=""):
        existing_task = self.tasks_collection.find_one({"task": task})
        if existing_task:
           #return jsonify({"error": "Task with the same name already exists"}), 400
            return None

        new_task = Task(task, description)
        self.tasks_collection.insert_one(new_task.to_dict())
        return new_task

    def remove_task(self, task_id):
        object_id = self.convert_to_objectid(task_id)

        # Delete task
        self.tasks_collection.delete_one({"_id": object_id})

        not_existing_task = not self.tasks_collection.find_one({"task": task_id})

        # Verify if delete was successful
        if not_existing_task:
            return True
        else:
            return False

    def toggle_task(self, task_id):
        object_id = self.convert_to_objectid(task_id)
        task = self.tasks_collection.find_one({"_id": object_id})

        if task:
            new_completed_status = not task["completed"]
            self.tasks_collection.find_one_and_update(
                {"_id": object_id}, {"$set": {"completed": new_completed_status}}
            )
            # return updeted task
            updated_task = self.tasks_collection.find_one({"_id": object_id})
            return updated_task
        else:
            return None

    def edit_task(self, task_id, new_task=None, new_description=None):

        object_id = self.convert_to_objectid(task_id)
        task = self.tasks_collection.find_one({"_id": object_id})

        if task:
            if new_task is not None:
                self.tasks_collection.find_one_and_update(
                    {"_id": object_id}, {"$set": {"task": new_task}}
                )
            if new_description is not None:
                self.tasks_collection.find_one_and_update(
                    {"_id": object_id}, {"$set": {"description": new_description}}
                )
            return self.tasks_collection.find_one({"_id": object_id})

        return None

    def get_all_tasks(self):
        tasks = self.tasks_collection.find()
        return [{**task, "_id": str(task["_id"])} for task in tasks]

    def get_task(self, task_id):
        object_id = self.convert_to_objectid(task_id)
        task = self.tasks_collection.find_one({"_id": object_id})
        task["_id"] = str(task["_id"])
        return task
    
    def get_task_by_taskname(self, task_name):
        task = self.tasks_collection.find_one({"task": task_name})
        task["_id"] = str(task["_id"])
        return task

    def convert_to_objectid(self, task_id):
        try:
            return ObjectId(task_id)
        except Exception as e:
            return False

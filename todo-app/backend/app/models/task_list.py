from app.models.task import Task


class TaskList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, description=""):
        new_task = Task(task, description)
        self.tasks[new_task.id] = new_task
        return new_task

    def remove_task(self, task_id):
        if task_id in self.tasks:
            self.tasks.pop(task_id)
            return True
        return False

    def toggle_task(self, task_id):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.toggle_completed()
            return task
        return None

    def edit_task(self, task_id, new_task=None, new_description=None):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if new_task is not None:
                task.task = new_task
            if new_description is not None:
                task.description = new_description
            return task
        return None

    def get_all_tasks(self):
        return [task.to_dict() for task in self.tasks.values()]

    def get_task(self, task_id):
        return self.tasks.get(task_id)

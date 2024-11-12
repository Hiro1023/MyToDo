
class Task:
    def __init__(self, task, description=""):
        self.task = task
        self.completed = False
        self.descriptions = description


    def to_dict(self):
        return {
            "task": self.task,
            "completed": self.completed,
            "descriptions": self.descriptions,
        }

    def toggle_completed(self):
        self.completed = not self.completed

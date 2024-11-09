import uuid


class Task:
    def __init__(self, task, description=""):
        self.id = self.generateID()
        self.task = task
        self.completed = False
        self.descriptions = description

    def generateID(self):
        return str(uuid.uuid4())
    
    def to_dict(self):
        return{
            "id": self.id,
            "task": self.task,
            "completed": self.completed,
            "descriptions": self.descriptions
        }
    
    def toggle_completed(self):
        self.completed = not self.completed
from datetime import timezone, datetime
import uuid

ID = uuid.uuid4().hex


class TaskList:
    def __init__(self):
        self.task = [
            {
                "id": ID,
                "created": datetime.now(timezone.utc),
                "completed": False,
                "task": "A simple flask smorest API"
            }
        ]

    def get_by_id(self, task_id):
        print(task_id, self.task)
        for task in self.task:
            if task["id"] == task_id:
                return task
        raise IndexError

    def update_task(self, task_id, payload):
        task = self.get_by_id(task_id)
        task.update(payload)
        return task

    def get_tasks(self):
        return {"tasks": self.task}

    def save_task(self, task):
        task["id"] = uuid.uuid4().hex
        task["created"] = datetime.now(timezone.utc)
        task["completed"] = False
        self.task.append(task)
        return task

    def delete_task(self, task_id):
        for index, task in enumerate(self.task):
            if task["id"] == task_id:
                self.task.pop(index)
                return
        raise IndexError

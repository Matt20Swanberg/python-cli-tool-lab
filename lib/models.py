"""Models for the task manager CLI"""

class Task:
    """Represent an individual task"""

    def __init__(self, title):
        """Initialize a new incomplete task"""
        self.title = title
        self.completed = False

    def complete(self):
        """Mark the task as completed and display confirmation"""
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

class User:
    """Represent a user and their associated tasks"""

    def __init__(self, name):
        """Initialize a user with an empty task list"""
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Add a task to the user's task list"""
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        """Return the task matching the given title, or None if not found"""
        for task in self.tasks:
            if task.title == title:
                return task
        return None
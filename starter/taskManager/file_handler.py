import json
from Task import Task
def save_tasks(task_list):
   
    try:
        with open("tasks.json", "w") as file:
            tasks_data = []

            for task in task_list:
                tasks_data.append({
                    "title": task.title,
                    "due_date": str(task.due_date) if task.due_date else None,
                    "completed": task.completed
                })

            json.dump(tasks_data, file, separators=(",", ": "))

    except OSError as e:
        print(f"Error saving tasks: {e}")
           
           
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks_data = json.load(file)

            task_list = []

            for task in tasks_data:
                new_task = Task(task["title"], task["due_date"])
                new_task.completed = task["completed"]
                task_list.append(new_task)

            return task_list
    except FileNotFoundError:
        return []

    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return []

    except OSError as e:
        print(f"Error loading tasks: {e}")
        return []
   
            
                  
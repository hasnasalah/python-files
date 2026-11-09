from datetime import datetime
from Task import Task
# add_task(task_list, title, due_date=None): Creates a new Task and adds it to the list.
# If due_date is provided as a string, parse it into a datetime.date 
# (assume format “YYYY-MM-DD”). Use exception handling to catch parsing errors and inform the user.
def addTask(task_list, title,due_date=None):
    parsed_date=None
    if due_date is not None:
        try: 
            parsed_date=datetime.strptime(due_date,"%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format or date value")
            return
    task=Task(title,parsed_date)
    task_list.append(task)

def complete_task(task_list, index):
    try:
        task_list[index].completed = True
        print("Task completed!")
    except IndexError:
        print("Invalid task index.")
def delete_task(task_list, index):
    try:
        task_list.pop(index)
        print("Task deleted!")
    except IndexError:
        print("Invalid task index.")

def list_tasks(task_list):
    for task in task_list:
        print(task)
        
            
        
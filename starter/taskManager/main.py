
import todolist
import file_handler
task_list=file_handler.load_tasks()
while True:
    print("(A) Add a new task.\n(C) Mark a task as completed.\n(D) Delete a task.\n)(L) List all tasks.\n(Q) Quit.")
    choice=input("Please choose from (A-Q)").lower()
    if choice=="a":
       task_title=input("please Enter You Task: ")
       task_Due_Date=input("please Enter you Task Due date(YYY-MM-DD)")
       todolist.addTask(task_list,task_title,task_Due_Date)
       print("Task added!")
    elif choice=="c":
        task_To_Complet=input("please enter the task you want to mark complete: ")
        for index,task in enumerate(task_list):
            if task_To_Complet==task.title:
                todolist.complete_task(task_list,index)
            else:
                 print("task not found")
    elif choice=="d":
        task_To_delete=input("please enter the task you want to Delete: ")
        for index,task in enumerate(task_list):
           if task_To_delete==task.title:
              todolist.delete_task(task_list,index)
           else:
               print("task not found")
    elif choice=="l":
        print(("*")*14,"To Do List",("*")*14)
        todolist.list_tasks(task_list)
        print(("*")*40)
    elif choice.lower()=="q":
        file_handler.save_tasks(task_list)
        print("Quiting...")
        break
    else:
        print("Invalid choice")
    
         
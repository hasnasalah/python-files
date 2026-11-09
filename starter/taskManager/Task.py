class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title=title
        self.due_date=due_date
        self.completed=completed
        
    # __str__(self): Returns a well-formatted string representation of the task, e.g.,
    # "[-] Submit assignment (due 2025-03-10)", where [X] indicates a completed task.
    
    def __str__(self):
        if self.completed==True:
            x="X"
        else:
            x="-"
            
        return(f"[{x}] {self.title} due {self.due_date}")
    
    
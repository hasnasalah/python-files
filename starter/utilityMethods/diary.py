import os
from datetime import datetime
if os.path.exists("diary.txt"):
      print("File exists!")   
else:
       with open("diary.txt", "w") as file:
        pass

try:
    dairy=input("please enter you dairy?\n")
    timestamp=datetime.now()
    timed_dairy=f"{timestamp}--{dairy}\n"
    with open("diary.txt", "a") as file:
      file.write(timed_dairy)
      
    with open("diary.txt", "r") as file:
        for line in file:
            print(line, end="")
except OSError:
    print("Error Writing to a file")

except FileNotFoundError:
    print("Diary file not found!")

except OSError as e:
    print(f"Error reading file: {e}")

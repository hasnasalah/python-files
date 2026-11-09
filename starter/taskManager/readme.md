# Task Manager – Python

## Description
A simple command-line Task Manager application built with Python. It allows users to manage their daily tasks and save them for future use using JSON file storage.

## Features
- Add new tasks with a title and due date.
- Mark tasks as completed.
- Delete tasks.
- Display all tasks.
- Save tasks to a JSON file.
- Load previously saved tasks when the application starts.

## Project Structure

```text
taskManager/
│
├── main.py
├── Task.py
├── todolist.py
├── file_handler.py
└── tasks.json
```

## Technologies Used
- Python
- Object-Oriented Programming (OOP)
- JSON for data persistence
- File handling
- Exception handling

## How to Run

1. Clone this repository:

   ```bash
   git clone 
   ```

2. Navigate to the project directory:

   ```bash
   cd taskManager
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Data Storage
Tasks are stored in a `tasks.json` file. The application automatically loads previously saved tasks when it starts and saves changes when tasks are added, completed, or deleted.

## Author
Hasna Ben Jillali
NAME: DUKUYE IMMACULATE OGHENEFEGA
MATRIC:24/14536
DEPARTMENT: CYBERSECURITY
COURSE: SEN 201

1. PROJECT TITLE

Design and Implementation of a To-Do List Application Using Python

2. PROJECT DESCRIPTION

This project involves the design and implementation of a simple command-line To-Do List application using Python. The application allows users to manage tasks by adding, viewing, completing, and deleting tasks. The project follows all phases of the Software Development Life Cycle (SDLC).

3. SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)
   3.1 Requirement Analysis
   Functional Requirements

The system shall allow users to add a task.

The system shall display all tasks.

The system shall allow users to mark a task as completed.

The system shall allow users to delete a task.

The system shall store tasks persistently.

Non-Functional Requirements

The system shall be simple and user-friendly.

The system shall run on any platform with Python installed.

The system shall respond quickly to user input.

3.2 System Design
System Architecture

Command-line based application

Single Python program file

Text file used for data storage

Data Design

Each task consists of:

Task ID

Task description

Task status (Pending or Completed)

File Design

tasks.txt stores task records in the format:

TaskID|Description|Status

3.3 Implementation
Project Structure
todolist/
├── todolist.py
├── tasks.txt
└── README.md

Python Source Code (todolist.py)
TASK_FILE = "tasks.txt"

def load_tasks():
tasks = []
try:
with open(TASK_FILE, "r") as file:
for line in file:
task_id, description, status = line.strip().split("|")
tasks.append({
"id": int(task_id),
"description": description,
"status": status
})
except FileNotFoundError:
pass
return tasks

def save_tasks(tasks):
with open(TASK_FILE, "w") as file:
for task in tasks:
file.write(f"{task['id']}|{task['description']}|{task['status']}\n")

def view_tasks(tasks):
if not tasks:
print("No tasks available.")
else:
for task in tasks:
print(f"{task['id']}. {task['description']} [{task['status']}]")

def add_task(tasks):
description = input("Enter task description: ")
task_id = len(tasks) + 1
tasks.append({
"id": task_id,
"description": description,
"status": "Pending"
})
save_tasks(tasks)
print("Task added successfully.")

def complete_task(tasks):
view_tasks(tasks)
task_id = int(input("Enter task ID to complete: "))
for task in tasks:
if task["id"] == task_id:
task["status"] = "Completed"
save_tasks(tasks)
print("Task marked as completed.")
return
print("Task not found.")

def delete_task(tasks):
view_tasks(tasks)
task_id = int(input("Enter task ID to delete: "))
tasks[:] = [task for task in tasks if task["id"] != task_id]

    for index, task in enumerate(tasks):
        task["id"] = index + 1

    save_tasks(tasks)
    print("Task deleted successfully.")

def main():
tasks = load_tasks()
while True:
print("\n1. View Tasks")
print("2. Add Task")
print("3. Complete Task")
print("4. Delete Task")
print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if **name** == "**main**":
main()

3.4 Testing

The system was tested using manual testing techniques.

Test Cases

Adding a task displays the task correctly.

Viewing tasks lists all stored tasks.

Completing a task updates its status.

Deleting a task removes it from the list.

Exiting the program terminates execution successfully.

3.5 Deployment

The application is deployed by running the Python script on any system with Python installed.
The source code is uploaded to a GitHub repository for version control and access.

3.6 Maintenance

The system can be maintained by:

Fixing bugs

Improving performance

Adding new features such as deadlines or a graphical interface

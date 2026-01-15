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

if __name__ == "__main__":
    main()

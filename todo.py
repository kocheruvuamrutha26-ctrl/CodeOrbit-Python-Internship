"""
CodeOrbit Tech - Python Programming Internship
Task 2: To-Do List CLI App

Tasks are stored in a Python list during runtime.
An optional text-file save/load feature is included.
"""

TASK_FILE = "tasks.txt"


def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)
    print("Task added successfully.")


def view_tasks(tasks):
    """Display all tasks with numbers."""
    print("\n===== MY TO-DO LIST =====")

    if not tasks:
        print("No tasks available.")
        return

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_task(tasks):
    """Remove a task using its displayed number."""
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")


def save_tasks(tasks):
    """Save tasks to a text file."""
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    """Load tasks from the text file if it exists."""
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def main():
    """Run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\n========================")
        print("       TO-DO LIST")
        print("========================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Save and Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

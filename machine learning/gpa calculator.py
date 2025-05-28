class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do List.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            todo_list.view_tasks()
            task_index = input("Enter the index of the task to remove: ")
            try:
                task_index = int(task_index)
                todo_list.remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

import argparse
import sys
from src.models import Task
from src.storage import load_tasks, save_tasks, get_next_id

DEFAULT_STORAGE_FILE = "tasks.json"


def add_task(title: str, priority: str = "medium", filepath: str = DEFAULT_STORAGE_FILE) -> Task:
    """Add a new task and persist it to storage."""
    tasks = load_tasks(filepath)
    new_id = get_next_id(tasks)
    task = Task(id=new_id, title=title, completed=False, priority=priority)
    tasks.append(task)
    save_tasks(filepath, tasks)
    return task


def list_tasks(filepath: str = DEFAULT_STORAGE_FILE) -> list[Task]:
    """Return all persisted tasks."""
    return load_tasks(filepath)


def complete_task(task_id: int, filepath: str = DEFAULT_STORAGE_FILE) -> bool:
    """Mark a task as completed. Return True if found and updated."""
    tasks = load_tasks(filepath)
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            save_tasks(filepath, tasks)
            return True
    return False


def delete_task(task_id: int, filepath: str = DEFAULT_STORAGE_FILE) -> bool:
    """Delete a task by ID. Return True if found and removed."""
    tasks = load_tasks(filepath)
    initial_count = len(tasks)
    tasks = [task for task in tasks if task.id != task_id]
    if len(tasks) < initial_count:
        save_tasks(filepath, tasks)
        return True
    return False


def main() -> None:
    """CLI entry point for task-tracker."""
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")
    add_parser.add_argument(
        "--priority",
        type=str,
        default="medium",
        choices=["low", "medium", "high"],
        help="Task priority (default: medium)",
    )

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Complete a task by ID")
    complete_parser.add_argument("id", type=int, help="Task ID to mark complete")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task by ID")
    delete_parser.add_argument("id", type=int, help="Task ID to delete")

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title, args.priority)
        print(f"Added task #{task.id}: {task.title} [{task.priority}]")
    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            urgent_tag = " (URGENT)" if task.is_urgent() else ""
            print(f"{status} #{task.id}: {task.title} [{task.priority}]{urgent_tag}")
    elif args.command == "complete":
        if complete_task(args.id):
            print(f"Completed task #{args.id}.")
        else:
            print(f"Error: Task #{args.id} not found.", file=sys.stderr)
            sys.exit(1)
    elif args.command == "delete":
        if delete_task(args.id):
            print(f"Deleted task #{args.id}.")
        else:
            print(f"Error: Task #{args.id} not found.", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

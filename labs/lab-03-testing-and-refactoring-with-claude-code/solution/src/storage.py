import json
import os
from src.models import Task


def load_tasks(filepath: str) -> list[Task]:
    """Load tasks from a JSON file. Return empty list if file does not exist."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError):
        return []


def save_tasks(filepath: str, tasks: list[Task]) -> None:
    """Save a list of Task objects to a JSON file."""
    data = [task.to_dict() for task in tasks]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_next_id(tasks: list[Task]) -> int:
    """Calculate the next sequential ID for a new task."""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1

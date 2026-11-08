import pytest
from src.models import Task
from src.cli import add_task, list_tasks, complete_task, delete_task, _format_task


def test_add_task_success(tmp_path):
    """Verify add_task creates and persists a new task."""
    filepath = str(tmp_path / "tasks.json")
    task = add_task("Deploy app", priority="high", filepath=filepath)
    assert task.id == 1
    assert task.title == "Deploy app"
    assert task.priority == "high"

    persisted = list_tasks(filepath)
    assert len(persisted) == 1
    assert persisted[0].title == "Deploy app"


def test_add_task_empty_title_raises_value_error(tmp_path):
    """Verify add_task rejects empty or whitespace-only titles."""
    filepath = str(tmp_path / "tasks.json")
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        add_task("", filepath=filepath)

    with pytest.raises(ValueError, match="Task title cannot be empty"):
        add_task("   ", filepath=filepath)


def test_complete_task_success(tmp_path):
    """Verify complete_task marks an existing task as completed."""
    filepath = str(tmp_path / "tasks.json")
    add_task("Test task", filepath=filepath)
    assert complete_task(1, filepath=filepath) is True

    tasks = list_tasks(filepath)
    assert tasks[0].completed is True


def test_complete_task_nonexistent_returns_false(tmp_path):
    """Verify complete_task returns False when task ID does not exist."""
    filepath = str(tmp_path / "tasks.json")
    assert complete_task(999, filepath=filepath) is False


def test_delete_task_success(tmp_path):
    """Verify delete_task removes an existing task."""
    filepath = str(tmp_path / "tasks.json")
    add_task("Task to delete", filepath=filepath)
    assert delete_task(1, filepath=filepath) is True

    tasks = list_tasks(filepath)
    assert len(tasks) == 0


def test_delete_task_nonexistent_returns_false(tmp_path):
    """Verify delete_task returns False when task ID does not exist."""
    filepath = str(tmp_path / "tasks.json")
    assert delete_task(999, filepath=filepath) is False


def test_format_task_helper():
    """Verify _format_task produces expected display strings."""
    task_normal = Task(id=1, title="Review PR", completed=False, priority="medium")
    assert _format_task(task_normal) == "[ ] #1: Review PR [medium]"

    task_urgent = Task(id=2, title="Fix security issue", completed=True, priority="high")
    assert _format_task(task_urgent) == "[x] #2: Fix security issue [high] (URGENT)"

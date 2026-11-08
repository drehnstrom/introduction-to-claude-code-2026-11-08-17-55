from src.models import Task
from src.storage import load_tasks, save_tasks, get_next_id


def test_load_tasks_nonexistent_file(tmp_path):
    """Loading from a non-existent file returns an empty list."""
    missing_file = str(tmp_path / "does_not_exist.json")
    tasks = load_tasks(missing_file)
    assert tasks == []


def test_load_tasks_invalid_json(tmp_path):
    """Loading from a file with invalid JSON returns an empty list."""
    corrupted_file = tmp_path / "corrupted.json"
    corrupted_file.write_text("NOT_VALID_JSON{{{")
    tasks = load_tasks(str(corrupted_file))
    assert tasks == []


def test_save_and_load_tasks_roundtrip(tmp_path):
    """Verify tasks are accurately persisted and reloaded."""
    filepath = str(tmp_path / "tasks.json")
    original_tasks = [
        Task(id=1, title="First Task", completed=False, priority="low"),
        Task(id=2, title="Second Task", completed=True, priority="high"),
    ]
    save_tasks(filepath, original_tasks)
    loaded_tasks = load_tasks(filepath)

    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].id == 1
    assert loaded_tasks[0].title == "First Task"
    assert loaded_tasks[0].completed is False
    assert loaded_tasks[0].priority == "low"
    assert loaded_tasks[1].id == 2
    assert loaded_tasks[1].is_urgent() is True


def test_get_next_id_empty_list():
    """Empty task list returns 1 as next ID."""
    assert get_next_id([]) == 1


def test_get_next_id_populated_list():
    """Populated task list returns max ID plus 1."""
    tasks = [
        Task(id=1, title="Task 1"),
        Task(id=5, title="Task 5"),
        Task(id=2, title="Task 2"),
    ]
    assert get_next_id(tasks) == 6

from src.models import Task


def test_task_creation_defaults():
    """Verify task initializes with default values."""
    task = Task(id=1, title="Test Task")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.completed is False
    assert task.priority == "medium"


def test_is_urgent_high_priority():
    """Verify is_urgent returns True for high priority (case-insensitive)."""
    assert Task(id=1, title="Urgent", priority="high").is_urgent() is True
    assert Task(id=2, title="Urgent", priority="HIGH").is_urgent() is True
    assert Task(id=3, title="Normal", priority="medium").is_urgent() is False
    assert Task(id=4, title="Low", priority="low").is_urgent() is False


def test_to_dict():
    """Verify serialization to dictionary."""
    task = Task(id=1, title="Sample", completed=True, priority="high")
    expected = {
        "id": 1,
        "title": "Sample",
        "completed": True,
        "priority": "high",
    }
    assert task.to_dict() == expected


def test_from_dict():
    """Verify deserialization from dictionary."""
    data = {
        "id": 5,
        "title": "Restored Task",
        "completed": True,
        "priority": "low",
    }
    task = Task.from_dict(data)
    assert task.id == 5
    assert task.title == "Restored Task"
    assert task.completed is True
    assert task.priority == "low"


def test_from_dict_defaults():
    """Verify deserialization with missing optional fields."""
    data = {"id": 10, "title": "Minimal Task"}
    task = Task.from_dict(data)
    assert task.id == 10
    assert task.title == "Minimal Task"
    assert task.completed is False
    assert task.priority == "medium"

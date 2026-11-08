from dataclasses import dataclass, asdict


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    priority: str = "medium"

    def is_urgent(self) -> bool:
        """Return True if task priority is high."""
        return self.priority.lower() == "high"

    def to_dict(self) -> dict:
        """Convert task instance to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task instance from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            completed=data.get("completed", False),
            priority=data.get("priority", "medium"),
        )

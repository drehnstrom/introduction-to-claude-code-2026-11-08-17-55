# Solution: Generating Code with Claude Code

## End State

- An updated `CLAUDE.md` configuration file in `~/projects/task-tracker` defining Python 3 conventions, test commands, and module architecture boundaries.
- A foundational data model in `src/models.py` defining the `Task` dataclass with `id`, `title`, `completed`, `priority`, and an `is_urgent()` helper method.
- A persistence service in `src/storage.py` with `load_tasks()`, `save_tasks()`, and `get_next_id()` using standard library JSON persistence.
- An interactive command-line entry point in `src/cli.py` using `argparse` with `add`, `list`, `complete`, and `delete` subcommands.
- A persisted `tasks.json` file verifying that tasks can be created, displayed, and marked complete from the shell.
- A clean Git repository with generated source files staged and committed.

## How to Verify

1. Navigate to the project directory and verify the source tree:

```bash
cd ~/projects/task-tracker
ls -la src/
```

Expected: `src/models.py`, `src/storage.py`, and `src/cli.py` are present.

2. Verify module imports and data model contracts:

```bash
python3 -c "from src.models import Task; from src.storage import load_tasks, save_tasks; print('Imports verified')"
```

Expected: Outputs `Imports verified` with exit code 0.

3. Verify CLI execution by adding tasks with different priorities:

```bash
python3 src/cli.py add "Write unit tests" --priority high
python3 src/cli.py add "Draft documentation" --priority low
```

Expected: Confirms addition of task #1 and task #2.

4. Verify listing and urgency formatting:

```bash
python3 src/cli.py list
```

Expected: Displays both tasks with status checkboxes, IDs, titles, priorities, and an `(URGENT)` indicator for task #1.

5. Verify task completion:

```bash
python3 src/cli.py complete 1
python3 src/cli.py list
```

Expected: Confirms completion of task #1, and `list` shows `[x]` for task #1.

6. Verify JSON persistence file contents:

```bash
cat tasks.json
```

Expected: A formatted JSON array containing the task objects.

7. Verify Git commit history:

```bash
git status
git log -1 --oneline
```

Expected: Working tree is clean, with the new source files committed.

## Built With

- Claude Code CLI (verified March 2025)
- Python 3.10+
- Git 2.x
- Unverified: Specific local terminal color themes for diff rendering

# Generating Code with Claude Code

## Time Required

20 minutes

## Overview

In this lab, you will direct Claude Code to scaffold and implement a modular Python task management CLI. You will craft high-precision directed prompts, coordinate module boundaries across data models, persistence services, and user interfaces, steer terminal diffs interactively, and safely reject flawed changes.

### You learn how to:
- Craft high-precision directed prompts with explicit boundaries and quality constraints.
- Scaffold multi-file project architectures incrementally using data contracts and services.
- Inspect, steer, and approve terminal diffs during interactive code generation.
- Safely reject unintended changes and verify repository status with version control.

## Scenario

Your team needs a command-line task management utility for the `task-tracker` project. Rather than writing boilerplate code by hand or copying disconnected snippets from a web browser chat, you will use Claude Code to scaffold a clean multi-file Python architecture. You will guide the agent to generate data models, JSON file persistence, and an interactive CLI entry point while maintaining full human-in-the-loop oversight through diff reviews.

## Lab Instructions

### Task 1: Update project guidelines and scaffold data contracts

In this task, you update your project configuration for Python development and use a high-precision prompt to generate foundational data models.

1. Open your terminal and navigate to the project directory created in the previous lab:

```bash
cd ~/projects/task-tracker
```

2. Update `CLAUDE.md` to define Python 3 conventions, test commands, and module architecture boundaries:

```markdown
# CLAUDE.md

## Build and Test Commands
- Run tests: `pytest`
- Run single test file: `pytest tests/test_<module>.py -v`
- Run CLI: `python3 src/cli.py --help`
- Run linter: `ruff check src/`

## Architecture and Code Style
- Project type: Python 3 command-line utility for task management
- Code style: Follow PEP 8 with snake_case for functions and variables, PascalCase for classes
- Data models: Define dataclasses in `src/models.py` with explicit type annotations
- Modularity: Keep storage in `src/storage.py` decoupled from CLI parsing in `src/cli.py`
- Safety: Never store secrets, passwords, or API keys in repository files
```

> [!NOTE]
> Codifying architecture boundaries in `CLAUDE.md` helps Claude Code choose consistent file paths and package conventions across all subsequent prompts.

3. Launch an interactive Claude Code session:

```bash
claude
```

4. Submit a high-precision prompt to scaffold the data model contract in `src/models.py`:

```text
Create src/models.py defining a Task dataclass with fields:
- id: int
- title: str
- completed: bool = False
- priority: str = "medium"

Include an is_urgent() method returning True when priority is "high" (case-insensitive).
Add to_dict() and from_dict(cls, data: dict) methods for serialization.
Include type annotations and docstrings.
```

5. Inspect the terminal diff presented by Claude Code before confirming file creation.

> [!IMPORTANT]
> Verify that the diff header targets `src/models.py`, that all lines are marked with green additions (`+`), and that no existing files were touched.

6. Type `y` and press Enter to approve the change and write `src/models.py` to disk.

7. In a separate terminal or after exiting, verify that `src/models.py` exists:

```bash
python3 -c "from src.models import Task; t = Task(1, 'Test', priority='high'); print(t.is_urgent())"
```

> [!TIP]
> Establishing data contracts first ensures downstream service and interface modules import agreed field names rather than guessing object structures.

### Task 2: Implement storage services with multi-turn prompting

In this task, you ground prompts in existing files and use multi-turn refinement to build a persistence layer.

1. In your active Claude Code session, prompt the agent to create `src/storage.py` grounded in `src/models.py`:

```text
Create src/storage.py to persist tasks to JSON:
- Import Task from src.models
- load_tasks(filepath: str) -> list[Task]: Load tasks from a JSON file; return an empty list if the file does not exist or is invalid JSON
- save_tasks(filepath: str, tasks: list[Task]) -> None: Serialize and write Task objects to the target file with 2-space indentation
Include type annotations, docstrings, and graceful handling of missing files.
```

2. Review the proposed diff. Notice that Claude Code reads `src/models.py` to import `Task` and calls `Task.from_dict()` and `task.to_dict()` automatically.

3. Approve the proposed modification by typing `y`.

4. Submit an iterative follow-up prompt in the same session to add an ID generation helper:

```text
Add a helper function get_next_id(tasks: list[Task]) -> int to src/storage.py.
It should return 1 if tasks is empty, or the maximum task id plus 1.
```

5. Inspect the hunk header and verify that the diff only adds the `get_next_id` function without modifying `load_tasks` or `save_tasks`.

6. Approve the change by typing `y`.

### Task 3: Scaffold the CLI entry point and steer file modifications

In this task, you generate the CLI entry point, practice steering a proposed diff, and test your application from the shell.

1. In your active Claude Code session, prompt the agent to scaffold `src/cli.py`:

```text
Create src/cli.py using argparse to provide a command-line interface for task-tracker.
Support add, list, and complete subcommands wired to src.models and src.storage.
```

2. When Claude Code displays the proposed diff, do not approve it immediately. Practice steering the modification by providing corrective feedback.

3. Type `e` or enter corrective feedback to refine the implementation:

```text
Ensure default storage uses "tasks.json". In the list command, display tasks with status as [x] or [ ], show an (URGENT) tag for urgent tasks, and print a clear message when no tasks exist. In complete, display an error message and exit with status code 1 if the task id is not found.
```

4. Inspect the revised diff to verify that Claude Code incorporated your formatting and error handling requirements.

5. Type `y` to accept and write `src/cli.py`.

6. Exit the interactive session:

```text
/exit
```

7. From your shell, run the CLI help command to inspect the available subcommands:

```bash
python3 src/cli.py --help
```

8. Add two tasks with different priorities:

```bash
python3 src/cli.py add "Write unit tests" --priority high
python3 src/cli.py add "Draft documentation" --priority low
```

9. List your tasks to verify output formatting and urgency indicators:

```bash
python3 src/cli.py list
```

10. Mark task #1 as complete:

```bash
python3 src/cli.py complete 1
```

11. List tasks again to confirm that task #1 displays as completed:

```bash
python3 src/cli.py list
```

12. Inspect the generated `tasks.json` file on disk:

```bash
cat tasks.json
```

> [!NOTE]
> The JSON file should contain two serialized task objects, with task #1 marked with `"completed": true`.

### Task 4: Practice rejecting flawed changes and rollbacks

In this task, you submit a deliberately vague prompt, inspect an unconstrained diff, reject the modification, and verify repository safety.

1. Launch Claude Code in interactive mode:

```bash
claude
```

2. Submit a deliberately vague, unconstrained prompt:

```text
Optimize everything and rewrite all modules to make them faster.
```

3. Observe the proposed diff. Notice how unconstrained prompts lead Claude Code to make arbitrary architectural assumptions, alter function signatures, or modify multiple files at once.

> [!WARNING]
> Never accept a diff that makes unrequested modifications or alters public interfaces. Vague follow-up prompts compound errors; rejecting immediately is the safest course of action.

4. Type `n` and press Enter to reject the proposed change.

5. Notice that Claude Code immediately stops file modifications and reports that the change was declined without modifying any files.

6. Exit the interactive session:

```text
/exit
```

7. Use Git commands in your shell to confirm that your working tree remained clean and untouched:

```bash
git status
```

> [!TIP]
> If unintended edits are ever written to disk, you can inspect changes with `git diff` and revert modified files using `git restore <file>` or `git checkout -- <file>`.

### Bonus Task 5: Extend the CLI and commit your generated code

With fewer step-by-step instructions, use single-prompt mode to add a deletion command, verify its behavior, and commit your work to Git.

1. Use single-prompt mode (`-p`) to add a `delete` subcommand to `src/cli.py` that accepts a task ID and removes it from `tasks.json`:

```bash
claude -p "In src/cli.py, add a delete subcommand that accepts an integer task id, removes the matching task from tasks.json, and prints a confirmation. Print an error and exit with status 1 if the task id does not exist."
```

2. Review and approve the proposed diff when prompted.

3. Verify the delete command from your shell:

```bash
python3 src/cli.py delete 1
python3 src/cli.py list
```

4. Confirm that only task #2 remains in `tasks.json`.

5. Stage and commit your new source files and updated guidelines:

```bash
git status
git add src/ CLAUDE.md
git commit -m "feat: implement task manager CLI with models, storage, and commands"
```

6. Confirm that your Git working tree is clean:

```bash
git status
```

## Congratulations!

In this lab, you have:
- Crafted high-precision directed prompts with explicit boundaries and quality constraints.
- Scaffolded multi-file project architectures incrementally using data contracts and services.
- Inspected, steered, and approved terminal diffs during interactive code generation.
- Safely rejected unintended changes and verified repository status with version control.

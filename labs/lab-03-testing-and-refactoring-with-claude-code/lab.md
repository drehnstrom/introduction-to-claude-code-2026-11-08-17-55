# Testing and Refactoring with Claude Code

## Time Required

25 minutes

## Overview

In this lab, you will direct Claude Code to author automated test suites with pytest, diagnose and repair runtime defects using terminal feedback, and refactor code safely using test-backed characterization. You will guide the agent through targeted test generation, inspect failure tracebacks, apply minimal bug fixes without altering test assertions, and restructure existing code while preserving public contracts.

### You learn how to:
- Author automated unit and service tests with pytest using targeted prompts.
- Execute scoped test runs and interpret terminal exit codes and tracebacks.
- Diagnose and repair defects using regression tests and minimal code patches.
- Refactor source code safely while preserving public contracts and verifying green suites.

## Scenario

Your team’s `task-tracker` CLI has core functionality in place, but it lacks automated test coverage, contains edge-case validation defects, and has mixed concerns in its CLI entry point. Before adding new features or shipping to users, you need a robust automated testing safety net. You will direct Claude Code to scaffold comprehensive pytest suites, reproduce and resolve an input validation bug, and refactor formatting logic safely without breaking existing behavior.

## Lab Instructions

### Task 1: Direct Claude Code to author and run data model tests

In this task, you prepare your workspace, update project guidelines for pytest, and instruct Claude Code to author and execute automated unit tests for your data models.

1. Open your terminal and navigate to your project directory:

```bash
cd ~/projects/task-tracker
```

> [!NOTE]
> If you are starting fresh or need to restore clean baseline files, copy `starter/CLAUDE.md`, `starter/src/models.py`, `starter/src/storage.py`, and `starter/src/cli.py` from `labs/lab-03-testing-and-refactoring-with-claude-code/starter/` into `~/projects/task-tracker/`.

2. Verify that `pytest` is installed in your Python environment:

```bash
pytest --version
```

> [!TIP]
> If `pytest` is not installed, install it by running `python3 -m pip install pytest`.

3. Update `CLAUDE.md` to ensure Claude Code recognizes pytest test commands and conventions:

```markdown
# CLAUDE.md

## Build and Test Commands
- Run all tests: `pytest`
- Run single test file: `pytest tests/test_<module>.py -v`
- Run specific test: `pytest tests/test_<module>.py -k "<test_name>" -v`
- Run CLI: `python3 src/cli.py --help`
- Run linter: `ruff check src/ tests/`

## Architecture and Code Style
- Project type: Python 3 command-line utility for task management
- Code style: Follow PEP 8 with snake_case for functions and variables, PascalCase for classes
- Data models: Define dataclasses in `src/models.py` with explicit type annotations
- Modularity: Keep storage in `src/storage.py` decoupled from CLI parsing in `src/cli.py`
- Testing: Keep unit tests in `tests/` using pytest and `tmp_path` fixtures for file isolation
- Safety: Never store secrets, passwords, or API keys in repository files
```

4. Launch an interactive Claude Code session:

```bash
claude
```

5. Direct Claude Code to author automated unit tests for `src/models.py`:

```text
Create tests/test_models.py using pytest to thoroughly test Task in src/models.py:
- test_task_creation_defaults: verify id, title, completed=False, priority="medium"
- test_is_urgent_high_priority: verify is_urgent() returns True for "high" and "HIGH", and False for "medium" and "low"
- test_to_dict: verify dictionary serialization structure
- test_from_dict: verify object creation from a complete dictionary
- test_from_dict_defaults: verify object creation when completed and priority are omitted
After creating the file, run pytest tests/test_models.py -v to verify all tests pass.
```

6. Inspect the proposed diff presented by Claude Code.

> [!IMPORTANT]
> Verify that Claude Code places the test file in `tests/test_models.py`, imports `Task` from `src.models`, and uses descriptive assertion statements.

7. Approve file creation by typing `y` and pressing Enter.

8. When prompted to approve the shell command `pytest tests/test_models.py -v`, type `y` to execute it.

9. Confirm that Claude Code reports 5 passing tests with exit code 0.

### Task 2: Test persistence services and execute scoped test suites

In this task, you direct Claude Code to author service tests using pytest fixtures and practice scoped test execution strategies.

1. In your active Claude Code session, prompt the agent to scaffold tests for `src/storage.py` using isolated temporary directories:

```text
Create tests/test_storage.py using pytest and the tmp_path fixture to test src/storage.py:
- test_load_tasks_nonexistent_file: loading from a missing path returns an empty list
- test_load_tasks_invalid_json: loading from a corrupted JSON file returns an empty list
- test_save_and_load_tasks_roundtrip: saving Task instances and reloading them preserves all fields and urgency status
- test_get_next_id_empty_list: returns 1 when task list is empty
- test_get_next_id_populated_list: returns max id plus 1 when tasks exist
Ensure tests use tmp_path so the actual tasks.json file in the project root is never touched.
Run pytest tests/test_storage.py -v after creating the file.
```

2. Review the proposed diff. Notice that Claude Code uses pytest’s built-in `tmp_path` fixture to construct isolated file paths like `str(tmp_path / "tasks.json")`.

3. Approve the file creation and test execution by typing `y`.

4. Confirm that all 5 storage tests pass cleanly.

5. Direct Claude Code to execute a targeted test case using the `-k` filter:

```text
Run only the ID generation tests in tests/test_storage.py using pytest -k "test_get_next_id" -v
```

6. Review the command execution output. Notice how Claude Code runs `pytest tests/test_storage.py -k "test_get_next_id" -v`, executes only the matching tests, and deselects unrelated tests.

> [!TIP]
> Running targeted tests while actively authoring features keeps feedback loops fast and conserves token context.

7. Direct Claude Code to execute the entire test suite across all test files:

```text
Run the full pytest suite with verbose output
```

8. Confirm that Claude Code executes `pytest -v` and reports that all 10 tests across `test_models.py` and `test_storage.py` pass.

### Task 3: Reproduce and fix an edge-case defect using regression tests

In this task, you write a failing regression test to expose an input validation defect, direct Claude Code to diagnose the failure traceback, and apply a minimal fix without altering test assertions.

1. In your active Claude Code session, direct the agent to add initial CLI tests that include validation for empty task titles:

```text
Create tests/test_cli.py using pytest and tmp_path:
- test_add_task_success: verify add_task() creates and persists a valid task
- test_add_task_empty_title_raises_value_error: verify add_task("", filepath=...) and add_task("   ", filepath=...) raise ValueError with message "Task title cannot be empty"
Run pytest tests/test_cli.py -v after writing the file.
```

2. Review the proposed diff in `tests/test_cli.py` and type `y` to approve it.

3. Approve the test run command when prompted.

4. Observe the test failure reported by Claude Code:

```text
FAILED tests/test_cli.py::test_add_task_empty_title_raises_value_error - Failed: DID NOT RAISE <class 'ValueError'>
```

> [!NOTE]
> Claude Code parses the failure traceback directly from stderr, identifying that `add_task()` allowed empty titles through without raising `ValueError`.

5. Prompt Claude Code to diagnose the failure and apply a targeted fix to production code:

```text
Diagnose why test_add_task_empty_title_raises_value_error failed.
Fix src/cli.py so add_task() validates that title is non-empty after stripping whitespace, raising ValueError("Task title cannot be empty") if invalid.
Do not modify the test assertion in tests/test_cli.py.
Run pytest tests/test_cli.py -v after applying the fix.
```

6. Carefully inspect the proposed diff for `src/cli.py`.

> [!WARNING]
> Verify that the diff modifies `src/cli.py` by adding a validation guard clause at the start of `add_task()`. Reject any diff that attempts to weaken or delete the assertion in `tests/test_cli.py`.

7. Type `y` to accept the fix and run the test suite.

8. Verify that `pytest tests/test_cli.py -v` now passes with 2 passing tests.

9. Direct Claude Code to verify that the entire test suite remains green:

```text
Run the full pytest suite to verify no regressions occurred
```

10. Confirm that all 12 tests across all three test files pass with exit code 0.

### Task 4: Execute a safe refactoring loop and enforce code quality

In this task, you execute the safe refactoring loop by verifying your test baseline, directing Claude Code to extract display helpers and guard clauses, and verifying post-refactoring behavior.

1. In your active Claude Code session, confirm your green baseline before refactoring:

```text
Run pytest -q to confirm our test suite is fully green before we refactor
```

2. Direct Claude Code to refactor console formatting in `src/cli.py`:

```text
Refactor src/cli.py:
1. Extract the task display formatting logic from main() into a private helper function _format_task(task: Task) -> str that formats the status checkbox, id, title, priority, and urgent indicator.
2. In main(), catch ValueError when calling add_task(), print "Error: <message>" to stderr, and exit with code 1.
3. Keep all existing public function signatures and return types unchanged.
4. Add complete type annotations and docstrings.
5. Run pytest after refactoring to confirm all tests remain green.
```

3. Review the proposed diff.

> [!IMPORTANT]
> Confirm that `_format_task()` encapsulates string formatting, that public function signatures (`add_task`, `list_tasks`, `complete_task`, `delete_task`) remain identical, and that existing business logic was not altered.

4. Type `y` to accept the refactored code and run the test suite.

5. Confirm that all 12 tests pass immediately after refactoring, verifying zero regressions.

6. Direct Claude Code to perform a code quality check across source and test files:

```text
Inspect src/ and tests/ for unused imports, syntax issues, or style inconsistencies.
Fix any issues found while preserving all application behavior.
Run pytest afterwards to verify everything passes.
```

7. Review any proposed cleanup diffs and approve them with `y`.

8. Confirm that the full test suite remains completely green.

### Bonus Task 5: Extend test coverage and commit the verified codebase

With fewer step-by-step hints, instruct Claude Code to add comprehensive tests for remaining CLI functions, verify behavior from the shell, and commit your tested codebase to version control.

1. Direct Claude Code in your active session to extend `tests/test_cli.py`:

```text
In tests/test_cli.py, add tests for:
- test_complete_task_success and test_complete_task_nonexistent_returns_false
- test_delete_task_success and test_delete_task_nonexistent_returns_false
- test_format_task_helper: verify _format_task() output for normal and urgent tasks
Run the full pytest suite to ensure all tests pass.
```

2. Review the proposed additions and approve them.

3. Confirm that Claude Code reports 17 passing tests across the entire test suite.

4. Exit the interactive Claude Code session:

```text
/exit
```

5. From your shell, verify that the CLI rejects empty titles and formats valid tasks properly:

```bash
python3 src/cli.py add "   "
python3 src/cli.py add "Write release notes" --priority high
python3 src/cli.py list
```

> [!NOTE]
> The first command should output `Error: Task title cannot be empty` to stderr and exit with code 1. The second and third commands should add and display task #1 with the `(URGENT)` indicator.

6. Check your Git status to review all modified and newly created files:

```bash
git status
```

7. Stage all changes and commit them with a conventional commit message:

```bash
git add CLAUDE.md src/ tests/
git commit -m "test: add comprehensive pytest suite and refactor CLI formatting"
```

8. Confirm that your working directory is clean:

```bash
git status
```

## Congratulations!

In this lab, you have:
- Authored automated unit and service tests with pytest using targeted prompts.
- Executed scoped test runs and interpreted terminal exit codes and tracebacks.
- Diagnosed and repaired defects using regression tests and minimal code patches.
- Refactored source code safely while preserving public contracts and verifying green suites.

# Solution: Testing and Refactoring with Claude Code

## End State

- An updated `CLAUDE.md` file in `~/projects/task-tracker` codifying scoped test commands, testing conventions with pytest, and linter commands.
- A unit test suite in `tests/test_models.py` verifying data model initialization, defaults, case-insensitive urgency detection, and serialization round-trips.
- An integration test suite in `tests/test_storage.py` using pytest’s `tmp_path` fixture to test missing files, corrupted JSON payloads, round-trip persistence, and ID generation without modifying workspace files.
- A regression test and bug fix in `src/cli.py` ensuring `add_task()` rejects empty or whitespace-only titles with a clear `ValueError`.
- A refactored `src/cli.py` module featuring an extracted `_format_task()` helper function, guard clauses for validation, full type hints, docstrings, and verified backwards compatibility.
- An extended CLI test suite in `tests/test_cli.py` verifying task creation, validation, completion, deletion, and console formatting.
- A clean Git working tree with all test suites and refactored code staged and committed.

## How to Verify

1. Navigate to the project directory and verify the directory structure:

```bash
cd ~/projects/task-tracker
ls -la tests/
```

Expected: `tests/test_models.py`, `tests/test_storage.py`, and `tests/test_cli.py` are present.

2. Run the targeted data model unit tests:

```bash
pytest tests/test_models.py -v
```

Expected: All 5 model tests pass with exit code 0.

3. Run the targeted storage service tests:

```bash
pytest tests/test_storage.py -v
```

Expected: All 5 storage tests pass with exit code 0.

4. Run the targeted CLI and regression tests:

```bash
pytest tests/test_cli.py -v
```

Expected: All 7 CLI tests pass with exit code 0, including empty title validation and helper formatting.

5. Execute the full test suite across all modules:

```bash
pytest -v
```

Expected: All 17 tests pass with exit code 0.

6. Verify that the CLI rejects empty titles at runtime:

```bash
python3 src/cli.py add "   "
```

Expected: Fails with status code 1 and prints `Error: Task title cannot be empty` to stderr.

7. Verify that normal CLI operations function correctly:

```bash
python3 src/cli.py add "Review pull request" --priority high
python3 src/cli.py list
```

Expected: Confirms addition and formats the task list with checkbox and `(URGENT)` indicator.

8. Verify Git status and commit history:

```bash
git status
git log -1 --oneline
```

Expected: Working tree is clean, and the latest commit records the testing and refactoring milestone.

## Built With

- Claude Code CLI (verified March 2025)
- Python 3.10+
- pytest 8.x
- Git 2.x
- Unverified: Specific local terminal color themes for diff rendering

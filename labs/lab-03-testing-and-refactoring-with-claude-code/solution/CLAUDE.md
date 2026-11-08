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

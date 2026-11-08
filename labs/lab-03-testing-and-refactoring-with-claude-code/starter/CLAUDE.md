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

# Copy Edit Report: Introduction to Claude Code

## Pass: 2026-11-08

| Field | Value |
| :--- | :--- |
| Editor model | Claude 3.7 Sonnet |
| Session | Fresh (yes) |
| Scope | Slides and labs (`course/*.md`, `labs/**/lab.md`) |

### Glossary

| Term | Form used | Notes |
| :--- | :--- | :--- |
| Claude Code | `Claude Code` | Official product name |
| Git | `Git` | Capitalized as VCS name in visible prose; `git` for CLI commands |
| Bash | `Bash` | Capitalized as shell name in visible prose; `bash` for code tags |
| pytest | `pytest` | Test runner name in lowercase code/command references |
| CLAUDE.md | `CLAUDE.md` | Configuration file identifier |

### Fix counts

| Type | Count |
| :--- | :--- |
| Spelling | 0 |
| Grammar | 2 |
| Smart quotes | 8 |
| Em-dashes / ampersands | 0 |
| Consistency | 6 |

### Representative fixes

- `course/01-getting-started.md` / Human-in-the-Loop Safety Model: Standardized “git history” to “Git history” and “bash commands” to “Bash commands” in visible prose.
- `course/01-getting-started.md` / Launching Claude Code Sessions: Standardized “git commit messages” to “Git commit messages”.
- `course/02-prompting-for-code-generation.md` / What You Learned: Corrected verb tense from “approve” to “approved” (“Inspected, reviewed, and approved proposed file modifications safely”) for grammatical parallelism.
- `course/02-prompting-for-code-generation.md` / Prompt Evolution: Replaced curly quotes inside inline code backticks with straight double quotes (`"Build a weather script"` and `"Create src/weather.py using urllib and json"`).
- `course/02-prompting-for-code-generation.md` / Quiz 1: Replaced curly quotes inside inline code backticks with straight double quotes across options A–D and the quiz answer.
- `course/02-prompting-for-code-generation.md` / Handling Flawed Changes and Rollbacks: Standardized “rely on git” and “revert via git” to “Git” in prose.
- `labs/lab-02-generating-code-with-claude-code/lab.md` / Task 3: Formatted `"completed": true` with inline code backticks to protect quotes.
- `labs/lab-03-testing-and-refactoring-with-claude-code/lab.md` / Congratulations: Corrected verb tense from “Refactor” to “Refactored” to match past-tense completion structure and mirror “You learn how to”.

### Left unchanged

- `claude`, `git`, `npm`, `ruff`, and `pytest` kept as lowercase command-style names in CLI invocations and shell snippets
- Inline code and fenced code blocks untouched
- `Lab link: TODO` left exactly as written on all lab slides
- Metadata comments (`<!-- course-title: ... -->`, `<!-- course-theme: roi-alt-theme -->`, layout directives) preserved intact

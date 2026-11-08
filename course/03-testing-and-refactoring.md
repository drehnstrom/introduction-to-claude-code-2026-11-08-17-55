<!-- course-title: Introduction to Claude Code -->
<!-- course-theme: roi-alt-theme -->

<!-- layout: title -->
![ROI Logo](images/roi-logo-with-name.png)

Introduction to Claude Code

# Chapter 3: Testing and Refactoring with Claude Code

---

# Chapter 3: Objectives

- Direct Claude Code to write tests, diagnose failures, and refactor code
- Instruct Claude Code to write and run automated test suites
- Diagnose error traces and fix bugs using interactive terminal feedback
- Refactor source code to improve structure, maintainability, and quality
- Write automated tests, resolve failures, and refactor code with Claude Code

---

<!-- layout: navigation -->
# Chapter 3

- **Writing and Running Automated Tests**
- Diagnosing and Fixing Bugs
- Code Refactoring and Code Quality
- Lab: Testing and Refactoring with Claude Code

---

<!-- layout: card-layout -->
# The Agentic Testing Loop

### Test Discovery
- Claude Code inspects `CLAUDE.md` and repository manifests to locate test runners.
- Recognizes established test tools like `pytest`, `vitest`, `jest`, or `go test`.

### Test Authoring
- Scaffolds dedicated test files matching naming patterns like `test_*.py` or `*.test.ts`.
- Authors test fixtures, assertions, and boundary checks aligned with project types.

### Test Execution
- Executes test commands directly in the local terminal shell with your approval.
- Captures standard output, error streams, and exit codes to validate pass/fail status.

---

# Directing Claude Code to Author Tests

- **Specify test targets and frameworks**: Name the exact module and testing tool
  - Clarify whether tests belong in a separate `tests/` directory or alongside source files
  - Mandate coverage for happy paths, boundary inputs, and expected exceptions
- **Ground tests in real requirements**: Describe expected behavior over implementation details
  - Tests should validate external contracts rather than internal private variables
  - Direct the agent to use standard assertion libraries and test fixtures

```bash
# Prompt Claude Code to generate a comprehensive test suite
claude -p "Create tests/test_weather.py using pytest:
- Test fetch_weather() with a valid city returning expected dictionary keys
- Test fetch_weather() with an unknown city raising CityNotFoundError
- Mock network calls with unittest.mock so tests run offline
Run pytest after creating the file to confirm all tests pass."
```

---

<!-- layout: 2-column -->
# Running Tests in Claude Code

### Automated Tool Execution
- Claude Code runs test commands via its integrated Bash tool
- Asks for explicit permission before executing shell commands
- Displays the exact command: `pytest tests/test_weather.py -v`
- Inspects exit codes (`0` for success, non-zero for failure)

### Scoped Execution Strategies
- **Full suite**: Run entire test suites to check for unintended regressions
- **Targeted file**: Focus execution on a single test file during active feature work
- **Specific test case**: Run a single failing test to isolate behavior quickly

<!-- below-columns -->

> [!TIP]
> Tell Claude Code to run targeted tests while writing code, then run the full suite before finishing the task.

---

<!-- layout: 3-column -->
# Robust Test Authoring Patterns

### Mocking External APIs
- Isolate unit tests from network calls and external databases
- Use standard mocks or fixtures to return predictable payloads
- Keeps test suites fast and completely deterministic

### Edge Case Coverage
- Test boundary values such as empty strings, zero, and negative numbers
- Verify timeout behavior and invalid data formats
- Validates system resilience against malformed inputs

### Clear Failure Messages
- Write descriptive test function names: `test_fetch_weather_timeout_raises_error`
- Include informative assertion messages
- Ensures failures clearly communicate what broke and why

---

<!-- layout: navigation -->
# Chapter 3

- Writing and Running Automated Tests
- **Diagnosing and Fixing Bugs**
- Code Refactoring and Code Quality
- Lab: Testing and Refactoring with Claude Code

---

<!-- layout: 2-column -->
# Automated Failure Diagnosis

### Raw Terminal Output
- Dense stack traces often span dozens of internal library frames
- Developers must manually trace calls back to source lines
- Context switches between test output, source files, and documentation

### Claude Code Agent Analysis
- Analyzes stderr and filters tracebacks to your repository code
- Reads the exact source file and failing line immediately
- Correlates assertion expectations with the actual runtime values
- Formulates a hypothesis explaining why the defect occurred

<!-- below-columns -->

> [!NOTE]
> Claude Code reads terminal test output directly, eliminating the need to copy-paste tracebacks between windows.

---

# The Interactive Debugging Workflow

- **Capturing the defect**: Direct Claude Code to run the failing test and inspect output
  - The agent identifies the exact failure point and reads surrounding source logic
- **Hypothesis and targeted fix**: Proposes a focused diff addressing the root cause
  - Modifies application logic rather than masking symptoms with broad catch blocks

```text
> Run pytest tests/test_storage.py and fix any failures.

Claude Code:
Running: pytest tests/test_storage.py
Captured failure: KeyError: 'priority' in save_tasks() at storage.py:24
Root cause: save_tasks() expects all tasks to have 'priority', but legacy tasks omit it.

Proposed change to src/storage.py:
@@ -23,2 +23,2 @@
-    "priority": task["priority"]
+    "priority": task.get("priority", "medium")

Allow this change? (y/n/e)
```

---

<!-- layout: 3-column -->
# Bug Fixing Anti-Patterns

### Modifying the Test Assertion
- Changing test expectations to match buggy output
- Defeats the purpose of test verification
- Fix: Always confirm intended behavior before touching tests

### Swallowing Exceptions
- Wrapping failing code in `except Exception: pass`
- Conceals errors and leads to silent data corruption
- Fix: Address the root cause and handle expected exceptions explicitly

### Unfocused Patching
- Rewriting entire functions when one line failed
- Introduces new regressions across unrelated code
- Fix: Keep bug fixes minimal, targeted, and verified by tests

---

<!-- layout: card-layout -->
# Closing the Loop with Regression Tests

### Reproduce First
- Write or run a failing test that reproduces the bug reliably before changing source code.
- Confirms that the defect is real and measurable.

### Apply Minimal Fix
- Inspect the proposed diff to verify it solves only the identified defect.
- Reject unnecessary modifications to surrounding functions.

### Verify Green Suite
- Re-run the specific failing test to confirm it now passes.
- Execute the full test suite to guarantee no existing features were broken.

---

<!-- layout: navigation -->
# Chapter 3

- Writing and Running Automated Tests
- Diagnosing and Fixing Bugs
- **Code Refactoring and Code Quality**
- Lab: Testing and Refactoring with Claude Code

---

<!-- layout: card-layout -->
# Refactoring Vectors in Claude Code

### Structural Simplification
- Break long, complex procedures into focused helper functions.
- Flatten deeply nested conditionals into early returns and guard clauses.

### Type Safety and Clarity
- Introduce type annotations, dataclasses, or typed interfaces.
- Replace raw dictionaries and tuples with explicit domain data structures.

### Dead Code Elimination
- Identify unused functions, obsolete parameters, and dead variables.
- Remove outdated comments and temporary debugging statements.

---

<!-- layout: 2-column -->
# The Safe Refactoring Loop

### Pre-Refactoring Safety Check
- Ensure all existing unit tests pass cleanly before editing code
- Establish a known green baseline in version control
- If tests are missing, prompt Claude Code to write tests first

### Verified Post-Refactoring State
- Apply targeted structural changes without altering public APIs
- Re-run the full test suite immediately after applying edits
- Green test suite confirms that functional behavior remains intact

<!-- below-columns -->

> [!IMPORTANT]
> Never refactor code that lacks test coverage. Direct Claude Code to author baseline characterization tests before restructuring code.

---

# Prompting for Targeted Refactoring

- **Define explicit refactoring goals**: Tell Claude Code exactly what to restructure
  - State which functions to decompose, rename, or modularize
  - Mandate that external function signatures and return types stay unchanged
- **Enforce quality constraints**: Demand type hints, docstrings, and linter compliance

```bash
# Prompt Claude Code to refactor without breaking existing contracts
claude -p "Refactor src/weather.py:
1. Extract URL construction and HTTP request logic from fetch_weather()
   into a private _send_request() helper function
2. Add type hints and docstrings across all functions
3. Preserve all existing public function signatures and return types
4. Run pytest to confirm all tests remain green after refactoring"
```

> [!TIP]
> Explicitly instruct Claude Code: “Do not change public function signatures or external behavior.”

---

<!-- layout: 3-column -->
# Refactoring Pitfalls to Avoid

### Scope Creep
- Adding new feature functionality during a refactoring pass
- Makes it difficult to isolate what broke if tests fail
- Fix: Separate refactoring tasks from new feature development

### Breaking Public Contracts
- Renaming public functions or changing parameter types
- Breaks external modules and downstream callers
- Fix: Deprecate gradually or keep signatures identical

### Accidental Logic Changes
- Simplifying boolean logic or regex patterns incorrectly
- Alters subtle edge case handling
- Fix: Lean on comprehensive tests to catch behavioral drift

---

# Automating Code Quality and Linting

- **Directing linter and formatter runs**: Use Claude Code to enforce project style rules
  - Invoke tools like `ruff`, `flake8`, `eslint`, or `prettier` through the CLI
  - Instruct Claude Code to inspect linter reports and fix warnings systematically
- **Project-wide consistency**: Codify style commands in `CLAUDE.md` for repeatable execution

```bash
# Direct Claude Code to resolve linting and formatting issues
claude -p "Run ruff check src/ and fix all reported style violations.
Do not alter application logic or disable lint rules with inline comments.
Run pytest afterwards to verify all tests still pass."
```

> [!NOTE]
> Claude Code can parse linter diagnostics and resolve syntax warnings, unused imports, and formatting inconsistencies in a single automated pass.

---

<!-- layout: navigation -->
# Chapter 3

- Writing and Running Automated Tests
- Diagnosing and Fixing Bugs
- Code Refactoring and Code Quality
- **Lab: Testing and Refactoring with Claude Code**

---

# Testing and Refactoring with Claude Code

Lab link: TODO

---

# What You Learned

- Directed Claude Code to write tests, diagnose failures, and refactor code
- Instructed Claude Code to write and run automated test suites
- Diagnosed error traces and fixed bugs using interactive terminal feedback
- Refactored source code to improve structure, maintainability, and quality
- Wrote automated tests, resolved failures, and refactored code with Claude Code

---

# Quiz 1 of 3

**How does Claude Code detect whether an automated test run succeeded or failed?**

- A. It asks the user to manually verify and type whether tests passed
- B. It reads the test runner exit code and parses stdout and stderr for errors
- C. It uploads the test file to a remote cloud validator for assessment
- D. It estimates pass or fail probability based on code length

---

# Quiz 1: Answer

**How does Claude Code detect whether an automated test run succeeded or failed?**

**Correct: B.** It reads the test runner exit code and parses stdout and stderr for errors

- Claude Code executes test commands via its integrated Bash tool
- An exit code of `0` signals success; non-zero exit codes signal failures
- The agent captures tracebacks from standard error to locate exact failure lines
- It uses this feedback loop to propose corrective code adjustments

---

# Quiz 2 of 3

**What is the most critical prerequisite before directing Claude Code to refactor source code?**

- A. Deleting existing tests so Claude Code can write new ones from scratch
- B. Having a green, passing automated test suite that verifies existing behavior
- C. Disabling all linters and compiler warnings
- D. Merging all open branches into the main branch

---

# Quiz 2: Answer

**What is the most critical prerequisite before directing Claude Code to refactor source code?**

**Correct: B.** Having a green, passing automated test suite that verifies existing behavior

- Refactoring alters code structure without modifying external functional behavior
- Passing tests provide an objective safety net to detect unintended behavioral regressions
- If tests are missing, prompt Claude Code to generate baseline characterization tests first
- Re-running tests immediately after refactoring confirms that application contracts remain intact

---

<!-- layout: 2-column -->
# Quiz 3 of 3: Discussion

### Prompt
A test suite fails after Claude Code modifies a core utility module. To make the test pass, Claude Code proposes a diff that modifies the test assertion instead of fixing the utility module.

### Discuss
- Why is modifying test assertions a dangerous default when diagnosing test failures?
- How should a developer evaluate whether the test or the production code is incorrect?
- What corrective prompt should the developer provide to Claude Code?

---

<!-- layout: 2-column -->
# Quiz 3: Discussion Points

**Claude Code proposes altering a test assertion to resolve a test failure.**

### Strong Answers Mention
- Changing assertions masks underlying defects and weakens test regression guarantees
- Verify original business requirements and specifications before accepting test modifications
- Reject the proposed diff and instruct Claude Code: “The test assertion represents the required contract; fix the production logic in the utility module instead”
- Re-run the full test suite after fixing production logic to verify no side effects occurred

### Watch For
- “If the test passes, the code is ready for production”
- Allowing Claude Code to weaken test assertions without verifying intended requirements
- Failing to inspect diffs when Claude Code edits files in `tests/`

---

# Questions and Answers

Questions?

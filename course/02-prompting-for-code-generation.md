<!-- course-title: Introduction to Claude Code -->
<!-- course-theme: roi-alt-theme -->

<!-- layout: title -->
![ROI Logo](images/roi-logo-with-name.png)

Introduction to Claude Code

# Chapter 2: Prompting for Code Generation

---

# Chapter 2: Objectives

- Prompt Claude Code to scaffold project files and generate feature code
- Craft effective, context-rich prompts for accurate code generation
- Generate and coordinate multi-file project architectures across source trees
- Inspect, review, and approve proposed file modifications safely
- Direct Claude Code to generate project code and verify the output

---

<!-- layout: navigation -->
# Chapter 2

- **Effective Prompting in Claude Code**
- Generating Multi-File Projects
- Inspecting and Approving File Changes
- Lab: Generating Code with Claude Code

---

<!-- layout: 2-column -->
# Prompting an Agent vs a Chatbot

### Conversational Chatbots
- Generate isolated code blocks in a web chat window
- Require manual copy-pasting into your local files
- Cannot verify file existence or existing project styles
- Treat each query as a text-completion request

### Claude Code CLI Agent
- Inspects your codebase before generating any code
- Writes and modifies files directly on your local disk
- Follows existing naming patterns and project conventions
- Executes local shell tools to validate its output

<!-- below-columns -->

> [!NOTE]
> In Claude Code, prompts are action requests for an autonomous agent, not just requests for code snippets.

---

<!-- layout: card-layout -->
# Anatomy of a High-Precision Prompt

### Core Objective
- State the exact feature, utility, or data model to build.
- Name the expected behavior and operational purpose clearly.

### Explicit Boundaries
- Specify exact file paths and module target locations.
- Define which libraries, frameworks, or versions to use.

### Quality Constraints
- Mandate error handling, type annotations, and docstrings.
- Declare acceptance criteria and functions that must be exported.

---

<!-- layout: 2-column -->
# Prompt Evolution: Vague vs Directed

### Vague Prompt
- `“Build a weather script”`
- Generates arbitrary dependencies
- Places files in unexpected locations
- Misses error handling and edge cases
- Requires multiple rounds of cleanup

### Directed Prompt
- `“Create src/weather.py using urllib and json”`
- Declares exact module location and dependencies
- Requests `parse_args()` and type hints
- Specifies graceful handling of `HTTPError`
- Produces production-ready code immediately

<!-- below-columns -->

> [!TIP]
> Tell Claude Code what file to create, what libraries to use, and how to handle errors to avoid unexpected implementation choices.

---

# Interactive Multi-Turn Prompting

- **Iterative refinement**: Break complex features into sequential conversational turns
  - Turn 1: Scaffold base data types and function signatures
  - Turn 2: Implement core business logic and error handling
  - Turn 3: Add input validation and CLI argument parsing
- **Targeted guidance**: Steer Claude Code with specific corrective instructions between turns

```text
> Create src/weather.py with a fetch_weather(city: str) function using urllib.request.
  Do not install external dependencies. Return a typed dictionary.

Claude Code:
Inspecting project root...
Created src/weather.py with fetch_weather function.

> Now add a main() function with argparse supporting --city and --units flags.
```

---

# Grounding Prompts with Local Context

- **Referencing project files**: Name existing files directly in your prompt to anchor context
  - Claude Code reads referenced files automatically to align with current patterns
  - Prevents the agent from re-inventing existing helper utilities or data types
- **Quoting error messages**: Paste terminal stack traces directly into interactive turns
  - Directs the agent to the exact failing line and module
  - Allows Claude Code to inspect the surrounding code and propose targeted remedies

> [!NOTE]
> You do not need to paste the full content of existing files into your prompt. Simply referencing the relative path gives Claude Code the access it needs.

---

<!-- layout: navigation -->
# Chapter 2

- Effective Prompting in Claude Code
- **Generating Multi-File Projects**
- Inspecting and Approving File Changes
- Lab: Generating Code with Claude Code

---

<!-- layout: card-layout -->
# Planning Multi-File Architectures

### Modular Separation
- Divide responsibilities across dedicated files for models, services, and interfaces.
- Keep data definitions decoupled from business logic and presentation layers.

### Project Conventions
- Match existing folder hierarchies such as `src/`, `pkg/`, or `internal/`.
- Maintain consistent file naming patterns across all newly created modules.

### Manifest Alignment
- Ensure all new dependencies are declared in package configuration files.
- Align entry points with `pyproject.toml`, `package.json`, or root scripts.

---

# Scaffolding Projects with Structured Prompts

- **Comprehensive layout requests**: Define the multi-file architecture in a single directive
  - Claude Code plans the file creation sequence and executes each creation step
  - Ensures clean import paths and shared interface definitions from the start

```bash
# Prompt Claude Code to scaffold a cohesive multi-file project
claude -p "Scaffold a task management CLI in src/:
- src/models.py: Task dataclass with id, title, and completed status
- src/storage.py: JSON file persistence functions load_tasks() and save_tasks()
- src/cli.py: argparse entry point with add, list, and complete commands
Include type hints and docstrings across all modules."
```

> [!IMPORTANT]
> When requesting multi-file projects, explicitly list each intended file path and its core responsibility in the initial prompt.

---

<!-- layout: 2-column -->
# Coordinating Module Boundaries

### Data Contracts First
- Define models and dataclasses in `src/models.py`
- Establish clear type definitions before writing logic
- Prevents downstream consumer modules from guessing field names

### Dependent Services
- Import defined types into `src/storage.py` and `src/cli.py`
- Validate that method signatures accept and return agreed data models
- Guarantees clean separation of concerns across files

<!-- below-columns -->

> [!TIP]
> Ask Claude Code to create shared data models first, then generate service and interface layers in subsequent steps.

---

<!-- layout: 3-column -->
# Multi-File Failure Modes

### Circular Imports
- Modules importing each other mutually
- Causes runtime import failures
- Fix by isolating shared types in a dedicated model file

### Orphaned Modules
- Creating helper files that no entry point ever calls
- Clutters source repositories
- Fix by specifying entry point wiring in your prompt

### Missing Exports
- Submodules omitting public symbols or `__all__` lists
- Leads to unresolved import warnings
- Fix by directing Claude to export top-level APIs cleanly

---

# Incremental Construction Pattern

- **Avoid the all-at-once trap**: Generating ten files simultaneously increases hallucination risk
  - The model may invent non-existent functions across distant modules
  - Reviewing massive multi-file changes overwhelms the developer
- **Adopt an incremental pipeline**: Build and verify layer by layer
  - Step 1: Generate foundational models and storage layer
  - Step 2: Verify imports and execute a basic sanity check
  - Step 3: Prompt for the CLI entry point and user-facing commands

> [!TIP]
> Keep generation steps focused on 2 to 3 related files at a time. This keeps diffs reviewable and minimizes interface mismatches.

---

<!-- layout: navigation -->
# Chapter 2

- Effective Prompting in Claude Code
- Generating Multi-File Projects
- **Inspecting and Approving File Changes**
- Lab: Generating Code with Claude Code

---

<!-- layout: 2-column -->
# The Terminal Diff Review Loop

### Proposed Modifications
- Claude Code presents unified color-coded diffs before modifying files
- Green lines with `+` denote additions
- Red lines with `-` denote deletions
- Unchanged context lines provide location orientation

### Human Authorization
- The agent halts execution and awaits your explicit decision
- Requires deliberate approval before saving edits to disk
- Prevents accidental overwrites of existing application logic

<!-- below-columns -->

> [!IMPORTANT]
> The diff review prompt is your primary safeguard. Never approve a diff without inspecting the proposed changes line by line.

---

# Reading Terminal Diffs Accurately

- **Unified diff anatomy**: Understand the components of Claude Code diff previews
  - Target file path and modification type (create, edit, or delete)
  - Hunk headers indicating target line numbers and surrounding context
  - Added and removed lines showing exact proposed modifications

```text
Claude Code wants to edit src/models.py:

@@ -10,6 +10,10 @@ class Task:
     id: int
     title: str
     completed: bool = False
+    priority: str = "medium"
+
+    def is_urgent(self) -> bool:
+        return self.priority.lower() == "high"

Allow this change? (y/n/e)
```

---

<!-- layout: 3-column -->
# Review Responses: Accept, Steer, or Reject

### Accept (`y`)
- Proposed code meets all requirements
- No unintended edits or side effects
- Writes changes to disk and continues task execution

### Steer (`e` or feedback)
- Proposed logic is close but needs adjustment
- Provide feedback to redirect the agent
- Claude Code recalculates the diff based on input

### Reject (`n`)
- Implementation is flawed or off-target
- Halts the proposed modification immediately
- Preserves original file contents on disk untouched

---

<!-- layout: card-layout -->
# Safe Review Verification Checklist

### Targeted Scope
- Verify that the diff modifies only the requested files.
- Watch for accidental changes to unrelated configuration files.

### Interface Integrity
- Confirm that existing function signatures and return types are preserved.
- Ensure existing callers will not break when changes apply.

### Clean Code Practices
- Check that temporary debug statements and print logs are removed.
- Verify that no API secrets or credentials have been hardcoded.

---

# Handling Flawed Changes and Rollbacks

- **Interrupting undesirable execution**: Press `Ctrl+C` once to halt active tool runs
  - Stops Claude Code before it begins generating unneeded files
  - Keeps the interactive session open so you can re-prompt immediately
- **Leveraging version control**: Rely on git as your safety net
  - Use `git status` and `git diff` outside or within Claude Code to inspect state
  - Revert unintended changes quickly using `git checkout -- <file>` or `git restore`

> [!CAUTION]
> If Claude Code produces unintended file modifications, do not attempt to fix them with vague follow-ups. Reject the change or revert via git, then provide explicit constraints.

---

<!-- layout: navigation -->
# Chapter 2

- Effective Prompting in Claude Code
- Generating Multi-File Projects
- Inspecting and Approving File Changes
- **Lab: Generating Code with Claude Code**

---

# Generating Code with Claude Code

Lab link: TODO

---

# What You Learned

- Prompted Claude Code to scaffold project files and generate feature code
- Crafted effective, context-rich prompts for accurate code generation
- Generated and coordinated multi-file project architectures across source trees
- Inspected, reviewed, and approve proposed file modifications safely
- Directed Claude Code to generate project code and verified the output

---

# Quiz 1 of 3

**Which prompt produces the most reliable and accurate code generation when using Claude Code?**

- A. `“Write an authentication system for this application that is secure”`
- B. `“Create src/auth.py with an authenticate_user function using bcrypt, returning a UserSession dataclass”`
- C. `“Make this codebase better by adding modern features and clean code”`
- D. `“Generate ten files for our user registration flow and decide on the libraries yourself”`

---

# Quiz 1: Answer

**Which prompt produces the most reliable and accurate code generation when using Claude Code?**

**Correct: B.** `“Create src/auth.py with an authenticate_user function using bcrypt, returning a UserSession dataclass”`

- Specifies the exact target path (`src/auth.py`) rather than guessing directory structure
- Names the target function and algorithm (`authenticate_user` with `bcrypt`)
- Defines explicit return data types (`UserSession` dataclass) to establish contracts
- Avoids vague slogans that lead to unpredictable third-party dependencies

---

# Quiz 2 of 3

**What should you do when Claude Code presents a terminal diff that contains an unintended file edit?**

- A. Approve the change anyway and fix the mistake manually later in an external editor
- B. Exit your terminal and reinstall Claude Code from scratch
- C. Reject the change or provide corrective feedback explaining what to adjust
- D. Delete the repository and re-clone it from GitHub

---

# Quiz 2: Answer

**What should you do when Claude Code presents a terminal diff that contains an unintended file edit?**

**Correct: C.** Reject the change or provide corrective feedback explaining what to adjust

- Claude Code pauses at every file modification to keep the human developer in control
- Rejecting (`n`) leaves the file system untouched and allows you to give redirection instructions
- Providing specific feedback guides Claude Code to generate a revised, accurate diff
- Approving flawed changes creates compounding errors across subsequent steps

---

<!-- layout: 2-column -->
# Quiz 3 of 3: Discussion

### Prompt
Your team is using Claude Code to scaffold a new multi-file microservice. A developer enters a single high-level prompt asking for a complete project, and Claude Code immediately proposes creating eight files at once.

### Discuss
- What architectural and code quality risks occur when generating eight files simultaneously?
- How should the developer break down this task into an iterative prompting workflow?
- What verification steps should be performed before approving changes at each step?

---

<!-- layout: 2-column -->
# Quiz 3: Discussion Points

**A developer enters a single broad prompt and Claude Code proposes creating eight files simultaneously.**

### Strong Answers Mention
- High risk of circular imports, inconsistent interface contracts, or phantom helper utilities
- Scaffolding incrementally: data models and storage first, followed by services, then entry points
- Reviewing diffs in smaller chunks (2 to 3 files) to maintain thorough inspection standards
- Running local syntax checks or test commands between generation phases to catch defects early

### Watch For
- “Approving all files at once saves time and we can test it at the very end”
- Assuming the agent automatically resolves all cross-module dependencies without guidance
- Overlooking package manifest dependencies or entry point wiring

---

# Questions and Answers

Questions?

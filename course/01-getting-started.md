<!-- course-title: Introduction to Claude Code -->
<!-- course-theme: roi-alt-theme -->

<!-- layout: title -->
![ROI Logo](images/roi-logo-with-name.png)

Introduction to Claude Code

# Chapter 1: Getting Started with Claude Code

---

# Chapter 1: Objectives

- Launch Claude Code and navigate command-line project workflows
- Understand Claude Code architecture, capabilities, and terminal integration
- Navigate Claude Code CLI commands and interactive session controls
- Initialize project directories and establish project context for Claude Code
- Launch Claude Code in the terminal and initialize a new project workspace

---

<!-- layout: navigation -->
# Chapter 1

- **Introduction to Claude Code**
- CLI Navigation and Commands
- Project Initialization and Context
- Lab: Starting Claude Code and Initializing a Project

---

# Terminal-Native Agentic Coding

- **Direct shell integration**: Claude Code operates inside your local terminal environment
  - Runs directly where your compilers, linters, and git branches already live
  - Eliminates the friction of copying snippets between browser windows and editors
- **Autonomous tool execution**: Plans and carries out multi-step engineering tasks
  - Searches project trees, inspects code symbols, and edits files in place
  - Executes shell commands and evaluates terminal outputs to verify its work

> [!NOTE]
> Claude Code combines the analytical reasoning of Claude models with direct command-line access to local development environments.

---

<!-- layout: 2-column -->
# Browser Chat vs Terminal Agent

### Browser-Based Chat
- Isolated from your local file system
- Requires manually copying code back and forth
- Lacks visibility into build or test results
- Cannot verify file paths or project dependencies

### Claude Code CLI
- Directly navigates repository file trees
- Applies targeted edits and creates project files
- Runs test suites and inspects exit codes
- Maintains context across multiple shell commands

<!-- below-columns -->

> [!TIP]
> Claude Code eliminates manual context transfer by reading your codebase directly from disk.

---

<!-- layout: card-layout -->
# Core Capabilities

### Codebase Discovery
- Navigates repository hierarchies and locates definitions across source files.
- Identifies relevant files automatically without requiring manual file uploads.

### In-Place Editing
- Produces precise line diffs to update existing functions and modules.
- Creates new files and directories while respecting established naming conventions.

### Shell Verification
- Executes unit tests and linter commands directly in the active project shell.
- Analyzes stderr output and stack traces to resolve issues iteratively.

---

# Human-in-the-Loop Safety Model

- **Explicit user authorization**: Claude Code requests permission before modifying files or running commands
  - Color-coded diffs display proposed file changes before writes occur
  - Shell commands show exact arguments and target paths before execution
- **Safe read-only defaults**: Directory navigation and file searches execute automatically
  - Inspecting files and reading git history proceed without interruption
  - Write operations, script executions, and system modifications require confirmation

> [!IMPORTANT]
> Always review proposed file diffs and bash commands before approving them, especially when commands affect disk state or git history.

---

<!-- layout: navigation -->
# Chapter 1

- Introduction to Claude Code
- **CLI Navigation and Commands**
- Project Initialization and Context
- Lab: Starting Claude Code and Initializing a Project

---

# Launching Claude Code Sessions

- **Interactive mode**: Launching `claude` opens an ongoing collaborative conversation
  - Ideal for exploratory coding, debugging, and iterative multi-step features
- **Single-prompt mode**: The `-p` flag executes a query and returns directly to your shell
  - Useful for quick explanations, git commit messages, or pipeline integration

```bash
# Navigate to your project directory and start an interactive session
cd ~/projects/payment-service
claude

# Or run a single query and exit immediately
claude -p "Explain the auth flow defined in src/auth.py"
```

---

<!-- layout: 2-column -->
# Interactive Session Controls

### Keystroke Shortcuts
- `Ctrl+C`: Interrupts current thinking or running tool calls without terminating the session
- `Ctrl+D` or `/exit`: Cleanly exits the Claude Code interactive session
- `Esc`: Cancels active prompt editing or returns to previous menus
- `Shift+Enter`: Inserts a newline for multi-paragraph prompts

### Session Management
- Interactive turns keep conversational memory within the current terminal run
- Pressing `Ctrl+C` once halts execution and returns to the prompt
- Pressing `Ctrl+C` twice exits Claude Code completely

<!-- below-columns -->

> [!TIP]
> If Claude Code begins an unneeded file search or lengthy tool command, press `Ctrl+C` once to halt the action and redirect the agent.

---

<!-- layout: 3-column -->
# Essential Slash Commands

### Session State
- `/clear`: Resets active conversation history and starts a fresh session
- `/compact`: Condenses prior conversation history to conserve token context
- `/exit`: Terminates the interactive session and returns to shell

### Configuration
- `/init`: Analyzes repository structure and scaffolds a `CLAUDE.md` guide
- `/config`: Views and modifies user preferences and runtime options
- `/doctor`: Diagnoses network, authentication, and toolchain health

### Diagnostics
- `/cost`: Summarizes total token consumption and API expenses
- `/review`: Initiates a code review of changes made during the session
- `/help`: Displays available slash commands and usage descriptions

---

# Managing Context Window and Costs

- **Context window accumulation**: Every prompt, file read, and tool output occupies context tokens
  - As sessions expand, larger contexts increase latency and cost per query
  - Very long sessions can degrade model precision on specific tasks
- **Compacting conversation memory**: Use `/compact` to preserve key decisions while freeing space
  - Summarizes prior discussions and retained file paths into a condensed overview
  - Maintains task context without paying for raw outputs from earlier commands

> [!WARNING]
> Monitor session size using `/cost`. If a session spans multiple unrelated tasks, use `/clear` to start fresh with zero token overhead.

---

<!-- layout: navigation -->
# Chapter 1

- Introduction to Claude Code
- CLI Navigation and Commands
- **Project Initialization and Context**
- Lab: Starting Claude Code and Initializing a Project

---

<!-- layout: card-layout -->
# Project Context Discovery

### Root Detection
- Locates `.git` markers and project manifests to determine repository boundaries.
- Resolves all relative file paths from the detected project root.

### Ecosystem Inspection
- Identifies languages, package managers, and dependencies automatically.
- Recognizes configurations such as `package.json`, `pyproject.toml`, or `go.mod`.

### Targeted Search
- Scans files on demand rather than pre-indexing your entire hard drive.
- Respects `.gitignore` rules to exclude dependencies and build outputs.

---

# Bootstrapping Projects with `/init`

- **Automatic project inspection**: Running `/init` analyzes repository structure and tooling
  - Detects runtime versions, testing frameworks, and linter configurations
  - Scaffolds a starter `CLAUDE.md` file customized for your project
- **Shared project memory**: Generated guidelines persist across sessions and team members

```text
> /init
Analyzing project structure...
Found: TypeScript project with npm, vitest, and eslint
Detected test command: npm test
Detected build command: npm run build
Created CLAUDE.md in project root.
```

> [!NOTE]
> Run `/init` when first introducing Claude Code to a repository, then commit `CLAUDE.md` to version control for your team.

---

<!-- layout: 2-column -->
# Crafting Effective `CLAUDE.md` Files

### High-Value Instructions
- Precise test commands: `pytest tests/unit/ -v`
- Strict build commands: `npm run build`
- Architecture boundaries: `Never import ORM models inside UI components`
- Code styling conventions: `Use snake_case for Python utility functions`

### Common Anti-Patterns
- Pasting full code files or redundant API reference docs
- Generic slogans such as `write clean and readable code`
- Outdated commands that conflict with active configuration files
- Storing secrets, passwords, or personal access tokens

<!-- below-columns -->

> [!TIP]
> Keep `CLAUDE.md` concise and operational. Claude reads this file on every session start, so every line should provide actionable guidance.

---

# Working Directory Hygiene

- **Launch from project root**: Always run `claude` from the top-level directory of your repository
  - Ensures accurate relative paths when referencing nested modules
  - Prevents accidental edits outside the intended project boundary
- **Leverage `.gitignore`**: Claude Code respects `.gitignore` rules automatically
  - Excludes `node_modules`, `.venv`, and build artifacts from searches
  - Keeps context tokens focused on source files rather than generated files

> [!CAUTION]
> Never start Claude Code inside a parent directory containing untrusted scripts, sensitive user data, or unrelated proprietary repositories.

---

<!-- layout: navigation -->
# Chapter 1

- Introduction to Claude Code
- CLI Navigation and Commands
- Project Initialization and Context
- **Lab: Starting Claude Code and Initializing a Project**

---

# Starting Claude Code and Initializing a Project

Lab link: TODO

---

# What You Learned

- Launched Claude Code and navigated command-line project workflows
- Understood Claude Code architecture, capabilities, and terminal integration
- Navigated Claude Code CLI commands and interactive session controls
- Initialized project directories and established project context for Claude Code
- Launched Claude Code in the terminal and initialized a new project workspace

---

# Quiz 1 of 3

**How does Claude Code interact with your local development environment during a task?**

- A. It runs in a remote sandbox and cannot view local project files
- B. It reads local files, proposes targeted edits, and executes shell commands with user approval
- C. It automatically commits and pushes all changes to GitHub without asking
- D. It replaces your shell and prevents using native command-line utilities

---

# Quiz 1: Answer

**How does Claude Code interact with your local development environment during a task?**

**Correct: B.** It reads local files, proposes targeted edits, and executes shell commands with user approval

- Claude Code operates directly in your local terminal workspace
- Read operations allow the agent to explore files and inspect project structure
- Write operations and command executions require explicit user confirmation by default
- It complements existing command-line tools rather than replacing them

---

# Quiz 2 of 3

**What is the primary role of the `CLAUDE.md` file in a project repository?**

- A. It stores user authentication tokens and API secret keys
- B. It serves as a lock file to prevent multiple terminal sessions
- C. It provides persistent instructions, build commands, and conventions for Claude Code
- D. It compiles source code into executable binary packages

---

# Quiz 2: Answer

**What is the primary role of the `CLAUDE.md` file in a project repository?**

**Correct: C.** It provides persistent instructions, build commands, and conventions for Claude Code

- Claude Code loads `CLAUDE.md` to understand project-specific commands and conventions
- It specifies exact build, test, and lint commands so the agent runs the correct tools
- Committing `CLAUDE.md` ensures all team members and agent sessions share identical standards
- Sensitive credentials should never be committed to `CLAUDE.md`

---

<!-- layout: 2-column -->
# Quiz 3 of 3: Discussion

### Prompt
Your team is onboarding Claude Code across multiple existing repositories. Developers are debating whether to maintain detailed `CLAUDE.md` files or rely entirely on Claude’s automatic project detection.

### Discuss
- What limitations exist when relying solely on automatic detection?
- What essential instructions should be codified in `CLAUDE.md` from day one?
- How should teams balance concise instructions against comprehensive documentation?

---

<!-- layout: 2-column -->
# Quiz 3: Discussion Points

**Your team is debating whether to maintain `CLAUDE.md` files or rely entirely on automatic project detection.**

### Strong Answers Mention
- Automatic detection identifies package managers but misses project-specific test flags and workflow rules
- Crucial day-one items: primary test runner command, build step, linter command, and architecture constraints
- Keeping `CLAUDE.md` brief avoids consuming unnecessary context window tokens on every turn
- Treating `CLAUDE.md` as version-controlled code that evolves with repository changes

### Watch For
- Treating `CLAUDE.md` as an exhaustive software manual instead of operational agent guidance
- Assuming Claude Code can automatically divine team-specific conventions or forbidden library imports
- Storing confidential API tokens or environment secrets inside `CLAUDE.md`

---

# Questions and Answers

Questions?

# Starting Claude Code and Initializing a Project

## Time Required

15 minutes

## Overview

In this lab, you will launch Claude Code, navigate interactive session controls, and initialize project context for a new development workspace. You will inspect toolchain health using diagnostics, practice session management with slash commands, bootstrap project configuration with `/init`, and craft an operational `CLAUDE.md` guide.

### You learn how to:
- Launch Claude Code in interactive and single-prompt modes.
- Navigate interactive session controls and execute essential slash commands.
- Manage conversation state and token context with compacting and clearing.
- Initialize project context using `/init` to generate and customize `CLAUDE.md`.

## Scenario

Your team is beginning development on a new project named `task-tracker`. Rather than manually copying code snippets between browser windows and re-explaining project conventions in every prompt, you need a terminal-native workflow. You will establish the project workspace, verify your Claude Code environment, and configure persistent project guidelines in `CLAUDE.md`.

## Lab Instructions

### Task 1: Create a project workspace and verify your environment

In this task, you create a dedicated project directory and verify your Claude Code installation and authentication health.

1. Open your terminal.

2. Create and navigate into a new directory named `task-tracker`:

```bash
mkdir -p ~/projects/task-tracker
cd ~/projects/task-tracker
```

3. Initialize a Git repository for the project:

```bash
git init
```

4. Create a `.gitignore` file to exclude common dependencies and environment files:

```bash
cat << 'EOF' > .gitignore
node_modules/
dist/
.env
.DS_Store
EOF
```

> [!NOTE]
> Claude Code respects `.gitignore` rules automatically. This prevents the agent from reading generated build artifacts or third-party packages, keeping your token context focused on source files.

5. Run the Claude Code doctor command from your shell to confirm your CLI environment and credentials:

```bash
claude doctor
```

> [!TIP]
> The `claude doctor` command checks CLI version compatibility, network reachability, and authentication status before you start an active session.

### Task 2: Launch an interactive session and explore navigation controls

In this task, you launch Claude Code in interactive mode, practice navigation shortcuts, and manage session memory with slash commands.

1. Launch an interactive Claude Code session from your project directory:

```bash
claude
```

2. Display the available slash commands and shortcuts:

```text
/help
```

3. Run the in-session diagnostic command to view your active session configuration:

```text
/doctor
```

4. Submit a simple prompt to observe how Claude Code reads your workspace:

```text
What files currently exist in this directory?
```

> [!NOTE]
> Claude Code automatically reads your repository tree to discover existing files. Read-only exploration proceeds without prompting for confirmation.

5. Check the accumulated token usage and estimated cost for your current session:

```text
/cost
```

6. Compact the conversation history to condense earlier turns and conserve context tokens:

```text
/compact
```

7. Reset your conversation history to return to a clean slate without exiting the CLI:

```text
/clear
```

### Task 3: Bootstrap project context and craft a CLAUDE.md guide

In this task, you use the `/init` slash command to scaffold project guidelines, then customize `CLAUDE.md` with operational commands and architecture rules.

1. In your active Claude Code session, initialize project context:

```text
/init
```

> [!NOTE]
> Claude Code scans your workspace, detects your repository structure, and scaffolds a starter `CLAUDE.md` file in the project root.

2. Exit the interactive session:

```text
/exit
```

3. Inspect the contents of the generated `CLAUDE.md` file:

```bash
cat CLAUDE.md
```

4. Replace the contents of `CLAUDE.md` with explicit instructions, build commands, and coding standards for the `task-tracker` project:

```markdown
# CLAUDE.md

## Build and Test Commands
- Run tests: `npm test`
- Build project: `npm run build`
- Run linter: `npm run lint`

## Architecture and Code Style
- Project type: Node.js and TypeScript console utility
- Code style: Use camelCase for variable names and PascalCase for TypeScript classes
- Modularity: Keep business logic separated from CLI input handling
- Safety: Never store secrets, passwords, or API keys in repository files
```

> [!IMPORTANT]
> Keep `CLAUDE.md` concise and operational. Claude Code loads this file at the start of every session, so every line should provide actionable rules rather than generic advice.

### Task 4: Execute single-prompt queries and verify human-in-the-loop safety

In this task, you use single-prompt mode for quick command-line tasks and observe how Claude Code enforces human-in-the-loop confirmation before creating files.

1. Run a single-prompt query to verify that Claude Code reads your updated `CLAUDE.md`:

```bash
claude -p "Summarize the test and build commands specified in CLAUDE.md"
```

2. Query your repository structure using single-prompt mode:

```bash
claude -p "What files exist in the project and what does CLAUDE.md instruct regarding safety?"
```

> [!NOTE]
> The `-p` flag executes your query, outputs the response to stdout, and exits immediately back to your shell.

3. Launch an interactive session to observe user authorization on file modifications:

```bash
claude
```

4. Ask Claude Code to create a starter `package.json` file for the project:

```text
Create a minimal package.json file for task-tracker with a test script set to "echo 'no tests yet'; exit 0"
```

5. Review the proposed file diff displayed in your terminal before approving it.

> [!WARNING]
> Always inspect proposed file modifications and shell commands carefully before confirming them, especially when changes affect files or repository history.

6. Confirm the file creation when prompted by Claude Code.

7. Terminate the session:

```text
/exit
```

### Bonus Task 5: Version control your project memory

With fewer step-by-step instructions, commit your project configuration to Git so teammates and future sessions share identical guidance.

1. Review your Git status to see untracked files:

```bash
git status
```

2. Stage `.gitignore`, `CLAUDE.md`, and `package.json`:

```bash
git add .gitignore CLAUDE.md package.json
```

3. Ask Claude Code in single-prompt mode to suggest a standard conventional commit message:

```bash
claude -p "Suggest a conventional commit message for adding project configuration, .gitignore, and CLAUDE.md"
```

4. Commit the staged files using your chosen commit message:

```bash
git commit -m "chore: initialize project configuration and CLAUDE.md guidelines"
```

5. Confirm that your working directory is clean:

```bash
git status
```

## Congratulations!

In this lab, you have:
- Launched Claude Code in interactive and single-prompt modes.
- Navigated interactive session controls and executed essential slash commands.
- Managed conversation state and token context with compacting and clearing.
- Initialized project context using `/init` to generate and customize `CLAUDE.md`.

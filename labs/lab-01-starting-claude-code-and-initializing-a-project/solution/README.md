# Solution: Starting Claude Code and Initializing a Project

## End State

- A local project directory named `~/projects/task-tracker` initialized as a Git repository.
- A `.gitignore` file excluding `node_modules/`, `dist/`, `.env`, and OS metadata files.
- An operational `CLAUDE.md` configuration file defining build and test commands, architecture boundaries, and code styling rules.
- A minimal `package.json` file scaffolded through Claude Code with human-in-the-loop review and approval.
- An initial Git commit containing the project configuration and baseline instructions.

## How to Verify

1. Verify the project directory and Git commit history:

```bash
cd ~/projects/task-tracker
git status
git log -1 --oneline
```

Expected: Working tree is clean, with the configuration commit recorded.

2. Inspect the contents of `CLAUDE.md`:

```bash
cat CLAUDE.md
```

Expected: The file defines build commands (`npm test`, `npm run build`, `npm run lint`) and architecture and style guidelines.

3. Verify that Claude Code reads project instructions in single-prompt mode:

```bash
claude -p "What test command is specified in CLAUDE.md?"
```

Expected: Claude Code responds with `npm test` as instructed in `CLAUDE.md`.

4. Run CLI diagnostics:

```bash
claude doctor
```

Expected: All diagnostic checks for authentication, permissions, and network connectivity report healthy.

## Built With

- Claude Code CLI (verified March 2025)
- Git 2.x
- Node.js 20+
- Unverified: Specific local authentication providers (tested against standard Anthropic API key and Claude Pro subscription auth)

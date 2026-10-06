# Notes: the formats this folder follows

Read on 2026-10-06 from the official pages. Each file in this folder,
then the lines it rests on.

## skills/frame/SKILL.md: the skill (Agent Skills standard)

https://agentskills.io/specification

> A skill is a directory containing, at minimum, a `SKILL.md` file

> The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

> `name` | Yes | Max 64 characters. Lowercase letters, numbers, and hyphens only. Must not start or end with a hyphen.

> Must not contain consecutive hyphens (`--`)
> Must match the parent directory name

> `description` | Yes | Max 1024 characters. Non-empty. Describes what the skill does and when to use it.

Checked with the reference validator the page names
(`skills-ref`, 0.1.1): `agentskills validate skills/frame` prints
`Valid skill`. A copy in a folder named `Frame-bad` fails with
`Directory name 'Frame-bad' must match skill name 'frame'`, so the
check does catch a wrong name.

## .claude-plugin/plugin.json: the Claude Code plugin

https://code.claude.com/docs/en/plugins/manifest-reference

> Save the manifest at `.claude-plugin/plugin.json` under the plugin root. Put every other plugin file at the plugin root, not inside `.claude-plugin/`. That includes `skills/`, `commands/`, and `hooks/`.

> `name` is the only required key.

> Skills | `skills/` | One `<name>/SKILL.md` per skill.

`claude plugin validate --strict .claude-plugin/plugin.json` passes
(Claude Code 2.1.289).

## plugin.json: the Codex and ChatGPT plugin (Agent Plugins schema)

https://developers.openai.com/codex/plugins/build

> For a portable Agent Plugins package, add `plugin.json` at the plugin root and declare the Agent Plugins schema.

> Existing `.codex-plugin/plugin.json` files remain supported as a compatibility fallback.

> Portable packages discover skills from the root skills/ directory

The schema at https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
requires `$schema` and `name`; `name` matches its pattern.

## .claude-plugin/marketplace.json: the catalog both tools read

https://code.claude.com/docs/en/plugin-marketplaces

> A plugin marketplace is a directory or repository with a `.claude-plugin/marketplace.json` file that lists your plugins and where to fetch each one.

> The file requires a `name`, an `owner`, and a `plugins` array.

https://developers.openai.com/codex/plugins/build

> The ChatGPT desktop app can read marketplace files from:
> - a repo marketplace at `$REPO_ROOT/.agents/plugins/marketplace.json`
> - a legacy-compatible marketplace at `$REPO_ROOT/.claude-plugin/marketplace.json`

`claude plugin validate --strict .` passes. With this folder added as a
local marketplace, under a throwaway settings folder for each tool:
`claude plugin install frame@agent-receipts` installs it and
`claude plugin details frame` lists `Skills (1) frame`;
`codex plugin add frame@agent-receipts` (codex-cli 0.160.0) installs it
and `codex plugin list` shows `installed, enabled 1.0.0`.

## frame.zip: the upload for Claude.ai and ChatGPT

https://support.claude.com/en/articles/12512180-using-skills-in-claude

> Navigate to Customize > Skills

> Package your skill folder as a ZIP file

> Skills are available for users on Free, Pro, Max, Team, and Enterprise plans.

> This feature requires code execution to be enabled

https://help.openai.com/en/articles/20001066-skills-in-chatgpt

> Upload a skill: Go to Skills, select Create, then select Upload from your computer.

> Skills are available to eligible ChatGPT Business, Enterprise, Healthcare, and Edu users, subject to workspace settings and product availability.

The zip holds one folder, `frame/`, with `SKILL.md` inside.

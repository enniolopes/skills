# skills

[![validate](https://github.com/enniolopes/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/enniolopes/skills/actions/workflows/validate.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENCE)

Portable capabilities for AI assistants.

Pick a capability, install it in your AI, and describe the job you want done. Standalone skills follow the open [Agent Skills](https://agentskills.io) format so the same capability can work across compatible hosts.

## Quick start

1. **Choose a capability** below.
2. **Install it** using the shortest path for your AI.
3. **Ask for the outcome you want.** You usually do not need special commands.

For example:

> Use Branding Studio to audit this existing brand, preserve valid equity, and recommend what should change.

## Choose a capability

| Capability | Type | Use it for |
|---|---|---|
| [**Branding Studio**](skills/branding-studio/) | Skill | Create, audit, apply, and evolve brands, identity systems, naming, positioning, and brand books. |
| [**Landing Page**](skills/landing-page/) | Skill | Research, design, build, redesign, and refine high-end marketing landing pages and homepages. |
| [**Explorer**](skills/explorer/) | Skill | Find non-obvious, defensible connections, hypotheses, analogies, and alternatives before deciding. |
| [**Research**](systems/research/) | System | Run rigorous scientific research with method, persistent research state, exploration, and independent review. |

### Example prompts

**Branding Studio**
> Create a professional brand system for this company from the material I provided. Inspect what is already true before asking me questions.

**Landing Page**
> Design and build a landing page for this product from the existing repo, product context, and business goals.

**Explorer**
> Explore non-obvious connections between X and Y. Give me the strongest defensible hypotheses and the test that would distinguish each one.

**Research**
> Start a research project on whether X affects Y. Help me formulate the question, define what would refute it, and proceed rigorously.

## Install

### ChatGPT

For a standalone Skill, where Skills are available on your account:

1. Open **Plugins** in the sidebar.
2. Open the **Skills** tab.
3. Select **Create → Upload from your computer**.
4. Upload the skill ZIP from [GitHub Releases](https://github.com/enniolopes/skills/releases).

Workspace admins can also import this repository as a plugin marketplace from **Workspace settings → Plugins → Add → Import marketplace** using:

```text
https://github.com/enniolopes/skills
```

### Claude Code

Add the marketplace once:

```text
/plugin marketplace add enniolopes/skills
```

Then install what you want:

```text
/plugin install branding-studio@enniolopes
/plugin install landing-page@enniolopes
/plugin install explorer@enniolopes
/plugin install research@enniolopes
```

### Gemini CLI

Standalone Skills can be installed directly from this repository:

```bash
gemini skills install https://github.com/enniolopes/skills.git --path skills/<name>
```

For example:

```bash
gemini skills install https://github.com/enniolopes/skills.git --path skills/branding-studio
```

### Deep Code

Standalone Skills are discovered from Agent Skills directories. Install the chosen `skills/<name>/` directory at either:

```text
~/.agents/skills/<name>/        # user-level
.deepcode/skills/<name>/        # project-level
```

### Other Agent Skills hosts

Install the chosen `skills/<name>/` directory using the host's normal Agent Skills flow.

> **Note:** standalone Skills are the most portable unit. A **System** composes multiple pieces, so installation support can vary by host. `research` currently installs as a plugin through the repository marketplace in supported plugin hosts.

## Skill, Agent, or System?

You do not need to know the repository architecture to use these. The distinction is simple:

- **Skill** — a reusable capability that gives your AI specialized expertise or a workflow. Example: Branding Studio.
- **Agent** — an independent specialist role, usually used when separate context, tools, authority, or review matter.
- **System** — several Skills and/or Agents that are meant to work together as one product. Example: Research.

Choose by the outcome you need; the type mainly tells you how the capability is packaged.

## Using a capability

After installation, describe the task normally. On hosts that support automatic Skill activation, the AI can select the relevant Skill when your request matches it. You can also name the capability explicitly when you want to make the intent unambiguous.

Give it the real material whenever possible: files, repositories, existing documents, source data, current designs, or business context. These capabilities are designed to inspect available reality instead of making you restate everything manually.

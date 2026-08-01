# Contributing to sec-toolkit

Thanks for helping keep this list useful. This document describes the bar for adding or updating an entry.

## What belongs here

Tools a security practitioner would actually reach for during authorized work: penetration tests, red-team engagements, purple-team exercises, security assessments, and incident response. Defensive tooling is included because modern engagements are rarely offense-only.

## What does not belong here

- Commercial-only tools with no free tier
- Tools with no public source or distribution
- Anything primarily malicious in intent (ransomware builders, credential stealers, botnet kits)
- Duplicates of tools already listed
- Tools that have been archived for over a year with no functional replacement value

Dual-use tools (C2 frameworks, post-exploitation kits) are included with a one-line context note.

## Entry format

Every entry follows this shape:

```markdown
* [Name](https://github.com/owner/repo) — One-sentence description. When to reach for it.
```

Optional suffixes:

- Maintenance note: `*Unmaintained since YYYY; still works for X.*` for tools that are stable but no longer actively developed
- Context note for dual-use tools: `*C2 framework. Use only in authorized engagements.*`

## How to propose a change

1. **Broken link or outdated description?** Open an issue using the "Broken link / outdated entry" template. Even better: open a PR with the fix.
2. **New tool?** Open an issue using the "New tool suggestion" template. Include the GitHub URL, a one-sentence description, and which section it belongs to. If it's a dual-use tool, note that explicitly.
3. **New section?** Open an issue first to discuss placement. Don't open a PR that adds a new top-level section without prior discussion.

## PR requirements

- One logical change per PR
- Markdown must pass `markdownlint`
- All links must be `https://` unless the destination genuinely only supports `http://`
- Description must be a single sentence, present tense, no marketing language ("best", "awesome", "amazing")
- No emojis in the description body

## Style

- Use sentence case for section headers
- Alphabetize entries within each section
- Keep descriptions under 140 characters where possible
- Use the `—` em-dash between the link and the description

## Review process

The maintainer reviews PRs weekly. If a PR sits for more than two weeks without a response, ping the thread once. Hostile or spam PRs will be closed without comment.

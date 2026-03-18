# Brantham Brain

Searchable knowledge base for Brantham Partners. Contains decisions, bug fixes, patterns, strategies, session logs, and deal intelligence.

## Quick Start (for collaborators)

### 1. Clone

```bash
git clone https://github.com/bxq7gv2vds-ctrl/brantham-vault.git
cd brantham-vault
```

### 2. Install QMD

```bash
npm install -g @tobilu/qmd
```

QMD is a local semantic search engine over markdown files. It runs fully offline — no API keys needed.

**Requirements:** Node.js 18+. First run downloads small ML models (~1.6 GB total, cached locally).

### 3. Index the vault

```bash
# Register this folder as a collection
qmd collection add vault . "**/*.md"

# Add context (improves search quality)
qmd context add vault "Brantham Partners knowledge base — strategic decisions, resolved bugs, reusable patterns, architecture docs, M&A deal intelligence, session logs"

# Generate embeddings (first time takes ~2 min)
qmd embed
```

### 4. Search

```bash
# Natural language query (recommended — hybrid search + reranking)
qmd query "how does the scoring pipeline work"

# Keyword search (fast, exact)
qmd search "BODACC procedures"

# Semantic search (meaning-based)
qmd vsearch "deal enrichment strategy"

# Read a specific document
qmd get vault/brantham/patterns/agent-decision-quality.md
```

### 5. Stay up to date

```bash
# Pull latest notes and re-index
./update.sh
```

Or manually:

```bash
git pull
qmd update
qmd embed
```

## For AI Agents (Claude Code, Cursor, etc.)

QMD exposes an MCP server for AI integration:

```bash
# Start MCP server (stdio transport)
qmd mcp
```

Add to your Claude Code MCP config (`~/.claude/mcp_servers.json`):

```json
{
  "qmd": {
    "command": "qmd",
    "args": ["mcp"]
  }
}
```

Then your AI agent can search the brain directly via MCP tools (`query`, `get`, `multi_get`).

## Update Script

Run `./update.sh` to pull the latest changes and re-index. That's it.

## Structure

```
vault/
  _system/          # Master indexes (MOCs), templates
  brantham/         # Brantham Partners — pipeline, agents, deals, bugs, patterns
  website/          # Website / SEO Machine
  founder/          # Strategic decisions, assumptions, journal
  patterns/         # Cross-project reusable patterns
  reports/          # Generated reports
```

## Notes

- All content is markdown — readable without any tooling
- QMD indexes and embeddings are local (`.qmd/` and `~/.cache/qmd/`) — not in the repo
- Updates are pushed automatically by the vault owner

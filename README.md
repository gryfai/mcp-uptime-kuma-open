# mcp-uptime-kuma-open

This is the open version of our Uptime Kuma MCP server.
It is open to for personal use and small companies
can freely use this internally for their operations. See our license for more information.
This version is released under the BSL license. We do provide a hosted solution with more
functionality baked in to the closed source version. If you want the more advanced version,
please contact us on hello (at) gryfai.com

The repository is still active and we will add to it continously.
We are painfully aware that we lack testing, but we have tested it with a couple of clients.
It is all good to go! Writing tests is the next thing on our agenda.

# The open version
This version is exposing a limited but useful set of tools to interact with
Uptime Kuma via your favorite LLM tool.

This server provide these functions:
- Retrieval of monitor status, both all and individual
- Get monitor beats
- Retrieval of notifications, both all and individual
- Retrieval of status pages, both all and individual
- Retrieval of heartbeats
- Retrieval of tags, both all and individual
- Retrieval of database size
- Retrieval of status page maintenance.

All of these are read-only in the open version.

We are releasing this open version under BSL with change license to Apache 2.0 in the future.
Both to provide you with excellent tools but also make sure that the time and effort we invest in
maintaining this repository is not being abused.
You may of course develop a competing open source service by yourself. We encourage competition and open source.
We are only regulating the code base so that our codebase is not used in a competing SaaS or other projects for monetary gain.

#  Want more?
GryfAi has a more powerful version of this that can be hosted via our solution.
It includes capabilities such as
- Adding, editing and deleting monitors
- Adding, editing and deleting notifications
- Adding, editing and deletion of tags
- Maintenance functionality
- Docker functionality
- API-key management
- Proxy management

Just contact us at: hello (at) gryfai.com

# Installation and usage (end users).
Install locally, set env vars, then let your MCP client launch the STDIO server. You usually don’t need to run it manually unless debugging.

1. Create and activate a virtual environment (Python 3.10+). When activated, `python` points to the venv interpreter.
2. Install the package inside that venv: `pip install .` (or `uv pip install .`).
3. Configure environment variables for your Uptime Kuma instance:
   - `UPTIME_KUMA_URL` (default: `http://localhost:3001`)
   - `UPTIME_KUMA_USERNAME`
   - `UPTIME_KUMA_PASSWORD`
4. Point your MCP client to the command `python -m mcp_uptime_kuma_open.server` (examples below). If your client runs outside the venv, give the full path to the venv’s python (e.g. `.venv/bin/python -m mcp_uptime_kuma_open.server`). The client will spawn it over STDIO.

Client notes (all use STDIO; keys match current client docs):

Gemini CLI
- Add a server entry in your Gemini CLI MCP config (per current docs, `mcpServers` in `~/.config/gemini/cli.json`):
```
{
  "mcpServers": {
    "uptime-kuma": {
      "command": "python -m mcp_uptime_kuma_open.server"
    }
  }
}
```
- Restart or reload the CLI so it picks up the new server.

Codex CLI
- Add a STDIO server entry in your Codex config (current releases use `mcpServers` in `codex.yaml`):
```
mcpServers:
  uptime-kuma:
    command: ["python", "-m", "mcp_uptime_kuma_open.server"]
```
- Save and restart the Codex CLI to load the server.

Claude CLI
- Add the MCP server to your Claude CLI config (current format: `mcpServers` in `~/.config/anthropic/claude/config.json`):
```
{
  "mcpServers": {
    "uptime-kuma": {
      "command": "python -m mcp_uptime_kuma_open.server"
    }
  }
}
```
- Run `claude` as normal; it will launch the STDIO server automatically.

Claude Desktop
- Open MCP settings and add a new STDIO server:
  - Name: `uptime-kuma`
  - Command: `python -m mcp_uptime_kuma_open.server`
- Save, then re-open a conversation to activate the server.

We also offer a commercial HTTP/SSE version that can provide better performance. Feel free to use the open STDIO version under the provided license, or contact us if you prefer the hosted HTTP/SSE option.

Please know that the installation instructions might change. Compare with the latest version of your client and adjust variables.
We know that some clients sometimes behaves better if you run it straight in the venv.
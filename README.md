# agentforge-federation-plugin

Test rig for the AgentForge frontend federation/iframe surface (TAP-765).

The plugin serves a minimal HTML widget at `/api/federation-test/widget`.
`PluginFrame.tsx` renders that route inside an `<iframe>` — this plugin
exercises that surface without requiring Vite Module Federation or any
external bundling step.

## What it provides

| Surface | Value |
|---|---|
| Widget route | `GET /api/federation-test/widget` — HTML with `data-testid` markers |
| Status route | `GET /api/federation-test/status` — JSON health probe |
| Nav entry | label "Federation Test", icon "Globe", route "/federation-test" |
| Agent | `federation-test-agent` under `project.federation-test` namespace |
| Runner | `FederationRunner.run()` returns `"federation:ok"` — deterministic, no LLM |

## Install

```bash
# From the plugin directory
uv pip install -e .

# Or from the AgentForge project to run the backend smoke tests
uv pip install -e /path/to/agentforge-federation-plugin
uv run pytest backend/tests/test_federation_smoke.py -v
```

## Dev

```bash
cd agentforge-federation-plugin
uv sync --group dev
uv run pytest
```

## Widget HTML markers

The widget HTML includes `data-testid` attributes for test targeting:

- `federation-widget` — root div
- `federation-version` — version string paragraph
- `federation-status` — status paragraph (text: "ready")

The widget also posts a `postMessage` to the parent window:

```js
{ type: "federation-ready", version: "<version>" }
```

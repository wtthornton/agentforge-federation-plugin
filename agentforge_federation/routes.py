"""Federation plugin HTTP routes.

GET /api/federation-test/widget  — minimal HTML widget for PluginFrame iframe mount
GET /api/federation-test/status  — health/version probe
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from agentforge_federation import __version__

router = APIRouter(prefix="/api/federation-test", tags=["federation-test"])


def _build_widget_html(version: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Federation Widget</title></head>
<body>
  <div id="federation-root" data-testid="federation-widget">
    <h1>Federation Widget</h1>
    <p data-testid="federation-version">agentforge-federation-plugin v{version}</p>
    <p data-testid="federation-status">ready</p>
  </div>
  <script>
    window.parent.postMessage({{ "type": "federation-ready", "version": "{version}" }}, "*");
  </script>
</body>
</html>"""


@router.get("/status")
async def status() -> dict:
    return {"status": "ok", "plugin": "federation-test", "version": __version__}


@router.get("/widget", response_class=HTMLResponse)
async def widget() -> HTMLResponse:
    return HTMLResponse(_build_widget_html(__version__))

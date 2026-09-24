"""
Swagger UI view — serves a self-contained Swagger UI page at the root URL.
The OpenAPI spec is inlined as a JavaScript object so no extra static
file configuration is required.
"""

import json
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .openapi import OPENAPI_SPEC


@ensure_csrf_cookie
def swagger_ui(request):
    """Serves the Swagger UI HTML page at http://127.0.0.1:8000/"""

    spec_json = json.dumps(OPENAPI_SPEC, indent=2)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>User & Role Management API — Swagger UI</title>
  <meta name="description" content="Interactive Swagger UI for the User & Role Management REST API." />

  <!-- Swagger UI CDN -->
  <link rel="stylesheet"
        href="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui.css" />

  <style>
    /* ── Base reset ─────────────────────────────────────────────── */
    *, *::before, *::after {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      font-family: "Inter", "Segoe UI", sans-serif;
      background: #0f1117;
      color: #e2e8f0;
      min-height: 100vh;
    }}

    /* ── Hero header ────────────────────────────────────────────── */
    .api-hero {{
      background: linear-gradient(135deg, #1a1f36 0%, #0d1b2a 50%, #111827 100%);
      border-bottom: 1px solid rgba(99,102,241,0.25);
      padding: 36px 48px 28px;
      position: relative;
      overflow: hidden;
    }}

    .api-hero::before {{
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 60% 80% at 10% 50%, rgba(99,102,241,0.12) 0%, transparent 70%),
        radial-gradient(ellipse 40% 60% at 90% 20%, rgba(16,185,129,0.08) 0%, transparent 70%);
      pointer-events: none;
    }}

    .hero-inner {{
      position: relative;
      display: flex;
      align-items: center;
      gap: 20px;
      max-width: 1400px;
      margin: 0 auto;
    }}

    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(99,102,241,0.15);
      border: 1px solid rgba(99,102,241,0.35);
      border-radius: 999px;
      padding: 6px 16px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #818cf8;
      margin-bottom: 10px;
    }}

    .hero-badge .dot {{
      width: 8px; height: 8px;
      background: #10b981;
      border-radius: 50%;
      box-shadow: 0 0 6px #10b981;
      animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50%       {{ opacity: 0.5; transform: scale(1.4); }}
    }}

    .hero-content h1 {{
      margin: 0 0 6px;
      font-size: clamp(22px, 4vw, 34px);
      font-weight: 800;
      background: linear-gradient(90deg, #e0e7ff 0%, #818cf8 50%, #10b981 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      line-height: 1.2;
    }}

    .hero-content p {{
      margin: 0;
      color: #94a3b8;
      font-size: 14px;
      max-width: 600px;
    }}

    .hero-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 18px;
    }}

    .pill {{
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.05em;
    }}
    .pill-green  {{ background: rgba(16,185,129,0.15); color: #10b981; border: 1px solid rgba(16,185,129,0.3); }}
    .pill-blue   {{ background: rgba(59,130,246,0.15); color: #60a5fa; border: 1px solid rgba(59,130,246,0.3); }}
    .pill-purple {{ background: rgba(139,92,246,0.15); color: #a78bfa; border: 1px solid rgba(139,92,246,0.3); }}
    .pill-orange {{ background: rgba(251,146,60,0.15); color: #fb923c; border: 1px solid rgba(251,146,60,0.3); }}

    .hero-stats {{
      margin-left: auto;
      display: flex;
      gap: 32px;
      flex-shrink: 0;
    }}

    .stat {{
      text-align: center;
    }}
    .stat-value {{
      font-size: 28px;
      font-weight: 800;
      color: #818cf8;
      line-height: 1;
    }}
    .stat-label {{
      font-size: 11px;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      margin-top: 4px;
    }}

    /* ── Swagger UI container ───────────────────────────────────── */
    #swagger-ui-container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 24px 32px 64px;
    }}

    /* ── Swagger UI dark-mode overrides ────────────────────────── */
    .swagger-ui {{
      font-family: "Inter", "Segoe UI", sans-serif !important;
    }}

    .swagger-ui .topbar         {{ display: none; }}
    .swagger-ui .info           {{ display: none; }}   /* We have our own hero */

    /* Background */
    .swagger-ui .wrapper,
    .swagger-ui .scheme-container {{ background: transparent; box-shadow: none; }}

    /* Tag sections */
    .swagger-ui .opblock-tag {{
      background: rgba(30,35,60,0.6);
      border: 1px solid rgba(99,102,241,0.2);
      border-radius: 10px;
      margin-bottom: 6px;
      padding: 12px 18px;
      backdrop-filter: blur(8px);
      font-size: 15px;
      font-weight: 700;
      color: #c7d2fe !important;
      letter-spacing: 0.02em;
    }}

    .swagger-ui .opblock-tag:hover {{
      border-color: rgba(99,102,241,0.4);
      background: rgba(30,35,60,0.8);
    }}

    .swagger-ui .opblock-tag small {{
      color: #64748b;
      font-size: 12px;
      font-weight: 400;
    }}

    /* Operation blocks */
    .swagger-ui .opblock {{
      border-radius: 10px;
      border: 1px solid rgba(255,255,255,0.07);
      margin-bottom: 8px;
      background: rgba(20,24,40,0.7);
      backdrop-filter: blur(6px);
      overflow: hidden;
    }}

    .swagger-ui .opblock .opblock-summary {{
      border: none !important;
      padding: 10px 18px;
    }}

    .swagger-ui .opblock .opblock-summary-method {{
      border-radius: 6px;
      font-size: 12px;
      font-weight: 800;
      min-width: 68px;
      text-align: center;
      letter-spacing: 0.06em;
    }}

    .swagger-ui .opblock.opblock-get    {{ border-left: 3px solid #10b981; }}
    .swagger-ui .opblock.opblock-post   {{ border-left: 3px solid #818cf8; }}
    .swagger-ui .opblock.opblock-put    {{ border-left: 3px solid #f59e0b; }}
    .swagger-ui .opblock.opblock-delete {{ border-left: 3px solid #f43f5e; }}

    .swagger-ui .opblock.opblock-get    .opblock-summary-method {{ background: #10b981; }}
    .swagger-ui .opblock.opblock-post   .opblock-summary-method {{ background: #818cf8; }}
    .swagger-ui .opblock.opblock-put    .opblock-summary-method {{ background: #f59e0b; color: #1a1a1a; }}
    .swagger-ui .opblock.opblock-delete .opblock-summary-method {{ background: #f43f5e; }}

    .swagger-ui .opblock-summary-path {{
      color: #e2e8f0 !important;
      font-size: 13px;
      font-family: "JetBrains Mono", "Fira Code", monospace;
    }}

    .swagger-ui .opblock-summary-description {{
      color: #94a3b8 !important;
      font-size: 12px;
    }}

    .swagger-ui .opblock-body {{
      background: rgba(10,12,25,0.6);
      border-top: 1px solid rgba(255,255,255,0.06);
    }}

    /* Section header inside expanded operation (Try it out area) */
    .swagger-ui .opblock .opblock-section-header {{
      align-items: center;
      background: rgb(24 144 255 / 26%);
      box-shadow: 0 1px 2px rgba(0, 0, 0, .1);
      display: flex;
      min-height: 50px;
      padding: 8px 20px;
    }}

    /* Text and labels */
    .swagger-ui label,
    .swagger-ui .parameter__name,
    .swagger-ui .parameter__type,
    .swagger-ui table thead tr th,
    .swagger-ui .response-col_status,
    .swagger-ui h4, .swagger-ui h5,
    .swagger-ui .tab li,
    .swagger-ui select,
    .swagger-ui p,
    .swagger-ui .markdown p,
    .swagger-ui .markdown li {{
      color: #cbd5e1 !important;
    }}

    .swagger-ui input[type=text],
    .swagger-ui textarea,
    .swagger-ui select {{
      background: rgba(15,17,30,0.9) !important;
      border: 1px solid rgba(99,102,241,0.3) !important;
      color: #e2e8f0 !important;
      border-radius: 6px;
    }}

    .swagger-ui .btn.execute {{
      background: linear-gradient(135deg, #818cf8, #6366f1) !important;
      border: none !important;
      border-radius: 7px !important;
      font-weight: 700 !important;
      letter-spacing: 0.04em;
      padding: 8px 20px !important;
      box-shadow: 0 2px 12px rgba(99,102,241,0.4);
      transition: transform 0.15s, box-shadow 0.15s;
    }}

    .swagger-ui .btn.execute:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 18px rgba(99,102,241,0.55);
    }}

    .swagger-ui .btn.cancel {{
      background: rgba(244,63,94,0.15) !important;
      border: 1px solid rgba(244,63,94,0.4) !important;
      color: #f43f5e !important;
      border-radius: 7px !important;
    }}

    /* Tables */
    .swagger-ui table tbody tr td {{
      border-color: rgba(255,255,255,0.06);
      color: #94a3b8;
    }}

    .swagger-ui table.headers td {{
      border-color: rgba(255,255,255,0.06);
    }}

    /* Response codes */
    .swagger-ui .response-col_status {{
      font-weight: 700;
    }}

    /* Model section */
    .swagger-ui section.models {{
      border: 1px solid rgba(99,102,241,0.2);
      border-radius: 10px;
      background: rgba(20,24,40,0.6);
    }}

    .swagger-ui section.models h4 {{
      color: #818cf8 !important;
    }}

    /* Scrollbars */
    ::-webkit-scrollbar       {{ width: 7px; height: 7px; }}
    ::-webkit-scrollbar-track {{ background: #0f1117; }}
    ::-webkit-scrollbar-thumb {{ background: rgba(99,102,241,0.4); border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: rgba(99,102,241,0.7); }}
  </style>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap"
        rel="stylesheet" />
</head>

<body>

  <!-- ── Hero Header ─────────────────────────────────────────── -->
  <header class="api-hero">
    <div class="hero-inner">
      <div class="hero-content" style="flex:1">
        <div class="hero-badge">
          <span class="dot"></span>
          Live API &nbsp;·&nbsp; OpenAPI 3.0
        </div>
        <h1>User &amp; Role Management API</h1>
        <p>
          Full-featured Django REST API for user authentication, role-based access control,
          bulk operations, and module-level permission checks.
        </p>
        <div class="hero-pills">
          <span class="pill pill-green">Django 6.1</span>
          <span class="pill pill-blue">Session Auth</span>
          <span class="pill pill-purple">RBAC</span>
          <span class="pill pill-orange">SQLite</span>
        </div>
      </div>

      <div class="hero-stats">
        <div class="stat">
          <div class="stat-value">18</div>
          <div class="stat-label">Endpoints</div>
        </div>
        <div class="stat">
          <div class="stat-value">3</div>
          <div class="stat-label">Tag Groups</div>
        </div>
        <div class="stat">
          <div class="stat-value">8000</div>
          <div class="stat-label">Port</div>
        </div>
      </div>
    </div>
  </header>

  <!-- ── Swagger UI ───────────────────────────────────────────── -->
  <div id="swagger-ui-container">
    <div id="swagger-ui"></div>
  </div>

  <script src="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui-bundle.js"></script>
  <script src="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui-standalone-preset.js"></script>

  <script>
    const spec = {spec_json};

    // ── CSRF helpers ──────────────────────────────────────────────────────────
    // Reads the Django csrftoken cookie (set after GET /api/user/csrf/ is called)
    function getCsrfCookie() {{
      const match = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]+)/);
      return match ? decodeURIComponent(match[1]) : null;
    }}

    // Fetches the CSRF cookie from Django if we don't already have it
    async function ensureCsrfCookie() {{
      if (!getCsrfCookie()) {{
        await fetch("/api/user/csrf/", {{ credentials: "include" }});
      }}
    }}

    // Kick off the CSRF fetch as soon as the page loads
    ensureCsrfCookie();
    // ─────────────────────────────────────────────────────────────────────────

    window.onload = function () {{
      SwaggerUIBundle({{
        spec: spec,
        dom_id: "#swagger-ui",
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
        ],
        layout: "StandaloneLayout",
        deepLinking: true,
        displayRequestDuration: true,
        defaultModelsExpandDepth: -1,
        defaultModelExpandDepth: 2,
        docExpansion: "list",
        filter: true,
        tryItOutEnabled: true,

        requestInterceptor: async (req) => {{
          // Always send cookies (needed for Django session auth)
          req.credentials = "include";

          // For state-changing methods, attach the CSRF token automatically
          const method = (req.method || "GET").toUpperCase();
          if (["POST", "PUT", "PATCH", "DELETE"].includes(method)) {{
            await ensureCsrfCookie();
            const token = getCsrfCookie();
            if (token) {{
              req.headers["X-CSRFToken"] = token;
            }}
          }}
          return req;
        }}
      }});
    }};
  </script>

</body>
</html>
"""

    return HttpResponse(html, content_type="text/html")


def openapi_json(request):
    """Returns the raw OpenAPI spec JSON at /api/schema.json"""
    return HttpResponse(
        json.dumps(OPENAPI_SPEC, indent=2),
        content_type="application/json"
    )

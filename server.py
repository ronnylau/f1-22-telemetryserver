import http.server
from pathlib import Path


PORT = 20776

Handler = lambda *args: http.server.SimpleHTTPRequestHandler(
    *args, directory=str(Path(__file__).parent / "webapp")
)


def serve(org, token):
    with http.server.ThreadingHTTPServer(("", PORT), Handler) as httpd:
        print(
            f"Telemetry app URL: http://85.14.247:{PORT}/index.html?org={org}&token={token}"
        )

        httpd.serve_forever()

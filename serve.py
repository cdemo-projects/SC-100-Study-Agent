"""
SC-100 Study Dashboard Server
Serves the dashboard HTML, study progress JSON, and transcript search.
Run: python serve.py
Opens in VS Code Simple Browser or your default browser.
"""

import http.server
import json
import os
import re
import socketserver
import webbrowser
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT = 8100
BASE_DIR = Path(__file__).parent
TRANSCRIPTS_DIR = BASE_DIR / "transcripts"
PROGRESS_FILE = BASE_DIR / "study-progress.json"
QUESTION_BANK_FILE = BASE_DIR / "question-bank.json"


class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/" or parsed.path == "/dashboard":
            self.send_file(BASE_DIR / "dashboard.html", "text/html")

        elif parsed.path == "/data":
            self.send_file(PROGRESS_FILE, "application/json")

        elif parsed.path == "/questions":
            self.send_file(QUESTION_BANK_FILE, "application/json")

        elif parsed.path == "/search":
            query = parse_qs(parsed.query).get("q", [""])[0].lower().strip()
            if not query:
                self.send_json([])
                return
            results = search_transcripts(query)
            self.send_json(results)

        else:
            super().do_GET()

    def send_file(self, filepath, content_type):
        try:
            content = filepath.read_text(encoding="utf-8")
            self.send_response(200)
            self.send_header("Content-Type", f"{content_type}; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        except FileNotFoundError:
            self.send_error(404)

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def log_message(self, format, *args):
        pass  # Quiet logging


def search_transcripts(query, max_results=50):
    results = []
    transcript_files = []

    # Collect all transcript files
    if TRANSCRIPTS_DIR.exists():
        for f in sorted(TRANSCRIPTS_DIR.glob("*.txt")):
            transcript_files.append(f)
        playlist_dir = TRANSCRIPTS_DIR / "playlist"
        if playlist_dir.exists():
            for f in sorted(playlist_dir.glob("*.txt")):
                transcript_files.append(f)

    for filepath in transcript_files:
        try:
            lines = filepath.read_text(encoding="utf-8").splitlines()
            for line in lines:
                if query in line.lower():
                    # Extract timestamp
                    ts_match = re.match(r"\[(\d{2}:\d{2})\]", line)
                    timestamp = ts_match.group(1) if ts_match else "--:--"
                    text = re.sub(r"^\[\d{2}:\d{2}\]\s*", "", line)

                    # Highlight match
                    pattern = re.compile(re.escape(query), re.IGNORECASE)
                    highlighted = pattern.sub(lambda m: f"<mark>{m.group()}</mark>", text)

                    results.append({
                        "file": filepath.stem,
                        "timestamp": timestamp,
                        "text": text,
                        "highlighted": highlighted,
                    })
                    if len(results) >= max_results:
                        return results
        except Exception:
            continue

    return results


def main():
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"SC-100 Study Dashboard running at {url}")
        print("Press Ctrl+C to stop.\n")

        # Try to open in VS Code Simple Browser, fall back to default browser
        try:
            webbrowser.open(url)
        except Exception:
            pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nDashboard stopped.")


if __name__ == "__main__":
    main()

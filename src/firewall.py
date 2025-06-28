from flask import request, abort
import re

class Firewall:
    def __init__(self):
        self.app = None

    def init_app(self, app):
        self.app = app
        self.register_hooks()

    def register_hooks(self):
        @self.app.before_request
        def run_all_checks():
            self.block_known_bots()
            self.validate_payload()
            self.detect_injection()
            self.block_ip()

    def block_known_bots(self):
        ua = request.headers.get("User-Agent", "").lower()
        if any(bot in ua for bot in ["curl", "python", "httpclient", "scrapy"]):
            abort(403, "Bots are not allowed")

    def validate_payload(self):
        if request.content_length and request.content_length > 10000:
            abort(413, "Payload too large")
        if request.method not in ["GET", "POST"]:
            abort(405)

    def detect_injection(self):
        suspicious_patterns = [
            r"(--|\b(select|union|insert|drop|update|delete)\b)",
            r"<script>",
            r"['\"].*?['\"]"
        ]
        for value in request.values.values():
            for pattern in suspicious_patterns:
                if re.search(pattern=pattern, string=value, flags=re.IGNORECASE):
                    self.log_threat(value)
                    abort(400, "Suspicious input detected")

    def block_ip(self):
        blacklist = []
        if request.remote_addr in blacklist:
            abort(403)

    def log_threat(self, payload):
        with open("firewall_logs.txt", "a") as f:
            f.write(f"{request.remote_addr} --- {payload}\n")


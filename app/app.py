# — RetailPulse Flask Application 
import sys
from pathlib import Path
APP_DIR = str(Path(__file__).parent)
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

from flask import Flask, request, redirect
from blueprints.dashboard import dashboard_bp

app = Flask(__name__)
app.secret_key = 'retailpulse-2026-vibe'
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

# Enforce HTTPS
@app.before_request
def enforce_https():
    if not request.is_secure and request.headers.get('X-Forwarded-Proto', 'https') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

# Register Blueprints
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
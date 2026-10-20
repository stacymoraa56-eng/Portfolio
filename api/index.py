"""Vercel entry point. Vercel routes requests to this Flask application."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import app  # noqa: E402

# Vercel detects and serves this WSGI application.

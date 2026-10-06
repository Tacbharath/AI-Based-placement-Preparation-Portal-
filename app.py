import os
import sys

# Ensure backend and root are in path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from backend.app import app, create_app
from backend.config import Config

application = app
handler = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.PORT, debug=Config.DEBUG)


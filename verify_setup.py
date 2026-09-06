"""
Forwarder wrapper for verify_setup.py (moved to tests/verify_setup.py).
Allows running 'python verify_setup.py' from project root.
"""
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

if __name__ == "__main__":
    test_path = os.path.join(PROJECT_ROOT, "tests", "verify_setup.py")
    with open(test_path, "r", encoding="utf-8") as f:
        code = compile(f.read(), test_path, "exec")
        exec(code, {"__name__": "__main__", "__file__": test_path})

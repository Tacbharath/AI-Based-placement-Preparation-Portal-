import os
import sys
import socket

# Ensure root and backend directories are in sys.path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from backend.app import app
from backend.config import Config


def get_local_ip():
    """Dynamically detect the host computer's local IPv4 address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Does not actually transmit packets; connects to routable IP to find local interface
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        try:
            local_ip = socket.gethostbyname(socket.gethostname())
        except Exception:
            local_ip = "127.0.0.1"
    finally:
        s.close()
    return local_ip


if __name__ == "__main__":
    port = Config.PORT
    local_ip = get_local_ip()
    is_debug = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "t")

    print("\n" + "=" * 70)
    print(" PREPPORTAL — AI CAREER PREPARATION & PLACEMENT PLATFORM")
    print("=" * 70)
    print(f" [*] Development Computer (Localhost) : http://127.0.0.1:{port}")
    print(f" [*] Development Computer (LAN IP)    : http://{local_ip}:{port}")
    print(f" [*] Other Laptop / Devices on Wi-Fi  : http://{local_ip}:{port}")
    print("-" * 70)
    print(" [!] IMPORTANT NOTICE FOR OTHER LAPTOPS / PHONES:")
    print("     Do NOT type '127.0.0.1' on the other laptop. '127.0.0.1' points")
    print("     only to that laptop itself.")
    print(f"     Open your browser on the second laptop and visit:")
    print(f"     --> http://{local_ip}:{port}")
    print(f"     --> http://{local_ip}:{port}/admin/login")
    print("-" * 70)
    print(" [i] Server Host Binding : 0.0.0.0 (Listening on all network interfaces)")
    print(f" [i] Active Port         : {port}")
    print("=" * 70 + "\n")

    app.run(host="0.0.0.0", port=port, debug=is_debug)

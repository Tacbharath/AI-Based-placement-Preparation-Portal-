"""
PrepPortal SQLite -> MySQL Migration Launcher
Run: python migrate_to_mysql.py
"""

import os
import sys

# Ensure root in path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.database.migrate_sqlite_to_mysql import migrate_database

if __name__ == "__main__":
    success = migrate_database()
    if not success:
        sys.exit(1)

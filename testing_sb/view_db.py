import sys
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "storage" / "bot_users.db"

def view_db():
    if not DB_PATH.exists():
        print(f"[ERROR] Database not found at: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bot_users ORDER BY id")
    rows = cursor.fetchall()
    conn.close()

    print(f"DB: {DB_PATH}")
    print(f"Total rows: {len(rows)}\n")
    print(f"{'ID':<5} {'Email':<40} {'Password':<12} {'Created At'}")
    print("-" * 85)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<40} {row[2]:<12} {row[3]}")

if __name__ == "__main__":
    view_db()

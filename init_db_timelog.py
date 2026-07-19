import sqlite3

DATABASE = "worklog.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            event_time TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

            customer TEXT,
            address TEXT NOT NULL,

            state TEXT,
            site_state TEXT,

            billable INTEGER DEFAULT 0,

            notes TEXT,
            pictures TEXT
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
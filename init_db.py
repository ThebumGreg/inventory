import sqlite3
from pathlib import Path

# Ensure the instance directory exists
Path("instance").mkdir(exist_ok=True)

DATABASE = "instance/inventory.db"

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Create bins table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bin_name TEXT NOT NULL,
    location TEXT,
    description TEXT,
    photo_filename TEXT,
    qr_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Create items table
cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bin_id INTEGER NOT NULL,
    item_name TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(bin_id) 
        REFERENCES bins(id)
        ON DELETE CASCADE
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
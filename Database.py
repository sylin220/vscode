import sqlite3
from datetime import datetime

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("shipments.db")
cursor = conn.cursor()

# Create a shipments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS shipments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_number INTEGER,
    container_number TEXT,
    carrier TEXT,
    origin TEXT,
    destination TEXT,
    eta DATE,
    delivery_date DATE,
    status TEXT
)
""")
conn.commit()
conn.close()
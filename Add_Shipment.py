import sqlite3
import pandas as pd # type: ignore

df = pd.read_excel("Shipments.xlsx")

conn = sqlite3.connect("shipments.db")
cursor = conn.cursor()

# Select and arrange Excel columns
columns = [
    "SHIPMENT NUMBER",
    "CONTAINER ID",
    "CARRIER",
    "ORIGIN CITY",
    "NA PORT",
    "ETA",
    "Delivery date",
    "STATUS"
]

# Prepare data for SQLite
data = df[columns].copy()

# Convert dates to YYYY-MM-DD
for col in ["ETA", "Delivery date"]:
    data[col] = pd.to_datetime(
        data[col], errors="coerce"
    ).dt.strftime("%Y-%m-%d")

# Replace missing values with None
data = data.astype(object).where(pd.notna(data), None)

# Convert DataFrame rows into tuples
records = list(data.itertuples(index=False, name=None))

cursor.executemany("""
INSERT INTO shipments (
    shipment_number,
    container_number,
    carrier,
    origin,
    destination,
    eta,
    delivery_date,
    status
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", records)

conn.commit()
conn.close()
print("Shipment added!")
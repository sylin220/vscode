import sqlite3

conn = sqlite3.connect("shipments.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM shipments")
shipments = cursor.fetchall()

for shipment in shipments:
    print(shipment)

conn.close()

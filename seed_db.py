import sqlite3

conn = sqlite3.connect("instance/inventory.db")

cursor = conn.cursor()

#cursor.execute("""
#INSERT INTO bins (title, location, description)
#VALUES
#('Camping Gear','Garage Shelf A','Camping equipment'),
#('Christmas Decorations','Attic','Holiday decorations'),
#('Networking','Office Closet','Network equipment')
#""")

cursor.execute("""
INSERT INTO items (bin_id, name, quantity)
VALUES
(1,'Tent',1),
(1,'Lantern',2),
(1,'Sleeping Bag',3),
(2,'Christmas Tree',1),
(2,'Lights',4)
""")

conn.commit()
conn.close()

print("Database seeded.")
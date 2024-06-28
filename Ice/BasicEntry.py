import sqlite3
# Create a connection to the database
conn = sqlite3.connect("IceCream.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table to store ice cream values 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Varieties (
        id INTEGER PRIMARY KEY,
        name TEXT,
        season TEXT,
        allergens TEXT
    )
""")

#Inserting values to the table 
cursor.execute("""
    INSERT INTO Varieties (name, season, allergens)
    VALUES
        ('Hot Choco Fudge', 'Winter', 'Nuts,Milk'),
        ('Classic Death By Chocolate', 'Winter', 'Milk,Nut,Wheat'),
        ('Gudbud Sundae', 'Summer', 'Milk,nuts'),
        ('Lychee Sundae', 'Summer', 'Milk,nuts'),
        ('Natrually Jackfruit and dry fruit Sunday', 'Summer', 'Milk,nuts'),
        ('ButterScotch Ice', 'Rainy', 'Milk'),
        ('Cookie Monster Sundae', 'Rainy', 'Milk,nuts,wheat'),
        ('Blue Berry Bliss', 'Rainy', 'Milk,nuts,wheat')
""")

#Create allergy table 
cursor.execute("""
            CREATE TABLE IF NOT EXISTS Allergy (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT
            )
        """)
allergies = [
            (1, 'Milk', 'Signs and symptoms of milk allergy range from mild to severe and can include wheezing, vomiting, hives and digestive problems. Milk allergy can also cause anaphylaxis — a severe, life-threatening reaction.'),
            (2, 'Nuts', 'People with a nut allergy may experience the following symptoms after exposure to some or all types of nut: coughing stomach pain nausea sneezing diarrhea itching, particularly around the face and mouth'),
            (3, 'Wheat', 'Wheat allergy signs and symptoms include: Swelling, itching or irritation of the mouth or throat Hives, itchy rash or swelling of the skin Nasal congestion Headache Difficulty breathing'),
        ]
cursor.executemany("""
            INSERT INTO Allergy (id, name, description)
            VALUES (?,?,?)
        """, allergies)

#Create a table for the cart 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cart (
        cartid INTEGER PRIMARY KEY,
        iceid INTEGER,
        name TEXT,
        quantity INTEGER
    )
""")
# cursor.execute("SELECT * FROM Cart")
# a=cursor.fetchall()
# print(a)
cursor.execute("Delete from Allergy where id=4")
# Commit the changes
conn.commit()
# Close the connection
conn.close()
print("Database Setup Complete")

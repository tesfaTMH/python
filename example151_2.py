import sqlite3

create_table = """
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
"""

insert_values = """
INSERT INTO People VALUES(
    'Ron',
    'Obvious',
    42
);
"""
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute(create_table)
    cursor.execute(insert_values)
def hours():
    print('Open 9-5 daily')

import zoo
zoo.hours()


import zoo as menagerie
menagerie.hours()


#Sql stuff
import sqlite3
import csv

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
''')

with open('books2.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        cursor.execute(
            'INSERT INTO books VALUES (?, ?, ?)',
            (row[0], row[1], int(row[2]))
        )

conn.commit()
conn.close()

print("Data added successfully.")


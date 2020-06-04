
import sqlite3

#  ------- SQLite --------

# !IMPORTANT ---> used TablePlus to view SQL db table

# EXTRA:
# data types: integer, real(float), text, blob(stored exactly as it was input)

# | p.139 - 139 |

def create_phonebook():
    with sqlite3.connect('PhoneBook.db') as db:
        cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS PhoneBook(
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    surname text NOT NULL,
    number text NOT NULL);''')

    first_names = ['Simon', 'Karen', 'Darren', 'Anne', 'Mark']
    surnames = ['Howels', 'Phillips', 'Smith', 'Jones', 'Smith']
    numbers = ['123446543', '123456543', '234576543', '234554323', '23454323']

    for i in range(0, 5):
        cursor.execute('''INSERT INTO PhoneBook(id, first_name, surname, number)
          VALUES(?,?,?,?)''', (i + 1, first_names[i], surnames[i], numbers[i]))
        db.commit()

    db.close()

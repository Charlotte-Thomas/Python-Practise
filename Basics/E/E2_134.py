
import sqlite3

#  ------- SQLite --------

# !IMPORTANT ---> used TablePlus to view SQL db table

# EXTRA:
# data types: integer, real(float), text, blob(stored exactly as it was input)

# | p.140 - 139 |

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


# | p.140 - 140 |

def view_phonebook(cursor):
    cursor.execute('SELECT * FROM  PhoneBook')
    for x in cursor.fetchall():
        print(x)

def insert_phonebook(cursor, db):
    newId = input('enter ID number: ')
    first_name = input('enter first name: ')
    surname = input('enter surname: ')
    number = input('enter phone number: ')
    cursor.execute('''INSERT INTO PhoneBook(id, first_name, surname, number)
      VALUES(?,?,?,?)''', (newId, first_name, surname, number))
    db.commit()

def search(cursor):
    surname = input('enter surname to search for: ')
    cursor.execute('SELECT * FROM PhoneBook WHERE surname=?', [surname])
    print(cursor.fetchall())

def del_person(cursor, db):
    person = input('enter the ID of person you want to delete: ')
    cursor.execute(f'DELETE FROM PhoneBook WHERE id={person}')
    db.commit()

def phonebook_options():
    with sqlite3.connect('PhoneBook.db') as db:
        cursor = db.cursor()

    print('''    1) View phone book
    2) Add to phone book
    3) Search for surname
    4) Delete person from phone book
    5) Quit ''')

    choice = int(input('choose a number from the selection: '))
    if choice == 1:
        view_phonebook(cursor)
    elif choice == 2:
        insert_phonebook(cursor, db)
    elif choice == 3:
        search(cursor)
    elif choice == 4:
        del_person(cursor, db)
    elif choice == 5:
        return
    else:
        raise Exception('not a choice')
    db.close()

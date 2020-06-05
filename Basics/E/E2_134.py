
import sqlite3

#  ------- SQLite --------

# !IMPORTANT ---> used TablePlus to view SQL db table

# EXTRA:
# data types: integer, real(float), text, blob(stored exactly as it was input)

# | p.140 - 139 & 140 |

def create_phonebook():
    with sqlite3.connect('database/PhoneBook.db') as db:
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
    with sqlite3.connect('database/PhoneBook.db') as db:
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


# | p.140 - 141 |

def create_BookInfo():
    with sqlite3.connect('database/BookInfo.db') as db:
        cursor = db.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Authors(
    name text PRIMARY KEY,
    birth_place text NOT NULL);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Books(
    id integer PRIMARY KEY,
    title text,
    author text,
    date_published integer);''')
    
    authors = [['Agatha Christie', 'Torquay'], ['Cecelia Ahern', 'Dublin'], ['J.K Rowling', 'Bristol'], ['Oscar Wilde', 'Dublin']]
    books = [
      ['De Profundis', 3, 1905],
      ['Harry Potter and the chamber of secrets', 2, 1998],
      ['Harry Potter and the prisoner of Azkaban', 2, 1999],
      ['Lyrebird', 1, 2017],
      ['Murder on the Orient Express', 0, 1934],
      ['Perfect', 1, 2017]]

    for i in range(0, 4):
        cursor.execute('''INSERT INTO Authors(name, birth_place)
          VALUES(?,?)''', (authors[i][0], authors[i][1]))
        db.commit()
    for i in range(0, 6):
        cursor.execute('''INSERT INTO Books(ID, title, author, date_published)
          VALUES(?,?,?,?)''', (i + 1, books[i][0], authors[books[i][1]][0], books[i][2]))
        db.commit()

    db.close()


# | p.140 - 142 |

def search_place():
    with sqlite3.connect('database/BookInfo.db') as db:
        cursor = db.cursor()
    cursor.execute('SELECT * FROM authors')
    print(cursor.fetchall())

    place = input('enter authors place of birth: ').capitalize()
    cursor.execute('SELECT * FROM authors WHERE birth_place == ?', [place])
    authors = cursor.fetchall()
    for author in authors:
        cursor.execute('SELECT * FROM books WHERE author == ?', [author[0]])
        print(cursor.fetchall())


import csv

#  ------- CSV Files --------

# EXTRA:
# CSV = comma seperated values
# greater control of data stored than a text file as rows are split into columns
# codes: w, x, r & a


# | p.95 - 111 |

def create_csv():
    file = open('CSVs/Books.csv', 'w')
    books = ['To Kill A Mockingbird', 'A Brief History of Time', 'The Great Gatsby', 'The Man Who Mistook His Wife for a Hat', 'Pride and Prejudice']
    authors = ['Harper Lee', 'Stephen Hawking', 'F. Scott Fitzgerald', 'Oliver Sacks', 'Jane Austen']
    years = ['1960', '1988', '1922', '1985', '1813']

    for i in range(0, 5):
        file.write(books[i] + ',' + authors[i] + ',' + years[i] + '\n')
    file.close()


# | p.95 - 112 |

def append_csv():
    file = open('CSVs/Books.csv', 'a')
    book_name = str(input('Enter a book name: '))
    author = str(input('Enter author name: '))
    date = str(input('Enter year released: '))
    file.write(book_name + ',' + author + ',' + date + '\n')
    file.close()

    file = open('CSVs/Books.csv', 'r')
    reader = list(csv.reader(file))
    for row in reader:
        print(row)
    file.close()


# | p.95 - 114 |

def books_by_year():
    start_year = int(input('enter a start year: '))
    end_year = int(input('enter an end year: '))
    file = open('CSVs/Books.csv', 'r')
    reader = list(csv.reader(file))

    for row in reader:
        if start_year <= int(row[2]) <= end_year:
            print(row)
    file.close()


# | p.95 - 115 |

def display_data():
    file = open('CSVs/Books.csv', 'r')
    reader = list(csv.reader(file))
    for row in enumerate(reader):
        print(f'row {row[0]}: {row[1]}')
    file.close()


# | p.95 - 116 |

def overwrite_csv():
    file = open('CSVs/Books.csv', 'r')
    reader = list(csv.reader(file))
    copy = reader[:]
    display_data()
    delete = int(input('Enter the row number you want to delete: '))
    edit = int(input('enter the row number you want to edit: '))
    section = int(input('enter number of section you want to edit (0-2): '))
    new_data = input('enter new data: ')
    copy[edit][section] = new_data
    copy.pop(delete)
    file.close()

    file = open('CSVs/Books.csv', 'w')
    for row in copy:
        file.write(','.join(row) + '\n')
    file.close()
    display_data()

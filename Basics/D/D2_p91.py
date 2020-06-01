

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

    for i in range(0, 4):
        file.write(books[i] + ', ' + authors[i] + ', ' + years[i] + '\n')
    file.close()



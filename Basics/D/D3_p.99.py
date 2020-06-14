import csv
import random

#  ------- Subprograms --------

# | p.102 - 118 |


def get_num():
    num = int(input('enter a number: '))
    return num


def count():
    num = get_num()
    for number in range(1, num + 1):
        print(number)


# | p.102 - 120 |

def result(ans, correct):
    if ans == correct:
        print('Correct!')
    else:
        print(f'incorrect, the correct answer is: {correct}')

def add():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    correct = num1 + num2
    ans = int(input(f'{num1} + {num2} = '))
    result(ans, correct)

def subtract():
    num1 = random.randint(24, 50)
    num2 = random.randint(1, 25)
    correct = num1 - num2
    ans = int(input(f'{num1} - {num2} = '))
    result(ans, correct)

def display_option():
    choice = int(input(' 1) Addition \n 2) Subtraction \n enter 1 or 2: '))
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    else:
        print('not an option')
        

# | p.103 - 122 & 123 |


def append_file():
    name = input('enter name: ')
    salary = input('enter salary: ')
    file = open('CSVs/Salaries.csv', 'a')
    file.write(name + ',' + salary + '\n')
    file.close()
    return name + ',' + salary


def view_records():
    file = open('CSVs/Salaries.csv', 'r')
    reader = csv.reader(file)
    records = []
    for row in reader:
        records.append(row)
    file.close()
    return records


def del_record():
    records = view_records()
    for row in enumerate(records):
        print(f'row: {row[0]} - {row[1]}')
    choice = int(input('state row you want to delete: '))
    if 0 <= choice <= len(records):
        records.pop(choice)
        file = open('CSVs/Salaries.csv', 'w')
        for row in records:
            file.write(','.join(row) + '\n')
        file.close()
        return records
    raise Exception('please enter a correct row number')


def show_salary_options():
    print('''    1) Add to file
    2) View all records
    3) Delete a record
    4) Quit program ''')

    choice = int(input('choose a number from the selection: '))
    if choice == 1:
        new_record = append_file()
        print('new record added:' + ' ' + new_record)
    elif choice == 2:
        records = view_records()
        print(records)
    elif choice == 3:
        records = del_record()
        print(f'new records: {records}')
    elif choice == 4:
        return
    else:
        raise Exception('not a choice')

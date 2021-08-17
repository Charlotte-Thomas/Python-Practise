import math


def calculate_square_root(number):
    if isinstance(number, int):
        if number > 500:
            square_root = round(math.sqrt(number), 2)
            print(f"the sqaure root of {number} is {square_root}")
            return square_root
        raise Exception("please provide a number over 500")
    raise TypeError("Please provide a number argument")


def get_user_input():
    number = int(input("enter a number over 500: "))
    return number


def main():
    number = get_user_input()
    calculate_square_root(number)


if __name__ == "__main__":
    main()

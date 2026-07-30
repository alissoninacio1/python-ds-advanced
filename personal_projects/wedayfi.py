#datefinder
from datetime import date

# #statics code
# day: int = 8
# month: int = 9
# year: int = 1823

# #-> Instantiating a specific date (Year, Month, Day)
# exact_date = date(year, month, day)
# day_name = exact_date.strftime("%A")

# print(day_name)



def which_day():
    print()
    # convert the input strings into integers using the int() function before passing them to date().
    day: int = int(input("day: "))
    month: int = int(int(input("month: ")))
    year: int = int(input("year: "))


    exact_date = date(year, month, day)
    day_name = exact_date.strftime("%A")
    print(day_name)


def main():
    which_day()


if __name__ == "__main__":
    main()
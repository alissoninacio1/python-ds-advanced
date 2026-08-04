
#from datatime import datetime
#as dt is to simplify the code
from datetime import datetime as dt


def pass_gen(site: str):
    formatted = dt.now().strftime("%H%M")

    resumed_name = site.lower().replace(" ", "")[:3]
    adjusted_name = resumed_name[0].upper() + resumed_name[1:3]

    #If your goal is simply to turn a string like " john doe " into "Joh", Python has a built-in .capitalize() method:python# Removes spaces, grabs first 3 letters, capitalizes index 0
    #adjusted_name = name.replace(" ", "")[:3].capitalize()

    print(f"{site}{formatted}")


def main():
    
    site: str = str(input("Write your location: "))
    pass_gen(site)


if __name__ == "__main__":
    main()
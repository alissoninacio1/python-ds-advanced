def initial_name_letters(name):
    """
    This function takes a name as input and returns the initials of the name.
    
    Parameters:
    name (str): The full name of a person.
    
    Returns:
    str: The initials of the name in uppercase.
    """
    # Split the name into parts
    parts = name.split()
    
    # Get the first letter of each part and convert to uppercase
    # Get an empty string to store the initials, get the fisrt letter of each part, convert it to uppercase, and join them together
    # the split() method splits the name into parts based on whitespace, and the join() method combines the initials into a single string.
    # split creates a list of words in the name, and the list comprehension iterates over each word to extract the first letter and convert it to uppercase. 

    #feature to remove "complements" from words
    parts = [part for part in parts if part.lower() != "de"]

    initials = "".join(part[0].upper() for part in parts)
    
    print(f"The initials of the name '{name}' are: {initials}")


# using main function as in other languages this is the enter point
def main():
    name = str(input("Enter a full name: "))
    initial_name_letters(name)

if __name__ == "__main__":    
    main()


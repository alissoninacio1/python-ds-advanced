def name_formatter(name):
    """
    Formats a name string by capitalizing the first letter of each word.

    Args:
        name (str): The name string to format.

    Returns:
        str: The formatted name string.
    """
    name_formatted = ' '.join(word.capitalize() for word in name.split())
    print(f"The formatted name is: {name_formatted}")

def main():
    name = str(input("Enter a full name: "))
    name_formatter(name)

if __name__ == "__main__":    
    main()
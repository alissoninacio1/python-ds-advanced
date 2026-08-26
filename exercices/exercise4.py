name: str = "Alisson"
surname: str = "Inacio"

full_name = name + " " + surname

print(full_name)

def char_count():
    count = len(full_name.replace(" ", ""))#replacing white spaces with empty string to count only characters
    print("The full name has", count, "characters.")

    """
    #or try this raw approach to count characters without using len() function
    count = 0 
    for _ in full_name:
        count += 1
        print("The full name has", count, "characters.")
    """
    

print(full_name.upper())
print(full_name.lower())
char_count()


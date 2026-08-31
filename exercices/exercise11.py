def vowel_count(string):
    """
    Counts the number of vowels in a given string.

    Parameters:
    string (str): The input string to count vowels in.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print(f"The number of vowels in the string is: {count}")


vowel_count("Hello World!")
vowel_count("Python Programming")

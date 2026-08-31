def phrase_words_count(phrase):
    """
    Count the number of words in a given phrase.

    Parameters:
    phrase (str): The input phrase to count words from.

    Returns:
    int: The number of words in the phrase.
    """
    # Split the phrase into words using whitespace as the delimiter
    # Split a string into a list where each word is a list item
    words = phrase.split()
    
    # Return the number of words
    print(len(words))
    print(words) #this is a list of words in the phrase


phrase_words_count("Hello World!")
phrase_words_count("Python Programming is fun!")

def find_largest_word():
    """
    This function prompts the user to input a sentence and returns the largest word in that sentence.
    If there are multiple words with the same length, it returns the first one encountered.
    """
    sentence = input("Please enter a sentence: ")

    #string.split(separator, maxsplit)
    # separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
    # maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

    largest = max(sentence.split(), key=len)

    print(f"The largest word in the sentence is: '{largest}'")

find_largest_word()
def check_if_word_is_palindrome(word):

    word = word.lower().replace(" ", "")


    if word == word[::-1]:
        print(f"The word '{word}' is a palindrome.")
    else:
        print(f"The word '{word}' is not a palindrome.")


def main():
    word = str(input("Enter a word: "))
    check_if_word_is_palindrome(word)



if __name__ == "__main__":
    main()
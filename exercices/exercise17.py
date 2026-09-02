def char_letters_count(word, char):
    count = 0

    for c in word:
        if c == char:
            count += 1

    print(f"The character '{char}' appears {count} times in the word '{word}'.")


def main():
    word = str(input("Enter a word: "))
    char = str(input("Enter a character to count: "))

    char_letters_count(word, char)


if __name__ == "__main__":
    main()

def cleaning_text(word):
    word = word.lower().replace(" ", "")

    # ext.replace(" ", "") Removes all spaces everywhere.
    # text.strip()Removes spaces only at the start and end.

    print(f"Cleaned text: {word}")


def main():
    word = str(input("Enter a word: "))
    cleaning_text(word)


if __name__ == "__main__":
    main()


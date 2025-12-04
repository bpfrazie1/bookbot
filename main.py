import sys
from calendar import c

from stats import character_frequency, sort_character_frequency, word_count


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    char_freq = character_frequency(book_text)
    sorted_char_freq = sort_character_frequency(char_freq)
    print("============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words.\n")
    print("--------- Character Count -------\n")
    for tuple in sorted_char_freq:
        print(f"{tuple[0]}: {tuple[1]}")
    print("============= END ===============")


main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text_length = len(get_words(text))
    text_chars = get_letters(text)
    text_char_count = get_letter_count(text, get_letters(text))
    print(f"--- Begin report of {book_path} ---")
    print(f"{text_length} words found in the document")
    print()
    print()
    for char in text_char_count:
        print(f"The '{char}' character was found {text_char_count[char]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    return text.split()

def get_letters(text):
    word_list = get_words(text)
    letters = set()
    letters_list = []
    for word in word_list:
        for letter in word:
            letters.add(letter.lower())
    for letter in letters:
        letters_list.append(letter)
    return letters_list

def get_letter_count(text, char_list):
    char_count = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in char_list:
        if char in alphabet:
            count = 0
            for letter in text:
                if char == letter.lower():
                    count += 1
            char_count[char] = count
    return char_count




main()
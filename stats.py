def word_count(text):
    words = text.split()
    return len(words)


def character_frequency(text):
    characters = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            characters[char] = characters.get(char, 0) + 1
    return characters


def sort_character_frequency(characters):
    sorted_chars = sorted(characters.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars

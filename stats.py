def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_char_dict(char_dict):
    # Retourne une liste de dictionnaires triés du plus grand au plus petit
    sorted_items = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    return [{"char": char, "num": count} for char, count in sorted_items]

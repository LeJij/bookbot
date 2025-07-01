import sys
from stats import get_word_count, get_char_count, sort_char_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    word_count = get_word_count(text)
    char_counts = get_char_count(text)
    sorted_chars = sort_char_dict(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

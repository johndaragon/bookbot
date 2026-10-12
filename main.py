import sys
from stats import get_word_count, get_character_count, chars_dict_to_sorted_list

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(path_to_file: str, word_count: int, sorted_char: list[tuple[str,int]]):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for chars in sorted_char:
        if chars[0].isalpha():
            print(f"{chars[0]}: {chars[1]}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookbot = get_book_text(sys.argv[1])
    num_words = get_word_count(bookbot)
    num_char = get_character_count(bookbot)
    sorted_num_char = chars_dict_to_sorted_list(num_char)
    print_report(sys.argv[1],num_words,sorted_num_char)

main()

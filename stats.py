def get_word_count(book_text: str) -> int:
    book_split = book_text.split()
    word_count = len(book_split)
    return word_count

def get_character_count(book_text: str) -> dict[str,int]:
    book_text_lower = book_text.lower()
    chars = list(book_text_lower)
    char_count = {}
    for i in range(0,len(chars)):
        if chars[i] in char_count:
            char_count[chars[i]] += 1
        else:
            char_count[chars[i]] = 1
    return char_count

def sort_on(char_count: tuple[str,int]) -> int:
    return char_count[1]

def chars_dict_to_sorted_list(char_count: dict[str,int]) -> list[tuple[str,int]]:
    unsorted_list = []
    sorted_list = []
    for chars in char_count:
        dict_str = chars
        dict_int = char_count[chars]
        tuple_str_int = (dict_str,dict_int)
        unsorted_list.append(tuple_str_int)
    sorted_list = sorted(unsorted_list, key=sort_on,reverse=True)
    return sorted_list

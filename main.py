import sys

from stats import get_word_count, list_of_dicts, which_word


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def print_chars(char_array, word_count, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_array:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    word_count = get_word_count(book)
    word_dict = which_word(book)
    dict_list = list_of_dicts(word_dict)
    # print(dict_lit)
    print_chars(dict_list, word_count, path)


main()

def sort_on(dict):
    return dict["num"]


def get_word_count(book):
    book = book.split()
    return len(book)


def which_word(book):
    word_dict = {}
    for char in book:
        char = char.lower()
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1
    return word_dict


def list_of_dicts(dict_of_chars):
    dict_list = []
    for char in dict_of_chars:
        dict_list.append({"char": char, "num": dict_of_chars[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

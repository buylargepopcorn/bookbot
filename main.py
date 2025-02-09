def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    total_char = get_num_char(text)
    print(f"{num_words} words found in the document.")
    char_report(total_char)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def char_report(total_char):
    for char in total_char:
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {total_char[char]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
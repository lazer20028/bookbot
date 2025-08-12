import sys
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import count
from stats import count_characters



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    words_number = count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_number} total words")
    print("--------- Character Count -------")
    char_counts = count_characters(book_text)
    for item_dict in char_counts:
        print(f"{item_dict["char"]}: {item_dict["num"]}")
    print("============= END ===============")
main()

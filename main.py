from stats import book_wordcount
from stats import book_character_count
from stats import sort_characters
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {book_wordcount(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    book_characters = book_character_count(get_book_text(sys.argv[1]))
    sorted_characters = sort_characters(book_characters)
    for item in sorted_characters:
        if item["character"].isalpha():
            print(f"{item["character"]}: {item["count"]}")
    print("============= END ===============")

main()
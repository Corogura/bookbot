def book_wordcount(book_content):
    book_content = book_content.split()
    return len(book_content)

def book_character_count(book_content):
    characters = {}
    book_content = book_content.lower()
    for c in book_content:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sort_characters(book_characters):
    sorted_characters = []
    for c in book_characters:
        c = {
            "character": c,
            "count": book_characters[c]
        }
        sorted_characters.append(c)
    sorted_characters.sort(reverse=True, key=sort_key)
    return sorted_characters

def sort_key(dict):
    return dict["count"]
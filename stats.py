def count(text):
    x=len(text.split())
    return x


def sort_on(items):
    return items["num"]

def count_characters(text):
    dictionary={}
    for character in text:
        if character.isalpha():
            character = character.lower()
            if character in dictionary:
                dictionary[character] = dictionary[character] + 1
            else:
                dictionary[character]=1
    my_list = []
    for char, num in dictionary.items():
        my_list.append({"char": char,"num": num})
    my_list.sort(reverse=True, key=sort_on)
    return my_list
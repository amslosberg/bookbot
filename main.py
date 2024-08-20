def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    lower_case = file_contents.lower()
    num = count_words(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num} words found in the document\n")
    count_characters(lower_case)

def count_words(book):
    count = 0
    words = book.split()
    for word in words:
        count+=1
    return count

def count_characters(book):
    words = book.split()
    char = {}
    for word in words:
        for letter in word:
            if letter in char.keys():
                char[letter] += 1
            else:
                char[letter] = 1
   # print(char)
    sort_characters(char)
    print("--- End report ---")
def sort_on(dict):
    return dict["num"]

def sort_characters(dict):
    #sorted_list = dict.sort(reverse = True, key=sort_on)
    sorted_list = []
    for char in dict:
        if char.isalpha():
            temp_dict = {}
            temp_dict["num"] = dict[char]
            temp_dict["char"] = char
            sorted_list.append(temp_dict)
    sorted_list.sort(reverse = True, key=sort_on)
    for i in range(0,len(sorted_list)):
        num = sorted_list[i]["num"]
        char = sorted_list[i]["char"]
        print(f"The '{num}' character was found {char} times")

main()
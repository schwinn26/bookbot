#import the needed function(s) from stats.py
from stats import get_num_words
from stats import get_num_characters

def get_book_text(filepath):
    #set variable(s)
    file_contents=""

    #open the file
    with open(filepath) as f:
        file_contents = f.read()

    #return the contents of the file
    return file_contents

def main():
    #print the contents of the set txt file (commented out below line)
    #print(get_book_text('books/frankenstein.txt'))

    total_characters_dict = get_num_characters('books/frankenstein.txt')

    #print the number of words in the set txt file
    print(f"{get_num_words('books/frankenstein.txt')} words found in the document")
    
    print(total_characters_dict)

main()


#import the get_num_words function from stats.py
from stats import get_num_words

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

    #print the number of words in the set txt file
    print(f"{get_num_words('books/frankenstein.txt')} words found in the document")

main()


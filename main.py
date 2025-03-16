#import the needed function(s) from stats.py
from stats import get_num_words
from stats import get_num_characters
from stats import sort_char_count

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
    #print(f"{get_num_words('books/frankenstein.txt')} words found in the document")

    #print(total_characters_dict)

    total_characters_dict = get_num_characters('books/frankenstein.txt')
    sorted_chars = sort_char_count(total_characters_dict) 
    
     # Print the report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words('books/frankenstein.txt')} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()


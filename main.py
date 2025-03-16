def get_book_text(filepath):
    #set variable(s)
    file_contents=""

    #open the file
    with open(filepath) as f:
        file_contents = f.read()

    #return the contents of the file
    return file_contents

def main():
    #print the contents fo the set file
    print(get_book_text('books/frankenstein.txt'))

main()


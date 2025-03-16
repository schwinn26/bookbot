def get_book_text(filepath):
    #set variable(s)
    file_contents=""

    #open the file
    with open(filepath) as f:
        file_contents = f.read()

    #return the contents of the file
    return file_contents

def get_num_words(filepath):
    #set variable(s)
    num_words=0
    words=[]

    #open the file
    with open(filepath) as f:
        str_file = f.read()
        words=str_file.split()
        #loop over the items in the words list and increase num_words by 1 each time
        for word in words:
            num_words+=1
    
    #return total num_words
    return num_words

def main():
    #print the contents of the set txt file (commented out below line)
    #print(get_book_text('books/frankenstein.txt'))

    #print the number of words in the set txt file
    print(f"{get_num_words('books/frankenstein.txt')} words found in the document")

main()


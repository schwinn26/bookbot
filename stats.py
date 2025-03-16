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
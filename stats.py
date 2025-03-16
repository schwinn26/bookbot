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

def get_num_characters(filepath):
    dict_letter={}
    with open(filepath) as f:
        str_file = f.read()
        for character in str_file:
            character_lower = character.lower()
            if character_lower in dict_letter:
                dict_letter[character_lower]+=1
            else:
                dict_letter[character_lower]=1
        return dict_letter
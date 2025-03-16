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
    #set variable(s)
    dict_letter={}

    #open the file to be read
    with open(filepath) as f:
        #read the file
        str_file = f.read()
        #loop over each character in the string. if the character exist add 1 to the count for that dictionary key, if not make a new dictionary key and set the count to 1
        for character in str_file:
            character_lower = character.lower()
            if character_lower in dict_letter:
                dict_letter[character_lower]+=1
            else:
                dict_letter[character_lower]=1
        #return the dictionary
        return dict_letter
    
def sort_char_count(char_count):
    # Create a list of dictionaries
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    
    # Define a helper function for sorting
    def sort_on(dict_item):
        return dict_item["count"]
    
    # Sort the list
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
from data_structures.hashtable import Hashtable
import string

def first_repeated_word(input_text):
    words = [word.strip(string.punctuation).lower() for word in input_text.split()]
    dict = Hashtable()
    for word in words:
        if word in dict.keys():
            return word
        dict.set(word, None)

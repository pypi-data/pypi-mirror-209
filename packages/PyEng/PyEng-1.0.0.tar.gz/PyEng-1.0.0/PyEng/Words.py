# PyEng - Words

# Imports
import os
from difflib import get_close_matches
import json

# Set Directory
directory = os.path.dirname(os.path.realpath(__file__))
directory = directory.replace(os.sep, "/")

# Variables
dictionaryJSON = json.load(open(directory + "/data/dictionary.json", encoding="utf8"))

# Function 1 - Meaning
def meaning(word):
    # Check Data Type
    if (isinstance(word, str)):
        # Convert to Lower Case
        word = word.lower()

        # Check for Meaning
        if (word in dictionaryJSON):
            return dictionaryJSON[word]
        elif (len(get_close_matches(word, dictionaryJSON.keys())) > 0):
            return "Did you mean '{0}' instead? Try it again with the correct word.".format(get_close_matches(word, dictionaryJSON.keys())[0])
        else:
            return "The word doesn't exist. Please try again."
    else:
        raise Exception("The 'word' argument must be a string.")

# Function 2 - Anagram
def anagram(string1, string2):
    # Nested Functions
    def lengthOfStrings(a, b): return len(a) == len(b)
    def sortStrings(a, b): return sorted(a) == sorted(b)

    # Check Data Type
    if (isinstance(string1, str) and isinstance(string2, str)):
        # Convert to Lower Case
        string1 = string1.lower()
        string2 = string2.lower()

        # Check if Anagram
        if (lengthOfStrings(string1, string2) and sortStrings(string1, string2)):
            return True
        else:
            return False
    else:
        raise Exception("The 'string1' and 'string2' arguments must be a string.")
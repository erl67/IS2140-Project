import Classes.Path as Path
import re
# import string

puncRE = '[^\w\s]'

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class WordTokenizer:

    def __init__(self, content):
        # Tokenize the input texts.

        #remove punctuation
        content = re.sub(puncRE, " ", content)

        #trying faster way to remove punctuation, didn't work
        # content = content.str.maketrans(dict.fromkeys(string.punctuation, ' '))

        #split content into list of words
        self.words = content.split(" ")

        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.
        word = ""

        try:
            #pop off the first word, ignore if it's a single letter or space
            while word == "" or len(word) == 1:
                word = self.words.pop(0)

            #when list is empty return None        
        except IndexError: 
            word = None

        # print(f"{word=}")

        return word
import Classes.Path as Path
from nltk.stem import PorterStemmer

ps = PorterStemmer()

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class WordNormalizer:

    def __init__(self):
        return

    def lowercase(self, word):
        # Transform the word uppercase characters into lowercase.

        return word.lower()

    def stem(self, word):
        # Return the stemmed word with PorterStemmer
        
        # return word #for testing speed without stemmer
        return ps.stem(word)

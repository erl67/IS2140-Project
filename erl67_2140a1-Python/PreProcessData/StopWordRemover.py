import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class StopWordRemover:

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.

        self.stopwords = []

        #read entire file, split words into list
        with open(Path.StopwordDir, 'r', encoding="ANSI") as file:
            self.stopwords = file.read().split()

        # print(self.stopwords)
        return

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.

        #compare word with list of stopwords, removing if true
        if word in self.stopwords:
            return True

        return False

import Classes.Path as Path
import re

#source: https://stackoverflow.com/a/12982689
HTML_TAGS = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

#trying different methods to parse url data
# breakURLs = "[@:/.-=_?]"
# breakURLs = "[@:.-=_?/]"
# breakURLs = "[@:/.-_?=]"
# breakURLs = '[^a-zA-Z0-9 \n\.]/g'
# breakURLs = '[^a-zA-Z0-9 \n\.]'
# breakURLs = "/[^A-Z0-9]/ig"
breakURLs = "[@:/.-=_?]"

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class TrecwebCollection:

    def __init__(self):
        # 1. Open the file in Path.DataWebDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!
        self.start = "<DOC>"
        self.end = "</DOC>"
        self.docNoStart = "<DOCNO>"
        self.docNoEnd = "</DOCNO>"
        self.textStart = "</DOCHDR>"
        self.textEnd = "</DOC>"
        self.file = open(Path.DataWebDir, 'r', encoding="ANSI")

        print(f"\n{self.file}")
        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        # 3. the HTML tags should be removed in document content.
        docNo = ""
        content = ""
        temp = ""       #variable to hold each line as it's read

        #read through file in a loop
        while temp := self.file.readline():

            #extract document number
            if self.docNoStart in temp:
                docNo = temp.replace(self.docNoStart, "").replace(self.docNoEnd, "").strip()
                # print(f"{docNo=}")

            #read text of document
            elif self.textStart in temp:
                while temp := self.file.readline():

                    #remove start and end tags and line breaks when complete
                    if self.textEnd in temp:
                        content = content.replace(self.textStart, "").replace(self.textEnd, "").replace('\n', ' ')
                        break  

                    content += temp

            #stop reading at end of current document
            if self.end in temp:
                break
            elif temp == "": #eof
                self.file.close()
                return ["", ""]

        #remove HTML tags
        content = re.sub(HTML_TAGS, ' ', content)

        #split URLs and hyphenated words
        content = re.sub(breakURLs, " ", content)

        # print(f"\n{docNo=}\n{content=}")

        return [docNo, content]
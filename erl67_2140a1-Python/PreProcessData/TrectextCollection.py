import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class TrectextCollection:

    def __init__(self):
        # 1. Open the file in Path.DataTextDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!

        self.start = "<DOC>"
        self.end = "</DOC>"
        self.docNoStart = "<DOCNO>"
        self.docNoEnd = "</DOCNO>"
        self.textStart = "<TEXT>"
        self.textEnd = "</TEXT>"
        self.file = open(Path.DataTextDir, 'r', encoding="ANSI")

        print(f"\n{self.file}")
        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.

        docNo = ""
        content = ""
        temp = ""       #variable to hold each line as it's read

        #loop to read file until end
        while temp := self.file.readline():
        
            #extract document number
            if self.docNoStart in temp:
                docNo = temp.replace(self.docNoStart, "").replace(self.docNoEnd, "").strip()
                # print(f"{docNo=}")

            #extract document text in a loop    
            elif self.textStart in temp:
                while temp := self.file.readline():     #loop to read content of document

                    #remove start and end tags
                    if self.textEnd in temp:
                        content = content.replace(self.textStart, "").replace(self.textEnd, "").replace('\n', ' ')
                        break  

                    content += temp

            #stop reading at end of current document
            if self.end in temp:
                break
            elif temp == "": #return when end of file is reached
                self.file.close()
                return ["", ""]

        # print(f"{docNo=} {content=}" )

        return [docNo, content]

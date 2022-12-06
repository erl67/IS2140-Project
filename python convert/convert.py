import sys, argparse, json, re

# clear; python .\convert.py -f "Conscience.txt" -t "Conscience" -a "Ames,William" -u "http://www.digitalpuritan.net/Digital%20Puritan%20Resources/Ames,%20William/Conscience.pdf"
stopwords = []
puncRE = '[^\w\s]'

def get_args(argv):
    parser = argparse.ArgumentParser(description="Library Book Converter. Text to JSON.")
    parser.add_argument('-f', '--file', required=True, type=str)
    parser.add_argument('-t', '--title', required=True, type=str)
    parser.add_argument('-a', '--author', required=True, type=str)
    parser.add_argument('-u', '--url', required=True, default="Unavailable", type=str)
    return parser.parse_args()

def isStopword(word):
    global stopwords
    if word in stopwords or len(word) <= 2:
        return True
    return False

def convert_file(f, t, a, u):
    dictionary = {
    "title": t,
    "author": a,
    "file": f,
    "url": u,
    "content" : ""
    }

    content = ""
    tempContent = []
    temp = ""
    file = open("./text/" + f, 'rt', encoding="utf-8")

    while temp := file.readline():
        temp = temp.strip()
        if temp == '':
            continue

        #remove punctuation and stopwords
        words = re.sub(puncRE, "", temp).split(" ")
        for word in words:
            if not isStopword(word):
                tempContent.append(word)
    file.close()

    content = ' '.join(tempContent)
    print(f"{content=}")

    dictionary["content"] = content

    json_object = json.dumps(dictionary, indent=4)
    with open("./json/" + a + "_" + t + ".json", "w") as file:
        file.write(json_object)

def main(argv):
    args = get_args(argv)
    with open("./stopword.txt", 'r', encoding="ANSI") as file:
        stopwords = file.read().split()
    if not args.file:
        print("Command line arguments must be supplied\n")
    else:
        convert_file(args.file, args.title, args.author, args.url)
 
if __name__ == "__main__":
    main(sys.argv[1:])

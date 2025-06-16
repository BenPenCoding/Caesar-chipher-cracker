from read_english_dictionary import load_words
englishDict = load_words()

string = "Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald"  #Input string

def getCaesars(string):    #Finds all possible shifts
    
    strings = []

    for i in range(1,26):
        newString = ""

        for char in string:
            asc = ord(char)
            
            if asc > 64 and asc < 91: #UPPERCASE
                newString += chr(65 + ((asc-65)+i)%26)
                
            elif asc > 96 and asc < 123: #LOWERCASE
                newString += chr(97 + ((asc-97)+i)%26)
                
            elif char == " ":	#Symbol
                newString += "#"
            
            else:
                newString += char
                
        strings.append(newString)
    print(strings)
    return strings

def getWords(strings):  #Seperates text from noise such as symbols
    
    allWords = []
    
    for string in strings:
        words = []
        currentWord = ""

        for char in string:

            if char == '#':
                words.append(currentWord) if currentWord else None
                currentWord = ""

            else:
                currentWord += char

        allWords.append(words)
        
    return allWords

def getBestStrings(allWords):	#Returns a list with the head being the most likely shift, and the tail being any other somewhat likely shifts
    
    listsWithWords = []

    for words in allWords:		
        numWords = 0

        for word in words:
            numWords += 1 if word.lower() in englishDict else 0

        if numWords > 0:
            listsWithWords.append([words, numWords])
    
    largestNum = 0
    listWithMostWords = []
    if listsWithWords:
        
        for List in listsWithWords:
            num = List[1]

            if num > largestNum:
                largestNum = num
                listWithMostWords = List
    
        listsWithWords.pop(listsWithWords.index(listWithMostWords))
        listWithMostWords = listWithMostWords[0]
        
        return " ".join(listWithMostWords), listsWithWords.sort(key=lambda L: L[1], reverse=True)
    
    else:
        
        return "No valid results from caesar cipher check."
    
def displayResults(results):    #Displays results in an understandable way
    
    if results == "No valid results from caesar cipher check.":
        print(results)
    
    else:
        print(f"Best result: {results[0].replace('#','.')}")

        if results[1]:

            for result in results[1]:
                print("Other result: {result.replace('#','.')}.")
    
results = getBestStrings(getWords(getCaesars(string)))
displayResults(results)

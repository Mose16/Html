#File name
file = open("python.txt", "r")




###---Functions---###
def readFileLines(file):
    lines = file.readlines()
    return lines     
    
def createFile(fileName, text):
    newFile = open(fileName + ".txt", "w+")
    newFile.write(text)
    return

def addPass(line):
    try:
        line.find("def")
    except ValueError:
        return line
    else:
        pos = line.find("(") + 1
        line = line[:pos] + "passing variables: " + line[pos:]
        return line
        
def wordReplace(line):
    for word in WORDS:
        if line.find(word) != -1:
            pos = line.find(word)
            
            line = line[:pos] + PSEUDO[word] + line[pos + len(word) - 1:]
    return line
        
            
        

###---Variables---###
PSEUDO = {
    "def ":"Define function called",
    "class ":"Define class called"
}

WORDS = [
    "def ",
    "class "
]





###-------Main Code-------###
lines = readFileLines(file)
newFile = ""
for line in lines:
    line = addPass(line)
    line = wordReplace(line)
    
    newFile += "\n" + line

print(newFile)



createFile("generatedFile", newFile)
    
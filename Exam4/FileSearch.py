import Epic
import os

def readData(file):
    files = os.listdir(".")
    for file in files:
        if file.endswith(".txt"):
            f = open(file)
            l = []
            for line in f:
                l.append(line)
        print l
    return l

#def searchFile():
    




def main():
    readData(file)
    search = Epic.userString("Enter a search term: ")
    
    
    
    

main()
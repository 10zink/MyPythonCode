import json
import Epic

# Programmed by Tenzin Khunkhyen
# 4/16/17 for my Python Class
# This program is for Exam 5
# This program just reads a json file and then prints information from a dictionary based on either
# a category search or a keyword search.




#This function reads the json file and converts it into a dictionary
def fileReader():
    jsonTxt = ""
    f = open('PetStore.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    petStore = json.loads(jsonTxt)

    return petStore


#This function takes in a dictionary and also string "a"
def sorter(petStore, a):
    answers = ""
    
    #This if statement is for category search
    if(a == 'c'):
        userInput = Epic.userString("Enter a category: ")
        print ""
        for cat in petStore:
            if(cat["Category"].lower() == userInput):
                print "%s  -  $%s" % (cat["Product"], cat["Price"])

    
    #This if statement is for keyword search
    if(a == 'k'):
        userInput = Epic.userString("Enter a keyword: ")
        print ""
        for key in petStore:
            if(userInput in key["Product"].lower()):
                print "%s  -  $%s" % (key["Product"], key["Price"])

    return answers   
        
        
        
def main():
    
    b = Epic.userString("Search by category (c) or keyword (k)?")
    a = b.lower()
   
   #This line calls the method
    d = sorter(fileReader(), a)
    print d

main()
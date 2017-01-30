import Epic

# Programmed by Tenzin khunkhyen
# 1/30/17 for my Python Class
# Song Creator program
# Creates a song with the user inputs using lists and prints using forloop

#creating the lits for the verses
verse1 = []
verse2 = []
verse3 = []
verse4 = []

#setting the lists with the user inputs
verse1 = Epic.userString("Enter the first verse: ")
verse2 = Epic.userString("Entert he second verse: ")
verse3 = Epic.userString("Entert he third verse: ")
verse4 = Epic.userString("Entert he fourth verse: ")





#not using lists for the chorus due to calculations
chorus = Epic.userString("Enter the chorus: ")
repeat = Epic.userInt("Eneter the chourus repeat: ")

#creating space between the chorus
totalchor = (chorus + " ") * repeat 
#creating the last chorus line
lastchor = totalchor + chorus

onemoretime = ["...one more time!..."]


#settings the list to caps

   



#.lower() to convert to lowercase
#.upper() to convert to uppercase

#creating the song list with the order of verses
song = [verse1.upper(),totalchor.lower(),verse2.upper(),totalchor.lower(),verse3.upper(),totalchor.lower(),verse4.upper(),lastchor.lower()]


#creating the song with the one more time and the repeat
songPt1 = song + onemoretime + song


blank = "_______________"
#remove = "cookies"

#prints the list
print songPt1



    
#creates the forloop to print line by line
for line in songPt1:
    
    print "\n%s" %line
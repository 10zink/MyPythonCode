import Epic

# Programmed by Tenzin Khunkhyen
# 2/19/17 for my Python Class
# This program shows the number of bird sightings




#----------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds(filename):
    B = {}
    for line in open('Birds.txt'):
        line = line.lower() #sets the text file to lower case
        temp  = line.split(',')
        BirdName = temp[0].strip()
        BirdCount = int(temp[1].strip())
        if BirdName not in B:
            BirdCount = int(temp[1].strip()) #default bird count
            B[BirdName] = BirdCount
        else:
             B[BirdName] += int(temp[1].strip()) #adds the bird counts
        
   
    return B
# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(B,go):#go is the boolean variable that determines the exit of the program
   userInput = ''
   
   while go:
       userInput = Epic.userString("Enter a bird name: ")
       userInput = userInput.lower() #sets the userinput to lower case
       if userInput == 'exit':#exit statment prints 
           go = False
           print "Bye"
       elif userInput in B:
           print "I have seen that bird " + str(B[userInput]) + " time(s)."
       else:
           print "I have see that bird 0 time(s)."
      
           
def main():
    askUser(countBirds('Birds.txt'), True)
    
    
   

main()
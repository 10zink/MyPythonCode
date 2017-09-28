import Epic

# Programmed by Tenzin Khunkhyen
# Python Spring 2017 
# 4/30/17 for Exam 6

# This simple program creates two list, with three elements each. 
# One list is a list of weapons and another is of suspects.
# The program takes user input and then calculates the number of possible outcomes.
# When it reaches the only possible outcome, it prints out the solution. 


#user() asks the user if the clue is about a weapon or a suspect
def user():
    Input = Epic.userString("Is the clue about a weapon or a suspect (w or s)?").lower()
    
    return Input
    #returns the userinput
    


#initialList(weapons, suspects) ask the users to enter a list of weapons and suspects, and then returns the possibile options left.    
def initialList(weapons, suspects):
    x = ""
    L1 = []
    for weapon in weapons:
        for suspect in suspects:
                L1.append("%s %s" % (weapon, suspect))
        
    x  = ("%s possibilites left." % len(L1))
    
    return x
    
    

def main():
    #here we create the two lists, weapons and suspects, and then convert them to lower case. 
    weapons = ["Candlestick", "Wrench", "Pipe"]
    weapons2 = [x.lower() for x in weapons]
   
    suspects = ["Miss Scarlet", "Col Mustard", "Mr Green"]
    suspects2 = [y.lower() for y in suspects]
    

    #calling the initialList function
    print "%s " % (initialList(weapons, suspects))


    #set the gamover variable to false
    gameover = False
    
    while gameover == False:
    
        #calling the user() function
        userInput = user()
    
        
        if(userInput == 'w'):
            #here I used the lower cased list, that way we can get an updated list as we eliminate weapons
            weaponUsed = Epic.userString("Enter the weapon that was not used %s" % (weapons2)).lower() 
            if weaponUsed in weapons2:
                weapons2.remove(weaponUsed)
                L2 = []
                for weapon in weapons2:
                    for suspect in suspects2:
                        L2.append("%s %s" % (weapon, suspect))
                
                print ""
                print "%s possibilites left." % len(L2)
             
               
            #here if the possibile options is equal to 1, it prints out the remaining option as the answer, and then changes gameover to True
            if(len(L2) == 1):
                print "The suspect is  %s and the weapon used was the %s " % (suspects2, weapons2) 
                gameover = True
              
            
        if(userInput == 's'):
            #here I used the lower cased list, that way we can get an updated list as we eliminate suspects
            suspectUsed = Epic.userString("Enter the inocent suspect %s" % (suspects2)).lower()
            if suspectUsed in suspects2:
                suspects2.remove(suspectUsed)
                L3 = []
                for weapon in weapons2:
                    for suspect in suspects2:
                        L3.append("%s %s" % (weapon, suspect))
        
                print ""
                print "%s possibilites left." % len(L3)
               
                
            #here if the possibile options is equal to 1, it prints out the remaining option as the answer, and then changes gameover to True    
            if(len(L3) == 1):
                print "The suspect is  %s and the weapon used was the %s " % (suspects2, weapons2) 
                gameover = True
                
     
      
        
main()
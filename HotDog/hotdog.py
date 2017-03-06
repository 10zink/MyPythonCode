import time
import random
import Epic
# Programmed by Tenzin Khunkhyen
# 3/5/17 for my Python Class
# HotDogContest


#function that checks the user's guess with the actual winner and then returns a prompt.    
def correct(guess, winner):
    if guess.lower() == winner.lower():
        statement = "\nYou gusses right, %s wins!" %winner
    else:
        statement = "\nYou guess wrong, the winner was %s" %winner
        
    return statement



#main function which runs the program
def main():
   
    tom = 0
    sally = 0
    fred = 0
    
    guess = Epic.userString("Pick a winnder (Tom, Sally, or Fred: ")
   
    print "Ready, Set, Eat!\n"
    keepGoing = True
    while keepGoing:
        #I created three seperate random number ranges to procduce different numbers for each contestant
        tNumber = random.randrange(1,6) 
        sNumber = random.randrange(1,6)
        fNumber = random.randrange(1,6)
        
        tom = tom + tNumber
        sally = sally + sNumber
        fred = fred + fNumber
        
        time.sleep(2)
        print "\nchomp..    chomp...     chomp... \n"
        print "Tom has eaten %s hot dogs!" %tom
        print "Sally has eaten %s hot dogs!" %sally
        print "Fred has eaten %s hot dogs!" %fred
        
        #the following if statement then determined the winner
        if tom >= 50:
            winner = "Tom"
            keepGoing = False
        elif sally >= 50:
            winner = "Sally"
            keepGoing = False
        elif fred >= 50:
            winner = "Fred"
            keepGoing = False
        
   
    print "%s" %correct(guess,winner)
    

main()
import time
import random
import Epic




def main():
    
    tom = 0
    sally = 0
    fred = 0
    
    keepGoing = True
    guess = Epic.userString("Pick a winnder (Tom, Sally, or Fred: ")
    print "Ready, Set, Eat!\n"
    while keepGoing:
        tNumber = random.randrange(1, 6)
        sNumber = random.randrange(1, 6)
        fNumber = random.randrange(1, 6)
        
        tom = tom + tNumber
        sally = sally + sNumber
        fred = fred + fNumber
        
        time.sleep(3)
        print "\nchomp..    chomp...     chomp... \n"
        print "Tom has eaten %s hot dogs!" %tom
        print "Sally has eaten %s hot dogs!" %sally
        print "Fred has eaten %s hot dogs!" %fred
        
        if tom >= 50:
            winner = "Tom"
            
            keepGoing = False
        elif sally >= 50:
            winner = "Sally"
            
           
            keepGoing = False
        elif fred >= 50:
            winner = "Fred"
       
            keepGoing = False
    if guess.lower() == winner.lower():
        print "\nYou gusses right, %s wins!" %winner
    else:
        print "\nYou guess wrong, the winner was %s" %winner
main()
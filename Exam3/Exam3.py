import Epic
import random
# Programmed by Tenzin Khunkhyen
# 3/19/2017 for my Python Class
# Exam 3


#Function creates the deck and then selects one element in list and then adds it back to the list. Then it shuffles.
def creatingDeck():
    choices = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
    r = random.randrange(0, 10)
    choices.append(choices[r])
    random.shuffle(choices)
    
    return choices

#within this go function, I basically created a new  empty array called finalChoices that was took the new shuffled array.
def go():
    keepTrying = True
    attempts = 1
    finalChoices = []
    finalChoices = creatingDeck()
  
    while keepTrying:
        
        firstCard = Epic.userInt("Pick the first card to turn over (0-9):")
        secondCard = Epic.userInt("Pick the second card to turn over (0-9):")
        
        #by using nested if statements I was able to create the security measure that would prevent any numbers below 0,
        #or the same card being selected twice.
        
        if (firstCard == secondCard or firstCard < 0 or secondCard < 0):
            print "Invalid choices. You must pick difference cards and the card must be a number from 0-9."
           
        else:
            print finalChoices[firstCard]
            print finalChoices[secondCard]
            
            if(finalChoices[firstCard] == finalChoices[secondCard]):
                print "You win! It took you %s tries." %attempts
                attempts = 0
                keepTrying = False
            else:
                attempts = attempts + 1
    
    
#I was just having a brain fart and couldn't think of other functions to create. I personally felt that the program itself was 
#already pretty clean and simple. But I know that I am probably forgeting something. 
def main():
    
    go()
    
       

main()    
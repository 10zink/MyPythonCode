import Epic
#Perfect Shuffle
# Programmed by Tenzin Khunkhyen
# 3/26/17 for my Python Class
# This program uses functions to create a deck, shuffle the deck and then deal the cards.


rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

#this function creates the deck, it also adds the text between the two lists
def buildDeck(rank, suit):
    deck = []
    middle = " of "
    for r in rank:
        for s in suit:
            deck.append(r + middle + s)
    return deck

#this function splits the deck in two and then creates a new deck
def shuffleDeck(deck):
    firstHalf = deck[:26]
    secondHalf = deck[26:]
    newDeck = []
    for i in range(0, len(firstHalf)):
        newDeck.append(firstHalf[i])
        newDeck.append(secondHalf[i])
            
    return newDeck
    
this function deals 5 cards  
def deal(newDeck):
    inhand = newDeck[:5]
    
    return inhand
    

def main():
    d = buildDeck(rank, suit)
    # print d
    
    s = shuffleDeck(d)
    # print s
    
    # hand = deal(s)
    # print hand
   
    numShuffle = Epic.userInt("How many times do you want me to shuffle?")
    for i in range(0, numShuffle):
        s = shuffleDeck(s)
            
    print deal(s)
       
main()
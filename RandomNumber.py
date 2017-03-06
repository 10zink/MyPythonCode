import random
import Epic

def main():
    ans = random.randrange(1, 11)
    keepgoing = True
    count = 0
    while keepgoing:
        guess = Epic.userInt("Enter a guess from 1 to 10:")
        if guess == ans:
            print "You Win!"
            print "Total Attempts: %i" %count
            keepgoing = False
            count = count + 1
            
        if guess > ans:
            print "Too High!"
            count = count + 1
            
        if guess < ans:
            print "Too Low!"
            count = count + 1

main()
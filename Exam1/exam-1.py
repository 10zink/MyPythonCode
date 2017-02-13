import Epic
# Programmed by Tenzin Khunkhyen
# 2/12/17 for my Python Class
# This program is for Exam1, and it basically reads two txt files and fines the average and also the count of max speed.
#


# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    file = open(filename)
    l = []
    
    for line in file:
        l.append(line)
    
    l = [int(i) for i in l]
    
    return l

    
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
    dataF = [float(i) for i in l]
    totalCount = len(dataF) #finds the len of the list and stores value into totalCount
    listTotal = sum(dataF) #adds the values inside lists and stores value into listTotal
    
    average = listTotal/totalCount #finding average
    
    return average
    
    
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
    numberSpeeders = 0
    for speed in l:
        if(speed > maxSpeed):
            numberSpeeders += 1
    
    return numberSpeeders    
            
        
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    #This just prints out the prompt before the calculations are printed out. 
    prompt = ("Determines the number of people speeding during rush hour and not during rush hour."  
              "\nAlso determines the total fines during rush hour and not during rush hour. " 
              "\nA person is considered speeding if they are traveling faster than 69 MPH. " 
              "\nThe fine for speeding during rush hour is $150.  "
              "\nThe fine for speeding not during rush hour is $100.")

    print prompt
    
    print "\n"
    
    
   
    rush = readData("datarush.txt")  #reads the data file data-rush.txt 
    avgR = getAverage(rush) #uses the getAverage function to get the average
    print "The average speed during rush hour was %.2f" %avgR
    
    
    notRush = readData("datanotrush.txt") #reads the data file data-not-rush.txt
    avgNR = getAverage(notRush) #uses the getAverage function to get average
    print "The average speed not during rush hour was %.2f" %avgNR
    
    #Since Mark did not clarify if the maxspeed was suppose to a user input,
    #I just set maxSpeed to 69 within my main()
    maxSpeed = 69
   
   #numSpeedersR and numSpeedersNR calculate the number of speeders and the total fine give out
    numSpeedersR = countSpeeders(rush,maxSpeed)
    rushFine = 150 * numSpeedersR
    print "There were %i speeders during rush hour. Total fine = $%i" %(numSpeedersR, rushFine)
    

    numSpeedersNR = countSpeeders(notRush, maxSpeed)
    notRushFine = 100 * numSpeedersNR
    print "There were %i speeders not during rush hours. Total fine = $%i" %(numSpeedersNR, notRushFine)
    
# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()
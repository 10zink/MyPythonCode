import Epic

# Programmed by Tenzin Khunkhyen
# 2/5/17 for my Python Class
# This program uses functions to import and analyze temperature data.




#creates a read File and then stores it into a list
def readTemps():
    file = open('temps.txt', 'r')
    temps = []
    for line in file:
        temps.append(line)
    
    #removes the \n from list
    temps2 = [t.replace('\n', '') for t in temps]
    finaltemps = [float(i) for i in temps2]
   
    return finaltemps


#this function calculates the average within a list from start to stop
def calculateAvg(finaltemps, start, stop):

    rangevalue = finaltemps[start:stop]
    #rangefinal = [float(o) for o in rangevalue]
    #print rangevalue
    
    count = len(rangevalue)
    #print count
   
    finalsum = sum(rangevalue)
   
    #print finalsum
   
    average = finalsum/count
    
    #print average 
    
    return average
    

#Formula for average deviation
"""
def calculateAveDev(finaltemps, average):
    count = len(finaltemps)
    #print count 
    
    tempnum2 = 0
    
    for i in finaltemps:
        tempnum = abs(i-average)
        tempnum2 += tempnum
        
    AvgDev = tempnum2/count
        
        
    return AvgDev
"""   

#This function counts the number of positive numbers in the list    
def ispositive(finaltemps, start, stop):
    rangevalue = finaltemps[start:stop]
    
    count = 0
    for w in rangevalue:
        if( w > 0):
            count += 1
        
    return count



def percentagesplit(finaltemps, firstQ):
    count = len(finaltemps)

    percent = (firstQ)/float(100)
  
    thesplit = int(count * percent)
   
    return thesplit
   
    
def remainder(finaltemps, thesplit):
    count = len(finaltemps)
    
    remain = count - thesplit
    
    return remain




def main():
   
   print "Enter the what percentage split you would like to use."
   
   firstQ = Epic.userInt("Please enter the first percentage split you would like to use.")
   one = percentagesplit(readTemps(), firstQ)
   

   print "The second split is %i ." %remainder(readTemps(),percentagesplit(readTemps(), firstQ))
   
   two = remainder(readTemps(),percentagesplit(readTemps(), firstQ))
  
   print "\n"
   
   #calling the function for the avg first 81 years
   avg81years = calculateAvg(readTemps(), 0, one)
  
   print "During the first %i years, the average deviation from the temperature anomoly is  %.13f " % (one, avg81years) 
   
   #calling the ispositive function on the first 81 years
   ispos81 = ispositive(readTemps(), 0, one)
   
   print "During the first %i years, %i had a positive temperature anomoly" % (one, ispos81)
   
   
   
   
  
   #calling the function for the avg last 35 years
   avg35year = calculateAvg(readTemps(), one, 116)
   
   print "During the last %i years, the average deviation from the temperature anomoly is  %.13f" %(two, avg35year)
   
   #calling the ispositive function on the last 35 years
   ispos35 = ispositive(readTemps(), one, 116)
   
   print "During the last %i years, %i had a positive temperature anomoly" %(two, ispos35)
   

   
   
    
main()

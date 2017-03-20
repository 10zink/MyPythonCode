import Epic 
# Programmed by Tenzin Khunkhyen
# 2/26/17 for my Python Class
# This program is for Exam2
# This program reads in a file and then sorts them into a dictionary and then places them inside seperate lists
# one strange thing I did notice was that the order of the list seemed to be a off. But noneless the program works. 

#I know I probbaly don't need to import epic, but I just left it just in case in the future I want to refine this program. 

#File Reader
def readData():
    d = {}
    for line in open("timings.txt"):
        lst = line.split(",")
        catagorys = lst[0].strip()
        timing = lst[1].strip()
        
        d[catagorys] = [timing]
        #dict((k, int(v)) for k, v in d.iteritems())
        for key in d.keys():
            d[key] = [float(d[key][0])]
            
    return d
      
#File Sorters  
def dataBase(d, e):
    #creating the empty lists
    status = []
    cube = []
    square = []
    advanced = []
    intermediate = []
    average = []
    pathetic = []
    
    #this initial for loop goes through the names (keys) in the dictionary
    for data in d:
        tList = d[data] #this returns the value from the key(data) in the dictionary
        for t in tList: #this for loop then go through the values
            if t >= 0 and t < 10:
                cube.append(data)

            elif t >= 10 and t < 20:
                square.append(data)
               
            elif t >= 20 and t < 30:
                advanced.append(data)
                
            elif t >= 30 and t < 40:
                intermediate.append(data)
                
            elif t >= 40 and t < 60:
                average.append(data)
                
            elif t >60:
                pathetic.append(data)
    
    #The following was a method I discovered, and due to the short amount of time, I had no choice but to use
    #this werid formating trick. \n for new line and \t for tabs
    #the .join(list_name) converts a list to a string
    str1 = ' \n\t'.join(cube)
    str2 = ' \n\t'.join(square)
    str3 = ' \n\t'.join(advanced)
    str4 = ' \n\t'.join(intermediate)
    str5 = ' \n\t'.join(average)
    str6 = ' \n\t'.join(pathetic)
    
    
    #I created if statments to determine what gets returned, as in what list gets returned. 
    if e == 1:
        return str1
    elif e == 2:
        return str2
    elif e == 3:
        return str3
    elif e == 4:
        return str4
    elif e == 5:
        return str5
    elif e == 6:
        return str6
   
    
#within the main I also used \n and \t for formating help. 
def main():
    
    print "Cube Head (0-9.99):"
    one = dataBase(readData(),1)
    print "\t%s \n" % one
    
    print "Square Master (10-19.99):"
    two = dataBase(readData(),2)
    print "\t%s \n" % two
    
    print "Advance Twister (20-29.99):"
    three = dataBase(readData(),3)
    print "\t%s \n" % three
    
    print "Intermediate Turner (30-39.99):"
    four = dataBase(readData(),4)
    print "\t%s \n" % four
    
    print "Average Mover (40-59.99):"
    five = dataBase(readData(),5)
    print "\t%s \n" % five
    
    print "Pathetic (60 and beyond):"
    six = dataBase(readData(),6)
    print "\t%s\n" % six
    
main()

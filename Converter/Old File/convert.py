import Epic

# print prompts
def prompt():
        print "\nWhat type of number would you like to enter?"
        print '{} {}'.format('B - ', 'Binary')
        print '{} {}'.format('O - ', 'Octal')
        print '{} {}'.format('D - ', 'Decimal')
        print '{} {}'.format('H - ', 'Hexadecimal')
        print '{} {}'.format('C - ', 'Binary Coded Decimal')
        print '{} {}'.format('E - ', 'Exit')
        print '\n'
        
   

### BINARY ####

# binary to decimal
def binaryTOdecimal(userInput):
    # decimal = 0
    # for digit in userInput:
    #     decimal = decimal*2 + int(digit)
    
    # #returns int
    # return decimal
    return (int(userInput, 2))
 
# binary to octal
def binaryTOoctal(userInput):
    # decimal = 0
    # for digit in userInput:
    #     decimal = decimal*2 + int(digit)
    
    # return oct(int(decimal))
    temp = int(userInput, 2)
    return "{0:o}".format(temp)
    
# binary to hex
def binaryTOhex(userInput):
    # decimal = 0
    # for digit in userInput:
    #     decimal = decimal*2 + int(digit)
    
    # return hex(int(decimal))
    temp = int(userInput, 2)
    return str("{0:x}".format(temp)).upper()

# binary to BCD
def binaryTObcd(userInput):
    temp = int(userInput, 2)
    
    BCD = ""
    
    while(temp!= 0):
        t = int(temp)%10
        tBCD = str("{0:b}".format(int(t)))
        while(len(tBCD)<4):
            tBCD = '0%s' % tBCD
        BCD = tBCD + " " + BCD
        temp = int(temp)/10
        
    return BCD



### DECIMAL ####

# decimal to Binary
def decimalToBinary(userInput):
    return "{0:b}".format(int(userInput))
    
# decimal to Octal
def decimalTOoctal(userInput):
    return "{0:o}".format(int(userInput))

# decimal to Hex
def decimalTOhex(userInput):
    return str("{0:x}".format(int(userInput))).upper()

# decimal to BCD
def decimalTObcd(userInput):
    BCD = ""
    while(userInput!= 0):
        t = int(userInput)%10
        tBCD = str("{0:b}".format(int(t)))
        while(len(tBCD)<4):
            tBCD = '0%s' % tBCD
        BCD = tBCD + " " + BCD
        userInput = int(userInput)/10
                
    return BCD

 


### OCTAL ####

# octal to decimal
def octalTOdecimal(userInput):
   
    #returns string
    return int(userInput, 8)
    
# octal to binary
def octalTObinary(userInput):
    
    temp = int(userInput, 8)
    
    return "{0:b}".format(int(temp))
    
# octal to hex
def octalTOhex(userInput):
    temp = int(userInput, 8)
    
    return str("{0:x}".format(int(temp))).upper()
    
# octal to BCD
def octalTObcd(userInput):
    temp = int(userInput, 8)
    
    BCD = ""
    while(temp!= 0):
        t = int(temp)%10
        tBCD = str("{0:b}".format(int(t)))
        while(len(tBCD)<4):
            tBCD = '0%s' % tBCD
        BCD = tBCD + " " + BCD
        temp = int(temp)/10
        
    return BCD




### HEXADECIMAL ####

# hex to decimal
def hexTOdecimal(userInput):
    return int(userInput, 16)

# hex to binary
def hexTObinary(userInput):
    
    temp = int(userInput, 16)
    
    return "{0:b}".format(int(temp))

# hex to octal
def hexTOoctal(userInput):
    
    temp = int(userInput, 16)
    
    return "{0:o}".format(int(temp))

# hex to bcd
def hexTObcd(userInput):
    
    temp = int(userInput, 16)
    
    BCD = ""
    while(temp!= 0):
        t = int(temp)%10
        tBCD = str("{0:b}".format(int(t)))
        while(len(tBCD)<4):
            tBCD = '0%s' % tBCD
        BCD = tBCD + " " + BCD
        temp = int(temp)/10
        
    return BCD




### BINARY CODED DECIMAL ####

# bcd to decimal
def bcdTOdecimal(userInput):
    # 0001 0000  or 00010000
    temp = userInput.replace(" ","")
    # temp = 00010000
    
    start = 0
    end = 4
    go = len(temp)/4
    total = 0
    multi = 1
    grandTotal = 0
    answer = ""
    
    while(go != 0):
        Set = temp[start:end]
        # 0001
        
        reSet = Set[::-1]
        # 1000
        
        for num in reSet:
            if(num == '0'):
                total = total + 0
                multi = multi * 2
            else:
                total = total + multi
                multi = multi * 2
        
          
        answer += str(total)
        multi = 1
        total = 0
        start = end
        end = (end*2) + 1
        go = go - 1
        
    
    return answer

# bcd to binary
def bcdTObinary(userInput):
    # 0001 0000  or 00010000
    temp = userInput.replace(" ","")
    # temp = 00010000
    
    start = 0
    end = 4
    go = len(temp)/4
    total = 0
    multi = 1
    grandTotal = 0
    answer = ""
    
    while(go != 0):
        Set = temp[start:end]
        # 0001
        
        reSet = Set[::-1]
        # 1000
        
        for num in reSet:
            if(num == '0'):
                total = total + 0
                multi = multi * 2
            else:
                total = total + multi
                multi = multi * 2
        
          
        answer += str(total)
        multi = 1
        total = 0
        start = end
        end = (end*2) + 1
        go = go - 1
        
    
    return "{0:b}".format(int(answer))

# bcd to octal
def bcdTOoctal(userInput):
      # 0001 0000  or 00010000
    temp = userInput.replace(" ","")
    # temp = 00010000
    
    start = 0
    end = 4
    go = len(temp)/4
    total = 0
    multi = 1
    grandTotal = 0
    answer = ""
    
    while(go != 0):
        Set = temp[start:end]
        # 0001
        
        reSet = Set[::-1]
        # 1000
        
        for num in reSet:
            if(num == '0'):
                total = total + 0
                multi = multi * 2
            else:
                total = total + multi
                multi = multi * 2
        
          
        answer += str(total)
        multi = 1
        total = 0
        start = end
        end = (end*2) + 1
        go = go - 1
        
    
    return "{0:o}".format(int(answer))
     
# bcd to hex
def bcdTOhex(userInput):
          # 0001 0000  or 00010000
    temp = userInput.replace(" ","")
    # temp = 00010000
    
    start = 0
    end = 4
    go = len(temp)/4
    total = 0
    multi = 1
    grandTotal = 0
    answer = ""
    
    while(go != 0):
        Set = temp[start:end]
        # 0001
        
        reSet = Set[::-1]
        # 1000
        
        for num in reSet:
            if(num == '0'):
                total = total + 0
                multi = multi * 2
            else:
                total = total + multi
                multi = multi * 2
        
          
        answer += str(total)
        multi = 1
        total = 0
        start = end
        end = (end*2) + 1
        go = go - 1
        
    
    return str("{0:x}".format(int(answer))).upper()
    
        
        
        

def main():
    
    exit = False
    print "~~Welcome to the Magic Number Converter!~~"

    while(exit == False):
        
        #prints prompt
        prompt()
        
        # raw_input allows to print a statement and also take an input on the same line. 
        startType = raw_input("Number Type:  ").upper()
        


        # Checker for valid inputs and Exit
        while(True):
            if(startType != 'D' and startType != 'O' and startType != 'H' and startType != 'C' and startType != 'B' and startType != 'E'):
                print "Please enter a valid response."
                startType = raw_input("\nWhat type of number would you like to enter? ").upper()
            
            elif(startType == 'E'):
                print "\nThank you, Good bye!"
                quit() 
            else:
                break
        
         
    
        #takes number to be converted
        userInput = raw_input("\nPlease enter a number to convert.  ")

        #prints prompt
        prompt()
        
        endType = raw_input("Number Type:  ").upper()
        print "\n"
        
        # Checker for valid inputs and Exit
        while(True):
            if(endType == 'E'):
                exit = True
                print "\nThank you, Good bye!"
                quit()  
            
            elif(endType != 'D' and endType != 'O' and endType != 'H' and endType != 'C' and endType != 'B'):
                print "Please enter a valid response."
                endType = raw_input("\nWhat type of number would you like to enter? ").upper()
                
            elif(startType == endType):
                print "Error! You can not pick the same number type!"
                print "Try again!\n \nPick a new end number type!"
                prompt()
                endType = raw_input("Number Type:  ").upper()
                print "\n"
            else:
                break
        
      
        
            
        # call function to change decimal to binary
        if(startType == 'D' and endType == 'B'):
            print "Answer:  %s" % (decimalToBinary(userInput))
            print "\n"
        
        # call function to change from decimal to octal
        elif(startType == 'D' and endType == 'O'):
            print "Answer:  %s " % (decimalTOoctal(userInput))
            print "\n"
        
        # call function to change from decimal to hex    
        elif(startType == 'D' and endType == 'H'):
            print "Answer:  %s" % (decimalTOhex(userInput))
            print "\n"
        
        # call function to change from decimal to BCD
        elif(startType == 'D' and endType == 'C'):
            print "Answer:  %s" % (decimalTObcd(userInput))
            print "\n"        
        
        
        
            
        # call function to change binary to decimal
        elif(startType == 'B' and endType == 'D'):
            print "Answer:  %i " % (binaryTOdecimal(userInput))
            print "\n"
        
        # call function to change binary to octal
        elif(startType == 'B' and endType == 'O'):
            print "Answer:  %s" % (binaryTOoctal(userInput))
            print "\n"
        
        # call function to change binary to hex
        elif(startType == 'B' and endType == 'H'):
            print "Answer:  %s" % (binaryTOhex(userInput))
            print "\n"
        
        # call function to change binary to BCD
        elif(startType == 'B' and endType == 'C'):
            print "Answer:  %s" % (binaryTObcd(userInput))
            print "\n"
            
            
        
            
        # call function to change from octal to decimal
        elif(startType == 'O' and endType == 'D'):
            print "Answer:  %s" % (octalTOdecimal(userInput))
            print "\n"
        
        # call function to change from octal to binary
        elif(startType == 'O' and endType == 'B'):
            print "Answer:  %s" % (octalTObinary(userInput))
            print "\n"
        
        # call function to change from octal to hex
        elif(startType == 'O' and endType == 'H'):
            print "Answer:  %s" % (octalTOhex(userInput))
            print "\n"
        
        # call function to change from octal to BCD
        elif(startType == 'O' and endType == 'C'):
            print "Answer:  %s" % (octalTObcd(userInput))
            print "\n"
    
    

    
        # call function to change from hex to decimal
        elif(startType == 'H' and endType == 'D'):
            print "Answer:  %s" % (hexTOdecimal(userInput))
            print "\n"
        
        # call function to change from hex to binary
        elif(startType == 'H' and endType == 'B'):
            print "Answer:  %s" % (hexTObinary(userInput))
            print "\n"
            
        # call function to change from hex to octal
        elif(startType == 'H' and endType == 'O'):
            print "Answer:  %s" % (hexTOoctal(userInput))
            print "\n"
        
        # call function to change from hex to BCD
        elif(startType == 'H' and endType == 'C'):
            print "Answer:  %s" % (hexTObcd(userInput))
            print "\n"
        
        
        
        
        # call function to change from bcd to decimal
        elif(startType == 'C' and endType == 'D'):
            print "Answer:  %s" % bcdTOdecimal(userInput)
            print "\n"
        
        # call function to change from bcd to binary
        elif(startType == 'C' and endType == 'B'):
            print "Answer:  %s" % bcdTObinary(userInput)
            print "\n"
        
        # call function to change from bcd to octal
        elif(startType == 'C' and endType == 'O'):
            print "Answer:  %s" % bcdTOoctal(userInput)
            print "\n"
        
        # call function to change from bcd to hex
        elif(startType == 'C' and endType == 'H'):
            print "Answer:  %s" % bcdTOhex(userInput)
            print "\n"


main()



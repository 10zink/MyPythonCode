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


# decimal to Binary
def decimalToBinary(userInput):
    # binaryNum = bin(int(userInput))[2:]
  
    #returns string
    return "{0:b}".format(int(userInput))
    
# decimal to Octal
def decimalTOoctal(userInput):
    
    #returns string
    # return oct(int(userInput))
    return "{0:o}".format(int(userInput))

# decimal to Hex
def decimalTOhex(userInput):
    # return hex(int(userInput))
    return "{0:x}".format(int(userInput))

# decimal to BCD
def decimalTObcd(userInput):
    # x = str(userInput)
    # temp = 0
    # for char in x:
    #     temp = (temp << 4) + int(char)
    # return temp
    binaryNum = bin((inuserInput)[2:]
    BCD = ""
    while(userInput!= 0):
        t = int(userInput%10)
        tBCD = str("{0:b}".format(t))
        while(tBCD.len()<4):
            tBCD = '0%s' %tBCD

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
    return "{0:x}".format(temp)



    
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
    
    return "{0:x}".format(int(temp))
    
 



def main():
    
    
    exit = False
    print "~~Welcome to the Magic Number Converter!~~"
    
    
    while exit == False:
        
        #prints prompt
        prompt()
        
        startType = Epic.userString("").upper()
        if(startType == 'E'):
            exit = True
            print "\nThank you, Good bye!"
            break
        
        
        userInput = raw_input("\nPlease enter a number to convert.  ")
        
        #prints prompt
        prompt()
        
        endType = Epic.userString("").upper()
        print '\n'
        
        if(endType == 'E'):
            exit = True
            print "\nThank you, Good bye!"
            break
      
        
        #call function to change decimal to binary
        elif(startType == 'D' and endType == 'B'):
            print "Answer:  %s" % (decimalToBinary(userInput))
            print "\n"
        
        
        #call function to change from decimal to octal
        elif(startType == 'D' and endType == 'O'):
            print "Answer:  %s " % (decimalTOoctal(userInput))
            print "\n"
        
        #call function to change from decimal to hex    
        elif(startType == 'D' and endType == 'H'):
            print "Answer:  %s" % (decimalTOhex(userInput))
            print "\n"
        
        #call function to change from decimal to BCD
        elif(startType == 'D' and endType == 'C'):
            print "Answer:  %i" % (decimalTObcd(userInput))
            print "\n"        
        
        
        
            
        #call function to change binary to decimal
        elif(startType == 'B' and endType == 'D'):
            print "Answer:  %i " % (binaryTOdecimal(userInput))
            print "\n"
        
        #call function to change binary to octal
        elif(startType == 'B' and endType == 'O'):
            print "Answer:  %s" % (binaryTOoctal(userInput))
            print "\n"
        
        #call function to change binary to hex
        elif(startType == 'B' and endType == 'H'):
            print "Answer:  %s" % (binaryTOhex(userInput))
            print "\n"
            
            
            
            
        #call function to change from octal to decimal
        elif(startType == 'O' and endType == 'D'):
            print "Answer:  %s" % (octalTOdecimal(userInput))
            print "\n"
        
        #call function to change from octal to binary
        elif(startType == 'O' and endType == 'B'):
            print "Answer:  %s" % (octalTObinary(userInput))
            print "\n"
        
        #call function to change from octal to hex
        elif(startType == 'O' and endType == 'H'):
            print "Answer:  %s" % (octalTOhex(userInput))
            print "\n"
        
       
    
    
main()



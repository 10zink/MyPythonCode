import Epic


# print menu prompt
def mainMenu():
    menu = ("\n        Please pick either"
            "\n Option 1: Convert a sign integer"
            "\n Option 2: Convert between number systems"
            "\n Option 3: Quit Program."
            "\n Option 4: Run Program Test"
            "\n")
    print menu

# print prompt 1
def prompt1():
    print "\nWhat type of number would you like to convert?"
    print '{} {}'.format('D - ', 'Decimal')
    print '{} {}'.format('S - ', 'Sign Magnitude')
    print '{} {}'.format('1 - ', '1\'s Complement')
    print '{} {}'.format('2 - ', '2\'s Complement')
    print '{} {}'.format('E - ', 'Exit')
    print '\n'
    
# print prompt 2
def prompt2():
    print '\n'
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
    return (int(userInput, 2))
 
# binary to octal
def binaryTOoctal(userInput):
    temp = int(userInput, 2)
    return "{0:o}".format(temp)
    
# binary to hex
def binaryTOhex(userInput):
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
        
    
    return ("{0:o}".format(int(answer)))
     
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
    
        
      
# function to change decimal to _____.
def DecimalTo(endType, userInput):
    # call function to change from decimal to binary
    if(endType == 'B'):
        print "Answer:  %s" % (decimalToBinary(userInput))
        print "\n"
    
    # call function to change from decimal to octal
    elif(endType == 'O'):
        print "Answer:  %s " % (decimalTOoctal(userInput))
        print "\n"
    
    # call function to change from decimal to hex    
    elif(endType == 'H'):
        print "Answer:  %s" % (decimalTOhex(userInput))
        print "\n"
    
    # call function to change from decimal to BCD
    elif(endType == 'C'):
        print "Answer:  %s" % (decimalTObcd(userInput))
        print "\n"        
# function to change binary to ______. 
def BinaryTo(endType, userInput):
    # call function to change binary to decimal
    if(endType == 'D'):
        print "Answer:  %i " % (binaryTOdecimal(userInput))
        print "\n"
    
    # call function to change binary to octal
    elif(endType == 'O'):
        print "Answer:  %s" % (binaryTOoctal(userInput))
        print "\n"
    
    # call function to change binary to hex
    elif(endType == 'H'):
        print "Answer:  %s" % (binaryTOhex(userInput))
        print "\n"
        
    # call function to change binary to BCD
    elif(endType == 'C'):
        print "Answer:  %s" % (binaryTObcd(userInput))
        print "\n"

# function to change octal to ______.
def OctalTo(endType, userInput):
    # call function to change from octal to decimal
    if(endType == 'D'):
        print "Answer:  %s" % (octalTOdecimal(userInput))
        print "\n"

    # call function to change from octal to binary
    elif(endType == 'B'):
        print "Answer:  %s" % (octalTObinary(userInput))
        print "\n"
    
    # call function to change from octal to hex
    elif(endType == 'H'):
        print "Answer:  %s" % (octalTOhex(userInput))
        print "\n"
    
    # call function to change from octal to BCD
    elif(endType == 'C'):
        print "Answer:  %s" % (octalTObcd(userInput))
        print "\n"

# function to change hex to  _____.
def HexTo(endType, userInput):
    # call function to change from hex to decimal
    if(endType == 'D'):
        print "Answer:  %s" % (hexTOdecimal(userInput))
        print "\n"
    
    # call function to change from hex to binary
    elif(endType == 'B'):
        print "Answer:  %s" % (hexTObinary(userInput))
        print "\n"
        
    # call function to change from hex to octal
    elif(endType == 'O'):
        print "Answer:  %s" % (hexTOoctal(userInput))
        print "\n"
    
    # call function to change from hex to BCD
    elif(endType == 'C'):
        print "Answer:  %s" % (hexTObcd(userInput))
        print "\n"

# function to change bcd to _____.
def BcdTo(endType, userInput):
    # call function to change from bcd to decimal
    if(endType == 'D'):
        print "Answer:  %s" % bcdTOdecimal(userInput)
        print "\n"
    
    # call function to change from bcd to binary
    elif(endType == 'B'):
        print "Answer:  %s" % bcdTObinary(userInput)
        print "\n"
    
    # call function to change from bcd to octal
    elif(endType == 'O'):
        print "Answer:  %s" % bcdTOoctal(userInput)
        print "\n"
    
    # call function to change from bcd to hex
    elif(endType == 'H'):
        print "Answer:  %s" % bcdTOhex(userInput)
        print "\n"



###  DECIMAL  ###

# decimal to Sign Mag
def decimalToSignMagnitude(userInput):
    if("-" in userInput):
        userInput = userInput.replace("-", "")
        if(int(userInput)<8):
            temp = "{0:03b}".format(int(userInput))
            temp = "1"+temp
            bitSize = 0
            
            bitSize = temp + "    Bit Size: " + str(len(temp))
            return bitSize
        elif(int(userInput)<16):
            temp = "{0:07b}".format(int(userInput))
            temp = "1"+temp
            bitSize = 0
            
            bitSize = temp + "    Bit Size: " + str(len(temp))
            return bitSize
            
        elif(int(userInput)<256):
            temp = "{0:015b}".format(int(userInput))
            temp = "1"+temp
            bitSize = 0
            
            bitSize = temp + "    Bit Size: " + str(len(temp))
            return bitSize
        
        elif(int(userInput)>255):
            temp = "{0:b}".format(int(userInput))
            temp = "1"+temp
            bitSize = 0
            
            bitSize = temp + "    Bit Size: " + str(len(temp))
            return bitSize
          
  
    else:
        if(int(userInput)<8):
            temp = "{0:04b}".format(int(userInput))
            bitSize = 0
            
            bitSize = temp + " " + "Bit Size: " + str(len(temp))
            return bitSize
        elif(int(userInput)<16):
            temp = "{0:08b}".format(int(userInput))
            bitSize = 0
            
            bitSize = temp + " " + "Bit Size: " + str(len(temp))
            return bitSize
        elif(int(userInput)<256):
            temp = "{0:016b}".format(int(userInput))
            bitSize = 0
            
            bitSize = temp + " " + "Bit Size: " + str(len(temp))
            return bitSize
        elif(int(userInput)>255):
            temp = "{0:b}".format(int(userInput))
            bitSize = 0
            
            bitSize = temp + " " + "Bit Size: " + str(len(temp))
            return bitSize

# decimal to 1's complement
def decimalToOnes(userInput):
    if("-" in userInput):
        userInput = userInput.replace("-", "")
        temp = "{0:b}".format(int(userInput))
        temp = "0"+ temp
        tempfinal = ''
        bitSize = 0
        for x in temp:
            if(x == '1'):
                tempfinal = tempfinal + '0'
            elif(x == '0'):
                tempfinal = tempfinal + '1'
        
        bitSize = tempfinal + "    Bit Size: " + str(len(tempfinal))        
        
        return bitSize;
        
    else:
        
        temp = "{0:b}".format(int(userInput))
        temp = "0" + temp
        bitSize = 0
        
        bitSize = temp + "    Bit Size: " + str(len(temp))
        return bitSize
 
# decimal to 2's complement        
def decimalToTwos(userInput):
    if("-" in userInput):
        NUM = int(userInput.replace("-", ""))
        newInput = int(userInput)
        if(int(NUM)<8):
            numberBits = 4
            if(newInput < 0):
                # << is the bitwise Op same as multiplying x by 2**y.
                newInput = ( 1<<numberBits ) + newInput
            temp = '{:0%ib}' % numberBits
            totalBit = 0
            
            return temp.format(newInput) + "    Bit Size: " + str(len(temp.format(newInput)))
        
        elif(int(NUM)<16):
            numberBits = 8
            if(newInput < 0):
                newInput = ( 1<<numberBits ) + newInput
            temp = '{:0%ib}' % numberBits
            totalBit = 0
            return temp.format(newInput) + "    Bit Size: " + str(len(temp.format(newInput)))
            
        elif(int(NUM)<255):
            numberBits = 16
            if(newInput < 0):
                newInput = ( 1<<numberBits ) + newInput
            temp = '{:0%ib}' % numberBits
            totalBit = 0
            return temp.format(newInput) + "    Bit Size: " + str(len(temp.format(newInput)))
        
        elif(int(NUM)>255):
            numberBits = 255
            if(newInput < 0):
                newInput = ( 1<<numberBits ) + newInput
            temp = '{:0%ib}' % numberBits
            totalBit = 0
            return temp.format(newInput) + "    Bit Size: " + str(len(temp.format(newInput)))
        
    else:
        
        temp = "{0:b}".format(int(userInput))
        temp = "0" + temp
        bitSize = 0
        
        bitSize = temp + " " + "Bit Size: " + str(len(temp))
        return str(bitSize)


###  ONES COMPLEMENT  ### 

# 1's complement to decimal
def onesToDec(userInput):
    temp = str(userInput)
    
    tempfinal = ''
    bitSize = 0
    if(temp[0] == '1'):
        for x in temp:
            if(x == '1'):
                tempfinal = tempfinal + '0'
            elif(x == '0'):
                tempfinal = tempfinal + '1'
    
        #newFinal = tempfinal[1:]
        Final = int(tempfinal, 2)
        bitSize = "-" + str(Final) + "    Bit Size: " + str(len(str(Final)))        
        
        return bitSize;
    elif(temp[0] == '0'):
        Final = int(temp, 2)
        bitSize = str(Final) + "    Bit Size: " + str(len(str(Final)))        
        
        return bitSize;

# 1's complement to 2's complement
def onesToTwo(userInput):
    temp = str(userInput)[::-1]
    tempfinal = ''
    bitSize = 0
    if(userInput[0]== '1'):
        for i in range(0, len(temp)):
            if(temp[i] == '1'):
            	tempfinal += '0'
            
            elif(temp[i] == '0'):
            	tempfinal  += '1'
            	break
        
        Final = ((tempfinal+temp[i+1:])[::-1])
        
        bitSize = Final + "    Bit Size: " + str(len(Final))
        
        return  bitSize
    elif(userInput[0]=='0'):
        return userInput


### TWOS COMPLEMENT  ###

# 2's complement to decimal
def twosToDec(userInput):
    temp = str(userInput)
    bitSize = 0
    if(temp[0] == '1'):
        tempfinal = ''
        temp = str(userInput)[::-1] 
        for i in range(0, len(temp)):
            if(temp[i] == '0'):
            	tempfinal += '1'
            
            elif(temp[i] == '1'):
            	tempfinal  += '0'
            	break
        Final = ((tempfinal+temp[i+1:])[::-1])
        hold = ''
        for x in Final:
            if(x == '1'):
                hold = hold + '0'
            elif(x == '0'):
                hold = hold + '1'
    
        Final = int(hold, 2)
        bitSize = "-" + str(Final) + "    Bit Size: " + str(len(str(Final)))        
        
        return bitSize;
        
    elif(temp[0] == '0'):
        Final = int(temp, 2)
        bitSize = str(Final) + "    Bit Size: " + str(len(str(Final)))        
        
        return bitSize;
        
# 2's complement to 1's complement        
def twosToOne(userInput):
    temp = str(userInput)[::-1] 
    tempfinal = ''
    bitSize = 0
    if(userInput[0]=='1'):
        for i in range(0, len(temp)):
            if(temp[i] == '0'):
            	tempfinal += '1'
            
            elif(temp[i] == '1'):
            	tempfinal  += '0'
            	break
        
        Final = ((tempfinal+temp[i+1:])[::-1])
        
        bitSize = Final + "    Bit Size: " + str(len(Final))
        
        return  bitSize
    elif(userInput[0]=='0'):
        return userInput


# function to change decimal to _____.
def sDecimalTO(endType, userInput):
    if(endType == 'S'):
        print "Answer:  %s" % (decimalToSignMagnitude(userInput))
        print "\n"
    
    if(endType == '1'):
        print "Answer:  %s" % (decimalToOnes(userInput))
        print "\n"
    
    if(endType == '2'):
        print "Answer:  %s" % (decimalToTwos(userInput))
        print "\n"

#  function to change 1's comp to _____.
def sOnesTO(endType, userInput):
    if(endType == 'D'):
        print "Answer:  %s" % (onesToDec(userInput))
        print "\n"
    
    if(endType == '2'):
        print "Answer:  %s" % (onesToTwo(userInput))
        print "\n"
        
# # function to change 2's comp to _____.
def TwosTO(endType, userInput):
    if(endType == 'D'):
        print "Answer:  %s" % (twosToDec(userInput))
        print "\n"

    if(endType == '1'):
        print "Answer:  %s" % (twosToOne(userInput))
        print "\n"




def main():
    
    exit = False
    print "~~ Welcome to the Magic Number Converter! ~~"

    while(exit == False):
        
        #prints menu prompt
        mainMenu()
        
        option = raw_input("Enter 1 or 2 or  3:   ")
        print '\n'
        # checks user input
        notNum = False
        while(notNum == False):
            if(option != '1' and option != '2' and option != '3' and option != '4'):
                print "\nPlease enter a valid response!"
                print "\n"
                option = raw_input("Enter 1 or  2 or 3:   ")
            else:
                notNum = True
        
        # signed integers  >>>>>           
        if(option == '1'):
            print "~~ Welcome to the Sign Integer Converter! ~~"
            #prints prompt
            prompt1()
            
            #takes number type
            startType = raw_input("Number Type: ").upper()
            
            # Checker for valid inputs and Exit
            while(True):
                if(startType != 'D' and startType != '1' and startType != '2' and startType != 'E'):
                    print "Please enter a valid response."
                    startType = raw_input("\nWhat type of number would you like to enter? ").upper()
                elif(startType == 'S'):
                    print "Please enter D - Decimal or 1 - 1's Complement or 2 - 2's Complement"
                    startType = raw_input("\nWhat type of number would you like to enter?").upper()
                elif(startType == 'E'):
                    print "\nThank you, Good bye!"
                    quit() 
                else:
                    break
            
            #takes number to be converted
            userInput = raw_input("\nPlease enter a number to convert.  ")
            
            #checks userInput
            while(True):
                if(userInput.isdigit() == False and "-" not in userInput):
                    print "Please enter a valid response."
                    userInput = raw_input("\nPlease enter a number to convert.  ")
                    
                else:
                    break
                
            #prints prompt
            prompt1()
            
            endType = raw_input("Number Type:  ").upper()
            
            print "\n"
                       # Checker for valid inputs and Exit
            while(True):
                if(endType == 'E'):
                    exit = True
                    print "\nThank you, Good bye!"
                    quit()  
                
                elif(endType != 'D' and endType != '1' and endType != '2' and endType != 'E'):
                    print "Please enter a valid response."
                    endType = raw_input("\nWhat type of number would you like to enter? ").upper()
                
                #This will prompt the user to enter a decimal if the user wants to convert to 1's or 2's
                elif(endType == 'S'):
                    print "Please enter D - Decimal or 1 - 1's Complement or 2 - 2's Complement"
                    endType = raw_input("\nWhat type of number would you like to enter? ").upper()
                    
                elif(startType == endType):
                    print "Error! You can not pick the same number type!"
                    print "Try again!\n \nPick a new end number type!"
                    prompt1()
                    endType = raw_input("Number Type:  ").upper()
                    print "\n"
                else:
                    break
            
            if(startType == 'D'):
                sDecimalTO(endType, userInput)
                
            elif(startType == '1'):
                sOnesTO(endType, userInput)
            
            elif(startType == '2'):
                TwosTO(endType, userInput)
        
        # number systems  >>>>>    
        if(option == '2'):
            print "\n~~ Welcome to the Number Systems Converter! ~~"
            #prints prompt 2
            prompt2()
            
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
            while(True):
                if('-' in userInput):
                    print "Please enter a valid response."
                    userInput = raw_input("\nPlease enter a number to convert.  ")
                    
                elif(userInput.isdigit() == False):
                    print "Please enter a valid response."
                    userInput = raw_input("\nPlease enter a number to convert.  ")
                    
                else:
                    break
            
            #prints prompt
            prompt2()
            
            endType = raw_input("Number Type:  ").upper()
            print "\n"
            
            
            # Checker for valid inputs and Exit
            while(True):
                if(endType == 'E'):
                    exit = True
                    print "\nThank you, Good bye!"
                    quit()  
                
                elif(endType != 'D' and endType != 'O' and endType != 'H' and endType != 'C' and endType != 'B' and endType != 'E'):
                    print "Please enter a valid response."
                    endType = raw_input("\nWhat type of number would you like to enter? ").upper()
                    
                elif(startType == endType):
                    print "Error! You can not pick the same number type!"
                    print "Try again!\n \nPick a new end number type!"
                    prompt2()
                    endType = raw_input("Number Type:  ").upper()
                    print "\n"
                else:
                    break
            
          
            # call function to change from decimal to ______. 
            if(startType == 'D'):
                DecimalTo(endType,userInput)
                
            # call function to change from binary to ______.    
            elif(startType == 'B'):
                BinaryTo(endType, userInput)
            
            # call function to change from octal to ______. 
            elif(startType == 'O'):
                OctalTo(endType, userInput)
        
            # call function to change from hex to ______.     
            elif(startType == 'H'):
                HexTo(endType, userInput)
            
            # call function to change from bcd to ______.    
            elif(startType == 'C'):
                BcdTo(endType, userInput)
        
        # exit  >>>>>     
        elif(option == '3'):
            print "\nGood Bye!"
            exit = True
        
        # Test  >>>>>  
        elif(option == '4'):
            print "\nTest Running..."
            
            print "\n~~~~~~~~~Number System Test~~~~~~~~~"
            
            # call function to change from decimal to ______.
            #{
            a = ("\n        Decimal to Binary:"
                 "\nDecimal = 10"
                 "\nBinary: 1010")
            print a
            print "Program: %s" %(decimalToBinary(10))
            
            b = ("\n        Decimal to Octal:"
                 "\nDecimal = 10"
                 "\nOctal: 12")
            print b
            print "Program: %s" %(decimalTOoctal(10))
            
            c = ("\n        Decimal to Hex:"
                 "\nDecimal = 10"    
                 "\nHex: A")
            print c
            print "Program: %s" %(decimalTOhex(10))
           
            d = ("\n        Decimal to BCD:"
                 "\nDecimal = 10"    
                 "\nBCD: 00010000")
            print d
            print "Program: %s" %(decimalTObcd(10))
            #}
                    
            # call function to change from binary to ______.    
            #{
            a = ("\n        Binary to Decimal:"
                 "\nBinary = 1010"    
                 "\nDecimal: 10")
            print a
            print "Program: %s" %(binaryTOdecimal('1010'))
            
            b = ("\n        Binary to Octal:"
                 "\nBinary = 1010"    
                 "\nOctal: 12")
            print b
            print "Program: %s" %(binaryTOoctal('1010'))
            
            c = ("\n        Binary to Hex:"
                 "\nBinary = 1010"    
                 "\nHex: A")
            print c
            print "Program: %s" %(binaryTOhex('1010'))
        
            d = ("\n        Binary to BCD:"
                 "\nBinary = 1010"    
                 "\nBCD: 00010000")
            print d
            print "Program: %s" %(binaryTObcd('1010'))
            #}
            
            # call function to change from octal to ______. 
            #{
            a = ("\n        Octal to Decimal:"
                 "\nOctal = 12"
                 "\nDecimal: 10")
            print a
            print "Program: %s" %(octalTOdecimal('12'))
            
            b = ("\n        Octal to Binary:"
                 "\nOctal = 12"    
                 "\nBinary: 1010")
            print b
            print "Program: %s" %(octalTObinary('12'))
            
            c = ("\n        Octal to Hex:"
                 "\nOctal = 12"
                 "\nHex: A")
            print c
            print "Program: %s" %(octalTOhex('12'))
        
            d = ("\n        Octal to BCD:"
                 "\nOctal = 12"    
                 "\nBCD: 00010000")
            print d
            print "Program: %s" %(octalTObcd('12'))
            #}
            
            # call function to change from hex to ______.     
            #{
            a = ("\n        Hex to Decimal:"
                 "\nHex = A"
                 "\nDecimal: 10")
            print a
            print "Program: %s" %(hexTOdecimal('A'))
            
            b = ("\n        Hex to Binary:"
                 "\nHex = A"
                 "\nBinary: 1010")
            print b
            print "Program: %s" %(hexTObinary('A'))
            
            c = ("\n        Hex to Octal:"
                 "\nHex = A"    
                 "\nOctal: A")
            print c
            print "Program: %s" %(hexTOoctal('A'))
        
            d = ("\n        Hex to BCD:"
                 "\nHex = A"    
                 "\nBCD: 00010000")
            print d
            print "Program: %s" %(hexTObcd('A'))
            #}
            
            # call function to change from bcd to ______.    
            #{
            a = ("\n        BCD to Decimal:"
                 "\nBCD = 00010000"    
                 "\nDecimal: 10")
            print a
            print "Program: %s" %(bcdTOdecimal('00010000'))
            
            b = ("\n        BCD to Binary:"
                 "\nBCD = 00010000"
                 "\nBinary: 1010")
            print b
            print "Program: %s" %(bcdTObinary('00010000'))
            
            c = ("\n        BCD to Octal:"
                 "\nBCD = 00010000"
                 "\nOctal: 12")
            print c
            print "Program: %s" %(bcdTOoctal('00010000'))
        
            d = ("\n        BCD to Hex:"
                 "\nBCD = 00010000"
                 "\nHex: A")
            print d
            print "Program: %s" %(bcdTOhex('00010000'))    
            #}
            
            print "\n"
            print "\n~~~~~~~~~Sign Integer Test~~~~~~~~~"
            
            # Decimal to SignMagnitude, 1's, 2's 
            #{
            a = ("\n        Decimal to SignMagnitude:"
                 "\nDecimal = -10"
                 "\nSignMagnitude: 10001010")
            print a
            print "Program: %s" %(decimalToSignMagnitude('-10'))
            
            b = ("\n        Decimal to SignMagnitude:"
                 "\nDecimal = 10"
                 "\nSignMagnitude: 00001010")
            print b
            print "Program: %s" %(decimalToSignMagnitude('10'))
            
            
            c = ("\n        Decimal to 1's Complement:"
                 "\nDecimal = -10"
                 "\nOnes Complement: 10101")
            print c
            print "Program: %s" %(decimalToOnes('-10'))
            
            d = ("\n        Decimal to 1's Complement:"
                 "\nDecimal = 10"
                 "\nOnes Complement: 01010")
            print d
            print "Program: %s" %(decimalToOnes('10'))
            
            e = ("\n        Decimal to 2's Complement:"
                 "\nDecimal = -10"
                 "\nTwos Complement: 11110110")
            print e
            print "Program: %s" %(decimalToTwos('-10'))
            
            f = ("\n        Decimal to 2's Complement:"
                 "\nDecimal = 10"
                 "\nTwos Complement: 01010")
            print f
            print "Program: %s" %(decimalToTwos('10'))
            #}
            
            # 1's Complement to Decimal and 2's Complement
            #{
            a = ("\n        One's Complement to Decimal:"
                 "\nOnes = 01010"
                 "\nDecimal: 10")
            print a
            print "Program: %s" %(onesToDec('01010'))
            
            b = ("\n        One's Complement to Decimal:"
                 "\nOnes = 10101"
                 "\nDecimal: -10")
            print b
            print "Program: %s" %(onesToDec('10101'))
            
                
            c = ("\n        One's Complement to Two's Complement:"
                 "\nOnes = 01010"
                 "\nTwo: 01010")
            print c
            print "Program: %s" %(onesToTwo('01010'))
            
            d = ("\n        One's Complement to Two's Complement:"
                 "\nOnes = 10101"
                 "\nTwo: 10110")
            print d
            print "Program: %s" %(onesToTwo('10101'))
            #}
            
            # 2's Complement to Decimal and 1's Complement
            #{
            a = ("\n        Two's Complement to Decimal:"
                 "\nTwos = 10110"
                 "\nDecimal: -10")
            print a
            print "Program: %s" %(twosToDec('10110'))
            
            b = ("\n        Two's Complement to Decimal:"
                 "\nTwos = 01010"
                 "\nDecimal: 10")
            print b
            print "Program: %s" %(twosToDec('01010'))
            
                
            c = ("\n        Two's Complement to One's Complement:"
                 "\nTwos = 10110"
                 "\nOnes: 10101")
            print c
            print "Program: %s" %(twosToOne('10110'))
            
            d = ("\n        Two's Complement to One's Complement:"
                 "\nTwos = 01010"
                 "\nOnes: 01010")
            print d
            print "Program: %s" %(twosToOne('01010'))
            #}
            exit = True
            
    
main()



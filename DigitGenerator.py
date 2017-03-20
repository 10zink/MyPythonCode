import Epic
import random

def makePIN(count):
    digits = []
    for i in range(0, count):
        digits.append(random.randrange(0,10))
    return digits

def main():
    keepTrying = True
    while keepTrying:
            digitCount = Epic.userInt("How many digits in your PIN?")
            digits = makePIN(digitCount)
            print digits
            yesOrNo = Epic.userString("Generate another one? (y/n)")
            keepTrying = (yesOrNo == 'y')

main()
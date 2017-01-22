#Program by Tenzin Khunkhyen
#RecipeConverter
#1/22/17 Python Class

#Creating the scanners to take the user inputs
print " -- Orignal Recipe -- "
print "Enter the amount of Flour (cups): ",
flour = raw_input()
print "Enter the amount of Water (cups): ",
water = raw_input()
print "Enter the amount of Salt (teaspoons): ",
salt = raw_input()
print "Enter the amount of Yeast (teaspoons): ",
yeast = raw_input()

#Creating the key piece that will determine the outcome
print "Enter the loaf adjustment factor (e.g. 2.0 double the size): ",
adjustmentfactor = raw_input()

#converting the adjustment factor intoa  float, from a string.
adjustmentfactor = float(adjustmentfactor)

#just creating a space for neatness
print " "

print " -- Modified Recipe -- "

#So I converted the initial measurements taken above to float within the math,below 
print "BreadFlour: %.2f cups." % (float(flour)*adjustmentfactor)

print "Water: %.2f cups." % (float(water)*adjustmentfactor)

print "Salt: %.2f teaspoons." % (float(salt)*adjustmentfactor)

print "Yeast: %.2f teaspoons." % (float(yeast)*adjustmentfactor)

print "Happy Baking!"


#creating space
print " "

#Converting to grams
print " -- Modified Recipe -- "

#So I converted the initial measurements taken above to float within the math,below 

print "BreadFlour: %.2f grams." % ((float(flour)*120) * (adjustmentfactor))

print "Water: %.2f grams." % ((float(water)*237)*(adjustmentfactor))

print "Salt: %.2f grams." % ((float(salt)*5)*(adjustmentfactor))

print "Yeast: %.2f grams." % ((float(yeast)*3)*(adjustmentfactor))

print "Happy Baking!"






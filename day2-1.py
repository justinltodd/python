#!/Users/Justin/anaconda/bin/python
"""
Write a script that takes a user inputted number and prints
whether it is positive, negative or zero, with
"The inputted number is (positive/negative/zero)" depending."
"""

print " "
number = int(raw_input("Enter a postive or negative number or zero: "))
print " "
if number > 0:
    print " " , number , "is a postive integer!"
    print " "
elif number < 0:
    print " " , number , "is a negative interger!"
    print " "
else:
    print " " , number , " is equal to Zero!"
    print " "

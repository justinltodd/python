#!/Users/Justin/anaconda/bin/python
'''
Write a script that takes two user inputted numbers and prints
"The first number is larger" or "The second number is
larger" depending on which is larger.
'''

x = int(raw_input("Enter a number for X: "))
y = int(raw_input("Enter a number for Y: "))

if x > y:
    print x , "is larger than" , y
elif y > x:
    print y , "is larger than" , x
elif x == y:
    print x , "equal to" , y

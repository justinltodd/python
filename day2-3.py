#!/Users/Justin/anaconda/bin/python
'''
Write a script that computes the factorial of a user inputted number.
'''

x = int(raw_input("Enter a number to see the factorial value: "))

factorial = 1

if x < 0:
    print "Cannot find factorial for negative numbers ie." , x
elif x == 0:
    print "Factorial for" , x , "is 1"
else:
    while x >= 1:
        factorial = factorial * x
        x = x - 1
        print factorial

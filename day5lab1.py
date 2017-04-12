#!/Users/Justin/anaconda/bin/python
'''
Day 5
'''

def count(num):
    '''
    Adds one to an input number
    INPUT: num as int or float
    OUTPUT: Results to counting to the input number
    '''

    while num > 0:
        print "number is : " , num
        num -= 1

num = int(raw_input("Enter a number to count to: "))
count(num)
#print number
print count.__doc__

def vertical(user):
    '''
    Vertically outputs tex
    INPUT: String
    OUTPUT: Vertical String
    '''

    for c in user:
        print c

user = raw_input("Please enter a string: ")
vertical(user)

print vertical.__doc__

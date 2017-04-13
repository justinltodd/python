#!/Users/Justin/anaconda/bin/python
'''
Part 2 - Advanced Practice Day5
'''

def calculate(num):
    '''
    Function to calculate input values from users
    INPUT: String
    OUTPUT: Phonetic term
    '''

    total_beers = 99

    if num <= total_beers:
        remaining = total_beers - num
        print "There are", remaining , "beers remaining on the wall!"
    else:
        print "There are only" , total_beers , "beers on the wall not" , num

num = int(raw_input("How many beers did you drink?: "))
calculate(num)

print calculate.__doc__

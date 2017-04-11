#!/Users/Justin/anaconda/bin/python
'''
Square values in Dictionary.
'''
values = raw_input("Please enter numbers separated by dashes ( - ): ").split("- ")
#print values


#numbers = dict_string.split("- ")


sum_dict = {}
for numbers_stri in values:
    numbers = int(numbers_stri)
    #print numbers
    sum_dict[numbers] = numbers ** 2

# Dict comp way of doing this
square_dict = {int(numbers): int(numbers) ** 2 for numbers in values}

print sum_dict
print square_dict

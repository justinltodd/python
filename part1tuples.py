#!/Users/Justin/anaconda/bin/python
'''

'''

x_list = raw_input("Please enter numbers separated by commas and a space ex 5, 6,: ")

numbers = x_list.split(", ")
print numbers

x_tuple = []

for pair in zip(numbers[::2], numbers[1::2]):
    x_tuple.append(pair)

x_tuple = [pair for pair in zip(numbers[::2], numbers[1::2])]

print x_tuple

#!/Users/Justin/anaconda/bin/python
"""
Happy Numbers
"""

my_num_str = raw_input("Pick a number: ")

my_num = 0
max_iteration = 0

while my_num != 1 and max_iteration < 10:
    my_num = 0
    for n in range(0,len(my_num_str)):
        print "Integer to index into my_num_str: ", n
        cur_digit = int(my_num_str[n])
        my_num = my_num + cur_digit ** 2
        print "Updated: ", my_num
    my_num_str = str(my_num)
    max_iteration += 1

if my_num == 1:
    print "Your number is HAPPY!"
else:
    print "Your number is SAD!"

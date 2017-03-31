#!/Users/Justin/anaconda/bin/python
#  Horoscope - AUTH JUSTIN TODD

print "XXXXXXXXXXX"
print " "
print "Welcome!!!"

first_name = str(raw_input("Type First name: "))
#print first_name
last_name = str(raw_input("Type Last name: "))
print ""
print first_name , last_name
print ""
current_month = 0

while current_month == 0:
        raw_month = int(raw_input("Enter Birthday as a number: "))
        if raw_month > 0 and raw_month < 13:
            current_month = raw_month
        else:
            print "Please enter a number between 1 and 12"

#print "outside while loop" , current_month

if current_month == 1:
    print "Your month is January"
elif current_month == 2:
    print "Your month is February"
elif current_month == 3:
    print "Your month is March"
elif current_month == 4:
    print "Your month is April"
elif current_month == 5:
    print "Your month is May"
elif current_month == 6:
    print "Your month is June"
elif current_month == 7:
    print "Your month is July"
elif current_month == 8:
    print "Your month is August"
elif current_month == 9:
    print "Your month is September"
elif current_month == 10:
    print "Your month is October"
elif current_month == 11:
    print "Your month is November"
else:
    print "Your month is December"

print " "
print "XXXXXXXXXXX"

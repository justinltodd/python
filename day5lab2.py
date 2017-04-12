#!/Users/Justin/anaconda/bin/python
'''

'''

phone_dict={'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo',
'F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliett','K':'Kilo',
'L':'Lima','M':'Mike','N':'November','O':'Oscar','P':'Papa','Q':'Quebec',
'R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform','V':'Victor', 'W':'Whiskey',
'X':'X-ray','Y':'Yankee','Z':'Zulu'}

phonetic = []

def phonetic_it(user_input):
    '''
    Phonetic
    INPUT: String
    OUTPUT: Phonetic term
    '''
    user_input = user_input.upper()
    values = [values for values in user_input]

    for i in values:
        phonetic.append(phone_dict[i])
    print phonetic

    #print phone_dict[coord_location]

user_input = raw_input("Enter a word: ")
phonetic_it(user_input)


print phonetic_it.__doc__

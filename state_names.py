#!/Users/Justin/anaconda/bin/python
'''
Get Capital city from dictionarty.
'''

state = raw_input("Enter state name for capital city: ").capitalize()

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                    'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                    'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}


#print state

#state_answer = state_dictionary[state]
#print state_answer
if state in state_dictionary:
    city = state_dictionary[state]
    print "Capital of", state , "is", city
else:
    print "Capital of", state , "is unknown!"

#!/Users/Justin/anaconda/bin/python
'''

'''

import string
from collections import Counter

gf_txt1 = "Let's go ride our bikes to get tacos. I love you!"
gf_txt2 = "Love, I LOVE YOU!"
dd_txt = "Oh dude, you are going to love this weed I just got"
boss1="Yeah........I'm gonna need you to come in on Saturday."
boss2="Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too."

txt_list = [gf_txt1 ,gf_txt2, dd_txt, boss1, boss2]
print txt_list[0]

#scoring dictionary
girlfriend = {'love':15, 'tacos':3, 'bikes':20}
drugDealer= {'weed':20 , 'dude':10, 'oh':5 }
boss = {'need':4, 'come':20, 'ahh':10}

print girlfriend['love']

num = int(raw_input("Enter an integer 0-4: "))
txt_org = txt_list[num]
print txt_org
txt = txt_org.lower()
print txt
txt = txt.translate(None, string.punctuation)
txt_list = txt.split(' ')

word_count = {}
for word in txt_list:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
print ""
print word_count
print ""

#Code Below replaces lines 34-39 if using from collections import Counter
word_frequency = Counter(txt_list)
print word_frequency

gf_score, dd_score, b_score = 0,0,0

for word, freq in word_count.iteritems():
    if word in girlfriend:
        gf_score = gf_score + girlfriend[word] * freq
    elif word in drugDealer:
        dd_score = dd_score + drugDealer[word] * freq
    elif word in boss:
        b_score = b_score + boss[word] * freq

print txt_org
print "Girlfriend: {} | Drug Dealer Score {} | Boss Score: {}".format(gf_score,dd_score,b_score)

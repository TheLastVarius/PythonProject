#!/usr/bin/python
import re
def letters(big_string):
    Mass=''
    Alphavit=['A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'Y', 'W']
    for i in range(len(big_string)):
        for j in range(len(Alphavit)):
            if big_string[i] == Alphavit[j]:
                Mass=Mass + Alphavit[j]
    return Mass
 
def palindrome(pali):
    m = ''
    for i in range(1,len(pali)+1):
        m += pali[-i]
    if pali == m:
        ret = "Palindrom"
    else:
        ret = "Ne Palindrom"
    return ret

def find_letter(where, letter):
    search = '(['+ letter.upper() +  ','+  letter +'].*?) '
    m=re.findall(search, where)
    return m
 
def mix_words(just_string):
    import random
    s = '' 
    search = '(\w*\w)'
    m = re.findall(search,just_string)
    random.shuffle(m)
    for i in range(len(m)):
	s = s + m[i] + ' '
    return s

print letters("Trees Are So Kind")
 
print palindrome("avid diva")
 
print find_letter("Bears are the best animals ever", 'b')
 
print mix_words("Bears are the best animals ever") 

#!/usr/bin/python
def letters(big_string):
    Mass = ''
    Alphavit=['A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'Y', 'W']
    for every_letter in big_string:
        for letter_alph in Alphavit:
            if every_letter == letter_alph:
                Mass = Mass + letter_alph
    return Mass
 
def palindrome(pali):
    if pali == pali[::-1]:
        ret = "Palindrom"
    else:
        ret = "Ne Palindrom"
    return ret

def find_letter(where, letter):
   retlist = []
   my_list = where.split()
   for my_letter in my_list:
	if my_letter[0] == letter or my_letter[0] ==  letter.upper():
	    retlist.append(my_letter)
   return ' '.join(retlist)
 
def mix_words(just_string):
    import random
    retstring = '' 
    search_word = just_string.split()
    random.shuffle(search_word)
    for word in search_word:
        retstring = retstring + word + ' '
    return retstring

print letters("Trees Are So Kind")
 
print palindrome("avid diva")
 
print find_letter("Bears are the best animals ever", 'b')
 
print mix_words("Bears are the best animals ever") 

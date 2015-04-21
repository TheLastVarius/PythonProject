#!/usr/bin/python

def multipliers(number):
    factors = []
    divider = 2
    while number  > 1:
        while number % divider == 0:
            factors.append(divider)
            number /= divider
        divider += 1
    return factors
 
def equation(a, b, c):
    import math    
    x1=(- b + math.sqrt(b ** 2 - 4 * a * c))/2 * a
    x2=(- b - math.sqrt(b ** 2 - 4 * a * c))/2 * a
    if float.is_integer(x1) and float.is_integer(x2): 
	n = [x1, x2]
    else: n = "None Results"
    return n

def simple(number):
    import math
    ret_phrase = "Prostoye"
    for divider in range(2, int(math.sqrt(number))):
        if number%divider == 0:
            ret_phrase = "NEPROSTOYE"
    return ret_phrase
 	
# atm uses only 100, 50, 20, 10, 5 and 1 notes.
def atm(summ):
    retspis = []
    for nom in [100, 50, 20, 10, 5, 1]:
        col_cup = summ//nom
        summ = summ - col_cup * nom
        retspis.append(col_cup)
    return retspis
 
print multipliers(30030)
 
print equation(2, 19, 35) # 2x^2 + 19x + 35 = 0
 
print simple(13)
 
print atm(287)

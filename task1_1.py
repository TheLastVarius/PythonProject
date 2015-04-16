#!/usr/bin/python

def multipliers(number):
    factors = []
    d = 2
    while number  > 1:
        while number % d == 0:
            factors.append(d)
            number /= d
        d += 1
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
    z="Prostoye"
    for i in range(2,number-1):
        if number%i == 0:
	    print i
            z="NEPROSTOYE"
	    return z
    return z
 	
# atm uses only 100, 50, 20, 10, 5 and 1 notes.
def atm(summ):
    A=[]
    for i in [100, 50, 20, 10, 5, 1]:
        k = summ//i
        summ = summ - k * i
        A.append(k)
    return A
 
print multipliers(30030)
 
print equation(2, 19, 35) # 2x^2 + 19x + 35 = 0
 
print simple(13)
 
print atm(287)

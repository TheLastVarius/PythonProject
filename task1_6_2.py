#!/usr/bin/python
#coding:utf8


import math
import itertools


#Задание 1_6_2. Функции. Часть А. Написать функцию, возвращающую несколько значений. 
#Объявление функции.
def resh(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = math.copysign(b,-1) + math.sqrt(D) / (2 * a)
        x2 = math.copysign(b,-1) - math.sqrt(D) / (2 * a)
        return x1, x2


#Задание 1_6_2. Часть В. Написать генератор. 
#Объявление функции.
def all_comb(randomlist):
    for element in itertools.permutations(randomlist):
        yield element

#Задание 1_6_2. Часть С. Написать генератор на lambda, nested function, closure.
def all_comb_nest(randomlist):
    def all_comb_ret_nest():
        for element in itertools.permutations(randomlist):
            yield element
    return all_comb_ret_nest
        


#Задание 1_6_2. Функции. Часть А. Написать функцию, возвращающую несколько значений. 
#Работа с функцией.
print "Введите значения коэффициентов а, b, с, для уравнения вида ax^2 + bx +c = 0"
try:
    x1, x2 = resh(input(), input() , input())
except TypeError:
    print "Корней нет"
else:
    print "Корни уравнения таковы х1 = %s , x2 = %s" % (x1,x2)
print "--------------------------------------------------------"

#Задание 1_6_2. Часть B. Написать генератор.
#Работа с функцией.
for comb_list in all_comb(input()):
    print comb_list

#Задание 1_6_2. Часть С. Написать генератор на lambda, nested function, closure.
#Работа с функцией.
nest_func = all_comb_nest(input())
for comb_list in nest_func():
    print comb_list

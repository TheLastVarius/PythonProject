#!/usr/bin/python
#coding:utf8


import os
import math
import time
import itertools


#Задание 1_6_2. Функции. Часть А. Написать функцию, возвращающую несколько значений. 
def resh(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = math.copysign(b,-1) + math.sqrt(D) / (2 * a)
        x2 = math.copysign(b,-1) - math.sqrt(D) / (2 * a)
        return x1, x2

print "Введите значения коэффициентов а, b, с, для уравнения вида ax^2 + bx +c = 0"
try:
    x1, x2 = resh(input(), input() , input())
except TypeError:
    print "Корней нет"
else:
    print "Корни уравнения таковы х1 = %s , x2 = %s" % (x1,x2)
print "--------------------------------------------------------"


#Задание 1_6_2. Часть В. Написать генератор. 
def all_comb(randomlist):
    for element in itertools.permutations(randomlist):
        yield element

print "Генератор, введите список вида a,b,c,..."
for comb_list in all_comb(input()):
    print comb_list


#Задание 1_6_2. Часть С. Написать генератор на lambda, nested function, closure.
def all_comb_nest(randomlist):
    def all_comb_ret_nest():
        for element in itertools.permutations(randomlist):
            yield element
    return all_comb_ret_nest
        
print "Генератор на lambda, введите список вида a,b,c,..."
lamb_gen = lambda: itertools.permutations(input())
for element in lamb_gen():
    print element

print "Генератор на nest func, введите список вида a,b,c,..."
nest_func = all_comb_nest(input())
for comb_list in nest_func():
    print comb_list


#Задание 1_6_2. Часть d. Написать генератор на *args, **kwargs, optional, named
def func_args(*args, **kwargs):
    for arg in args:
        yield args

cloud = [1,2,3,4,5]
for element in func_args(cloud):
    print element

def func_opt_name(fish,dog="Sharic", cat="Murka"):
    work_list = [fish, dog, cat]
    for element in itertools.permutations(work_list):
        yield element

for element in func_opt_name("Molchun", "Baron"):
    print element

#Задание 1_6_2.py Часть е. Написать декоратор, показывающий время работы функции. 
def time_work_func_decor(randomfunc):
    def tmp_func(*args, **kwargs):
        t = time.time()
        res = randomfunc(*args, **kwargs)
        print "Время выполнения функции: %f" % (time.time()-t)
        return res
    return tmp_func


@time_work_func_decor
def summ_func(x, y):
    return x + y

print summ_func(1,2)


#Задание 1_6_2.py Часть е. Написать декоратор, выводящий имя функции перед её исполнением.
def func_name_decor(randfunc):
    def workfunc(*args, **kwargs):
        print randfunc.__name__
        return randfunc(*args)
    return workfunc

@func_name_decor
def summ(a,b):
    return a+b

print summ(6,2)


#Задание 1_6_2.py Часть е. Написать декоратор, запрещающий выполнение функции
#если она запущена не от указанного пользователя
def name_user_decor(randfunc):
    def workfunc(*args, **kwargs):
        if os.getlogin() == "ganjurbas":
            return randfunc(*args)
        else:
            print "Запрещено"
    return workfunc()

@name_user_decor
def best_os_name():
    return 'Ubuntu'

print best_os_name



#Задание 1_6_2.py Часть е. Написать декоратор. Если функция вернула True
#ничего не делать, если функция вернула строку, выбросить исключение
#с данной строкой в виде параметра. 
def except_func_decor(randfunc):
    def workfunc(*args, **kwargs):
        result = randfunc(*args)
        if result == True:
            return None
        if type(result) == type("Aaaaa"):
            raise NameError, result
    return workfunc()

@except_func_decor
def str_func():
    return "Random String"

print test_func
print str_func







#!/usr/bin/python
#coding:utf8


import itertools


#Блок функций для Блока А задания 1:
def list_modif(randomlist):
    yield [element*2 for element in randomlist]

def if_list_modif(randomlist):
    yield [element*element for element in randomlist]

def two_list_modif(randomlist1, randomlist2):
    yield dict(zip(randomlist1, randomlist2))


#Блок функций для блока Б задания 1:
def gen_list_modif(randomlist):
    return (element*2 for element in randomlist)

def gen_if_list_modif(randomlist):
    return (element*element for element in randomlist if element%2 == 0)

def gen_two_list_modif(randomlist1, randomlist2):
    return (element for element in randomlist1 if len(randomlist2[randomlist1.index(element)]) > 3)


#Блок A Задания 1_6_1. Comprehensions:
#Минимум три примера list comprehensions, возвращающие итератор
#1. Модифицируем список.
#2. Содержит условие.
#3. Использует два списка
for element in list_modif([1,2,3,4,5]):
    print element
for element in if_list_modif([1,2,3,4,5]):
    print element
for element in two_list_modif([1,2,3,4,5],['one','two','three','four','five']):
    print element
print "------------------------------------------------"


#Блок Б задания 1_6_1. Comprehensions:
#Минимум три примера list comprehensions, возвращающие генератор
#1. Модифицируем список.
#2. Содержит условие
#3. Использует два списка
for element in gen_list_modif([1,2,3,4,5]):
    print element
for element in gen_if_list_modif([1,2,3,4,5]):
    print element 
for element in gen_two_list_modif([1,2,3,4,5],['one','two','three','four','five']):
    print element
print "------------------------------------------------"


#Блок С задания 1_6_1. Comprehensions:
#Минимум 5 примернов работы с itertools. 
for element in itertools.takewhile(lambda filt_num: filt_num < 100, [10, 20, 50, 120, 300, 15]):
    print element

for element in itertools.dropwhile(lambda filt_num: filt_num < 100, [10, 20, 50, 120, 300, 15]):
    print element

for element in itertools.starmap(pow, [(1,1), (2,2), (3,3)]):
    print element

for element in itertools.chain(iter([1,2,3]), iter([4,5])):
    print element

for element in itertools.product('ABC', 'abc'):
    print element 

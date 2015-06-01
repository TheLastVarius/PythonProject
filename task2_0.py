#coding:UTF8
import re


work_file = open('html.txt','r')
tag_list = ['head', 'body', 'title'] #Список тегов, обрабатываемых программой.
whitespace_tag_list_in_file = [] #Список тегов, найденных в файле вместе с пробелами перед ними.
tag_list_in_file = [] #Cписок тегов, найденных в файле без пробелов.
tmp_list = [] #Cписок для хранения временных данных.
whitespace_list = [] #Cписок для хранения пробелов в строковом виде

#Создаёт список тегов с пробелами, и список тегов без пробелов, найденных в файле
for line in work_file:    
    for element in tag_list:
        whitespace_tag_list_in_file.append(re.findall(" *" + element, line))
        tmp_list.append(re.findall(element, line))
        for element in tmp_list:
            if len(element) < 1:
                tmp_list.remove(element)
        for element in whitespace_tag_list_in_file:
            if len(element) < 1:
                whitespace_tag_list_in_file.remove(element) #Результат работы блока
for element in tmp_list:
    tag_list_in_file.append(element[0])#Результат работы блока
tmp_list[:] = []
work_file.close()


#Делает из списка списков пробелов- список пробелов.
schet = 0
for element in whitespace_tag_list_in_file:
    whitespace_tag_list_in_file[schet] = element[0]
    schet = schet + 1


#Блок записывает в файл результата строки с открывающими тегами.
work_file = open('html.txt','r')
result_file = open("html_result.txt","w")
for element in tag_list_in_file:
    tmp_list.append("<"+element+">")
schet = 0
for line in work_file:
    result_file.write(line.replace(tag_list_in_file[schet],tmp_list[schet]))
    if schet < len(tmp_list)-1:
        schet = schet + 1
result_file.close()
tmp_list[:] = []
work_file.close()
result_file.close()


#Блок создаёт список с пробелами, соответственно каждому тегу.
for element in whitespace_tag_list_in_file:
    tmp_list.append(re.findall(" *", element))
for element in tmp_list:
    whitespace_list.append(element[0])
tmp_list[:] = []


#Дозапись в файл закрывающих тегов
result_file = open("html_result.txt","a")
schet = 0
for element in tag_list_in_file[::-1]:
    tmp_list.append(element)
for element in whitespace_list[::-1]:
    result_file.write(element + "</"+str(tmp_list[schet])+">\n")
    schet = schet + 1
result_file.close()

#coding:UTF8
import re


work_file = open('html.txt','r')
tag_list = ['head', 'body', 'title'] #Список тегов, обрабатываемых программой.
whitespace_tag_list_in_file = [] #Список тегов, найденных в файле вместе с пробелами перед ними.
tag_list_in_file = [] #Cписок тегов, найденных в файле без пробелов.
tmp_list = [] #Cписок для хранения временных данных.

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
work_file.close()
tmp_list[:] = []


#Блок записывает в файл результата строки с открывающими тегами.
work_file = open('html.txt','r')
result_file = open("html_result.txt","w")
for element in tag_list_in_file:
    tmp_list.append("<"+element+">")
schet = 0
for line in work_file:
    result_file.write(line.replace(tag_list_in_file[schet],tmp_list[schet]))
    schet = schet + 1
result_file.close()
tmp_list[:] = []


print tmp_list
print tag_list_in_file
print whitespace_tag_list_in_file

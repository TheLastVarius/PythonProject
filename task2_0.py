#coding:UTF8
import re

class Template:

    def __init__(self):
        self.wall_to_file = input("Введите путь к файлу\n")
        self.tag_list = []
        self.whitespace_tag_list_in_file = [] #Список тегов, найденных в файле вместе с пробелами перед ними.
        self.tag_list_in_file = [] #Cписок тегов, найденных в файле без пробелов.
        self.tmp_list = [] #Cписок для хранения временных данных.
        self.whitespace_list = [] #Cписок для хранения пробелов в строковом виде


    def tags_list(self):
        print("Введите список обрабатываемых тегов через запятую:\n")
        tags_str = input()
        for element in tags_str.split(','):
            self.tag_list.append(element)
        return None

    def treatments(self):
        try:
            work_file = open(self.wall_to_file,'r')
        except(FileNotFoundError):
            print ("Введите корректный путь к файлу. Программа завершена.")
#Создаёт список тегов с пробелами, и список тегов без пробелов, найденных в файле
        for line in work_file:
            for element in self.tag_list:
                self.whitespace_tag_list_in_file.append(re.findall(" *" + element, line))
                self.tmp_list.append(re.findall(element, line))
                for element in self.tmp_list:
                    if len(element) < 1:
                        self.tmp_list.remove(element)
                for element in self.whitespace_tag_list_in_file:
                    if len(element) < 1:
                        self.whitespace_tag_list_in_file.remove(element) #Результат работы блока
        for element in self.tmp_list:
            self.tag_list_in_file.append(element[0])#Результат работы блока
        self.tmp_list[:] = []
        work_file.close()
#Делает из списка списков пробелов- список пробелов.
        schet = 0
        for element in self.whitespace_tag_list_in_file:
            self.whitespace_tag_list_in_file[schet] = element[0]
            schet = schet + 1


#Блок записывает в файл результата строки с открывающими тегами.
        work_file = open('html.txt','r')
        result_file = open("html_result.txt","w")
        for element in self.tag_list_in_file:
            self.tmp_list.append("<"+element+">")
        schet = 0
        for line in work_file:
            result_file.write(line.replace(self.tag_list_in_file[schet],self.tmp_list[schet]))
            if schet < len(self.tmp_list)-1:
                schet = schet + 1
        result_file.close()
        self.tmp_list[:] = []
        work_file.close()
        result_file.close()



#Блок создаёт список с пробелами, соответственно каждому тегу.
        for element in self.whitespace_tag_list_in_file:
            self.tmp_list.append(re.findall(" *", element))
        for element in self.tmp_list:
           self. whitespace_list.append(element[0])
        self.tmp_list[:] = []


#Дозапись в файл закрывающих тегов
        result_file = open("html_result.txt","a")
        schet = 0
        for element in self.tag_list_in_file[::-1]:
            self.tmp_list.append(element)
        for element in self.whitespace_list[::-1]:
            result_file.write(element + "</"+str(self.tmp_list[schet])+">\n")
            schet = schet + 1
        result_file.close()
        print("Обработка завершена")
        return None


my_object = Template()

my_object.tags_list()
my_object.treatments()

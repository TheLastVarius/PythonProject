def try_func():
    ret_spis = []
    work_file = open('task1_5File.txt','r')
    string_from_file = work_file.read()
    
    print 'Please, enter length of phrase what you need:' 
    len_list = input()
    try:
        for element in range(len_list):
	    ret_spis.append(string_from_file[element])
    except IndexError:
	print 'Phrase don\'t have an amount element'
    else:
	return ret_spis
    finally:
	work_file.close()
	print 'Programm work end, file close'

print try_func()

def create_dict_twolist(randlist1, randlist2):
    return dict(zip(randlist1, randlist2)) 


def create_dict_twocort(spis_cort):
    return dict(spis_cort)


def dict_string(randdict, randstring):
    for key, value in randdict.iteritems():
        if key == randstring:
            randdict[key] = None
    return randdict


def two_dict(randdict1, randdict2):
    intsect=set(randdict1).intersection(randdict2)
    for key in intsect:
	del randdict1[key]
	del randdict2[key]
    randdict1.update(randdict2)
    return randdict1


def calc(oper_str, number1, number2): 
    my_dict = {'add':number1+number2, 
	       'mult':number1*number2, 
	       'div':number1/number2, 
	       'sub':number1-number2}
    return (my_dict[oper_str])


def replace_dict(randomdict):
    return {couple[1] : couple[0] for couple in randomdict.items()}
 
print create_dict_twolist([1,2,3], ['one', 'two', 'three'])
print create_dict_twocort([('one', 1), ('two', 2), ('three', 3)])
print dict_string({'cat':'home', 'dog':'street', 'monkey':'forest'},'dog')
print two_dict({'1':'one', '2':'two','3':'three','4':'four'}, {'1':'cat', '3':'dog', '5':'python', '6':'bee'})
print calc('add', 30, 5)
print replace_dict({'one':'1', 'three':'3', 'two':'2',  'four':'4'})

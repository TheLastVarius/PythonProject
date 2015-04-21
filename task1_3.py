def fun_repeat(randomlist):
    retlist = []
    for schet in randomlist:
	if randomlist.count(schet) > 1 and retlist.count(schet) < 1:
	        retlist.append(schet)
    return retlist

def data_type(randomlist):
    retlist = []
    type_list = [element.__class__.__name__ for element in randomlist]
    for element in type_list:
	addstr = element + ' => ' + str(type_list.count(element))
        if retlist.count(addstr) == 0:
	    retlist.append(addstr)
    return ' '.join(retlist)
		
def sort_last(randomlist):
    randomlist.sort(key = lambda randomlist:randomlist[-1])
    return randomlist

def spis_str(sortlist, randomstring):
    for element in sortlist:
	if randomstring > element:
	    sortlist.insert(sortlist.index(element)+1, randomstring)	    
    return sortlist
    
def twospis(list1,list2,element):
    list1.insert(list2.index(element), element)
    return list1

def str_nechet(randomstring):
    retstr = ''
    for word in list(randomstring.split()):
	if len(word) % 2 == 0:
	    retstr = retstr + word + ' '
    return retstr

def posled(randomlist):
    workspis =[]
    indexlist =[]
    schet = 0
    while schet  < len(randomlist) - 1:
        retspis = [randomlist[schet]]
	while randomlist[schet] == randomlist[schet+1]-1:
	    retspis.append(randomlist[schet+1])
	    schet += 1
	    if schet == len(randomlist) - 1:
	        break
	schet += 1
	workspis.append(retspis)

    lenspis = [len(schet) for schet in workspis]

    for schet in lenspis:
	if schet == max(lenspis):
	    indexlist.append(lenspis.index(schet))
	    del lenspis[lenspis.index(schet)]
	    lenspis.insert(0, 0)

    return [workspis[schet] for schet in indexlist]

print fun_repeat(['cat',3,4,5,6,7,8,2,3,4,'cat','bed'])
print data_type([2,5,6,3.5,4.6,'dog','python', 'cat', [2,3,4],[3,33]])
print sort_last(['BANANA', 'ZOEC', 'MassE', 'UpdateD', 'KalimanB'])
print spis_str(['Alibek','Caid','Dagestan','Erevan'], 'Bishkek')
print twospis([1,3,5,7,9], [2,4,6,8], 4)
print str_nechet('A long time ago in the far far galaxy')
print posled([1,2,3,4,10,11,12,13,7,5,6,5,5,12,3,4,5,6])

def fun_repeat(randomlist):
    retlist = []
    for i in randomlist:
	if randomlist.count(i) > 1:
	    if retlist.count(i) < 1:
	        retlist.append(i)
    return retlist

def data_type(randomlist):
    import re
    mystr = '' 
    searchstr=''
    retlist = []
    for i in randomlist:
        mystr = mystr + str(type(i))
    searchlist = re.findall('\'(\w*)\'', mystr)
    for i in searchlist:
	if retlist.count(i) < 1:
		searchstr = searchstr + str(i) + ' => ' +  str(searchlist.count(i)) + ' '
		retlist.append(i)
    return searchstr
		
def sort_last(randomlist):
    randomlist.sort(key = lambda randomlist:randomlist[-1])
    return randomlist

def spis_str(sortlist, randomstring):
    sortlist.sort()
    worklist = list(sortlist)
    worklist.append(randomstring)
    worklist.sort()
    sortlist.insert(worklist.index(randomstring), randomstring)
    return sortlist
    
def twospis(list1,list2,element):
    list1.insert(list2.index(element), element)
    return list1

def str_nechet(randomstring):
    retstr = ''
    for i in list(randomstring.split()):
	if len(i) % 2 == 0:
	    retstr = retstr + i + ' '
    return retstr

def posled(randomlist):
    workspis =[]
    indexlist =[]
    i = 0
    while i < len(randomlist) - 1:
        retspis = [randomlist[i]]
	while randomlist[i] == randomlist[i+1]-1:
	    retspis.append(randomlist[i+1])
	    i += 1
	    if i == len(randomlist) - 1:
	        break
	i += 1
	workspis.append(retspis)

    lenspis = [len(schet) for schet in workspis]

    for schet in lenspis:
	if schet == max(lenspis):
	    indexlist.append(lenspis.index(schet))
	    del lenspis[lenspis.index(schet)]
	    lenspis.insert(0, 0)

    return [workspis[schet] for schet in indexlist]

print fun_repeat(['cat',3,4,5,6,7,8,2,3,4,'cat','bed'])
print data_type([2,3.2,5,6,'dog','python', 'cat', [2,3,4],[3,33]])
print sort_last(['BANANA', 'ZOEC', 'MassE', 'UpdateD', 'KalimanB'])
print spis_str(['Alibek','Erevan','Caid','Dagestan'], 'Bishkek')
print twospis([1,3,5,7,9], [2,4,6,8], 4)
print str_nechet('A long time ago in the far far galaxy')
print posled([1,2,3,4,10,11,12,13,7,5,6,5,5,12,3,4,5,6])

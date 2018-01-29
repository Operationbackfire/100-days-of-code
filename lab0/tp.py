def getSublists(ls):
    result = []
    for sublist in ls:
        if isinstance(sublist,(list,tuple)):
   		    result+= [item for item in sublist if isinstance(item,(list,tuple))]
    return result   

def hasLists(ls):
    return len([item for item in ls if isinstance(item,(list,tuple))]) > 0

#ls1 = ('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))
#print(getSublists(ls1))
#ls2 = [('-', ('expt', 'x', 2), 1), ('/', 5, 2)]
#print(getSublists(ls2))
#ls3 = [('expt', 'x', 2)]
#print(hasLists([('expt', 'x', 2)]))

ls0 = 'x'
ls1 = ('expt', 'x', 2)
ls2 = ('+', ('expt', 'x', 2), ('expt', 'y', 2))
ls4 = ('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))

#print([item for item in ((2,3), 'x', 2) if isinstance(item,(list,tuple))])

print ls4[0],ls4[1], ls4[2]    
print len(ls4)
#print(hasLists(getSublist(('+', ('expt', 'x', 2), ((2,3), 'y', 2)))))
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*4

mygenerator = createGenerator()
print mygenerator

for i in mygenerator:
    print(i)


"""
mygenerator = (x*2 for x in range(3))
print mygenerator
for i in mygenerator:
    print(i)

####

try:
    yield("hoho")
except:
    

#####

def divide(x,y):
    try:
        result = x/y
    except ZeroDevisionError:
        print "Math exploded!"
    else:
        print "The result is:", result
    finally:
        print "finally leaving"

divide(4,2)

####

try: 
    raise KeyboardInterrupt
finally:
    print "Goodbye World"    

#####

class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
    def test(self):
        return "Is this a joke?"
        
try: 
    raise MyError("What the fuck!")
except MyError as e:
    print 'My exception occurred, value:', e.test(), e.value
    
raise MyError("oops")
"""

    


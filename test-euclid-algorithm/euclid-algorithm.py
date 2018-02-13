#80-4*18=8
#18-2*8=2
#8-4*2 = 0
from time import sleep
import unittest

def euclid_algo(a,b):
    i=1
    c = a - i*b
    #80 - 1*18 = 
    
    while (c>0):
        print "%s - %s*%s = %s" % (a,i,b,c) 
        i+=1  
        c = a - i*b
        
    if c == 0:
        print "%s - %s*%s = %s" % (a,i,b,c) 
        print "greatest common divisor is:",b
    
    if c > 0 or c < 0:
        return euclid_algo(b,c+b)

euclid_algo(80,18)
euclid_algo(72,17)
euclid_algo(100,10)
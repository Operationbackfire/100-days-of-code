#doesn't work
 
from timeit import Timer 
from recumemo import fib

print(fib(3))

for i in range(1,41):
	s = 'fib(' + str(i) + ')'
    t1 = timeit(s,setup = "from fibo import fib")
	time1 = t1.timeit()
    

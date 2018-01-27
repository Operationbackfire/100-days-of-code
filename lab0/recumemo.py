#https://www.python-course.eu/recursive_functions.php
#Python-Course.eu

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#print(fib(3))
    
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    
#print(fibi(3))

memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]
    
#print(fibm(3))

#Excercises
#1
def three(n):
    if n == 0:
        return 0
    return 3 + three(n-1)
    
#print(three(6))

#2
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

#print(sum(4))

#3
#This function is not writing anything to the screen
def pasc(n):
    for r in range(n+1):
        if r == 0: 
            return 1
        if r == n:
            return 1
        return pascal(n-1,r) + pascal(n-1,r-1)

#pasc(3)

#1. solutions from homepage (do not understand properly)
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(6))

#2. solution from homepage (do not understand properly)
def pascal1(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n-1)
        line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        line.insert(0,1)
        line.append(1)
    return line

#print(pascal1(6))

#https://www.python-course.eu/python3_recursive_functions.php
#More exercises.
#4 looks difficult and interesting.



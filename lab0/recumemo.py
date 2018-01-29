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

#1. solutions from homepage. ok.
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

#print(pascal(6))

#2. solution from homepage. ok.
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

#4
#def fibf(n):
#    return pascal(n)[0] + pascal(n-1)[]
#Eksempel: fibf(7) 
#Should return 1 + 5 + 6 + 1 = 13, 1 + 4 + 3 = 8, 5, 3, 2, 1 , 1
     
def fib_pascal(n,fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n-1, fib_pos+1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        
        #F.eks. f_p(5,0) kalder f_p(1,4) hvor 3 < 2 er falsk.
        #F.eks. f_p(6,0) kalder f_p(1,5) hvor 4 < 2 er falsk, 
        #og f_p(2,4) hvor 3 < 3 er falsk. 
        #In these cases
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)

#print(fib_pascal(3,0)[1])

def fib(n):
    return fib_pascal(n,0)[1]

#and now printing out the first ten Fibonacci numbers:
#for i in range(1,10):
#   print(fib(i))

#5. Not Recursive.

def eratos(n):
    a = []
    for i in range(n-1):
        a.append(i + 2)  
    #print(a)
    
    for i in range(len(a)):
        if (a[i]%2) == 0:
            a[i] = -1
        if (a[i]%3) == 0:
            a[i] = -1
        if (a[i]%5) == 0:
            a[i] = -1
        if (a[i]%7) == 0:
            a[i] = -1
    #print(a)        
    
    b = [2,3,5,7]
    
    for i in range(len(a)):
        if a[i] != -1:
            b.append(a[i]) 
    
    #print(b)

#eratos(120)

#5. solution from homepage. TRY TO UNDERSTAND THE CODE. LIST COMPREHENSION.
from math import sqrt

def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n + 1, i)]
        print("This is no_p: ")
        print(no_p)
        p = [x for x in range(2, n + 1) if x not in no_p]
        print("This is p: ")
        print(p)
        return p

#print(primes(6))

#LIST COMPREHENSION
#https://www.python-course.eu/python3_list_comprehension.php
a = [j for i in [2,3,4] for j in range(i*i,i*i+i*4,i)]
#forventet resultat [4,6,8,10,9,12,15,18,21,16,20,24,28,32]
#print(a)
#As expected. It is called List Comprehension.
b = [j for i in [] for j in range(i*i,i*i+i*4,i)]
#forventet res []
#print(b)
#ok

#Testing with primes(6)
c = [x for x in range(2, 2 + 1) if x not in []]
#print(c)
#
d = [j for i in [2] for j in range(i*2, 6 + 1, i)]
#print(d)
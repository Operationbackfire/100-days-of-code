# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = 'fill-me-in'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x*x*x

#raise NotImplementedError

#print(cube(2))

def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

#raise NotImplementedError

#print(factorial(4))

#tupples ()
#list 
def test(index, pattern,lst):
    m = 0
    for j in range(0,len(pattern)):
        if lst[index] == pattern[j]:
            m = m + 1
    return (m == len(pattern)-1)
       

def count_pattern(pattern, lst):
    n = 0
    for i in range(0,len(lst)-len(pattern)+1):
        if test(i, pattern,lst):
            n = n + 1
    #print(n)

#raise NotImplementedError

count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a','b','a')) 
count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a')) 

# Problem 2.2: Expression depth

#def deep(expr,n):
#    m = n
#    for i in range(0,len(expr)-1):
#        if isinstance(expr[i], (tuple)): 
#            n = n + 1
#            return deep(expr[i],n)
#    if m == n
#        return n
        #what has to be returned?
        #hvis ingen tuple, then returner            
    
 
# This code is taken from https://github.com/junoon53/mit-ocw-6.034-artificial-intelligence/blob/master/lab0/lab0.py   
def depth(expr):   
    depth = 0
    currentLists = expr
    
    def hasLists(ls):
        return len([item for item in ls if isinstance(item,(list,tuple))]) > 0
    
    def getSublists(ls):
   	    result = []
   	    for sublist in ls:
   		    if isinstance(sublist,(list,tuple)):
   			    result+= [item for item in sublist if isinstance(item,(list,tuple))]
            return result
    
    if isinstance(expr,(list,tuple)):
        #e.g. depth(('expt', 'x', 2)). Input is a tuple.
        depth+=1
        #Lets take as example depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))) => 4
        #It can be seen as tree structure.
        #hasLists(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))) => True
        while hasLists(currentLists):
            depth+=1
            #1. iteration: We get a list back, not a tuple: [('-', ('expt', 'x', 2), 1), ('/', 5, 2)]
            #2. iteration: [('expt', 'x', 2)]
            currentLists = getSublists(currentLists)
        return depth
    else:
        #e.g. depth('x'). Input is not a tuple.
        return 0

#raise NotImplementedError

#print depth('x')
#print depth(('expt', 'x', 2))
#print depth(('+', ('expt', 'x', 2), ('expt', 'y', 2)))
#print depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2))))

#ls0 = 'x'
#ls1 = ('expt', 'x', 2)
#ls2 = ('+', ('expt', 'x', 2), ('expt', 'y', 2))
#ls4 = ('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))

#it doesn't work
#def depth2(expr):
#    a = []
#    for j in range(len(expr)):
#        if isinstance(expr,(list,tuple)) == 0:
#            a.append(0)
#            if len(a) == len(expr):
#                return max(a)
#        else:
#            a.append(1 + depth2(expr[j]))
            
#print(depth2(ls4))

# Problem 2.3: Tree indexing

#it works
def tree_ref(tree, index):
    subtree = tree
    for i in index:
        subtree = subtree[i]
    return subtree

tree1 = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))

#it works
print tree_ref(tree1, (3, 1))
print tree_ref(tree1, (1, 1,1))
print tree_ref(tree1, (1,))


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = ""

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = ""

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = ""

# How many hours did this lab take?
HOURS = ""

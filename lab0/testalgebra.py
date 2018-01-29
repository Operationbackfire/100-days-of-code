class MyClass:
    i = 1
    def f(self):
        return "hello world"

#print MyClass.i
x = MyClass()
#print x.f()


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    
x = Complex(2,3)
#print x.r,x.i

class Person:
    job = 'teacher'
    
    def __init__(self, name):
        self.name = name
        
a = Person('Claus')
#print a.name
b = Person('Niels')
#print b.name

class Employee:
    pass

john = Employee()
john.name = 'John Doe'

#print john.name

class Expression:
    "This abstract class does nothing on its own."
    pass

class Sum(list, Expression):
    """
    A Sum acts just like a list in almost all regards, except that this code
    can tell it is a Sum using isinstance(), and we add useful methods
    such as simplify().

    Because of this:
      * You can index into a sum like a list, as in term = sum[0].
      * You can iterate over a sum with "for term in sum:".
      * You can convert a sum to an ordinary list with the list() constructor:
         the_list = list(the_sum)
      * You can convert an ordinary list to a sum with the Sum() constructor:
         the_sum = Sum(the_list)
    """
    def __repr__(self):
        return "Sum(%s)" % list.__repr__(self)
    
    #def test(self):
        
    def flatten(self):
        """Simplifies nested sums."""
        terms = []
        for term in self:
            #print isinstance(term, Sum)
            #print terms
            if isinstance(term, Sum):
                #print list(term)
                terms += list(term)
            else:
                terms.append(term)
        #print terms
        return Sum(terms)

x = Sum()
#print x
x.append('1')
#print x
x.append('7')
#print x
#print "x contains: "
#print x

xt = Sum()
xt.extend(['2',x,'4','5'])
#print "xt contains: "
#print xt
#print "xt after flattening: "
#print xt.flatten()
xpass = Sum(xt + x)
print xpass


class Product(list, Expression):
    """
    See the documentation above for Sum. A Product acts almost exactly
    like a list, and can be converted to and from a list when necessary.
    """
    def __repr__(self):
        return "Product(%s)" % list.__repr__(self)
        
    def flatten(self):
        """Simplifies nested products."""
        factors = []
        for factor in self:
            if isinstance(factor, Product):
                factors += list(factor)
            else:
                factors.append(factor)
        return Product(factors)

y = Product()
#print y
y.append('2')
#print y
y.append('x')
#print y
#print "y contains: "
#print y

yt = Product()
yt.extend(['x','y','z',y])
#print "yt contains: "
#print yt
#print "xt after flattening: "
#print yt.flatten()

def simplify_if_possible(expr):
    if isinstance(expr, Expression):
        return expr.simplify()
    else:
        return expr
        
def multiply(expr1, expr2):
    if not isinstance(expr1, Expression): expr1 = Product([expr1])
    if not isinstance(expr2, Expression): expr2 = Product([expr2])
    return do_multiply(expr1, expr2)

def do_multiply(expr1, expr2):
    if isinstance(expr1, Product) and isinstance(expr2,Product):
        exprout = Product(expr1 + expr2)
    if isinstance(expr1, Sum) and isinstance(expr2,Product):
        new_terms = [] #type list
        for term in expr1:
            new_terms.append(Product([term] + expr2)) 
            #the Product type derives the list operation: list(list1 + list2) = newlist from the list type
        exprout = Sum(new_terms) #type Sum
    if isinstance(expr1, Product) and isinstance(expr2,Sum):
        exprout = do_multiply(expr2,expr1)
    else: #Dette er Sum og Sum
        new_terms = []
        for t1 in expr1:
            for t2 in expr2:
                new_terms.append(Product([t1] + [t2]))
        exprout = Sum(new_terms)
    return exprout
        
    
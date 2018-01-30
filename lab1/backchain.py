from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

"""
print simplify(OR(1, 2, AND()))
print simplify(OR(1, 2, AND(3, AND(4)), AND(5)))
print simplify(AND('g1', AND('g2', AND('g3', AND('g4', AND())))))
print simplify(AND('g'))
print simplify(AND('g1', 'g1', 'g2'))
"""

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.
"""
def backchain_to_goal_tree(rules, hypothesis):
    #print "This is the newest hypothesis: "
    #print hypothesis
    results = [hypothesis]
    for r in rules:
        con = r.consequent()
        for e in con:
            #print e
            b = match(e, hypothesis)
            #print b
            if b or e == hypothesis:
                a = r.antecedent()
                print isinstance(a,str)
                if isinstance(a,str):
                #print "This is the antecendent: "
                #print a
                    n_hypo = populate(a,b)
                #print "This is the new hypothesis:  "
                #print n_hypo
                    results.append(backchain_to_goal_tree(rules,n_hypo))
                    results.append(n_hypo)
                #
                else: 
                    states = [populate(a_e, b) for a_e in a]
                    n_res = []
                    for state in states:
                        n_res.append(backchain_to_goal_tree(rules, state))
                    results.append(c_state(n_res,a))
    return simplify(OR(results))
"""

#Koden virker i en reduceret version
def backchain_to_goal_tree(rules, hypothesis):
    #print "This is the newest hypothesis: "
    #print hypothesis
    results = [hypothesis]
    for r in rules:
        con = r.consequent()
        for e in con:
            #print e
            b = match(e, hypothesis)
            #print b
            if b or e == hypothesis:
                a = r.antecedent()
                states = [populate(a_e, b) for a_e in a]
                n_res = []
                for state in states:
                    n_res.append(backchain_to_goal_tree(rules, state))
                results.append(c_state(n_res,a))
    return simplify(OR(results))

#fra https://github.com/junoon53/mit-ocw-6.034-artificial-intelligence/blob/master/lab1/backchain.py
def c_state(statements, rule):
    if isinstance(rule, AND):
        return AND(statements)
    elif isinstance(rule, OR):
        return OR(statements)
                
             
# Here's an example of running the backward chainer - uncomment
# it to see it work:
print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')



#cp = match("(?x) is a penguin", "Claus is a penguin")
#print cp
#print populate("(?x) is a penguin", cp)
#print match([test.consequent],['opus is a penguin'])
#match("(?x) is a (?y)", "John is a student")

#The following code is taken from 
#https://github.com/junoon53/mit-ocw-6.034-artificial-intelligence/blob/master/lab1/backchain.py
#I try to understand it.

"""
def backchain_to_goal_tree(rules, hypothesis):
    results = [hypothesis]
    for rule in rules:
        consequent = rule.consequent()
        for expr in consequent:
            bindings = match(expr, hypothesis)
            if bindings or expr == hypothesis:
                antecedent = rule.antecedent()
                if isinstance(antecedent, str):
                    new_hypothesis = populate(antecedent, bindings)
                    results.append(backchain_to_goal_tree(rules, new_hypothesis))
                    results.append(new_hypothesis)
                else:
                    statements = [populate(ante_expr, bindings) for ante_expr in antecedent]
                    new_results = []
                    for statement in statements:
                        new_results.append(backchain_to_goal_tree(rules, statement))
                    results.append(create_statement(new_results, antecedent))
    return simplify(OR(results))

def create_statement(statements, rule):
    if isinstance(rule, AND):
        return AND(statements)
    elif isinstance(rule, OR):
        return OR(statements)
# Here's an example of running the backward chainer - uncomment
# it to see it work:
print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
"""
# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = None

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = None

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = None

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = None

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = None

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = None

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

from graphs import *

#path1 = ['Common Area','Stairs','Grand Hall']

#print GRAPH1.is_valid_path(path1)

#print GRAPH1.get_edge('Common Area', 'Stairs')
#print GRAPH1.are_connected('Common Area', 'Stairs')
#print GRAPH1.get_connected_nodes('Common Area')
#print GRAPH1.set_heuristic('Common Area','Dungeon 5',2)
#print GRAPH1.get_heuristic('Dungeon 5','Common Area')
#print GRAPH1.get_heuristic('Hospital','Common Area')
#example:

#add_edge
#validate

#### IT WORKS
#calculate the length of a given path
#ex_path_in_GRAPH1 = ['Common Area','Stairs','Statues']
def get_path_length(graph,path):
    path_length = 0
    for i in range(len(path)-1):
         path_length += graph.get_edge(path[i],path[i+1]).length
    return path_length

#print get_path_length(GRAPH1,ex_path_in_GRAPH1)
####

####IT WORKS
def sort_by_path_length(graph,paths_list):
    
    a = range(len(paths_list))
    
    for i in range(len(paths_list)):
         a[i] = get_path_length(graph,paths_list[i])
    print a
    b = sorted(a)
    print b
    sorted_paths_list = range(len(paths_list))
    
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                sorted_paths_list[i] = paths_list[j]
    return sorted_paths_list
####

extended_list = ['Stairs']

def dfs1(graph, start, goal):
    
    ####
    if isinstance(start,str):
        left_path = [start] 
    else:
        left_path = start
    ####
    
    connected_nodes = GRAPH1.get_connected_nodes(left_path[-1])        
  
    #print "This is the connected_nodes: "
    #print connected_nodes
    
    ####
    for node_ext in extended_list:
        for node_con in connected_nodes:
            if node_ext == node_con:
                connected_nodes.remove(node_ext) 
    
    connected_nodes_nv = connected_nodes
    
    if not connected_nodes_nv:
        print "Node " + left_path[-1] + " is a leaf."
         
    extended_list.extend(connected_nodes_nv)
    
    #print "This is the extended_list: "
    #print extended_list
    
    ####
    
    ####
    agenda = range(len(connected_nodes_nv))
    
    for i in range(len(connected_nodes_nv)):
        agenda[i] = left_path + [connected_nodes_nv[i]]
    ####
    
    #print agenda
    #print sort_by_path_length(graph,agenda)
    
    #has to go throug
    for i in range(len(agenda)):
        if agenda[i][-1] == goal:
            print "A path to the goal has been found: " + str(agenda[i][-1])
        if not connected_nodes_nv:
            return left_path
        else:
            return dfs1(graph,agenda[i],goal)
    #raise NotImplementedError
#dfs1(GRAPH1,'Stairs','Dungeon 5') 
       



##https://github.com/junoon53/mit-ocw-6.034-artificial-intelligence/blob/master/lab2/lab2.py
#I HAVE TO LOOK THROUGH THE CODE TO UNDERSTAND IT.    
### THE FOLLOWING CODE IS TAKEN FROM
###https://github.com/junoon53/mit-ocw-6.034-artificial-intelligence/blob/master/lab2/lab2.py
def bfs(graph, start, goal):
    #This function is not recursively defined.
    pathList = [(start,)]
    if start == goal:
      return [start]
        
    while len(pathList) > 0:
        #print [ graph.get_heuristic(path[-1],goal) for path in pathList ]
        newPaths = []
        
        #picks the first path and extends it with alle its nodes. picks the second path and extends it with all its nodes. newPaths is filled with the new paths in every round
        while len(pathList) > 0:
            #f.eks. len([('S','A'),['S','B']))
            pathToExtend = pathList[0]
            #f.eks. ('S','A'). 
            #IMPORTANT: pathList is empty when the inner while-loop terminates.
            pathList.remove(pathList[0])
            
            """
            print "INSIDE"
            print pathList
            """
            
            #f.eks. 'A'
            nodeToExtend = pathToExtend[-1]
            """
            i += 1
            print i
            print nodeToExtend
            """
            
            newNodes = graph.get_connected_nodes(nodeToExtend)
            #f.eks. ['B','D','S']
            #print newNodes
            
            #Deletes newNodes that are already in pathToExtend
            if len(pathToExtend) > 1:
                newNodes = [ node for node in newNodes if node not in pathToExtend]
            #f.eks. ['B','D']
            #print pathToExtend
            
            #f.eks. check if 'G' is among ['B','D'] 
            if goal in newNodes:
                goalPath = pathToExtend + (goal,)
                #f.eks. ('S','A','D','G')
                #print "goalPath", goalPath
                return list(goalPath)
            #f.eks. [('S','A','B'),('S','A','D')]
            newPaths += [ pathToExtend + (node,) for node in newNodes ]
            #print "INSIDE"
            #print pathList
        #pathList is a global variable wiihin the 2 while loops. So   
        #pathList is empty when all the newPaths  
        pathList.extend(newPaths)
        #print "OUTSIDE"
        #print pathList
#print bfs(GRAPH1,'Stairs','Dungeon 5') 

#AGAIN SOME CODE FROM https://github.com/junoon53/mit-ocw-6.034-artificial-intelligence/blob/master/lab2/lab2.py

def dfs(graph, start, goal):
    pathList = [(start,)];
    
    reachedGoal = False
    if start == goal:
        return [start]
    
    while len(pathList) > 0:
        #print pathList
        #len([('S','A'),['S','B']))
        #('S','A')
        pathToExtend = pathList[0]
        #remove ('S','A') from [('S','A'),('S','B')]
        pathList.remove(pathList[0])
        #'A'
        nodeToExtend = pathToExtend[-1]
        newNodes = graph.get_connected_nodes(nodeToExtend)
        if len(pathToExtend) > 1:
            newNodes = [ node for node in newNodes if node not in pathToExtend ]
        if goal in newNodes:
            reachedGoal = True
            goalPath = pathToExtend + (goal,)
        
        #[('S','A','B'), ('S','A','D')]
        newPaths = [ pathToExtend + (node,) for node in newNodes ]
        
        #[('S','A','B'),('S','A','D'),('S','B')]
        newPaths.extend(pathList)
        pathList = newPaths
        if reachedGoal: break
    if reachedGoal:
        #print "goal path : " + str(goalPath)
        return goalPath
    else: return []

print bfs(GRAPH1,'Stairs','Dungeon 5') 

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
#AGAIN SOME CODE FROM https://github.com/junoon53/mit-ocw-6.034-artificial-intelligence/blob/master/lab2/lab2.py
def hill_climbing(graph, start, goal):
    pathList = [(start,)];
    reachedGoal = False
    if start == goal:
        return [start]
    while len(pathList) > 0:
        #print pathList
        #print [ graph.get_heuristic(path[-1],goal) for path in pathList ]
        #(S,A)
        pathToExtend = pathList[0]
        #Remove (S,A) from [(S,A),(S,B)]
        pathList.remove(pathList[0])
        #A
        nodeToExtend = pathToExtend[-1]
        #[B,D]
        newNodes = graph.get_connected_nodes(nodeToExtend)
        #removes already visited nodes
        if len(pathToExtend) > 1:
            newNodes = [ node for node in newNodes if node not in pathToExtend]
        #Looks after G in [B,D]
        if goal in newNodes:
            reachedGoal = True
            goalPath = pathToExtend + (goal,)
        
        #[(S,A,B),(S,A,D)]
        newPaths = [ pathToExtend + (node,) for node in newNodes ]
        ##print "newPaths" + str(newPaths)
        
        #find out which of the graphs are the longest.
        quickSort(graph,goal,newPaths)
        ##print "sortedPaths" + str(newPaths)
        newPaths.extend(pathList)
        pathList = newPaths
        if reachedGoal: break
    if reachedGoal:
        #print "goal path : " + str(goalPath)
        return list(goalPath)
    else: return []

## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.


## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''

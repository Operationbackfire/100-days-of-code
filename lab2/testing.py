from search import Graph
from graphs import *
import timeit

"""
def bfs1(graph, start, goal):
    #[('S',)]
    #[('S','A'),('S','B')]
    path_list = [(start,)]
    
    #We have to add and remove paths to the path_list. Everything is done at the front.
    while len(path_list) > 0:
        
        #will contain al the newly build paths after the second
        #while loop has finished. 
        new_paths = []
    
        #Takes care of on level at at a time. psth_list is emptied
        #and new_paths is filled up
        while len(path_list) > 0:
            #('S')
            #('S','A')
            path = path_list[0]
            #[('S',)]
            #[('S','B')]
            path_list.remove(path)
            #What is connected to 'S'? 'A' and 'B'
            #What is connected to 'A'? n1 and n2
            node = path[-1]
        
            connected_nodes = graph.get_connected_nodes(node) 
        
            #First time the length of the path is 1 and there is only one node on the path.
            if len(path) > 1:
                connected_nodes = [cnode for cnode in connected_nodes if cnode not in path]
            
            if goal in connected_nodes:
                isgoal = path + (goal,)
                return list(isgoal)
                
            new_paths += [path + (node,) for node in connected_nodes]
    
        path_list.extend(new_paths)
    
#print bfs(GRAPH1,'Stairs','Dungeon 5')

"""

#MY OWN VERSION AND IT WORKS    

def bfs(graph,start,goal):
    
    path_list = [(start,)]
    
    while len(path_list) > 0:
        
        path = path_list[0]
        path_list.remove(path)
        node = path[-1]
        
        connected_nodes = graph.get_connected_nodes(node) 
        if len(path) > 1:
            connected_nodes = [cnode for cnode in connected_nodes if cnode not in path]
        
        if goal in connected_nodes:
            return list(path + (goal,))
        
        path_list += [path + (node,) for node in connected_nodes]
"""
print "bfs: "
start = timeit.timeit()
print bfs(GRAPH1,'Dungeon 5','Common Area')
end = timeit.timeit()
print end - start
"""        
        
####

def dfs(graph,start,goal):
    
    path_list = [(start,)]
        
    while len(path_list) > 0:
            
        path = path_list[0]
        path_list.remove(path)
        node = path[-1]
            
        connected_nodes = graph.get_connected_nodes(node) 
        if len(path) > 1:
            connected_nodes = [cnode for cnode in connected_nodes if cnode not in path]
            
        if goal in connected_nodes:
            return list(path + (goal,))
            
        path_list = [path + (node,) for node in connected_nodes] + path_list
"""
print "dfs: "        
start = timeit.timeit()
print dfs(GRAPH1,'Dungeon 5','Common Area')
end = timeit.timeit()
print end - start 
""" 
 
def sort_paths(graph,path_list,goal):
    
    path_heuristic = []
    
    for path in path_list:
        node = path[-1]
        path_heuristic += [(path,graph.get_heuristic(node,goal))]
    
    path_heuristic = sorted(path_heuristic, key=lambda heu: heu[1]) 
    
    path_list_sorted = [path_heuristic[i][0] for i in range(len(path_heuristic))]
    
    return path_list_sorted

#like bfs
def hill_climbing(graph, start, goal):
    
    path_list = [(start,)]
        
    while len(path_list) > 0:
            
        path = path_list[0]
        path_list.remove(path)
        node = path[-1]
            
        connected_nodes = graph.get_connected_nodes(node) 
        if len(path) > 1:
            connected_nodes = [cnode for cnode in connected_nodes if cnode not in path]
            #heuristic = [graph.get_heuristic(node,goal) for node in connected_nodes]   
     
              
        if goal in connected_nodes:
            return list(path + (goal,))
        
        path_list = [path + (node,) for node in connected_nodes] + path_list
        
        #SORT NEW PATHS AND OLD PATHS ARE SORTED. AFTER ADDING CHILDREN TO AT PARENT THE SORTING IS PERFOMRED.
        path_list = sort_paths(graph,path_list,goal)
"""
print "hill climbing: "
start = timeit.timeit()
print hill_climbing(GRAPH1,'Dungeon 5','Common Area')
end = timeit.timeit()
print end - start
"""


#print hill_climbing(GRAPH1,'Hospital','Common Area')



#like bfs
def beam_search(graph, start, goal, beam_width):
        path_list = [(start,)]
        index = beam_width
        
        while len(path_list) > 0:
            path_list[:beam_width]
            new_paths = []
            
            while len(path_list) > 0:
                
                path = path_list[0]
                path_list.remove(path)
                node = path[-1]
        
                connected_nodes = graph.get_connected_nodes(node) 
                if len(path) > 1:
                    connected_nodes = [cnode for cnode in connected_nodes if cnode not in path]
    
                if goal in connected_nodes:
                    return list(path + (goal,))
                                
                new_paths += [path + (node,) for node in connected_nodes]
            
            path_list = new_paths    
            path_list = sort_paths(graph,path_list,goal)
 
"""            
print "beam_search: "                   
start = timeit.timeit()
print beam_search(GRAPH1,'Dungeon 5','Common Area',2)
end = timeit.timeit()
print end - start
"""

def path_length(graph,path):
    if len(path) == 1:
         return 0
    path_length = 0
    for i in range(len(path)-1):
         path_length += graph.get_edge(path[i],path[i+1]).length
    return path_length

def branch_and_bound(graph, start, goal):
    path_list = [((start,),0)]
    
    while len(path_list) > 0:
                
        path = path_list[0][0]
        node = path[-1]
        
        connected_nodes = graph.get_connected_nodes(node) 
        
        if len(path) > 1:
            connected_nodes = [cnode for cnode in connected_nodes if cnode not in path]
    
        if goal in connected_nodes:
            return list(path + (goal,))
                
        path_list = [( path+(node,), path_length(graph, path+(node,)) ) for node in connected_nodes] + path_list
        
        min_path = min(path_list, key = lambda t: t[1])
        
        for i in range(len(path_list)):
            
        
        path_list.remove()
        
        path_list
        
print branch_and_bound(GRAPH1,'Dungeon 5','Common Area')

###Solution for StackOverflow
def depth(l):
    depths = [depth(item) for item in l if isinstance(item, tuple)]

    if len(depths) > 0:
        return 1 + max(depths)

    return 1

ls0 = ('x')
ls1 = ()
ls2 = ('expt', 'x', 2)
ls3 = ('+', ('expt', 'x', 2), ('expt', 'y', 2))
ls4 = ('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))

tuples = [ls0, ls1, ls2, ls3, ls4]
#for tup in tuples:
    #print(depth(tup))
    
    

from search import Graph
from graphs import *

def bfs(graph, start, goal):
    #[('S',)]
    #[('S','A'),('S','B')]
    path_list = [(start,)]
    
    #We have to add and remove paths to the path_list. Everything is done at the front.
    while(len(path_list) > 0):
        new_paths = []
    
        while(len(path_list) > 0):
            #('S')
            #('S','A')
            path = path_list[0]
            #[('S',)]
            #[('S','B')]
            path_list.remove(path_list[0])
            #What is connected to 'S'? 'A' and 'B'
            #What is connected to 'A'? n1 and n2
            node = path[-1]
        
            connected_nodes = graph.get_connected_nodes(node) 
        
            #First time the length of the path is 1 and there is only one node on the path.
            if len(path) > 1:
                connected_nodes = [cnode for cnode in connected_nodes if not node in path]
        
            if goal in connected_nodes:
                isgoal = path + (goal,)
                return list(isgoal)
                
            new_paths += [path + (node,) for node in connected_nodes]
    
        path_list.extend(new_paths)
    
print bfs(GRAPH1,'Forbidden Area','Dungeon 5')
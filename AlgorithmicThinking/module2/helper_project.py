"""
Project part of Algorithmic Thinking 1 module 2
"""

from collections import deque

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order   



def fast_targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree, fast implementation
    
    Returns:
    A list of nodes
    """
    new_graph = copy_graph(ugraph)
    n = len(new_graph)
    
    DegreeSets = []
    for k in range(n):
        DegreeSets.append(set())
    
    L = []
    for i in new_graph.keys():
        d = len(new_graph[i])
        DegreeSets[d].add(i)
        #L.append(set())
    
    #i = 0
    
    for k in range(n-1, -1, -1):
                
        while len(DegreeSets[k]) > 0:
            node = DegreeSets[k].pop()
                       
            for neighbor in new_graph[node]:
                d = len(new_graph[neighbor])
                DegreeSets[d].remove(neighbor)
                DegreeSets[d-1].add(neighbor)
            
            #L[i].add(node)
            #i += 1
            L.append(node)           
            delete_node(new_graph, node)
            
    return L  



def bfs_visited(ugraph, start_node):
    """
    BREADTH-FIRST-SEARCH
    """
    visited = set()
    queue = deque()
    
    visited.add(start_node)    
    queue.append(start_node)
    
    while queue:
        node_j = queue.pop()
        
        for node in ugraph:
            if node_j in ugraph[node]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
    
    return visited 
	
	
	
def cc_visited(ugraph):
    """
    input: undirected graph
    return: set of connected components
    """
    
    remaining_nodes = set(ugraph.keys())
    connected = list()
    
    while len(remaining_nodes) > 0:
        start_node = remaining_nodes.pop()
        visited = bfs_visited(ugraph, start_node)
        connected.append(visited)
        remaining_nodes -= visited
      
    return connected   	
	
	
def largest_cc_size(ugraph):
    """
    returns largest cc size
    """
    
    components = cc_visited(ugraph)
    
    largest = 0
    for component in components:
        if len(component) > largest:
            largest = len(component)
    return largest



def compute_resilience(ugraph, attack_order):
    """
    resilience
    """
    resilience = [largest_cc_size(ugraph)]
    for removed_node in attack_order:
        ugraph.pop(removed_node) 
        ### Remove node from its neighbours here
        for neighbor in ugraph.keys():
            if removed_node in ugraph[neighbor]:
                ugraph[neighbor].remove(removed_node)
                
        resilience.append(largest_cc_size(ugraph))
    return resilience 	
	
	
### From here additional functions
def random_order(ugraph):
    nodes = ugraph.keys()
    random.shuffle(nodes)
    return nodes



def compute_num_of_edges(ugraph):
    nodes = ugraph.keys()
    count_dict = dict(zip(nodes, [0]*len(nodes)))
    
    for node in nodes:
        for edge in ugraph[node]:
            count_dict[edge] += 1
    
    return sum(count_dict.values())/2 



def make_complete_graph(num_nodes):
    """
    makes complete digraph
    """
    empty_dict = dict()
    if num_nodes <= 0:
        return empty_dict
    
    for node in range(num_nodes):
        empty_dict[node] = []
        for edge in range(num_nodes):
            if edge != node:
                empty_dict[node].append(edge)
        empty_dict[node] = set(empty_dict[node])    
    return empty_dict 
	
	

def ER_ugraph(n, p):
    """
    returns undirected ER graph
    """
    graph = dict()
    if n <= 0:
        return graph
               
    for i in range(n):
        try:
            graph[i]
        except:
            graph[i] = set()
                
        for j in range(n):
            try:
                graph[j]
            except:
                graph[j] = set()
            
            if j != i:
                a = random.random() 
                if a < p:
                    graph[i].add(j)
                    graph[j].add(i)
            
    return graph




"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

	def __str__(self):
	    return "num_nodes: " + str(self._num_nodes) + " node_numbers: " + str(self._node_numbers)
		

    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors	
		
		
		
def make_UPA(n,m):
    trials = n-m 
    UPA_graph = make_complete_graph(m) 
        
    experiment = UPATrial(m)
    for trial in range(trials):
        add_node = m + trial
        new_edges = experiment.run_trial(m)
        
        UPA_graph[add_node] = new_edges
        
        for edge in new_edges:
            UPA_graph[edge].add(add_node) 
        
    return UPA_graph		
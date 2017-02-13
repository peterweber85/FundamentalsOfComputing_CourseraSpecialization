"""
Stupid convention

"""

EX_GRAPH0 = {0: set([1, 2]), 1:set([]), 2:set([])}

EX_GRAPH1 = {0: set([1, 4, 5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}

EX_GRAPH2 = {0: set([1, 4, 5]), 1:set([2, 6]), 2:set([3, 7]), 3:set([7]),\
             4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1, 2]), 9:set([0, 3, 4, 5, 6, 7])}

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
	
	
	
	
	
def compute_in_degrees(digraph):
    """
    returns dict with keys = nodes, values = no. of in_degrees
    """
    nodes = digraph.keys()
    count_dict = dict(zip(nodes, [0]*len(nodes)))
    
    for node in nodes:
        for edge in digraph[node]:
            #print "pass"
            count_dict[edge] += 1
    return count_dict
    
	

	
	
def in_degree_distribution(digraph):
    """
    returns
    """
    nodes = digraph.keys()
    count_dict = dict(zip(nodes, [0]*len(nodes)))
    
    for node in nodes:
        for edge in digraph[node]:
            #print "pass"
            count_dict[edge] += 1
    
    dist_nodes = count_dict.values()
    dist_nodes_set = set(count_dict.values())
    dist_count_dict = dict(zip(dist_nodes, [0]*len(dist_nodes)))
        
    for node_set in dist_nodes_set:
        for count in dist_nodes:
            if count == node_set:
                dist_count_dict[node_set] += 1
        
    return dist_count_dict 
	
	
	
	
   

import urllib2
import matplotlib.pyplot as plt
import numpy as np
import random

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph
	
	
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
            count_dict[edge] += 1
    return count_dict	
	
	
def in_degree_distribution(digraph):
    """
    returns a dictionary with the distribution of in-degrees for digraph
    """
    nodes = digraph.keys()
    count_dict = dict(zip(nodes, [0]*len(nodes)))
    
    for node in nodes:
        for edge in digraph[node]:
            count_dict[edge] += 1
    
    dist_nodes = count_dict.values()
    dist_nodes_set = set(count_dict.values())
    dist_count_dict = dict(zip(dist_nodes, [0]*len(dist_nodes)))
        
    for node_set in dist_nodes_set:
        for count in dist_nodes:
            if count == node_set:
                dist_count_dict[node_set] += 1
        
    return dist_count_dict   



def make_ER_graph(n, p):
    """
    makes complete digraph
    """
    empty_dict = dict()
    if n <= 0:
        return empty_dict
    
    #V = range(n)
    #E = list()
        
    for i in range(n):
        empty_dict[i] = []
        for j in range(n):
            if j != i:
                a = random.random() 
                if a < p:
                    empty_dict[i].append(j)
        empty_dict[i] = set(empty_dict[i])    
    return empty_dict
	
	
	
	
class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]
    
    def __str__(self):
        return "num_nodes: " + str(self._num_nodes) + " node_numbers: " + str(self._node_numbers)
        #\n, "node_numbers: ", self._node_numbers

    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    
    

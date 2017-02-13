"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """ 
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)
    
    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def enqueue(self, item):
        """
        Add item to the queue.
        """        
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []


class Apocalypse(poc_grid.Grid):

    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            self._obstacle_list = obstacle_list
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie
            

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = [[EMPTY for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        distance_field = [[self._grid_width*self._grid_height for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        
        boundary = Queue()
        
        if entity_type == HUMAN:
            for item in self._human_list:
                boundary.enqueue(item)
            entity_list = self._human_list
                
        elif entity_type == ZOMBIE:
            for item in self._zombie_list:
                boundary.enqueue(item)
            entity_list = self._zombie_list
        
        # Use here lists directly
        current_cell = []
        for idx in range(len(entity_list)):
            current_cell = entity_list[idx]
            visited[current_cell[0]][current_cell[1]] = FULL
            distance_field[current_cell[0]][current_cell[1]] = 0
        
        current_cell = []
        while boundary.__len__() != 0:
            current_cell = boundary.dequeue()    
            for neighbor_cell in self.four_neighbors(current_cell[0],current_cell[1]):
                if visited[neighbor_cell[0]][neighbor_cell[1]] == EMPTY and (neighbor_cell[0],neighbor_cell[1]) not in self._obstacle_list:
                    visited[neighbor_cell[0]][neighbor_cell[1]] = FULL
                    boundary.enqueue(neighbor_cell)
                    distance_field[neighbor_cell[0]][neighbor_cell[1]] = distance_field[current_cell[0]][current_cell[1]] + 1

        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        temp_coord_list = []
        temp_dist_field = []
        updated_human_list = []
                
        for human in self._human_list:
            temp_coord_list = [human]
            temp_dist_field = [zombie_distance_field[human[0]][human[1]]]
            for neighbor_cell in self.eight_neighbors(human[0], human[1]):
                if neighbor_cell not in self._obstacle_list:
                    temp_coord_list.append(neighbor_cell)
                    temp_dist_field.append(zombie_distance_field[neighbor_cell[0]][neighbor_cell[1]])		       
            index = temp_dist_field.index(max(temp_dist_field))		
            updated_human_list.append(temp_coord_list[index])        
        
        self._human_list = updated_human_list       
            
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        temp_coord_list = []
        temp_dist_field = []
        updated_zombie_list = []
                
        for zombie in self._zombie_list:
            temp_coord_list = [zombie]
            temp_dist_field = [human_distance_field[zombie[0]][zombie[1]]]
            for neighbor_cell in self.four_neighbors(zombie[0], zombie[1]):
                if neighbor_cell not in self._obstacle_list:
                    temp_coord_list.append(neighbor_cell)
                    temp_dist_field.append(human_distance_field[neighbor_cell[0]][neighbor_cell[1]])		       
            index = temp_dist_field.index(min(temp_dist_field))		
            updated_zombie_list.append(temp_coord_list[index])        
        
        self._zombie_list = updated_zombie_list
        
# poc_zombie_gui.run_gui(Apocalypse(30, 40))

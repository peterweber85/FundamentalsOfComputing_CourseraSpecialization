"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # Define values and lists
    non_zero_elements = 0
    move_values = list()
    add_values = list()
    
    # Move elements in list to the left
    for dummy_i, value in enumerate(line):
        if value != 0:
            move_values.append(value)
            non_zero_elements += 1
    
    # Fill up list move_values with zeros
    for dummy_i in range(len(line)-non_zero_elements+1):
        move_values.append(0) 
    
    # Add up equal elements in list add_value
    dummy_i = 1
    while dummy_i < len(move_values):
        if move_values[dummy_i-1] == move_values[dummy_i] and move_values[dummy_i-1] != 0:
            add_values.append(2*move_values[dummy_i-1])
            non_zero_elements -= 1
            dummy_i = dummy_i + 2
            
        else:
            if move_values[dummy_i-1] == 0:
                dummy_i = dummy_i + 1
            else:
                add_values.append(move_values[dummy_i-1])
                dummy_i = dummy_i + 1
    
    # Fill list add_values with zeros
    for dummy_i in range(len(line)-non_zero_elements):
        add_values.append(0)  
        
    return add_values

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self._init_tile_indices = {UP: [(0, col_index) for col_index in range(grid_width)],
                                  DOWN: [(grid_height-1, col_index) for col_index in range(grid_width)],
                                  LEFT: [(row_index, 0) for row_index in range(grid_height)],
                                  RIGHT: [(row_index, grid_width-1) for row_index in range(grid_height)]}
        
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        TwentyFortyEight.new_tile(self)
        TwentyFortyEight.new_tile(self)
                
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        #return str(self._grid)
        return str(self._grid)
            
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self,direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # Define direction
        self._direction = direction
        init_tile_indices = self._init_tile_indices[direction]
                        
        for i_to_c in range(len(init_tile_indices)):
            dummy_x = init_tile_indices[i_to_c][0]
            dummy_y = init_tile_indices[i_to_c][1]
            
            temp_list = list() 
            temp_list.append((dummy_x, dummy_y))
            line = list()
            
            while 0 <= dummy_x and dummy_x <self._grid_height and 0 <= dummy_y and dummy_y < self._grid_width:
                dummy_x += OFFSETS[direction][0]
                dummy_y += OFFSETS[direction][1]
                temp_list.append((dummy_x, dummy_y))
                
                if dummy_x < 0 or dummy_x == self._grid_height or dummy_y < 0 or dummy_y == self._grid_width:
                    temp_list.pop()
            
            for dummy_i in range(len(temp_list)):
                line.append(self._grid[temp_list[dummy_i][0]][temp_list[dummy_i][1]])
            
            line = merge(line)
            
            for dummy_i in range(len(temp_list)):
                self._grid[temp_list[dummy_i][0]][temp_list[dummy_i][1]] = line[dummy_i]
            
        TwentyFortyEight.new_tile(self)
        #TwentyFortyEight.new_tile(self)
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        rand = random.randrange(0,10)
        if rand == 0:
            tile = 4
        else:
            tile = 2
        
        rows = range(self._grid_height)
        columns = range(self._grid_width)
        random.shuffle(rows)
        random.shuffle(columns)
        
        row_loop_must_break = False
        for dummy_row in rows:
            for dummy_col in columns:
                if self._grid[dummy_row][dummy_col] == 0:
                    self._grid[dummy_row][dummy_col] = tile
                    row_loop_must_break = True
                    break
            if row_loop_must_break:
                break
        return self._grid
                
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]

#obj = TwentyFortyEight(7, 4)

#poc_2048_gui.run_gui(obj)

#obj.set_tile(0, 0, 2)
#obj.set_tile(0, 1, 0)
#obj.set_tile(0, 2, 0)
#obj.set_tile(0, 3, 0)
#obj.set_tile(1, 0, 0)
#obj.set_tile(1, 1, 2)
#obj.set_tile(1, 2, 0)
#obj.set_tile(1, 3, 0)
#obj.set_tile(2, 0, 0)
#obj.set_tile(2, 1, 0)
#obj.set_tile(2, 2, 2)
#obj.set_tile(2, 3, 0)
#obj.set_tile(3, 0, 0)
#obj.set_tile(3, 1, 0)
#obj.set_tile(3, 2, 0)
#obj.set_tile(3, 3, 2)
#obj.move(UP) 



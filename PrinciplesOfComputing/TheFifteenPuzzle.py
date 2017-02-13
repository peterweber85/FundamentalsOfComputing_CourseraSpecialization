
"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui
import math

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # replace with your code
        if self._grid[target_row][target_col] != 0:
            return False
        elif target_row + 1 < self._height and target_col + 1 < self._height:
            for col in range(target_col + 1, self._width):
                if self._grid[target_row][col] != col + self._width *target_row:
                    return False
            
            for row in range(target_row + 1, self._height):
                for col in range(self._width):
                    if self._grid[row][col] != col + self._width * row:
                        return False
                
        return True
    
        
    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        circle_up_right = "urrdl"
        circle_left_down = "lddru"
        circle_down_right = "drrul"
        circle_up_left = "ulldr"
        
        move_str =""
        
        assert self.lower_row_invariant(target_row, target_col)
        delta = (self.current_position(target_row, target_col)[0] - target_row, self.current_position(target_row, target_col)[1] - target_col)
                
        if delta[0] == 0:
            for _ in range(int(math.fabs(delta[1]))):      
                move_str += "l" 
            for _ in range(int(math.fabs(delta[1]))-1):
                move_str += circle_up_right
                
        elif delta[1] == 0:								
            move_str += "u" * (int(math.fabs(delta[0])))
            move_str += circle_left_down *(int(math.fabs(delta[0]))-1)
            move_str += "ld"
        else:
            
            for _ in range(int(math.fabs(delta[0]))):
                move_str += "u"
            if delta[1] > 0:
                for _ in range(int(math.fabs(delta[1]))):
                    move_str += "r"								
                for _ in range(int(math.fabs(delta[1]))-1):
                    move_str += circle_up_left
                move_str += "ld"
                       
            elif delta[1] < 0:
                for _ in range(int(math.fabs(delta[1]))):
                    move_str += "l"																	
                for _ in range(int(math.fabs(delta[1]))-1):
                    move_str += circle_down_right
                   
                    move_str += "dru"
                    for _ in range(int(math.fabs(delta[0]))-1):
                        move_str += circle_left_down
                    move_str += "ld"
    
        self.update_puzzle(move_str)																	
        return move_str
                                    
    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0)
        
        circle_up_left = "ulldr"
                
        move_first_str ="ur"
        self.update_puzzle(move_first_str)
        curr_pos = self.current_position(target_row, 0)
        
        if curr_pos == (target_row, 0):
            move_str = "r" * (self._width - 2)
            self.update_puzzle(move_str)
                        
        elif curr_pos[0] == target_row-1:
            move_horizontal = 1 - curr_pos[1]
            if move_horizontal > 0:
                move_str = "l"
            elif move_horizontal < 0:
                move_str = "r" *(- move_horizontal)
                move_str += circle_up_left * (- move_horizontal)
                move_str += "l"
            move_str += "ruldrdlurdluurddlur"
            move_str += "r" * (self._width - 2)
            self.update_puzzle(move_str)
        elif curr_pos[0] < target_row - 1:
            delta =  (target_row - 1 - self.current_position(target_row, 0)[0], self.current_position(target_row, 0)[1] - 1)        
            if curr_pos[1] > 1:
                move_str = "u" * delta[0]
                move_str += "r" * delta[1]
                move_str += "dllur" * (delta[1] - 1)
                move_str += "dlurd" * (delta[0] - 1)
                move_str += "dluld"
            elif curr_pos[1] == 0:
                move_str = "u" * delta[0]
                move_str += "l"
                move_str += "druld" * delta[0]
            elif curr_pos[1] == 1:
                move_str = "l"
                move_str += "u" * delta[0]
                move_str += "druld" * delta[0]
            move_str += "ruldrdlurdluurddlur"
            move_str += "r" * (self._width - 2)
            self.update_puzzle(move_str)
        return move_first_str + move_str

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[0][target_col] != 0:
            return False
        elif 1 + 1 < self._height and target_col < self._height:
            for col in range(target_col, self._width):
                if self._grid[1][col] != col + self._width *1:
                    return False
            for row in range(1 + 1, self._height):
                for col in range(self._width):
                    if self._grid[row][col] != col + self._width * row:
                        return False
        return True
        
    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self.lower_row_invariant(1,target_col) == False:
            return False
        for col in range(target_col + 1, self._width):
            if self._grid[0][col] != col:
                return False
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col)
        move_first_str = "ld"
        self.update_puzzle(move_first_str)
        
        curr_pos = self.current_position(0, target_col)
        delta = target_col - 1 - curr_pos[1]
               
        if curr_pos == (0, target_col):
            return move_first_str
        
        elif curr_pos[0] == 0:
            move_str = "l" * delta
            move_str += "ruldr" * delta
            move_str += "ulr"
            move_str += "ld"
            
        elif curr_pos[0] == 1:
            move_str = "l" * delta
            move_str += "urrdl" * (delta - 1)
        
        move_str += "urdlurrdluldrruld"
        
        self.update_puzzle(move_str)
        return move_first_str + move_str

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row1_invariant(target_col)
        curr_pos = self.current_position(1, target_col)
        delta = target_col - curr_pos[1]
        move_str = ""
        
        if curr_pos[0] == 0:
            move_str += "l" * delta
            move_str += "ruldr" * delta
            move_str += "u"
                   
        elif curr_pos[0] == 1:
            move_str += "l" * delta
            move_str += "urrdl" * (delta - 1)
            move_str += "ur"
                           
        self.update_puzzle(move_str)
        return move_str

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        move_str = ""
        if self.get_number(1,1) == 0:
            move_str += "ul"
        if self.get_number(0,1) == 0:
            move_str += "l"
        if self.get_number(1,0) == 0:
            move_str += "u"
        
        move_while_str = "drul"
        self.update_puzzle(move_str)
        while self.lower_row_invariant(0,0) == False:
            move_str += move_while_str
            self.update_puzzle(move_while_str)
                        
        return move_str

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        move_str = ""
        row = self._height - 1
        col = self._width - 1        
        
        curr_pos_zero = self.current_position(0, 0)
        delta_0 = row - curr_pos_zero[0]
        delta_1 = col - curr_pos_zero[1]
        
        move_zero = "r" * delta_1 + "d" * delta_0
        self.update_puzzle(move_zero)
        
        for row in range(self._height - 1,1,-1):
            for col in range(self._width - 1,-1,-1):
                if col > 0 and row > 1:
                    move_str += self.solve_interior_tile(row,col)
                elif col == 0 and row > 1:
                    move_str += self.solve_col0_tile(row)
        
        for col in range(self._width - 1,1,-1):
            for row in range(1,-1,-1):
                if col > 1 and row == 1:
                    move_str += self.solve_row1_tile(col)
                elif col > 1 and row == 0:
                    move_str += self.solve_row0_tile(col)
        
        move_str += self.solve_2x2()
                
        return move_zero + move_str

# Start interactive simulation
# poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
#mypuzzle = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
#print mypuzzle
#mypuzzle.solve_2x2()
#mypuzzle.update_puzzle("ldl")
#mypuzzle.solve_puzzle()

#print mypuzzle
#mypuzzle.solve_interior_tile(2,1)

#print mypuzzle 

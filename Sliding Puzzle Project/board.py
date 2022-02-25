#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Karla Vazquez
# email: kkarlav@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
        
        # Put your code for the rest of __init__ below.
        num = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[num]
                if digitstr[num] == '0':
                    self.blank_r = r
                    self.blank_c = c
                num += 1
        # Do *NOT* remove our code above.


    ### Add your other method definitions below. ###
    def __repr__(self):
        """ Returns a string that represents the board
        object """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != '0':
                    s += self.tiles[r][c] + ' '
                else:
                    s += '_' + ' '
            s += '\n'
        return s      
    def move_blank(self, direction):
        """ Alters the 2-D list's internals to move the blank
        tile while also determining if the desired direction is possible, 
        and returning True or False depending on the move's possibility"""
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    if direction == 'up':
                        if r == 0:
                            return False
                        else:
                            self.tiles[r][c] = self.tiles[r-1][c]
                            self.tiles[r-1][c] = '0'
                            self.blank_r = r-1
                            self.blank_c = c
                            return True
                    if direction == 'down':
                        if r == 2:
                            return False
                        else:
                            self.tiles[r][c] = self.tiles[r+1][c]
                            self.tiles[r+1][c] = '0'
                            self.blank_r = r+1
                            self.blank_c = c
                            return True
                    if direction == 'right':
                        if c == 2:
                            return False
                        else:
                            self.tiles[r][c] = self.tiles[r][c+1]
                            self.tiles[r][c+1] = '0'
                            self.blank_r = r
                            self.blank_c = c+1
                            return True
                    if direction == 'left':
                        if c == 0:
                            return False
                        else:
                            self.tiles[r][c] = self.tiles[r][c-1]
                            self.tiles[r][c-1] = '0'
                            self.blank_r = r
                            self.blank_c = c-1
                            return True 
                    else:
                        return False 
    
    def digit_string(self):
        """ Returns a string of all the digits in the 3x3 square"""
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += self.tiles[r][c]
        return s
            
    def copy(self):
        """ Creates a deep copy of a called board"""
        copied_board = Board(self.digit_string())
        return copied_board  
    
    def num_misplaced(self):  
        """ Counts how many tiles are out of place relative to the goal state"""
        count = 0  
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != '0':
                    if GOAL_TILES[r][c] != self.tiles[r][c]:
                        count += 1
        return count
    
    def __eq__(self, other):
        """ Computes whether two called objects are equal to each other"""
        if self.digit_string() == other.digit_string():
            return True
        else:
            return False
    
    def row_away(self):
        """ Computes how many rows away a tile is from its solution"""
        total_rows = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != '0' and r != int(self.tiles[r][c]) // 3:
                    total_rows += 1
        return total_rows
              
    def col_away(self):
        """ Computes how many columns away a tile is from its solution"""
        total_cols = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != '0' and c != int(self.tiles[r][c]) % 3:
                    total_cols += 1
        return total_cols
        
                    
                    
                
            

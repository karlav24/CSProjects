#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """
        A constructor that initializes all the 
        attributes in the Searcher class
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
    
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self, new_state):
        """ adds a list containing the given state
        to the attribute self.states
        """
        self.states += [new_state]
    
    def should_add(self, state):
        """ Decides whether a given state
        should or should not be added to self.states"""
        if self.depth_limit != -1: 
            if self.depth_limit >= state.num_moves:
                if state.creates_cycle() == True:
                    return False
                else:
                    return True
            if state.num_moves > self.depth_limit:
                return False
        if self.depth_limit == -1:
            if state.creates_cycle() == True:
                return False
            else:
                return True
    def add_states(self, new_states):
        """ Adds multiple states at once by calling add_state"""
        for i in new_states:
            if self.should_add(i) == True:
                self.add_state(i)

    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """ Finds the solution for the 8 puzzle """            
        self.add_state(init_state)
        while self.states != []:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal() == True:
                return s
            else:
                s_succ = s.generate_successors()
                self.add_states(s_succ)
        return None 
### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    def next_state(self):
        """ Determines the next state to be tested"""
        s = self.states[0]
        self.states.remove(s)
        return s
class DFSearcher(Searcher):
    def next_state(self):
        """ Determines the next state to be tested """
        s = self.states[-1]
        self.states.remove(s)
        return s
def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ uses a board method to determine the 
    estimated moves needed to solve the 8 puzzle"""
    estimated_moves = state.board.num_misplaced()
    return estimated_moves

def h2(state):
    """ uses two board methods to estimate how many
    rows and columns a given tile is out of place from its solution"""
    out_of_place = state.board.row_away() + state.board.col_away()
    return out_of_place
    
class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """ a constructor that inherits from Searcher
        yet initializes the depth limit to be none and 
        initializes a heuristic attribute"""
        super().__init__(self)
        self.depth_limit = -1
        self.heuristic = heuristic
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """ Adds a sublist containing the priority value and
        the corresponding state to the attribute self.states"""
        self.states += [[self.priority(state), state]]
    
    def next_state(self):
        """ Chooses a state with the highest priority"""
        s = max(self.states)
        self.states.remove(s)
        return s[1]
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    def priority(self, state):
        """ computes and returns the priority by determining 
        the most optimal move while taking into account 
        the cost of that move """
        return -1 * (self.heuristic(state) + state.num_moves)

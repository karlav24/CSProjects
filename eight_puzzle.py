#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Karla Vazquez
# email: kkarlav@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def process_file(filename, algorithm, param):
    """ Processes an inputted file and calls find solution to 
    get the solution to a puzzle, counting the average states and
    moves it took to get to this point, as well as the total number of puzzles solved"""
    file = open(filename, 'r')
    tested = 0
    num_moves = 0
    puzzles = 0
    for line in file:
        line = line[:-1]
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        algorithm = str(algorithm)
        searcher = create_searcher(algorithm, param)
        soln = None
        try:
            soln = searcher.find_solution(init_state)
            if soln == None:
                print(line + ': no solution')
            else:
                print(line + ':', soln.num_moves, 'moves', searcher.num_tested, 'states tested')
                puzzles += 1
                num_moves += soln.num_moves
                tested += searcher.num_tested
        except KeyboardInterrupt:
            print(line + ': search terminated, no solution')
    if puzzles != 0:
        average_moves = num_moves / puzzles
        average_states = tested / puzzles
        print()
        print('solved', puzzles, 'puzzles')
        print('averages:', average_moves, 'moves,', average_states, 'states tested')
    
    else:
        print()
        print('solved 0 puzzles')    
     
def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return
    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

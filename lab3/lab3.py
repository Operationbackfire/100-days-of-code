# 6.034 Fall 2010 Lab 3: Games
# Name: <Your Name>
# Email: <Your Email>

from util import INFINITY

### 1. Multiple choice

# 1.1. Two computerized players are playing a game. Player MM does minimax
#      search to depth 6 to decide on a move. Player AB does alpha-beta
#      search to depth 6.
#      The game is played without a time limit. Which player will play better?
#
#      1. MM will play better than AB.
#      2. AB will play better than MM.
#      3. They will play with the same level of skill.
ANSWER1 = 0

# 1.2. Two computerized players are playing a game with a time limit. Player MM
# does minimax search with iterative deepening, and player AB does alpha-beta
# search with iterative deepening. Each one returns a result after it has used
# 1/3 of its remaining time. Which player will play better?
#
#   1. MM will play better than AB.
#   2. AB will play better than MM.
#   3. They will play with the same level of skill.
ANSWER2 = 0

### 2. Connect Four
from connectfour import *
from basicplayer import *
from util import *
#import tree_searcher

## This section will contain occasional lines that you can uncomment to play
## the game interactively. Be sure to re-comment them when you're done with
## them.  Please don't turn in a problem set that sits there asking the
## grader-bot to play a game!
## 
## Uncomment this line to play a game as white:
#run_game(human_player, basic_player)

## Uncomment this line to play a game as black:
#run_game(basic_player, human_player)

## Or watch the computer play against itself:
#run_game(basic_player, basic_player)

## Change this evaluation function so that it tries to win as soon as possible,
## or lose as late as possible, when it decides that one side is certain to win.
## You don't have to change how it evaluates non-winning positions.

testboard = ConnectFourBoard()
#print testboard
#Does not work by itself
#1
#print testboard.get_current_player_id()
#2
#print testboard.get_other_player_id()
#print testboard.get_board_array()
#print testboard.do_move(3)
#print testboard.do_move(3).get_cell(5,3)
#print testboard.do_move(3).get_board_array()
#print testboard.do_move(3).longest_chain(1)

#print testboard.do_move(3).do_move(3)
#print testboard.do_move(3).do_move(3).do_move(4)
#print testboard.do_move(3).do_move(3).do_move(4).longest_chain(2)

#print testboard.do_move(3).do_move(3).do_move(4).get_board_array()
#print testboard.do_move(3).do_move(3).do_move(4).longest_chain(1)
#test1board2m = testboard.do_move(3).do_move(3)
#test1board3m = testboard.do_move(3).do_move(3).do_move(4)
testboard = testboard.do_move(0).do_move(3).do_move(6).do_move(4).do_move(3)
#print testboard
#print basic_evaluate(test1board2m)

"""
print "Current player:",testboard.get_current_player_id()
score = basic_evaluate(testboard)
print "Score(basic):", score
basicscore = testboard.longest_chain(testboard.get_current_player_id())*10
"""

"""
print "Basicscore:", basicscore
print testboard.get_cell(5,3) == testboard.get_current_player_id()
print testboard.get_cell(5,4) == testboard.get_current_player_id()
minus = - abs(3-3) - abs(3-4)
print "Minus part:", minus
print testboard.get_cell(4,3) == testboard.get_other_player_id()
print testboard.get_cell(5,6) == testboard.get_other_player_id()
print testboard.get_cell(5,0) == testboard.get_other_player_id()
plus = +abs(3-3)+abs(3-6)+abs(3-0)
print "Plus part:", plus
print "Total score:", basicscore + minus + plus
"""

#nextmoves = get_all_next_moves(testboard)
#for i in nextmoves:
#    print(i)

#test1board2m = testboard.do_move(3).do_move(6)

#print basic_evaluate(test1board2m)

def focused_evaluate(board):
    """
    Given a board, return a numeric rating of how good
    that board is for the current player.
    A return value >= 1000 means that the current player has won;
    a return value <= -1000 means that the current player has lost
    """
    if board.is_game_over():
        score = -1000
    else:
        score = board.longest_chain(board.get_current_player_id()) * 10    
        """
        for row in range(6):
            for col in range(7):
                if board.get_cell(row, col) == board.get_current_player_id():
                    score -= 1
                elif board.get_cell(row, col) == board.get_other_player_id():
                    score += 1  
        """
           
    return score
"""    
score = focused_evaluate(testboard)
print "Score(focused):", score

t = range(4+1)
t[1] = testboard.do_move(0)
t[2] = testboard.do_move(0).do_move(3)
t[3] = testboard.do_move(0).do_move(3).do_move(6)
t[4] = testboard.do_move(0).do_move(3).do_move(6).do_move(4)
print minimax_find_board_value(testboard,depth=1,eval_fn=focused_evaluate)
print minimax_find_board_value(testboard,depth=2,eval_fn=focused_evaluate)
print minimax_find_board_value(testboard,depth=3,eval_fn=focused_evaluate)
"""

"""
for i in range(1,3+1):
    for j in range(1,4+1):
        print "Moves:",j,"Depth:",i,"Minimax:",minimax_find_board_value(t[j],depth=i,eval_fn=basic_evaluate)
"""


#nextboards = get_all_next_moves(testboard)
#print nextboards
#for nextboard in nextboards:
#    print minimax(nextboard,depth=1)

"""
#### This is an example of how the minimax is working.
minimax(testboard, depth = 3)
for move, new_board in get_all_next_moves(testboard):
    print new_board
    print "Move#:",move+1
    print "Minimax2: ", minimax_find_board_value(new_board, depth=2,eval_fn=basic_evaluate)
    for move1, new_board1 in get_all_next_moves(new_board):
        print "Minimax1: ", -1*minimax_find_board_value(new_board1, depth=1,eval_fn=basic_evaluate)
        #for move2, new_board2 in get_all_next_moves(new_board1):
        #    print "Minimax0: ",basic_evaluate(new_board2)
####
"""
    
## Create a "player" function that uses the focused_evaluate function
quick_to_win_player = lambda board: minimax(board, depth=5,
                                            eval_fn=focused_evaluate)

## You can try out your new evaluation function by uncommenting this line:
#run_game(basic_player, quick_to_win_player)

## Write an alpha-beta-search procedure that acts like the minimax-search
## procedure, but uses alpha-beta pruning to avoid searching bad ideas
## that can't improve the result. The tester will check your pruning by
## counting the number of static evaluations you make.
##
## You can use minimax() in basicplayer.py as an example.

"""JUST TESTING HOW THE TREE SEARCHER WORKS
tup_tree = ("A", None,
	    ("B", None,
		 ("C", None,
		  ("D", 2),
		  ("E", 2)),
		 ("F", None,
		  ("G", 0),
		  ("H", 4))
		 ),
		("I", None,
		 ("J", None,
		  ("K", 6),
		  ("L", 8)),
		 ("M", None,
		  ("N", 4),
		  ("O", 6))
		 )
		)
from tree_searcher import *
print tup_tree
tree = make_tree(tup_tree)
print "%s:\n%s" %("TREE_1", tree_as_string(tree))
"""


def alpha_beta_search(board, depth,
                      eval_fn,
                      get_next_moves_fn=get_all_next_moves,
		      is_terminal_fn=is_terminal):
    #f(x) then -1*f(y) then -1*(-1)*f(z) and finally f(alpha) is calculated as a number and is returned recursively, that makes every second evalution of val > best_val find the minimum. The first evaluation of val > best_val will be a minimum evalution of the leaf values. With negative values in the beginnning e.g. [-2,-3,-4] it still works val > best_val for [2,3,4] chooses 4 and that is exactly the the minimum -4.
    
    
    #This line 
    #best_val = None
    #is substituted for the following line
    
    #move is set to -1 in the beginning
    alpha = (-1000,-1,board)
    beta = (1000,-1,board)
    nodeType = 'max'
    
    
    #get_next_moves_fn returns a 2-tuple
    #move is a number between 0 and 6
    for move, new_board in get_next_moves_fn(board):
        #alpha_beta_find_board_value with new_board and dept-1. ONE LEVEL DOWN.
        #
        val = -1 * alpha_beta_find_board_value(nodeType, alpha[0], alpha[0], new_board, depth-1, 
                                            eval_fn,
                                            get_next_moves_fn,
                                            is_terminal_fn)
        #move is a number between 0 and 6
        if val > alpha[0]:
            alpha = (val,move,new_board)
        #alpha[0] >= val then the max has alredy been found 
        
        #this I don't understand. 
        if alpha[0] >= abs(beta[0]):
            break
    
        print "ALPHA-BETA: Decided on column %d with rating %d" % (alpha[1], alpha[0])
    
    #this I also don't get. Why return the move number? 
    #Answer: Because it should give the player the best move.
    return alpha[1]

def alpha_beta_find_board_value(nodeType, alpha, beta, board, depth, eval_fn,
                             get_next_moves_fn=get_all_next_moves,
                             is_terminal_fn=is_terminal):
    
    #We have gone a level down and need to change the nodeType.
    #We started with 'max'. So the first change must bo to 'min'.
    if nodeType == 'min':
        nodeType = 'max'
    if nodeType == 'max':
        nodeType = 'min'
    
    #Has to calculate the value of the all leaf boards.
    if is_terminal_fn(depth, board):
        board_value = eval_fn(board)
        if nodeType == 'max':
            #Lets assume we to go 2 levels down to reach the leafs.
            #Lets say the 'max' leafs has the board_values 1,2,3,4,5,6,7
            #Then one level up it must be a 'min' node.
            #Is 1 < 1000. Yes. Set beta = 1. Next iteration. Is 2 < 1. No.
            #Next iteration. Is 3 < 1. No. Und so weiter.
            #When the 7 iterations are complete beta is still 1.
            #Have we found the minimum of 1,2,3,4,5,6,7? Yes.  
            return board_value
        if nodeType == 'min':
            #Assume only 1 level down we have the leaves.
            #Is -1 > -1000. Yes. Set alpha = (1,movenode,boardnode). Is 2 > 1. Yes. 
            #Set alpha = (2,movenode,boardnode). So in the end alpha = (7,movenode,boardnode)
            return -board_value
    
    #This loop is just go deeper into the tree. All the way to the leafs.
    for move, new_board in get_next_moves_fn(board):
        print 'performing minimax on: ', new_board, ', depth :', depth
        val = -1*alpha_beta_find_board_value(nodeType,alpha,beta,new_board, depth-1, eval_fn,
                                               get_next_moves_fn, 
                                               is_terminal_fn)
        print 'got board value: ', val , 'depth: ', depth,'node type:',nodeType                          
        if nodeType == 'max':
            if val > alpha:
                #alpha is Max' Memory. 
                alpha = val
        if nodeType == 'min':
            if val < beta:
                beta = val
                
        if alpha >= beta:
            print 'alpha:',alpha,'>=','beta',beta,'at depth', depth,';pruning'
            break
    
    if nodeType == 'max':
        return alpha
    if nodeType == 'min':
        #Lets say that one round of the loop has been performed
        # in the 2 level example and the values for beta has been set to 1,2,3,1,2,3,4
        # for the seven nodes. beta is now returned to alpha_beta_search.
        #We know it has to maximize, so -1 > -1000. Yes. Set alpha = -1. 
        return beta
 
    
#from testingclass import *

#x = Complex(3.0, -4.5)
#print x.i,x.r

#myNode = Node("S",4,"MIN",["A","B","C"])
#myNode.set_children(["D","E"])
#print myNode.get_children()
#print myNode.value
#myNode.add("F")
#print tree_as_string(myNode)
#print myNode.get_children()
#print myNode.num_children()

#print tree_eval(myNode)
#Does not work???
#print tree_as_string(myNode)

#tup = ("S",("A",("B",("D","F")),"C"))
#print tup[0],type(tup[1])
#n = Node(tup[0],tup[1],"MIN")
#print n.value
#print len(tup)
#print len(("A",("B",("D","F")),"C"))
#print range(2,5)
#print make_tree(("S","K",("A",("B",("D","F")),"C")))
#print make_tree(("S","A"))

## Now you should be able to search twice as deep in the same amount of time.
## (Of course, this alpha-beta-player won't work until you've defined
## alpha-beta-search.)

alpha_beta_search(testboard,depth=4,eval_fn=basic_evaluate)


alphabeta_player = lambda board: alpha_beta_search(board,
                                                   depth=8,
                                                   eval_fn=focused_evaluate)

#run_game(basic_player, alphabeta_player)

## This player uses progressive deepening, so it can kick your ass while
## making efficient use of time:
ab_iterative_player = lambda board: \
    run_search_function(board,
                        search_fn=alpha_beta_search,
                        eval_fn=focused_evaluate, timeout=5)
#run_game(human_player, alphabeta_player)

## Finally, come up with a better evaluation function than focused-evaluate.
## By providing a different function, you should be able to beat
## simple-evaluate (or focused-evaluate) while searching to the
## same depth.

def better_evaluate(board):
    raise NotImplementedError

# Comment this line after you've fully implemented better_evaluate
better_evaluate = memoize(basic_evaluate)

# Uncomment this line to make your better_evaluate run faster.
# better_evaluate = memoize(better_evaluate)

# For debugging: Change this if-guard to True, to unit-test
# your better_evaluate function.
if False:
    board_tuples = (( 0,0,0,0,0,0,0 ),
                    ( 0,0,0,0,0,0,0 ),
                    ( 0,0,0,0,0,0,0 ),
                    ( 0,2,2,1,1,2,0 ),
                    ( 0,2,1,2,1,2,0 ),
                    ( 2,1,2,1,1,1,0 ),
                    )
    test_board_1 = ConnectFourBoard(board_array = board_tuples,
                                    current_player = 1)
    test_board_2 = ConnectFourBoard(board_array = board_tuples,
                                    current_player = 2)
    # better evaluate from player 1
    print "%s => %s" %(test_board_1, better_evaluate(test_board_1))
    # better evaluate from player 2
    print "%s => %s" %(test_board_2, better_evaluate(test_board_2))

## A player that uses alpha-beta and better_evaluate:
your_player = lambda board: run_search_function(board,
                                                search_fn=alpha_beta_search,
                                                eval_fn=better_evaluate,
                                                timeout=5)

#your_player = lambda board: alpha_beta_search(board, depth=4,
#                                              eval_fn=better_evaluate)

## Uncomment to watch your player play a game:
#run_game(your_player, your_player)

## Uncomment this (or run it in the command window) to see how you do
## on the tournament that will be graded.
#run_game(your_player, basic_player)

## These three functions are used by the tester; please don't modify them!
def run_test_game(player1, player2, board):
    assert isinstance(globals()[board], ConnectFourBoard), "Error: can't run a game using a non-Board object!"
    return run_game(globals()[player1], globals()[player2], globals()[board])
    
def run_test_search(search, board, depth, eval_fn):
    assert isinstance(globals()[board], ConnectFourBoard), "Error: can't run a game using a non-Board object!"
    return globals()[search](globals()[board], depth=depth,
                             eval_fn=globals()[eval_fn])

## This function runs your alpha-beta implementation using a tree as the search
## rather than a live connect four game.   This will be easier to debug.
def run_test_tree_search(search, board, depth):
    return globals()[search](globals()[board], depth=depth,
                             eval_fn=tree_searcher.tree_eval,
                             get_next_moves_fn=tree_searcher.tree_get_next_move,
                             is_terminal_fn=tree_searcher.is_leaf)
    
## Do you want us to use your code in a tournament against other students? See
## the description in the problem set. The tournament is completely optional
## and has no effect on your grade.
COMPETE = (None)

## The standard survey questions.
HOW_MANY_HOURS_THIS_PSET_TOOK = ""
WHAT_I_FOUND_INTERESTING = ""
WHAT_I_FOUND_BORING = ""
NAME = ""
EMAIL = ""


from util import INFINITY
from connectfour import *
from basicplayer import *
from util import *

testboard = ConnectFourBoard()
testboard = testboard.do_move(0).do_move(3).do_move(6).do_move(4).do_move(3)

nextmoves = get_all_next_moves(testboard)
for i,j in nextmoves:
    print i
    print j
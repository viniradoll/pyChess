import chess.core.board as Board
from chess.core.pieces import Pawn
from chess.core.datatypes import Color
from chess.core.datatypes import Square

def test_opposite_colors():
    assert Color.WHITE is not Color.BLACK

def test_initiate_board():
    board = Board.MatrixBoard()
    assert board.grid == [[None]*8]*8

def test_instanciate_pawn():
    board = Board.MatrixBoard()
    pawn = Pawn(Color.WHITE)
    assert isinstance(pawn.getMoveList(board, Square(row=1,col=5)), list)

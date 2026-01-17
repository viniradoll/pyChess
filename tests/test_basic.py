import chess.core.board as Board
import chess.core.datatypes as datatypes
import chess.core.pieces as pieces

def test_opposite_colors():
    assert datatypes.Color.WHITE is not datatypes.Color.BLACK

def test_initiate_board():
    board = Board.MatrixBoard()
    assert board.grid == [[None]*8]*8

def instanciate_board():
    board = Board.MatrixBoard()
    for i in range(8):
        board.setPieceAt(datatypes.Square(1,i), pieces.Pawn(datatypes.Color.WHITE))

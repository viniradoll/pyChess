from chess.core.datatypes.Board import MatrixBoard
from chess.core.datatypes.Pieces import Piece
from chess.core.datatypes.Color import Color

def test_opposite_colors():
    assert Color.WHITE is not Color.BLACK

def test_instanciate_piece():
    whiteBasePiece:Piece = Piece(Color.WHITE)

    blackBasePiece = Piece(color=Color.BLACK)

    assert isinstance(whiteBasePiece,Piece) and isinstance(blackBasePiece,Piece)

def test_initiate_board():
    board = MatrixBoard()
    assert board.grid == [[None]*8]*8

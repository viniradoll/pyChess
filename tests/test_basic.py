import chess.core.board as Board
import chess.core.datatypes as datatypes
import chess.core.pieces as pieces
import pytest

def test_opposite_colors():
    assert datatypes.Color.WHITE is not datatypes.Color.BLACK

def test_initiate_board():
    board = Board.MatrixBoard()
    assert board.grid == [[None]*8]*8

def test_instanciate_square():
    board = instanciate_board()
    with pytest.raises(ValueError):
        board.setPieceAt(datatypes.Square(12,5), pieces.Pawn(datatypes.Color.BLACK))
    with pytest.raises(ValueError):
        board.setPieceAt(datatypes.Square(-1,5), pieces.Pawn(datatypes.Color.BLACK))

def instanciate_board() -> Board.MatrixBoard:
    board = Board.MatrixBoard()
    for i in range(8):
        board.setPieceAt(datatypes.Square(1,i), pieces.Pawn(datatypes.Color.WHITE))
    return board

import chess.core.board as board
import chess.core.pieces as pieces
import chess.core.datatypes as datatypes

def test_instanciate_pawn():
    Board = board.MatrixBoard()
    pawn = pieces.Pawn(datatypes.Color.WHITE)
    assert isinstance(pawn.getMoveList(Board, datatypes.Square(row=1,col=5)), list)

def test_sliding_piece():
    class GenericSlidingPiece(pieces.SlidingPiece):
        def directions(self):
            return  [(1,0)]

    Piece = GenericSlidingPiece(datatypes.Color.WHITE)
    Board = board.MatrixBoard()
    row = 1
    PieceSquare = datatypes.Square(row,0)
    Board.setPieceAt(PieceSquare,Piece)

    moveList: list[datatypes.Move] = Board.getMovesAt(PieceSquare)

    assert len(moveList) == 6
    for move in moveList:
        row += 1
        assert move.from_sq == PieceSquare
        assert move.to_sq.col == PieceSquare.col
        assert move.to_sq.row == row

def test_multidimensional_sliding_piece():
    class GenericSlidingPiece(pieces.SlidingPiece):
        def directions(self):
            return  [(1,1),(-1,-1)]

    Piece = GenericSlidingPiece(datatypes.Color.WHITE)
    Board = board.MatrixBoard()
    PieceSquare = datatypes.Square(3,3)
    Board.setPieceAt(PieceSquare,Piece)

    moveList: list[datatypes.Move] = Board.getMovesAt(PieceSquare)
    for move in moveList:
        assert move.to_sq != PieceSquare
        assert move.to_sq.col == move.to_sq.row

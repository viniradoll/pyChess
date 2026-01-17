from .base import Piece
import chess.core.datatypes as datatypes
import chess.core.board as board

class Pawn(Piece):
    canPromote = True

    def getMoveList(self, board: board.Board, from_sq: datatypes.Square) -> list[datatypes.Square]:
        moveList: list[datatypes.Square] = []
        newSquare = datatypes.Square(from_sq.row+1, from_sq.col)
        if board.isAvailable(newSquare):
            moveList.append(newSquare)
        
            newSquare = datatypes.Square(from_sq.row+2, from_sq.col)
            if not self.hasMoved and board.isAvailable(newSquare):
                moveList.append(newSquare)

        newSquare = datatypes.Square(from_sq.row+1, from_sq.col+1)
        if board.isCapturable(newSquare, self.color):
            moveList.append(newSquare)

        newSquare = datatypes.Square(from_sq.row-1, from_sq.col+1)
        if board.isCapturable(newSquare, self.color):
            moveList.append(newSquare)

        return moveList
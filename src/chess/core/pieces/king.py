from chess.core.pieces import Piece
from chess.core.board import BoardView
from chess.core.datatypes import Square, Move

class King(Piece):
    def getMoveList(self, board: BoardView, from_sq: Square) -> list[Move]:
        moveList = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0:
                    continue
                newSquare = Square(from_sq.row+i,col=from_sq.col+j)
                if not board.isAvailable(newSquare) and not board.isCapturable(newSquare, self.color):
                    continue
                moveList.append(Move(from_sq,to_sq=newSquare))
        return moveList

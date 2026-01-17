from abc import ABC, abstractmethod
import chess.core.datatypes as datatypes
import chess.core.board as board

class Piece(ABC):
    # Pices has already moved in this game
    hasMoved: bool = False
    # If piece can promote on the last rank (e.g. Pawn)
    canPromote: bool = False
    # If piece can Castle (e.g. King)
    primaryCastlePiece: bool = False
    # If piece can help a piece Castle (e.g. Rook)
    secundaryCastlePiece: bool = False

    def __init__(self, color: datatypes.Color):
        self.color = color

    @abstractmethod
    def getMoveList(self, board: board.Board, from_sq: datatypes.Square) -> list[datatypes.Square]:
        return []
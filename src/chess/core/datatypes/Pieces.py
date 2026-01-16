from .Move import Move
from .Color import Color

class Piece:
    # Pices has already moved in this game
    hasMoved: bool = False
    # If piece can promote on the last rank (e.g. Pawn)
    canPromote: bool = False
    # If piece can Castle (e.g. King)
    primaryCastlePiece: bool = False
    # If piece can help a piece Castle (e.g. Rook)
    secundaryCastlePiece: bool = False

    def __init__(self, color: Color):
        self.color = color

    def onMove(self, move: Move):
        pass

    def getMoveList(self) -> list[Move]:
        return []

class Pawn(Piece):
    
    def getMoveList(self) -> list[Move]:
        return []
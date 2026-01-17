import chess.core.board as board
from abc import ABC, abstractmethod
import chess.core.datatypes as datatypes
import chess.core.pieces as pieces

class Board(board.BoardView, ABC):
    def __init__(self, size: int):
        self.size: int = size

    @abstractmethod
    def initialize(self):
        pass

    def setupStartingPosition(self, position: datatypes.Position):
        for square, piece in position.pieces:
            self.setPieceAt(square, piece=piece)

    @abstractmethod
    def getPieceAt(self,sq:datatypes.Square) -> pieces.Piece | None:
        return None

    @abstractmethod
    def setPieceAt(self,sq:datatypes.Square, piece: pieces.Piece):
        pass

    def getColorAt(self, sq: datatypes.Square) -> datatypes.Color | None:
        piece = self.getPieceAt(sq)
        return None if piece is None else piece.color
    
    def isInbound(self,sq:datatypes.Square) -> bool:
        return True if sq.col < self.size and sq.row < self.size else False

    def isEmpty(self, sq: datatypes.Square) -> bool:
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        return True if self.getPieceAt(sq) is None else False

    def isEnemy(self, sq:datatypes.Square, color: datatypes.Color) -> bool:
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        piece = self.getPieceAt(sq)
        return piece is not None and piece.color != color
    
    def isAvaiable(self, sq:datatypes.Square) -> bool:
        return self.isInbound(sq) and self.isEmpty(sq)

    def isCapturable(self,sq:datatypes.Square, color: datatypes.Color) -> bool:
        return self.isInbound(sq) and self.isEnemy(sq, color)
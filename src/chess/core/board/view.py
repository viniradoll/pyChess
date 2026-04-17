from abc import ABC, abstractmethod
import chess.core.datatypes as datatypes


class BoardView(ABC):
    def __init__(self, size: int=8):
        self.size = size

    @abstractmethod
    def getColorAt(self, sq: datatypes.Square) -> datatypes.Color | None:
        ...

    def isInbound(self,sq:datatypes.Square) -> bool:
        return 0 <= sq.row < self.size and 0 <= sq.col < self.size

    def isEmpty(self, sq: datatypes.Square) -> bool:
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        return True if self.getColorAt(sq) is None else False

    def isEnemy(self, sq:datatypes.Square, color: datatypes.Color) -> bool:
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        squareColor = self.getColorAt(sq)
        return squareColor is not None and squareColor != color

    def isAvailable(self, sq:datatypes.Square) -> bool:
        return self.isInbound(sq) and self.isEmpty(sq)

    def isCapturable(self,sq:datatypes.Square, color: datatypes.Color) -> bool:
        return self.isInbound(sq) and self.isEnemy(sq, color)
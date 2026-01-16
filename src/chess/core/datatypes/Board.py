from abc import ABC, abstractmethod
from chess.core.datatypes.Square import Square
from chess.core.datatypes.Color import Color
from chess.core.datatypes.Pieces import Piece
from chess.core.datatypes.Position import Position

class Board(ABC):
    def __init__(self, size: int):
        self.size: int = size

    @abstractmethod
    def initialize(self):
        pass

    def setupStartingPosition(self, position: Position):
        for square, piece in position.pieces:
            self.setPieceAt(square, piece=piece)

    @abstractmethod
    def getPieceAt(self,sq:Square) -> Piece | None:
        return None

    @abstractmethod
    def setPieceAt(self,sq:Square, piece: Piece):
        pass
    
    def isInbound(self,sq:Square) -> bool:
        return True if sq.col < self.size and sq.row < self.size else False

    def isEmpty(self, sq: Square) -> bool:
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        return True if self.getPieceAt(sq) is None else False

    def isEnemy(self, sq:Square, color: Color) -> bool:
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        piece = self.getPieceAt(sq)
        return piece is not None and piece.color != color
        

class MatrixBoard(Board):
    def __init__(self, size: int=8):
        super().__init__(size)
        self.grid: list[list[Piece | None]] = []
        self.initialize()

    def initialize(self):
        for i in range(self.size):
            self.grid.append([None] * self.size)

    def getPieceAt(self, sq: Square) -> Piece | None:
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        return self.grid[sq.row][sq.col]

    def setPieceAt(self,sq:Square, piece: Piece):
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        self.grid[sq.row][sq.col] = piece

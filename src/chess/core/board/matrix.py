from chess.core.board.base import Board
import chess.core.datatypes as datatypes
import chess.core.pieces as pieces

class MatrixBoard(Board):
    def __init__(self, size: int=8):
        super().__init__(size)
        self.grid: list[list[pieces.Piece | None]] = []
        self.initialize()

    def initialize(self):
        for i in range(self.size):
            self.grid.append([None] * self.size)

    def getPieceAt(self, sq: datatypes.Square) -> pieces.Piece | None:
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        return self.grid[sq.row][sq.col]

    def setPieceAt(self,sq:datatypes.Square, piece: pieces.Piece):
        if not self.isInbound(sq):
            raise ValueError(f"Square is not inbound row: '{sq.row}' col: '{sq.col}'")
        self.grid[sq.row][sq.col] = piece

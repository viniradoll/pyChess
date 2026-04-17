import chess.core.pieces as Pieces
from chess.core.datatypes.square import Square

class Position:
    pieces: list[tuple[Square, Pieces.Piece]]
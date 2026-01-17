from chess.core.pieces import SlidingPiece

class Rook(SlidingPiece):
    secundaryCastlePiece = True
    def directions(self):
        return [(1,0),(0,1),(-1,0),(0,-1)]
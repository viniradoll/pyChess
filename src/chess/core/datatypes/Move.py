import chess.core.datatypes as datatypes

class Move:
    from_sq: datatypes.Square
    to_sq: datatypes.Square
    def __init__(self, from_sq:datatypes.Square, to_sq:datatypes.Square):
        self.from_sq = from_sq  
        self.to_sq = to_sq

    def __repr__(self):
        return str({"from_sq": self.from_sq, "to_sq": self.to_sq})
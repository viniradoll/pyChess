from .Square import Square

class Move:
    from_sq: Square
    to_sq: Square
    def __init__(self, from_sq:Square, to_sq:Square):
        self.from_sq = from_sq  
        self.to_sq = to_sq
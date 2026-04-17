import pytest
import chess.core.board as board
import chess.core.datatypes as datatypes
import chess.core.pieces as pieces


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def empty_board() -> board.MatrixBoard:
    return board.MatrixBoard()


def board_with_pawn(row: int, col: int, color=datatypes.Color.WHITE) -> tuple[board.MatrixBoard, datatypes.Square]:
    b = empty_board()
    sq = datatypes.Square(row, col)
    b.setPieceAt(sq, pieces.Pawn(color))
    return b, sq


# ---------------------------------------------------------------------------
# MatrixBoard — inicialização
# ---------------------------------------------------------------------------

class TestMatrixBoardInit:
    def test_default_size(self):
        b = empty_board()
        assert b.size == 8

    def test_grid_starts_empty(self):
        b = empty_board()
        for row in b.grid:
            assert all(cell is None for cell in row)

    def test_custom_size(self):
        b = board.MatrixBoard(size=10)
        assert b.size == 10
        assert len(b.grid) == 10
        assert all(len(row) == 10 for row in b.grid)


# ---------------------------------------------------------------------------
# isInbound
# ---------------------------------------------------------------------------

class TestIsInbound:
    def test_valid_corners(self):
        b = empty_board()
        assert b.isInbound(datatypes.Square(0, 0))
        assert b.isInbound(datatypes.Square(7, 7))
        assert b.isInbound(datatypes.Square(0, 7))
        assert b.isInbound(datatypes.Square(7, 0))

    def test_out_of_bounds_positive(self):
        b = empty_board()
        assert not b.isInbound(datatypes.Square(8, 0))
        assert not b.isInbound(datatypes.Square(0, 8))
        assert not b.isInbound(datatypes.Square(8, 8))

    def test_out_of_bounds_negative(self):
        b = empty_board()
        assert not b.isInbound(datatypes.Square(-1, 0))
        assert not b.isInbound(datatypes.Square(0, -1))
        assert not b.isInbound(datatypes.Square(-1, -1))


# ---------------------------------------------------------------------------
# setPieceAt / getPieceAt
# ---------------------------------------------------------------------------

class TestSetAndGetPiece:
    def test_set_and_get(self):
        b = empty_board()
        sq = datatypes.Square(3, 4)
        pawn = pieces.Pawn(datatypes.Color.WHITE)
        b.setPieceAt(sq, pawn)
        assert b.getPieceAt(sq) is pawn

    def test_get_empty_square_returns_none(self):
        b = empty_board()
        assert b.getPieceAt(datatypes.Square(0, 0)) is None

    def test_set_out_of_bounds_raises(self):
        b = empty_board()
        with pytest.raises(ValueError):
            b.setPieceAt(datatypes.Square(8, 0), pieces.Pawn(datatypes.Color.WHITE))

    def test_set_negative_raises(self):
        b = empty_board()
        with pytest.raises(ValueError):
            b.setPieceAt(datatypes.Square(-1, 0), pieces.Pawn(datatypes.Color.WHITE))

    def test_get_out_of_bounds_raises(self):
        b = empty_board()
        with pytest.raises(ValueError):
            b.getPieceAt(datatypes.Square(8, 0))

    def test_overwrite_piece(self):
        b = empty_board()
        sq = datatypes.Square(0, 0)
        pawn = pieces.Pawn(datatypes.Color.WHITE)
        pawn2 = pieces.Pawn(datatypes.Color.BLACK)
        b.setPieceAt(sq, pawn)
        b.setPieceAt(sq, pawn2)
        assert b.getPieceAt(sq) is pawn2


# ---------------------------------------------------------------------------
# isEmpty / isEnemy / isAvailable / isCapturable / getColorAt
# ---------------------------------------------------------------------------

class TestBoardQueries:
    def test_isEmpty_on_empty_square(self):
        b = empty_board()
        assert b.isEmpty(datatypes.Square(0, 0))

    def test_isEmpty_on_occupied_square(self):
        b, sq = board_with_pawn(3, 3)
        assert not b.isEmpty(sq)

    def test_isEmpty_out_of_bounds_raises(self):
        b = empty_board()
        with pytest.raises(ValueError):
            b.isEmpty(datatypes.Square(8, 0))

    def test_getColorAt_empty_returns_none(self):
        b = empty_board()
        assert b.getColorAt(datatypes.Square(0, 0)) is None

    def test_getColorAt_returns_correct_color(self):
        b, sq = board_with_pawn(3, 3, datatypes.Color.BLACK)
        assert b.getColorAt(sq) == datatypes.Color.BLACK

    def test_isEnemy_against_opposite_color(self):
        b, sq = board_with_pawn(3, 3, datatypes.Color.BLACK)
        assert b.isEnemy(sq, datatypes.Color.WHITE)

    def test_isEnemy_against_same_color(self):
        b, sq = board_with_pawn(3, 3, datatypes.Color.WHITE)
        assert not b.isEnemy(sq, datatypes.Color.WHITE)

    def test_isEnemy_on_empty_square(self):
        b = empty_board()
        assert not b.isEnemy(datatypes.Square(0, 0), datatypes.Color.WHITE)

    def test_isEnemy_out_of_bounds_raises(self):
        b = empty_board()
        with pytest.raises(ValueError):
            b.isEnemy(datatypes.Square(-1, 0), datatypes.Color.WHITE)

    def test_isAvailable_empty_inbound(self):
        b = empty_board()
        assert b.isAvailable(datatypes.Square(0, 0))

    def test_isAvailable_occupied(self):
        b, sq = board_with_pawn(2, 2)
        assert not b.isAvailable(sq)

    def test_isAvailable_out_of_bounds(self):
        b = empty_board()
        assert not b.isAvailable(datatypes.Square(8, 8))

    def test_isCapturable_enemy(self):
        b, sq = board_with_pawn(4, 4, datatypes.Color.BLACK)
        assert b.isCapturable(sq, datatypes.Color.WHITE)

    def test_isCapturable_ally(self):
        b, sq = board_with_pawn(4, 4, datatypes.Color.WHITE)
        assert not b.isCapturable(sq, datatypes.Color.WHITE)

    def test_isCapturable_empty(self):
        b = empty_board()
        assert not b.isCapturable(datatypes.Square(4, 4), datatypes.Color.WHITE)

    def test_isCapturable_out_of_bounds(self):
        b = empty_board()
        assert not b.isCapturable(datatypes.Square(-1, 0), datatypes.Color.WHITE)
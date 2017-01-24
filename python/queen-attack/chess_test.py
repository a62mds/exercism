import unittest

from queen_attack import ChessObject, Piece, Space, Board
from queen_attack import board


class ChessPieceTest(unittest.TestCase):
    def test_white_queen_at_0_0(self):
        w = 'white'
        q = 'queen'
        r = 0
        c = 0
        wq = Piece(w, q, r, c)
        self.assertEqual(wq.color, w)
        self.assertEqual(wq.kind, q)
        self.assertEqual(wq.row, r)
        self.assertEqual(wq.col, c)

    def test_black_queen_at_7_7(self):
        b = 'black'
        q = 'queen'
        r = 7
        c = 7
        bq = Piece(b, q, r, c)
        self.assertEqual(bq.color, b)
        self.assertEqual(bq.kind, q)
        self.assertEqual(bq.row, r)
        self.assertEqual(bq.col, c)

    def test_invalid_color(self):
        color = 'purple'
        queen = 'queen'
        row = 3
        col = 4
        with self.assertRaises(ValueError):
            pq = Piece(color, queen, row, col)

    def test_invalid_kind(self):
        color = 'white'
        kind = 'martyr'
        row = 6
        col = 2
        with self.assertRaises(ValueError):
            wm = Piece(color, kind, row, col)

    def test_negative_row(self):
        color = 'white'
        kind = 'queen'
        row = -1
        col = 2
        with self.assertRaises(ValueError):
            wq = Piece(color, kind, row, col)

    def test_row_too_large(self):
        color = 'black'
        kind = 'queen'
        row = 8
        col = 6
        with self.assertRaises(ValueError):
            bq = Piece(color, kind, row, col)

    def test_negative_col(self):
        color = 'white'
        kind = 'queen'
        row = 5
        col = -1
        with self.assertRaises(ValueError):
            wq = Piece(color, kind, row, col)

    def test_col_too_large(self):
        color = 'black'
        kind = 'queen'
        row = 2
        col = 102394
        with self.assertRaises(ValueError):
            bq = Piece(color, kind, row, col)

    def test_queen_bottom_left_allowed_spaces(self):
        color = 'white'
        kind = 'queen'
        row = 0
        col = 0
        wq = Piece(color, kind, row, col)
        col0 = [(r, 0) for r in range(ChessObject._BOARD_LEN)]
        row0 = [(0, c) for c in range(ChessObject._BOARD_WID)]
        diag = [(d, d) for d in range(ChessObject._BOARD_WID)]
        self.assertEqual(wq.allowed_queen_moves(), set(col0 + row0 + diag))

    def test_queen_bottom_right_allowed_spaces(self):
        color = 'black'
        kind = 'queen'
        row = 0
        col = 7
        bq = Piece(color, kind, row, col)
        col7 = [(r, 7) for r in range(ChessObject._BOARD_LEN)]
        row0 = [(0, c) for c in range(ChessObject._BOARD_WID)]
        diag = [(d, 7-d) for d in range(ChessObject._BOARD_WID)]
        self.assertEqual(bq.allowed_queen_moves(), set(col7 + row0 + diag))

    def test_queen_top_right_allowed_spaces(self):
        color = 'white'
        kind = 'queen'
        row = 7
        col = 7
        wq = Piece(color, kind, row, col)
        col7 = [(r, 7) for r in range(ChessObject._BOARD_LEN)]
        row7 = [(7, c) for c in range(ChessObject._BOARD_WID)]
        diag = [(7-d, 7-d) for d in range(ChessObject._BOARD_WID)]
        self.assertEqual(wq.allowed_queen_moves(), set(col7 + row7 + diag))

    def test_queen_top_left_allowed_spaces(self):
        color = 'black'
        kind = 'queen'
        row = 7
        col = 0
        bq = Piece(color, kind, row, col)
        col0 = [(r, 0) for r in range(ChessObject._BOARD_LEN)]
        row7 = [(7, c) for c in range(ChessObject._BOARD_WID)]
        diag = [(7-d, d) for d in range(ChessObject._BOARD_WID)]
        self.assertEqual(bq.allowed_queen_moves(), set(col0 + row7 + diag))

    def test_queen_bottom_left_can_move_to(self):
        color = 'white'
        kind = 'queen'
        row = 0
        col = 0
        wq = Piece(color, kind, row, col)
        col0 = [(r, 0) for r in range(ChessObject._BOARD_LEN)]
        row0 = [(0, c) for c in range(ChessObject._BOARD_WID)]
        diag = [(d, d) for d in range(ChessObject._BOARD_WID)]
        all_spaces = set((r, c) for r in range(ChessObject._BOARD_LEN) for c in range(ChessObject._BOARD_WID))
        allowed_spaces = set(col0 + row0 + diag)
        disallowed_spaces = all_spaces - allowed_spaces
        can_move_to_allowed_spaces = all(wq.can_move_to(*s) for s in allowed_spaces)
        cannot_move_to_disallowed_spaces = all(not wq.can_move_to(*s) for s in disallowed_spaces)
        self.assertEqual(can_move_to_allowed_spaces, True)
        self.assertEqual(cannot_move_to_disallowed_spaces, True)


class BoardFnTest(unittest.TestCase):
    def test_board1(self):
        ans = ['________',
               '________',
               '___W____',
               '________',
               '________',
               '______B_',
               '________',
               '________']
        self.assertEqual(ans, board((2, 3), (5, 6)))

if __name__ == '__main__':
    unittest.main()

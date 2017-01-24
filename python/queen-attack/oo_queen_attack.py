class ChessObject:
    _BOARD_LEN = 8
    _BOARD_WID = 8
    _PIECE_COLORS = ['white', 'black']
    _PIECE_KINDS = ['queen']


class Piece(ChessObject):
    def __init__(self, color, kind, row, col):
        if color in self._PIECE_COLORS:
            self._color = color
        else:
            raise ValueError('Invalid piece color: {}'.format(color))
        if kind in self._PIECE_KINDS:
            self._kind = kind
        else:
            raise ValueError('Invalid piece kind: {}'.format(kind))
        if row in range(self._BOARD_LEN) and col in range(self._BOARD_WID):
            self._row = row
            self._col = col
        else:
            raise ValueError('Invalid position: ({}, {})'.format(row, col))
    @property
    def color(self):
        return self._color
    @property
    def kind(self):
        return self._kind
    @property
    def row(self):
        return self._row
    @row.setter
    def row(self, r):
        if r in range(0, self._BOARD_LEN):
            self._row = r
        else:
            raise ValueError('Cannot place piece in row {}'.format(r))
    @property
    def col(self):
        return self._col
    @col.setter
    def col(self, c):
        if c in range(0, self._BOARD_WID):
            self._col = c
        else:
            raise ValueError('Cannot place piece in col {}'.format(c))
    def allowed_queen_moves(self):
        def move_left(row, col):
            return (row, col-1)
        def move_right(row, col):
            return (row, col+1)
        def move_up(row, col):
            return (row+1, col)
        def move_down(row, col):
            return (row-1, col)
        def move_up_left(row, col):
            return move_up(*move_left(row, col))
        def move_up_right(row, col):
            return move_up(*move_right(row, col))
        def move_down_right(row, col):
            return move_down(*move_right(row, col))
        def move_down_left(row, col):
            return move_down(*move_left(row, col))
        moves = [move_left, move_right, move_up, move_down,
                 move_up_left, move_up_right, move_down_right, move_down_left]
        def get_accessible_spaces(move_in_direction, from_row, from_col):
            row = from_row
            col = from_col
            accessible_spaces = []
            while True:
                row, col = move_in_direction(row, col)
                if row in range(0, self._BOARD_LEN) and col in range(0, self._BOARD_WID):
                    accessible_spaces.append((row, col))
                else:
                    break
            return accessible_spaces
        allowed_moves = [(self._row, self._col)]
        for move in moves:
            allowed_moves += get_accessible_spaces(move, self._row, self._col)
        return set(allowed_moves)
    def can_move_to(self, row, col):
        allowed_moves = {'queen' : self.allowed_queen_moves}
        return (row, col) in allowed_moves[self._kind]()


class Space(ChessObject):
    def __init__(self, row, col, piece=None):
        self._row = row
        self._col = col
        self._piece = piece
    @property
    def row(self):
        return self._row
    @property
    def col(self):
        return self._col
    @property
    def piece(self):
        return self._piece


class Board(ChessObject):
    def __init__(self, *pieces):
        self._board = self.empty_board() if pieces else self.default_board()
        for piece in pieces:
            if not self._board[piece.row][piece.col].piece:
                self._board[piece.row][piece.col].piece = piece
            else:
                raise ValueError('Attempting to place two pieces on same space'
                                 ': ({r:d}, {c:d})'.format(piece.row, piece.col))
    def empty_board(self):
        return [[Space(r, c) for c in range(0, self._BOARD_WID)]
                for r in range(0, self._BOARD_LEN)]
    def default_board(self):
        return self.empty_board()
    def board_to_strlst(self):
        strlst = []
        for row in range(0, self._BOARD_LEN):
            rowstr = ''
            for col in range(0, self._BOARD_WID):
                if self._board[row][col].piece is None:
                    rowstr += '_'
                elif self._board[row][col].piece.color == 'white':
                    rowstr += 'W'
                elif self._board[row][col].piece.color == 'black':
                    rowstr += 'B'
        return strlst


def board(wq_position, bq_position):
    wq = Piece('white', 'queen', *wq_position)
    bq = Piece('black', 'queen', *bq_position)
    brd = Board(wq, bq)
    return brd.board_to_strlst()

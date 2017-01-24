class ChessPiece(object):
    _pieces = ['king', 'queen', 'rook', 'bishop', 'pawn']
    _colors = ['white', 'black']
    _rows = range(8)
    _cols = range(8)
    def __init__(self, color, piece, row, col):
        self.color = color
        self.piece = piece
        self.space = (row, col)
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, c):
        if c in ChessPiece._colors:
            self._color = c
        else:
            raise ValueError('{} is not a valid color'.format(c))
    @property
    def piece(self):
        return self._piece
    @piece.setter
    def piece(self, p):
        if p in ChessPiece._pieces:
            self._piece = p
        else:
            raise ValueError('{} is not a valid piece'.format(p))
    @property
    def space(self):
        return self._space
    @space.setter
    def space(self, row_col):
        if row_col[0] in ChessPiece._rows and row_col[1] in ChessPiece._cols:
            self._space = row_col
        else:
            raise ValueError('{} is not a valid position'.format(row_col))
    def move_left(self, row, col):
        return (row, col-1)
    def move_right(self, row, col):
        return (row, col+1)
    def move_up(self, row, col):
        return (row+1, col)
    def move_down(self, row, col):
        return (row-1, col)
    def move_up_left(self, row, col):
        return self.move_up(*self.move_left(row, col))
    def move_up_right(self, row, col):
        return self.move_up(*self.move_right(row, col))
    def move_down_right(self, row, col):
        return self.move_down(*self.move_right(row, col))
    def move_down_left(self, row, col):
        return self.move_down(*self.move_left(row, col))
    def can_attack(self, other):
        available_spaces = {'king'   : self.king_can_reach,
                            'queen'  : self.queen_can_reach,
                            'rook'   : self.rook_can_reach,
                            'bishop' : self.bishop_can_reach,
                            'pawn'   : self.pawn_can_reach}
        if self.space == other.space:
            raise ValueError('Two pieces occupying same space or '
                             'piece attempting to attack itself')
        elif self.color == other.color:
            return False
        else:
            return other.space in available_spaces[self.piece]()
    def get_accessible_spaces(self, move_in_direction, row, col):
        accessible_spaces = []
        while True:
            row, col = move_in_direction(row, col)
            if row in range(8) and col in range(8):
                accessible_spaces.append((row, col))
            else:
                break
        return accessible_spaces
    def king_can_reach(self):
        pass
    def queen_can_reach(self):
        moves = [self.move_left,
                 self.move_right,
                 self.move_up,
                 self.move_down,
                 self.move_up_left,
                 self.move_up_right,
                 self.move_down_right,
                 self.move_down_left]
        allowed_moves = []
        for move in moves:
            allowed_moves += self.get_accessible_spaces(move, *self.space)
        return set(allowed_moves)
    def rook_can_reach(self):
        pass
    def bishop_can_reach(self):
        pass
    def pawn_can_reach(self):
        pass

class ChessBoard(object):
    def __init__(self, *pieces):
        self.board = []
        for piece in pieces:
            self.place(piece)
    def place(self, piece):
        if any(p.space == piece.space for p in self.board):
            raise ValueError('Attempting to place piece in nonempty space')
        elif not (piece.space in [(r, c) for r in range(8) for c in range(8)]):
            raise ValueError('Attempting to place piece in nonexistant space')
        else:
            self.board.append(piece)
    def occupant(self, row, col):
        return next((p for p in self.board if p.space == (row, col)), None)
    def to_string(self):
        board_strings = []
        for row in range(8):
            row_string = ''
            for col in range(8):
                piece = self.occupant(row, col)
                if piece is None:
                    row_string += '_'
                elif piece.color == 'white':
                    row_string += 'W'
                else:
                    row_string += 'B'
            board_strings.append(row_string)
        return board_strings


####

def board(wq_pos, bq_pos):
    wq = ChessPiece('white', 'queen', *wq_pos)
    bq = ChessPiece('black', 'queen', *bq_pos)
    board = ChessBoard()
    board.place(wq)
    board.place(bq)
    return board.to_string()

def can_attack(wq_pos, bq_pos):
    wq = ChessPiece('white', 'queen', *wq_pos)
    bq = ChessPiece('black', 'queen', *bq_pos)
    return wq.can_attack(bq)

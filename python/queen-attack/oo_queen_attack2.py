from collections import namedtuple


ChessPiece = namedtuple('ChessPiece', 'piece color')

class ChessBoard:
    def __init__(self):
        self._board = [[None for _ in range(8)] for _ in range(8)]
    def place(self, piece, color, row, col):
        if self._board[row][col] is not None:
            raise Exception('Attempting to place piece in nonempty space')
        elif not (row in range(8) and col in range(8)):
            raise Exception('Attempting to place piece in nonexistant space')
        else:
            self._board[row][col] = ChessPiece(piece, color)
    def to_string(self):
        board_strings = []
        for row in self._board:
            row_string = ''
            for piece in row:
                if piece is None:
                    row_string += '_'
                elif piece.color == 'white':
                    row_string += 'W'
                else:
                    row_string += 'B'
            board_strings.append(row_string)
        return board_strings
    def can_attack(self, piece1, row1, col1, piece2, row2, col2):
        if (row1, col1) == (row2, col2):
            raise Exception('A piece cannot attack itself')
        reachable_spaces = {'queen' : self.queen_can_reach}
        if piece1.color == piece2.color:
            return False
        else:
            return (row2, col2) in reachable_spaces[piece1.piece](row1, col1)
    def queen_can_reach(self, from_row, from_col):
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
                if row in range(8) and col in range(8):
                    accessible_spaces.append((row, col))
                else:
                    break
            return accessible_spaces
        allowed_moves = []
        for move in moves:
            allowed_moves += get_accessible_spaces(move, from_row, from_col)
        return set(allowed_moves)

def gen_two_queen_board(white_queen_position, black_queen_position):
    board = ChessBoard()
    try:
        board.place('queen', 'white', *white_queen_position)
        board.place('queen', 'black', *black_queen_position)
    except:
        raise ValueError('Invalid position')
    return board

def board(white_queen_position, black_queen_position):
    board = gen_two_queen_board(white_queen_position, black_queen_position)
    return board.to_string()

def can_attack(wq_pos, bq_pos):
    board = gen_two_queen_board(wq_pos, bq_pos)
    wq = ChessPiece('queen', 'white')
    bq = ChessPiece('queen', 'black')
    return board.can_attack(wq, wq_pos[0], wq_pos[1], bq, bq_pos[0], bq_pos[1])

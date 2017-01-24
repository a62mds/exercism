from re import match


class MinesweeperSpace:
    _states = {' ' : 0, '*' : 1}
    @classmethod
    def allowed_states(cls):
        return self._states
    def __init__(self, x, y, state, nbs):
        self._x = x
        self._y = y
        self._state = self._states[state]
        self._nbs = nbs
    @property
    def xpos(self):
        return self._x
    @property
    def ypos(self):
        return self._y
    @property
    def state(self):
        return self._state
    @property
    def nbs(self):
        return self._nbs
    def __str__(self):
        return '[({0:}, {1:}), {2:}, {3:}]'.format(self._x, self._y, self._state, self._nbs)

class MinesweeperBoard:
    _row_regex = r'\|[\s\*]+\|'
    _hbnd_regex = r'^\+-+\+$'
    @classmethod
    def is_valid(cls, inp):
        if not (isinstance(inp, list) and all(isinstance(r, str) for r in inp)):
            raise ValueError('Input is not a list of strings')
        elif not all(len(r) == len(inp[0]) for r in inp):
            raise ValueError('Input has uneven rows')
        elif not (match(cls._hbnd_regex, inp[0]) and match(cls._hbnd_regex, inp[-1])
                  and all(match(cls._row_regex, r) for r in inp[1:-1])):
            raise ValueError('Invalid boundary or invalid char found')
        else:
            pass
    def __init__(self, inp):
        try:
            MinesweeperBoard.is_valid(inp)
        except ValueError as e:
            raise e
        self._board = self.strlst_to_board(inp)
    def __str__(self):
        return '\n'.join(self.board_to_strlst(print_nbs=True))
    def __getitem__(self, row_col):
        row, col = row_col
        return self._board[row][col]
    def strlst_to_board(self, strlst):
        board = []
        for row in range(1, len(strlst)-1):
            board.append([])
            for col in range(1, len(strlst[row])-1):
                board[row-1].append(MinesweeperSpace(row, col, strlst[row][col], self.count_nbs(row, col, strlst)))
        return board
    def count_nbs(self, row, col, strlst):
        num_rows = len(strlst)
        num_cols = len(strlst[0])
        num_nbs = 0
        for l in strlst[max(0, row-1) : min(row+2, num_rows+1)]:
            nbs = l[max(0, col-1) : min(col+2, num_cols+1)]
            for n in nbs:
                num_nbs += 1 if n == '*' else 0
        return num_nbs
    def board_to_strlst(self, print_nbs=False):
        hbnd = '+' + '-'*len(self._board[0]) + '+'
        strlst = [hbnd]
        for row in self._board:
            rowstr = '|'
            for space in row:
                if not space.state:
                    rowstr += str(space.nbs) if space.nbs and print_nbs else ' '
                else:
                    rowstr += '*'
            rowstr += '|'
            strlst.append(rowstr)
        strlst.append(hbnd)
        return strlst


def board(inp):
    msboard = MinesweeperBoard(inp)
    return msboard.board_to_strlst(print_nbs=True)

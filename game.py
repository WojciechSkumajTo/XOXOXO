__all__ = ["Game"]


class Board():

    X = 'X'
    O = 'O'
    EMPTY = ' '

    def __init__(self):
        self._board = [Board.EMPTY] * 9

    def get(self):
        return self._board[:]

    def put(self, position, counter):
        assert counter in [Board.X, Board.O]
        assert position in range(9)

        if self._board[position] != Board.EMPTY:
            return False

        self._board[position] = counter
        return True

    def move_available(self):
        return Board.EMPTY in self._board


class Game():

    X = Board.X
    O = Board.O
    EMPTY = Board.EMPTY

    PLAYERS = [X, O]

    def __init__(self):
        self._board = Board()
        self._turn = Game.PLAYERS[0]
        self._end = False
        self._winner = None

    def get_end(self):
        return self._end

    def get_winner(self):
        return self._winner

    def get_turn(self):
        return self._turn

    def get_board(self):
        return self._board.get()

    def get_turn_no(self):
        return Game.PLAYERS.index(self._turn)

    def check_winner(self):
        b = self._board.get()
        winning_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 6],
            [2, 4, 6],
        ]

        for i in winning_positions:
            if b[i[0]] == b[i[1]] and b[i[1]] == b[i[2]] and not b[i[0]] == Game.EMPTY:
                return True
            return False

    def make_move(self, position):
        assert position in range(9)

        if self._end:
            return False

        if not self._board.put(position, self._turn):
            return False

        if self.check_winner():
            self._winner = self._turn
            self._end = True
            return True

        if not self._board.move_available():
            self._end = True
            return True

        if self._turn == Game.PLAYERS[0]:
            self._turn = Game.PLAYERS[1]
        else:
            self._turn = Game.PLAYERS[0]

        return True

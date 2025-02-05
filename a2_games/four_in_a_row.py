'''
Four in a row

Author: Tony Lindgren
'''
from copy import deepcopy


class FourInARow:
    def __init__(self, player, chip):
        new_board = []
        for _ in range(7):
            new_board.append([])
        self.board = new_board
        self.action = list(range(7))
        if chip != 'r' and chip != 'w':
            print('The provided value is not a valid chip (must be, r or w): ', chip)
        if player == 'human' and chip == 'w':
            self.ai_player = 'r'
        else:
            self.ai_player = 'w'
        self.curr_move = chip

    def to_move(self):
        return self.curr_move

    # actions
    def actions(self):
        legal_actions = []
        for c in range(7):
            if len(self.board[c]) < 6:
                legal_actions.append(c)
        return legal_actions

    def result(self, action):
        dc = deepcopy(self)
        if self.to_move() == 'w':
            dc.curr_move = 'r'
            dc.board[action].append(self.to_move())
        else:
            dc.curr_move = 'w'
            dc.board[action].append(self.to_move())
        return dc

    def eval(self):

        h_value = 0

        matrix = [[0, 1, 2, 2, 1, 0],
                  [1, 2, 3, 3, 2, 1],
                  [2, 3, 4, 4, 3, 2],
                  [3, 4, 5, 5, 4, 3],
                  [2, 3, 4, 4, 3, 2],
                  [1, 2, 3, 3, 2, 1],
                  [0, 1, 2, 2, 1, 0]]

        for c in range(7):
            for r in range(len(self.board[c])):
                if self.board[c][r] == self.ai_player:
                    h_value += matrix[c][r]

        return h_value

    def is_terminal(self):
        # check vertical
        for c in range(0, len(self.board)):
            count = 0
            curr_chip = None
            for r in range(0, len(self.board[c])):
                if curr_chip == self.board[c][r]:
                    count = count + 1
                else:
                    curr_chip = self.board[c][r]
                    count = 1
                if count == 4:
                    if self.ai_player == curr_chip:
                        # print('Found vertical win')
                        return True, 100  # MAX ai wins positive utility
                    else:
                        # print('Found vertical loss')
                        return True, -100  # MIN player wins negative uti

        # check horizontal
        for r in range(0, len(self.board)-1):
            count = 0
            curr_chip = None
            curr_col = None
            for c in range(0, len(self.board)):
                if len(self.board[c]) > r:
                    if curr_chip == self.board[c][r] and curr_col+1 == c:
                        count += + 1
                        curr_col += 1
                    else:
                        curr_chip = self.board[c][r]
                        curr_col = c
                        count = 1
                    if count == 4:
                        if self.ai_player == curr_chip:
                            # print('Found horizontal win')
                            return True, 100  # MAX ai wins positive utility
                        else:
                            # print('Found horizontal loss')
                            return True, -100  # MIN player wins negative utility

        # check positive diagonal
        for c in range(7-3):
            for r in range(6-3):
                if len(self.board[c]) > r and len(self.board[c+1]) > r+1 and len(self.board[c+2]) > r+2 and len(self.board[c+3]) > r+3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c+1][r+1] and self.ai_player == self.board[c+2][r+2] and self.ai_player == self.board[c+3][r+3]:
                        # print('Found positive diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c+1][r+1] and self.ai_player != self.board[c+2][r+2] and self.ai_player != self.board[c+3][r+3]:
                        # print('Found positive diagonal loss')
                        return True, -100

        # check negative diagonal
        for c in range(4):
            for r in range(3, 6):
                if len(self.board[c]) > r and len(self.board[c+1]) > r-1 and len(self.board[c+2]) > r-2 and len(self.board[c+3]) > r-3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c+1][r-1] and self.ai_player == self.board[c+2][r-2] and self.ai_player == self.board[c+3][r-3]:
                        # print('Found negative diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c+1][r-1] and self.ai_player != self.board[c+2][r-2] and self.ai_player != self.board[c+3][r-3]:
                        # print('Found negative diagonal loss')
                        return True, -100

        # check draw
        for c in range(0, len(self.board)):
            if len(self.board[c]) < 6:
                return False, 0
        return True, 0

    def pretty_print_orig(self):
        for r in range(0, len(self.board)-1):  # Rad
            row_str = ""
            for c in range(0, len(self.board)):  # Kolumn
                if len(self.board[c]) > r:
                    row_str += self.board[c][r] + " "
                else:
                    row_str += "- "
            print(row_str)

    def pretty_print1(self):
        for c in range(0, len(self.board)):  # Rad
            row_str = ""
            for r in range(len(self.board)-1, 0):  # Kolumn
                if len(self.board[c]) > r:
                    row_str += self.board[c][r] + " "
                else:
                    row_str += "- "
            print(row_str)

    def pretty_print(self):
        list_row = []
        for r in range(0, len(self.board)-1):  # Rad
            row_str = ""
            for c in range(0, len(self.board)):  # Kolumn
                if len(self.board[c]) > r:
                    row_str += self.board[c][r] + " "
                else:
                    row_str += "_ "

            list_row.append(row_str)

        for i in list_row[::-1]:
            print(i)

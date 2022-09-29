import numpy as np


class Board:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.data = np.zeros((rows, cols))

    def drop_piece(self, row, col, piece) -> None:
        self.data[row][col] = piece

    def is_valid_location(self, col) -> bool:
        return self.data[self.rows - 1][col] == 0

    def get_next_open_row(self, col) -> int:
        for r in range(self.rows):
            if self.data[r][col] == 0:
                return r

    def print(self) -> None:
        print(np.flip(self.data, 0))

    def winning_move(self, piece) -> bool:
        # Check horizontal locations for win
        for c in range(self.cols - 3):
            for r in range(self.rows):
                if self.data[r][c] == piece and self.data[r][c + 1] == piece and self.data[r][c + 2] == piece and self.data[r][c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if self.data[r][c] == piece and self.data[r + 1][c] == piece and self.data[r + 2][c] == piece and self.data[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(self.cols - 3):
            for r in range(self.rows - 3):
                if self.data[r][c] == piece and self.data[r + 1][c + 1] == piece and self.data[r + 2][c + 2] == piece and self.data[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(self.cols - 3):
            for r in range(3, self.rows):
                if self.data[r][c] == piece and self.data[r - 1][c + 1] == piece and self.data[r - 2][c + 2] == piece and self.data[r - 3][c + 3] == piece:
                    return True

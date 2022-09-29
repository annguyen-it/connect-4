import math
import sys
import pygame
import pygame.event
from board import Board
from const import BLACK, BLUE, COLUMN_COUNT, HEIGHT, RADIUS, RED, ROW_COUNT, SQUARE_SIZE, WIDTH, YELLOW
from graphics import Graphics


class Game:
    def __init__(self) -> None:
        self.game_over = False
        self.turn = 0

        self.graphics = Graphics()
        self.board = Board(ROW_COUNT, COLUMN_COUNT)
        self.draw_board()
        self.graphics.update()

    def start(self) -> None:
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    self.graphics.rect(BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                    pos_x = event.pos[0]
                    if self.turn == 0:
                        self.graphics.circle(
                            RED,
                            (pos_x, int(SQUARE_SIZE/2)),
                            RADIUS
                        )
                    else:
                        self.graphics.circle(
                            YELLOW,
                            (pos_x, int(SQUARE_SIZE/2)),
                            RADIUS
                        )
                self.graphics.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.graphics.rect(BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                    # print(event.pos)
                    # Ask for Player 1 Input
                    if self.turn == 0:
                        pos_x = event.pos[0]
                        col = int(math.floor(pos_x / SQUARE_SIZE))

                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col)
                            self.board.drop_piece(row, col, 1)

                            if self.board.winning_move(1):
                                self.graphics.render(
                                    "Player 1 wins!!",
                                    RED,
                                    (40, 10)
                                )
                                self.game_over = True

                    # # Ask for Player 2 Input
                    else:
                        pos_x = event.pos[0]
                        col = int(math.floor(pos_x/SQUARE_SIZE))

                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col)
                            self.board.drop_piece(row, col, 2)

                            if self.board.winning_move(2):
                                self.graphics.render(
                                    "Player 2 wins!!",
                                    YELLOW,
                                    (40, 10)
                                )
                                self.game_over = True

                    self.board.print()
                    self.draw_board()

                    self.turn += 1
                    self.turn = self.turn % 2

                    if self.game_over:
                        self.graphics.wait(3000)

    def draw_board(self) -> None:
        for col in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                self.graphics.rect(
                    BLUE,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE +
                     SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                )
                self.graphics.circle(
                    BLACK,
                    (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                     int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)),
                    RADIUS
                )

        for col in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                cell = self.board.data[row][col]
                if cell == 1:
                    self.graphics.circle(
                        RED,
                        (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                         HEIGHT-int(row * SQUARE_SIZE + SQUARE_SIZE / 2)),
                        RADIUS
                    )
                elif cell == 2:
                    self.graphics.circle(
                        YELLOW,
                        (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                         HEIGHT-int(row * SQUARE_SIZE + SQUARE_SIZE / 2)),
                        RADIUS
                    )
        self.graphics.update()

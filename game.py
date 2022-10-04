import math
import sys
import time
import pygame
import pygame.event
from const import AI_LEVEL, AI_NAME, BLACK, BLUE, COLUMN_COUNT, HEIGHT, PLAY_WITH_AI, PLAYER1_COLOR, PLAYER1_NAME, PLAYER2_COLOR, PLAYER2_NAME, RADIUS, RED, ROW_COUNT, SQUARE_SIZE, WIDTH, YELLOW
from ai import AI
from board import Board
from graphics import Color, Graphics


class Game:
    def __init__(self) -> None:
        self.game_over = False
        self.turn = 1

        self.graphics = Graphics()
        self.board = Board(ROW_COUNT, COLUMN_COUNT)
        self.draw_board()
        self.graphics.update()
        self.player1_name = PLAYER1_NAME
        self.player2_name = AI_NAME if PLAY_WITH_AI else PLAYER2_NAME
        if PLAY_WITH_AI:
            self.ai = AI(self.board, AI_LEVEL)

    def start(self) -> None:
        while not self.game_over:
            if PLAY_WITH_AI and self.turn == 2:
                self.graphics.render(
                    "AI is thinking...",
                    PLAYER2_COLOR,
                    (40, 10)
                )
                print('AI')
                col, _ = self.ai.generateDecision()
                self.graphics.rect(BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                self.place(2, col)
                pygame.event.clear()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                    if event.type == pygame.MOUSEMOTION:
                        self.graphics.rect(BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                        pos_x = event.pos[0]
                        if self.turn == 1:
                            self.graphics.circle(
                                RED,
                                (pos_x, int(SQUARE_SIZE/2)),
                                RADIUS
                            )
                        elif not PLAY_WITH_AI:
                            self.graphics.circle(
                                YELLOW,
                                (pos_x, int(SQUARE_SIZE/2)),
                                RADIUS
                            )
                    self.graphics.update()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(event)
                        if PLAY_WITH_AI:
                            if self.turn == 1:
                                self.click(pos_x)
                        else:
                            self.click(pos_x)
            if self.game_over:
                self.graphics.wait(3000)

    def click(self, x: int) -> None:
        self.graphics.rect(
            BLACK, (0, 0, WIDTH, SQUARE_SIZE))
        col = int(math.floor(x / SQUARE_SIZE))
        self.place(self.turn, col)

    def place(self, player: int, col: int) -> bool:
        if self.board.is_valid_location(col):
            self.board.drop_piece(col, player)

            if self.board.winning_move(player):
                self.graphics.render(
                    "{} wins!".format(self.getName(player)),
                    Game.getColor(player),
                    (40, 10)
                )
                self.game_over = True
        else:
            return False
        self.board.print()
        self.draw_board()

        self.turn = 1 if self.turn == 2 else 2
        return True

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

    def getName(self, player: int) -> str:
        return self.player1_name if player == 1 else self.player2_name

    def getColor(player: int) -> Color:
        if player == 1:
            return PLAYER1_COLOR
        return PLAYER2_COLOR

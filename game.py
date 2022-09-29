import math
import sys
import pygame
import pygame.display
import pygame.event
import pygame.font
import pygame.draw
from board import Board
from const import BLACK, BLUE, COLUMN_COUNT, HEIGHT, RADIUS, RED, ROW_COUNT, SIZE, SQUARE_SIZE, WIDTH, YELLOW


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.board = Board()
        self.screen = pygame.display.set_mode(SIZE)
        self.game_over = False
        self.font = pygame.font.SysFont("monospace", 75)
        self.draw_board()
        pygame.display.update()

    def start(self) -> None:
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, BLACK,
                                     (0, 0, WIDTH, SQUARE_SIZE))
                    pos_x = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(
                            self.screen, RED, (pos_x, int(SQUARE_SIZE/2)), RADIUS)
                    else:
                        pygame.draw.circle(
                            self.screen, YELLOW, (pos_x, int(SQUARE_SIZE/2)), RADIUS)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, BLACK,
                                     (0, 0, WIDTH, SQUARE_SIZE))
                    # print(event.pos)
                    # Ask for Player 1 Input
                    if turn == 0:
                        pos_x = event.pos[0]
                        col = int(math.floor(pos_x/SQUARE_SIZE))

                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col)
                            self.board.drop_piece(row, col, 1)

                            if self.board.winning_move(1):
                                label = self.font.render(
                                    "Player 1 wins!!", 1, RED)
                                self.screen.blit(label, (40, 10))
                                game_over = True

                    # # Ask for Player 2 Input
                    else:
                        pos_x = event.pos[0]
                        col = int(math.floor(pos_x/SQUARE_SIZE))

                        if self.board.is_valid_location(col):
                            row = self.board.get_next_open_row(col)
                            self.board.drop_piece(row, col, 2)

                            if self.board.winning_move(2):
                                label = self.font.render(
                                    "Player 2 wins!!", 1, YELLOW)
                                self.screen.blit(label, (40, 10))
                                game_over = True

                    self.board.print()
                    self.draw_board()

                    turn += 1
                    turn = turn % 2

                    if game_over:
                        pygame.time.wait(3000)

    def draw_board(self) -> None:
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(
                    self.screen,
                    BLUE,
                    (c * SQUARE_SIZE, r * SQUARE_SIZE +
                     SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                )
                pygame.draw.circle(
                    self.screen,
                    BLACK,
                    (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                     int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)),
                    RADIUS
                )

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                cell = self.board.data[r][c]
                if cell == 1:
                    pygame.draw.circle(
                        self.screen,
                        RED,
                        (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                         HEIGHT-int(r * SQUARE_SIZE + SQUARE_SIZE / 2)),
                        RADIUS
                    )
                elif cell == 2:
                    pygame.draw.circle(
                        self.screen,
                        YELLOW,
                        (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                         HEIGHT-int(r * SQUARE_SIZE + SQUARE_SIZE / 2)),
                        RADIUS
                    )
        pygame.display.update()

import pygame
import pygame.display
import pygame.font
import pygame.draw
import pygame.time
from typing import Sequence, Tuple
from const import SIZE

Color = Tuple[int, int, int]

class Graphics:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        self.font = pygame.font.SysFont("monospace", 75)

    def update(self) -> None:
        pygame.display.update()

    def rect(self, color: Color, rect: Tuple[int, int, int, int]) -> None:
        pygame.draw.rect(self.screen, color, rect)

    def circle(self, color: Color, center: Tuple[float, float], radius: float) -> None:
        pygame.draw.circle(self.screen, color, center, radius)

    def render(self, text: str, color: Color, dest: Sequence[float]) -> None:
        label = self.font.render(text, True, color)
        self.screen.blit(label, dest)

    def wait(self, milliseconds: int) -> None:
        pygame.time.wait(milliseconds)

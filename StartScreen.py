import pygame
import random
import sys

# Skärmkonstanter
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 30


def start_screen(screen):
    """
    Startskärm för spelet.
    Visar introduktionstext och väntar på tangenttryckning för att starta spelet.
    """
    font = pygame.font.Font(None, FONT_SIZE)
    screen.fill(BLACK)
    intro_text = get_intro_text()

    y_position = HEIGHT // 4
    for line in intro_text:
        text = font.render(line, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, y_position))
        screen.blit(text, text_rect)
        y_position += FONT_SIZE

    pygame.display.flip()
    wait_for_key()


def get_intro_text():
    """
    Returnerar introduktionstexten för spelet.
    """
    return [
        "Välkommen, Alien Abductor!",
        # ... Resten av texten ...
        "Tryck på valfri tangent för att starta spelet...",
    ]


def wait_for_key():
    """
    Väntar på en tangenttryckning för att fortsätta.
    Avslutar spelet om QUIT-event inträffar.
    """
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

# Resten av din kod...

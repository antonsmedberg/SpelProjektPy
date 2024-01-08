import pygame
import random
import sys
from GameOverScreen import game_over_screen

# Initialiserar Pygame
pygame.init()

# Skärmkonstanter
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 30

# Skapar ett fönster
main_screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Changed variable name to 'main_screen'
pygame.display.set_caption("Spelets Startsida")

def start_screen(screen_to_use):
    """
    Visar startskärmen för spelet.
    Presenterar introduktionstext och väntar på användarens tangenttryckning för att påbörja spelet.
    """
    font = pygame.font.Font(None, FONT_SIZE)
    screen_to_use.fill(BLACK)  # Changed to 'screen_to_use'
    intro_text = get_intro_text()

    y_position = HEIGHT // 4
    for line in intro_text:
        text = font.render(line, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, y_position))
        screen_to_use.blit(text, text_rect)  # Changed to 'screen_to_use'
        y_position += FONT_SIZE

    pygame.display.flip()
    wait_for_key()


def get_intro_text():
    """
    Skapar och returnerar introduktionstexten för spelet.
    """
    return [
        "Välkommen, Alien Abductor!",
        # ... Fortsättning på texten ...
        "Tryck på valfri tangent för att starta spelet...",
    ]


def wait_for_key():
    """
    Väntar på att användaren trycker på en tangent. Avslutar spelet om användaren stänger fönstret.
    """
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


# Starta startskärmen
start_screen(main_screen)  # Changed argument to 'main_screen'

# Spelvariabler
score = 0  # Initialiserar poängen
running = True

# Huvudspelslingan
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Här kommer spellogiken
        # Uppdatera poängen vid behov

    # Kontrollera om spelet är över
    # if game_over_condition:
    #     running = False

# Visa game over-skärmen med slutpoängen
game_over_screen(main_screen, score)  # Updated to use 'main_screen'

# Stänger Pygame
pygame.quit()

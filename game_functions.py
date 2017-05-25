import sys

import pygame

def check_events(ship):
    """Reakcja na zdarzenia generowane przez klawiature i mysz"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Uaktualnienie obrazow na ekranie i przejscie do nowego ekranu."""
    # Odswiezenie ekranu w trakcie kazdej iteracji petli
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Wyswietlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()
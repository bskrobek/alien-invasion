import sys

import pygame
from settings import Settings
from ship import Ship

def run_game():
    #Inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    #Utworzenie statku kosmicznego
    ship = Ship(screen)

    #Rozpoczecie petli glownej gry
    while True:

        #Oczekiwanie na nacisniecie klawisza lub przycisku myszy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Odswiezenie ekranu w trakcie kazdej iteracji petli
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Wyswietlanie ostatnio zmodyfikowanego ekranu
        pygame.display.flip()

run_game()
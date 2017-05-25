import pygame

class Ship():

    def __init__(self, ai_settings,  screen):
        """Inicjalizacja statku kosmicznego i jego polozenie poczatkowe"""
        self.screen = screen
        self.ai_settings = ai_settings

        #Wczytanie obrazu statku kosmicznego i pobranie jego prostokata
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Kazdy nowy statek kosmiczny pojawia sie na dole ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Punkt srodkowy statku jest przechowywany w postaci liczby zmiennoprzecinkowej.
        self.center = float(self.rect.centerx)

        #Opcje wskazujace na poruszanie sie statku
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Uaktualnienie polozenia statku na podstawie opcji
        wskazujacej ne jego ruch
        """

        # Uaktualnienie wartosci punku srodkowego statku, a nie jego prostokata.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # Uaktualnienie obieku rect na podstawie wartosci self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Wyswietlanie statku kosmicznego w jego aktualnym polozeniu"""
        self.screen.blit(self.image, self.rect)
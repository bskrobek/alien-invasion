import pygame

class Ship():

    def __init__(self, screen):
        """Inicjalizacja statku kosmicznego i jego polozenie poczatkowe"""
        self.screen = screen

        #Wczytanie obrazu statku kosmicznego i pobranie jego prostokata
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Kazdy nowy statek kosmiczny pojawia sie na dole ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Wyswietlanie statku kosmicznego w jego aktualnym polozeniu"""
        self.screen.blit(self.image, self.rect)
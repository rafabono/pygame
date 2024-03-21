import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Representa a un solo alienígena en la flota"""
    def __init__(self, ai_configuraciones, pantalla):
        """Inicializa el alien y establece su posición inicial"""
        super(Alien, self).__init__()
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Carga la imagen de la nave y obtiene su rect
        self.imagen = pygame.image.load("imagenes/alien_julia.bmp")
        # Pygame trata las imágenes como rectángulos, por lo que debemos obtener el atributo rectángulo de la imagen.
        self.rect = self.imagen.get_rect()    

        # Inicia cada nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width  
        self.rect.y = self.rect.height

        # Almacena la posición exacta del alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibuja el alien en su posición actual"""
        self.pantalla.blit(self.imagen, self.rect)        
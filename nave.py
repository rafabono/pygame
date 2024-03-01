import pygame

class Nave():
    """Gestiona el comportamiento de la nave en el juego"""

    def __init__(self, ai_configuraciones, pantalla):
        """Inicializa la nave y establece posición de partida"""
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Carga la imagen de la nave y obtiene su rect
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        # Pygame trata las imágenes como rectángulos, por lo que debemos obtener el atributo rectángulo de la imagen.
        self.rect = self.imagen.get_rect()
        # Almacenamos en pantalla_rect el rect de la pantalla
        self.pantalla_rect = pantalla.get_rect()

        # Empieza cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom

        # Almacenamos centro con tipo float
        self.center = float(self.rect.centerx)

        # Bandera de movimiento
        self.moving_right = False
        self.moving_left = False

        

    def update(self):
        """Actuliza posición de la nave"""
        
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.ai_configuraciones.factor_velocidad_nave
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_configuraciones.factor_velocidad_nave
        # Actualizamos la propiedad centerx de rect de la nave con el valor obtenido según el movimiento
        self.rect.centerx = self.center

    def blitme(self):
        """Dibuja la nave en su posición actual"""
        self.pantalla.blit(self.imagen, self.rect)
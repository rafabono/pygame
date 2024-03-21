import pygame
# Importamos Group de pygame para poder agrupar las balas
from pygame.sprite import Group
# Importamos la clase Configuraciones
from configuraciones import Configuraciones
# Importamos la clase Nave
from nave import Nave
# Importamos la clase Alien
from alien import Alien
# Importamos funciones_juego
import funciones_juego as fj

def run_game():
    # Inicializa juego y crea objeto pantalla
    pygame.init()
    # Se instancia un objeta de la clase configuraciones
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode(
        (ai_configuraciones.screen_width,ai_configuraciones.screen_height))
    pygame.display.set_caption("Invasión alienígena")

    # Crea una nave. Importante, debe ir fuera del bucle while
    nave = Nave(ai_configuraciones, pantalla)
    # Crea un grupo para almacenar las balas
    balas = Group()
    # Crae un alien.
    alien = Alien(ai_configuraciones, pantalla)

    # Bucle principal del juego
    while True:
        
        # Escucha eventos de teclado o ratón
        fj.verificar_eventos(ai_configuraciones, pantalla, nave, balas)
        nave.update()
        # Actualiza balas y elimina las que salen de pantalla
        fj.update_balas(balas)
        # Verficamos el numero de balas que hay en la pantalla
        #print(len(balas))
        # Llama a la función para actualizar la pantalla
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave, alien, balas)

run_game()
import pygame
# Importamos Group de pygame para poder agrupar las balas
from pygame.sprite import Group
# Importamos la clase Configuraciones
from configuraciones import Configuraciones
# Importamos la clase Nave
from nave import Nave
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
    # Bucle principal del juego
    while True:
        
        # Escucha eventos de teclado o ratón
        fj.verificar_eventos(ai_configuraciones, pantalla, nave, balas)
        nave.update()
        # El método update del grupo balas llama al método update de cada bala
        balas.update()
        # Deshace las balas que han desparecido de la pantalla, para no consumir recursos
        fj.elimina_balas(balas)
        # Verficamos el numero de balas que hay en la pantalla
        #print(len(balas))
        # Llama a la función para actualizar la pantalla
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave, balas)



run_game()
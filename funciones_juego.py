import sys
import pygame
from bala import Bala

def verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas):
    if event.key==pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key==pygame.K_LEFT:
        nave.moving_left = True
    elif event.key==pygame.K_SPACE:
        fuego_bala(ai_configuraciones, pantalla, nave, balas)
    elif event.key==pygame.K_q:
        sys.exit()


def verificar_eventos_keyup(event, nave):
    if event.key==pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key==pygame.K_LEFT:
        nave.moving_left = False

def verificar_eventos(ai_configuraciones, pantalla, nave, balas):
    """Responde a las pulsaciones de teclas y movimientos del ratón"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas)
        elif event.type==pygame.KEYUP:
            verificar_eventos_keyup(event,nave)

def actualizar_pantalla(ai_configuraciones, pantalla, nave, balas):
    """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla"""
    # Rellenamos del color de fondo la pantalla
    pantalla.fill(ai_configuraciones.bg_color)
    # Vuelve a dibujar todas las balas detrás de la nave y los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    # Invocamos al método que pinta la nave
    nave.blitme()
    # Hace visible la pantalla dibujada más reciente
    pygame.display.flip()    

def update_balas(balas):
    """Actualiza posicion de las balas y elimina las balas que se salen de la pantalla para evitar que consuman recursos"""
    # El método update del grupo balas llama al método update de cada bala
    balas.update()
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

def fuego_bala(ai_configuraciones, pantalla, nave, balas):
    """Dispara una bala si aún no ha alcanzado el límite"""
    # Crea una nueva bala y la añade al grupo balas
    if len(balas) < ai_configuraciones.balas_allowed:
        nueva_bala = Bala(ai_configuraciones,pantalla,nave)
        balas.add(nueva_bala)
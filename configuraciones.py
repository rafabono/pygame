class Configuraciones():
    """Almacena las configuraciones del juego"""

    def __init__(self):
        """Inicializa las configuraciones del juego"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # Configuracion de la nave
        self.factor_velocidad_nave = 0.5

        # Configuración de la baja
        self.factor_velocidad_bala = 0.8
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = 60, 60, 60
        self.balas_allowed = 5
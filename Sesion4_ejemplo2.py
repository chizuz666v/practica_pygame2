import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación de pulsación")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 80, 80)

# Parámetros del círculo
x = ANCHO // 2
y = ALTO // 2
radio = 20
min_radio = 20
max_radio = 50
creciendo = True  # Estado: True = crece, False = se encoge
velocidad_radio = 1  # Qué tan rápido cambia el tamaño

# Control de FPS
clock = pygame.time.Clock()
FPS = 60

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar el radio (efecto de pulsación)
    if creciendo:
        radio += velocidad_radio
        if radio >= max_radio:
            creciendo = False
    else:
        radio -= velocidad_radio
        if radio <= min_radio:
            creciendo = True

    # Dibujar
    ventana.fill(NEGRO)
    pygame.draw.circle(ventana, ROJO, (x, y), radio)

    # Actualizar la pantalla
    pygame.display.flip()

    # Mantener animación fluida a 60 FPS
    clock.tick(FPS)
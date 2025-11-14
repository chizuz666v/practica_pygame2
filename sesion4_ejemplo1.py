import pygame
import sys

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rebote con velocidad variable")

# Colores
NEGRO = (0, 0, 0)
AZUL = (0, 120, 255)

# Propiedades del círculo
radio = 30
x = ANCHO // 2
y = ALTO // 2
velocidad_x = 5
velocidad_y = 4
aceleracion = 0.1  # incremento de velocidad en cada rebote

# Control de FPS
clock = pygame.time.Clock()
FPS = 60

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover el círculo
    x += velocidad_x
    y += velocidad_y

    # Rebote horizontal
    if x - radio <= 0 or x + radio >= ANCHO:
        velocidad_x = -velocidad_x
        # Aumenta un poco la magnitud (velocidad absoluta)
        if velocidad_x > 0:
            velocidad_x += aceleracion
        else:
            velocidad_x -= aceleracion

    # Rebote vertical
    if y - radio <= 0 or y + radio >= ALTO:
        velocidad_y = -velocidad_y
        if velocidad_y > 0:
            velocidad_y += aceleracion
        else:
            velocidad_y -= aceleracion

    # Dibujar todo
    ventana.fill(NEGRO)
    pygame.draw.circle(ventana, AZUL, (int(x), int(y)), radio)
    pygame.display.flip()

    # Mantener 60 cuadros por segundo
    clock.tick(FPS)
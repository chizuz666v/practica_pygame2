import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulación de Gravedad")

# Colores
NEGRO = (0, 0, 0)
AZUL = (100, 180, 255)

# Propiedades del círculo
radio = 30
x = ANCHO // 2
y = radio
vel_y = 0  # velocidad vertical inicial
gravedad = 0.5  # aceleración por frame
perdida_energia = 0.8  # conserva el 80% de la velocidad después del rebote

# Control de FPS
clock = pygame.time.Clock()
FPS = 60

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Aplicar gravedad (incrementa velocidad hacia abajo)
    vel_y += gravedad
    y += vel_y

    # Detectar colisión con el suelo
    if y + radio >= ALTO:
        y = ALTO - radio  # corregir posición
        vel_y = -vel_y * perdida_energia  # invertir dirección y perder energía

        # Si la velocidad es muy baja, detener (simula descanso)
        if abs(vel_y) < 1:
            vel_y = 0

    # Dibujar escena
    ventana.fill(NEGRO)
    pygame.draw.circle(ventana, AZUL, (int(x), int(y)), radio)
    pygame.display.flip()

    # Mantener 60 FPS
    clock.tick(FPS)
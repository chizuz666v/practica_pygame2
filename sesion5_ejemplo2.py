import pygame
import sys
import os

# ============================
#      sesion5_ej2.py
#  Sprite animado (2 frames)
# ============================

pygame.init()

# Ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sprite animado - Kris caminando")

clock = pygame.time.Clock()

# ============================
#   Cargar imágenes del sprite
# ============================

ruta1 = os.path.join("sprites", "kris_caminando1.png")
ruta2 = os.path.join("sprites", "kris_caminando2.png")

# Verificar si existen
if not os.path.exists(ruta1):
    print("ERROR: No se encuentra:", ruta1)
    pygame.quit()
    sys.exit()

if not os.path.exists(ruta2):
    print("ERROR: No se encuentra:", ruta2)
    pygame.quit()
    sys.exit()

# Cargar imágenes
frame1 = pygame.image.load(ruta1).convert_alpha()
frame2 = pygame.image.load(ruta2).convert_alpha()

# Lista de frames
frames = [frame1, frame2]
indice_frame = 0

# Tiempo entre animaciones
tiempo_cambio = 100     # ms por frame
ultimo_cambio = pygame.time.get_ticks()

# ============================
#       Bucle principal
# ============================

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Control del tiempo para cambiar de frame
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_cambio >= tiempo_cambio:
        indice_frame = (indice_frame + 1) % 2   # alterna 0 → 1 → 0 → 1...
        ultimo_cambio = tiempo_actual

    # Frame actual
    frame_actual = frames[indice_frame]
    ancho, alto = frame_actual.get_size()

    # Fondo
    ventana.fill((20, 20, 20))

    # Dibujar sprite al centro
    x = (ANCHO - ancho) // 2
    y = (ALTO - alto) // 2
    ventana.blit(frame_actual, (x, y))

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
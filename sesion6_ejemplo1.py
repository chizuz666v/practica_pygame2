import pygame
import sys

pygame.init()

# Ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Colisión con cambio de color")

clock = pygame.time.Clock()

# Rectángulo del jugador
player = pygame.Rect(100, 100, 60, 60)
color_player = (255, 0, 0)  # rojo

# Rectángulo objetivo
objetivo = pygame.Rect(500, 300, 80, 80)
color_objetivo = (0, 0, 255)  # azul

vel = 5

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimiento del jugador
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        player.x += vel
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        player.x -= vel
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        player.y -= vel
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        player.y += vel

    # --- Colisión ---
    if player.colliderect(objetivo):
        color_player = (0, 255, 0)  # verde
    else:
        color_player = (255, 0, 0)  # rojo normal

    ventana.fill((30, 30, 30))

    # Dibujar
    pygame.draw.rect(ventana, color_player, player)
    pygame.draw.rect(ventana, color_objetivo, objetivo)

    pygame.display.flip()
    clock.tick(60)
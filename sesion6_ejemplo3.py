import pygame
import sys
import random

pygame.init()

# -----------------------------------
# CONFIGURACIÓN DE VENTANA
# -----------------------------------
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Evitar Obstáculos - Sesión 6 Ejercicio 3")

clock = pygame.time.Clock()

# -----------------------------------
# JUGADOR
# -----------------------------------
player = pygame.Rect(100, 250, 60, 60)
vel_player = 5
color_player = (0, 150, 255)

# -----------------------------------
# OBSTÁCULOS (CÍRCULOS)
# -----------------------------------
num_obstaculos = 5
radio = 25
obstaculos = []

for _ in range(num_obstaculos):
    x = random.randint(radio, ANCHO - radio)
    y = random.randint(radio, ALTO - radio)
    vel = random.choice([3, 4, 5])
    obstaculos.append([x, y, vel])

# -----------------------------------
# REINICIAR JUEGO
# -----------------------------------
def reiniciar_juego():
    global player, obstaculos

    player.x, player.y = 100, 250
    obstaculos = []
    for _ in range(num_obstaculos):
        x = random.randint(radio, ANCHO - radio)
        y = random.randint(radio, ALTO - radio)
        vel = random.choice([3, 4, 5])
        obstaculos.append([x, y, vel])


# -----------------------------------
# COLISIÓN CÍRCULO - RECTÁNGULO
# -----------------------------------
def colision_rect_circulo(rect, cx, cy, r):
    # Puntos más cercanos del rectángulo al círculo
    mas_cercano_x = max(rect.left, min(cx, rect.right))
    mas_cercano_y = max(rect.top, min(cy, rect.bottom))

    # Distancia entre ese punto y el centro del círculo
    distancia = ((cx - mas_cercano_x)**2 + (cy - mas_cercano_y)**2)**0.5

    return distancia < r


# -----------------------------------
# BUCLE PRINCIPAL
# -----------------------------------
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimiento del jugador
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        player.y -= vel_player
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        player.y += vel_player
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        player.x -= vel_player
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        player.x += vel_player

    # Limitar movimiento a la ventana
    player.x = max(0, min(player.x, ANCHO - player.width))
    player.y = max(0, min(player.y, ALTO - player.height))

    # Mover obstáculos
    for obs in obstaculos:
        obs[0] += obs[2]  # mover en x

        # Rebotar en bordes horizontales
        if obs[0] - radio <= 0 or obs[0] + radio >= ANCHO:
            obs[2] *= -1

        # Revisar colisión con el jugador
        if colision_rect_circulo(player, obs[0], obs[1], radio):
            reiniciar_juego()

    # Dibujar
    ventana.fill((30, 30, 30))

    # Dibujar jugador
    pygame.draw.rect(ventana, color_player, player)

    # Dibujar obstáculos
    for obs in obstaculos:
        pygame.draw.circle(ventana, (255, 70, 70), (obs[0], obs[1]), radio)

    pygame.display.flip()
    clock.tick(60)
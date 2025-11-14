import pygame
import sys
import random

pygame.init()

# Ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Recolección de Objetos")

clock = pygame.time.Clock()

# Jugador (rectángulo)
player = pygame.Rect(100, 100, 60, 60)
vel = 5
color_player = (255, 0, 0)

# Objeto a recoger (círculo)
radio = 20
obj_x = random.randint(radio, ANCHO - radio)
obj_y = random.randint(radio, ALTO - radio)
color_obj = (255, 255, 0)

# Contador
contador = 0
fuente = pygame.font.Font(None, 40)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimiento
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        player.x += vel
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        player.x -= vel
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        player.y -= vel
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        player.y += vel

    # Limitar dentro de la ventana
    player.x = max(0, min(player.x, ANCHO - player.width))
    player.y = max(0, min(player.y, ALTO - player.height))

    # Verificar colisión con el círculo
    distancia = ((player.centerx - obj_x) ** 2 + (player.centery - obj_y) ** 2) ** 0.5
    if distancia < radio + max(player.width, player.height) / 2:
        contador += 1
        # Crear nuevo círculo aleatorio
        obj_x = random.randint(radio, ANCHO - radio)
        obj_y = random.randint(radio, ALTO - radio)

    ventana.fill((30, 30, 30))

    # Dibujar jugador
    pygame.draw.rect(ventana, color_player, player)

    # Dibujar objeto
    pygame.draw.circle(ventana, color_obj, (obj_x, obj_y), radio)

    # Dibujar contador
    texto = fuente.render(f"Recolectados: {contador}", True, (255, 255, 255))
    ventana.blit(texto, (20, 20))

    pygame.display.flip()
    clock.tick(60)
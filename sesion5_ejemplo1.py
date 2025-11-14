import pygame
import sys
import os

# Inicializar Pygame
pygame.init()

# Configurar ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ajuste de tamaño dinámico")

# Ruta correcta a la imagen dentro de la carpeta "sprites"
ruta_imagen = os.path.join("sprites", "krissprite.png")

# Verificar si la imagen existe
if not os.path.exists(ruta_imagen):
    print("ERROR: No se encontró la imagen en:", ruta_imagen)
    pygame.quit()
    sys.exit()

# Cargar imagen
imagen_original = pygame.image.load(ruta_imagen).convert_alpha()
ancho_original, alto_original = imagen_original.get_size()

# Escala inicial
escala = 1.0
incremento = 0.1

# Control de FPS
clock = pygame.time.Clock()
FPS = 60

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Controles del teclado
        if evento.type == pygame.KEYDOWN:

            # Detectar "+" (teclado principal con Shift o teclado numérico)
            if evento.key == pygame.K_KP_PLUS or (evento.key == pygame.K_EQUALS and pygame.key.get_mods() & pygame.KMOD_SHIFT):
                escala += incremento

            # Detectar "-"
            elif evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                escala -= incremento
                if escala < 0.1:
                    escala = 0.1

    # Calcular tamaño escalado
    nuevo_ancho = int(ancho_original * escala)
    nuevo_alto = int(alto_original * escala)

    # Redimensionar
    imagen_escalada = pygame.transform.smoothscale(imagen_original, (nuevo_ancho, nuevo_alto))

    # Dibujar en el centro
    ventana.fill((30, 30, 30))
    pos_x = (ANCHO - nuevo_ancho) // 2
    pos_y = (ALTO - nuevo_alto) // 2
    ventana.blit(imagen_escalada, (pos_x, pos_y))

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(FPS)
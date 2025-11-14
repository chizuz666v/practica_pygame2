import pygame
import sys
import os

pygame.init()

# --- Ventana ---
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Kris Direccional Animado")

clock = pygame.time.Clock()

# --- Función para cargar y ESCALAR imágenes ---
def cargar_imagen(nombre):
    ruta = os.path.join("sprites", nombre + ".png")

    if not os.path.exists(ruta):
        print("❌ ERROR: Falta la imagen:", ruta)
        return None

    img = pygame.image.load(ruta).convert_alpha()
    img = pygame.transform.scale(img, (60, 60))  # ← tamaño del personaje
    return img


# --- Cargar sprites por dirección ---
sprites = {
    "quieto": [
        cargar_imagen("kris_cansado")
    ],

    "abajo": [
        cargar_imagen("kris_caminandoDeFrente1")
    ],

    "derecha": [
        cargar_imagen("kris_caminando1"),
        cargar_imagen("kris_caminando2")
    ],

    "izquierda": [
        cargar_imagen("kris_caminandoAtras1"),
        cargar_imagen("kris_caminandoAtras2")
    ],

    "arriba": [
        cargar_imagen("kris_caminandoDeEspalda1"),
        cargar_imagen("kris_caminandoDeEspalda2"),
        cargar_imagen("kris_caminandoDeEspalda3")
    ]
}

# Verificación de imágenes faltantes
faltan = any(img is None for lista in sprites.values() for img in lista)

if faltan:
    print("\n❗ Soluciona los errores ANTES de continuar.")
    print("La ventana seguirá abierta.\n")

# --- Variables del personaje ---
x = ANCHO // 2
y = ALTO // 2
vel = 4

frame_index = 0
tiempo_cambio = 180
ultimo_tiempo = pygame.time.get_ticks()

direccion_actual = "quieto"
direccion_anterior = "quieto"  # ← para reiniciar animación al cambiar de dirección

# --- Bucle principal ---
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    moviendo = False

    # Movimiento / dirección
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        direccion_actual = "derecha"
        x += vel
        moviendo = True

    elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        direccion_actual = "izquierda"
        x -= vel
        moviendo = True

    elif teclas[pygame.K_w] or teclas[pygame.K_UP]:
        direccion_actual = "arriba"
        y -= vel
        moviendo = True

    elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        direccion_actual = "abajo"
        y += vel
        moviendo = True

    else:
        direccion_actual = "quieto"

    # Reiniciar animación si cambia la dirección
    if direccion_actual != direccion_anterior:
        frame_index = 0
        direccion_anterior = direccion_actual

    # Animación
    frames = sprites[direccion_actual]

    if None not in frames:
        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - ultimo_tiempo >= tiempo_cambio:
            frame_index = (frame_index + 1) % len(frames)
            ultimo_tiempo = tiempo_actual

        frame_actual = frames[frame_index]

        # --- ❗ LIMITAR MOVIMIENTO A LA VENTANA ---
        x = max(0, min(x, ANCHO - frame_actual.get_width()))
        y = max(0, min(y, ALTO - frame_actual.get_height()))

        ventana.fill((30, 30, 30))
        ventana.blit(frame_actual, (x, y))

    pygame.display.flip()
    clock.tick(60)
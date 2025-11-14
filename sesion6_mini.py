import pygame
import sys
import os
import random

pygame.init()

# --- Ventana ---
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Kris Mini Juego — Recolecta y Evita Obstáculos")

clock = pygame.time.Clock()

# --- Música ---
def cargar_musica(nombre):
    ruta = os.path.join("sprites", nombre + ".ogg")  # ← CORREGIDO: ahora usa .ogg

    if not os.path.exists(ruta):
        print("❌ Falta música:", ruta)
        return False

    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play(-1)  # 🔁 música en loop
    return True

cargar_musica("spamton_battle")

# --- Función para cargar imágenes ---
def cargar_imagen(nombre, tamaño=(60, 60)):
    extension = ".jpg" if nombre == "spamton_g" else ".png"
    ruta = os.path.join("sprites", nombre + extension)

    if not os.path.exists(ruta):
        print("❌ Falta imagen:", ruta)
        return None

    img = pygame.image.load(ruta).convert_alpha()
    return pygame.transform.scale(img, tamaño)

# --- Sprite del obstáculo ---
spamton_sprite = cargar_imagen("spamton_g", tamaño=(40, 40))

if spamton_sprite is None:
    print("⚠ Obstáculos usarán círculos porque falta la imagen.")

# --- Sprites del jugador ---
sprites = {
    "quieto": [cargar_imagen("kris_cansado")],
    "abajo": [cargar_imagen("kris_caminandoDeFrente1")],
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

# --- Jugador ---
x = ANCHO // 2
y = ALTO // 2
vel = 4
frame_index = 0
tiempo_cambio = 150
ultimo_tiempo = pygame.time.get_ticks()
direccion_actual = "quieto"
direccion_anterior = "quieto"

# --- Objeto a recolectar ---
radio_obj = 12
obj_x = random.randint(radio_obj, ANCHO - radio_obj)
obj_y = random.randint(radio_obj, ALTO - radio_obj)
puntos = 0

# --- Obstáculos ---
num_obstaculos = 5

def crear_obstaculos():
    lista = []
    for _ in range(num_obstaculos):
        ox = random.randint(0, ANCHO - 40)
        oy = random.randint(0, ALTO - 40)
        vx = random.choice([-160, -120, 120, 160])
        vy = random.choice([-160, -120, 120, 160])
        lista.append([ox, oy, vx, vy])
    return lista

obstaculos = crear_obstaculos()

# --- Texto ---
font = pygame.font.SysFont("arial", 32)
font_big = pygame.font.SysFont("arial", 50)

# --- Pantalla de reinicio ---
def esperar_reinicio():
    mensaje = font_big.render("¡Perdiste!", True, (255, 80, 80))
    mensaje2 = font.render("Presiona R para reintentar", True, (255, 255, 255))

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                return

        ventana.fill((20, 20, 20))
        ventana.blit(mensaje, (ANCHO//2 - mensaje.get_width()//2, ALTO//2 - 70))
        ventana.blit(mensaje2, (ANCHO//2 - mensaje2.get_width()//2, ALTO//2 + 10))

        pygame.display.flip()
        clock.tick(30)

# --- Colisión ---
def colision_rect_sprite(rect1, x2, y2, w2, h2):
    rect2 = pygame.Rect(x2, y2, w2, h2)
    return rect1.colliderect(rect2)

# --- Bucle principal ---
while True:
    dt = clock.tick(60) / 1000

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimiento
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        direccion_actual = "derecha"
        x += vel
    elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        direccion_actual = "izquierda"
        x -= vel
    elif teclas[pygame.K_w] or teclas[pygame.K_UP]:
        direccion_actual = "arriba"
        y -= vel
    elif teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        direccion_actual = "abajo"
        y += vel
    else:
        direccion_actual = "quieto"

    if direccion_actual != direccion_anterior:
        frame_index = 0
        direccion_anterior = direccion_actual

    frames = sprites[direccion_actual]
    if None in frames:
        continue

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_tiempo >= tiempo_cambio:
        frame_index = (frame_index + 1) % len(frames)
        ultimo_tiempo = tiempo_actual

    frame_actual = frames[frame_index]

    x = max(0, min(x, ANCHO - frame_actual.get_width()))
    y = max(0, min(y, ALTO - frame_actual.get_height()))

    player_rect = pygame.Rect(x, y, frame_actual.get_width(), frame_actual.get_height())

    # Recolectar
    closest_x = max(player_rect.left, min(obj_x, player_rect.right))
    closest_y = max(player_rect.top, min(obj_y, player_rect.bottom))
    dist = (closest_x - obj_x)**2 + (closest_y - obj_y)**2

    if dist <= radio_obj * radio_obj:
        puntos += 1
        obj_x = random.randint(radio_obj, ANCHO - radio_obj)
        obj_y = random.randint(radio_obj, ALTO - radio_obj)

    # Obstáculos
    choque = False
    for obs in obstaculos:
        ox, oy, vx, vy = obs
        ox += vx * dt
        oy += vy * dt

        if ox < 0:
            ox, vx = 0, -vx
        elif ox + 40 > ANCHO:
            ox, vx = ANCHO - 40, -vx

        if oy < 0:
            oy, vy = 0, -vy
        elif oy + 40 > ALTO:
            oy, vy = ALTO - 40, -vy

        obs[0], obs[1], obs[2], obs[3] = ox, oy, vx, vy

        if colision_rect_sprite(player_rect, ox, oy, 40, 40):
            choque = True

    if choque:
        pygame.mixer.music.stop()  # 🔇 Para la música
        esperar_reinicio()
        cargar_musica("spamton_battle")  # 🔁 Reanuda música
        puntos = 0
        x, y = ANCHO // 2, ALTO // 2
        obstaculos = crear_obstaculos()

    # Dibujar
    ventana.fill((30, 30, 30))

    pygame.draw.circle(ventana, (255, 255, 0), (obj_x, obj_y), radio_obj)

    for ox, oy, _, _ in obstaculos:
        if spamton_sprite:
            ventana.blit(spamton_sprite, (ox, oy))
        else:
            pygame.draw.circle(ventana, (255, 50, 50), (int(ox), int(oy)), 20)

    ventana.blit(frame_actual, (x, y))

    texto = font.render(f"Puntos: {puntos}", True, (255, 255, 255))
    ventana.blit(texto, (10, 10))

    pygame.display.flip()
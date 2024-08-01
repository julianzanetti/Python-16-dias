import pygame
import random
import math
from pygame import mixer

#Inicia pygame
pygame.init()

#Se crea la pantalla, con ancho y largo
pantalla = pygame.display.set_mode((800, 600))

#Titulo e icono.
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

#Variables para el sonido
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#Variables del Jugador
img_player = pygame.image.load("cohete.png")
player_x = 368
player_y = 500
player_mov = 0

#Variables del Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_mov = []
enemigo_y_mov = []
cant_enemigos = 6

for e in range(cant_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_mov.append(0.2)
    enemigo_y_mov.append(50)

#Variables de la bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_y_mov = 0.5
bala_visible = False

#Variable puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

#Texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 50)


def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (250, 250))


#Funcion mostrar puntaje
def mostar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#Funcion del jugador
def jugador(x, y):
    pantalla.blit(img_player, (x, y))


#Funcion del enemigo
def enemigo(x, y, enemigo):
    pantalla.blit(img_enemigo[enemigo], (x, y))


#Funcion de la bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


#Funcion detectar colisiones
def hay_colision(x1,y1,x2,y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distancia < 30:
        return True
    else:
        return False


#Loop del juego
se_ejecuta = True
while se_ejecuta:

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))

    #Iterar eventos
    for evento in pygame.event.get():

        # Evento = Cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_mov = -0.2
            if evento.key == pygame.K_RIGHT:
                player_mov = 0.2
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.set_volume(0.3)
                sonido_bala.play()
                nueva_bala = {
                    "x": player_x,
                    "y": player_y,
                    "velocidad": -0.3
                }
                balas.append(nueva_bala)

        #Evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                player_mov = 0

    #Modificar ubicacion jugador
    player_x += player_mov

    #Limitar bordes del jugador
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    #Modificar ubicacion enemigo
    for e in range(cant_enemigos):

        #Fin del juego
        if enemigo_y[e] > 450:
            for k in range(cant_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_mov[e]

        #Limitar bordes del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_mov[e] = 0.2
            enemigo_y[e] += enemigo_y_mov[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_mov[e] = -0.2
            enemigo_y[e] += enemigo_y_mov[e]

        #Colision?
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.set_volume(0.3)
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    #Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    jugador(player_x, player_y)

    #Mostrar puntaje
    mostar_puntaje(texto_x, texto_y)
    #Actualizar
    pygame.display.update()

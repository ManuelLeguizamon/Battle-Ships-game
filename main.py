import pygame as pg
import os
pg.mixer.init()
pg.font.init()
#---------------------------------------------V
WIDTH_WIN, HEIGHT_WIN = 1300, 650
WIN = pg.display.set_mode((WIDTH_WIN, HEIGHT_WIN))

VIDA_FONT = pg.font.SysFont("Rockwell", 40)
color_txt_vidas = (140, 140, 140)
#---------------------------------------------V

def drawWindow(ROJA_RECT, NAVE_ROJA, AMARILLA_RECT, NAVE_AMARILLA,VIDAS_ROJO ,VIDAS_AMARILLO, balas_rojo, balas_amarillo):
    WIN.blit(FONDO_ESPACIAL, (0,0)) # Fondo del juego
    WIN.blit(NAVE_ROJA, (ROJA_RECT.x, ROJA_RECT.y)) 
    WIN.blit(NAVE_AMARILLA, (AMARILLA_RECT.x, AMARILLA_RECT.y))
    pg.draw.rect(WIN, color_barra ,BARRA_DEL_MEDIO)
    TXT_ROJO = VIDA_FONT.render("VIDAS:" + str(VIDAS_ROJO), 1,color_txt_vidas)
    TXT_AMARILLO =  VIDA_FONT.render("VIDAS:"+ str(VIDAS_AMARILLO), 5,color_txt_vidas)
    WIN.blit(TXT_ROJO, (20, 10))
    WIN.blit(TXT_AMARILLO, (WIDTH_WIN-190, 10))

# Balas----V
    for BALA in balas_rojo:
        pg.draw.rect(WIN, COLOR_ROJO, BALA)
    for BALA in balas_amarillo:
        pg.draw.rect(WIN, COLOR_AMARILLO, BALA)

    pg.display.update()
#---------------------------------------------V
    # MOVIMIENTO DE LAS NAVES

MOVE = 7 # PAra controlar la velocidad de las naves

def movimiento_roja(KEY_PRESSED, ROJA_RECT):
    if KEY_PRESSED[pg.K_w] and ROJA_RECT.y - MOVE > 0:
        ROJA_RECT.y -= MOVE
    if KEY_PRESSED[pg.K_s] and ROJA_RECT.y + MOVE < HEIGHT_WIN - height_nave + 10:
        ROJA_RECT.y += MOVE
    if KEY_PRESSED[pg.K_a] and ROJA_RECT.x - MOVE > 0:
        ROJA_RECT.x -= MOVE
    if KEY_PRESSED[pg.K_d] and ROJA_RECT.x + MOVE < WIDTH_WIN//2 - width_nave - 10:
        ROJA_RECT.x += MOVE

def movimiento_amarilla(KEY_PRESSED, AMARILLA_RECT):
    if KEY_PRESSED[pg.K_UP] and AMARILLA_RECT.y - MOVE > 0:
        AMARILLA_RECT.y -= MOVE
    if KEY_PRESSED[pg.K_DOWN] and AMARILLA_RECT.y + MOVE < HEIGHT_WIN - height_nave + 10:
        AMARILLA_RECT.y += MOVE
    if KEY_PRESSED[pg.K_LEFT] and AMARILLA_RECT.x - MOVE > WIDTH_WIN//2 + 10:
        AMARILLA_RECT.x -= MOVE
    if KEY_PRESSED[pg.K_RIGHT] and AMARILLA_RECT.x + MOVE < WIDTH_WIN - width_nave - 10:
        AMARILLA_RECT.x += MOVE

    
#---------------------------------------------V
        # Configuracion basica de las imagenes  (naves, barra del medio y fondo)

width_nave, height_nave = 70, 80
NAVE_ROJA_IMG= pg.image.load(os.path.join("archivos","nave_roja.png"))
NAVE_ROJA = pg.transform.rotate(
    pg.transform.scale(NAVE_ROJA_IMG, (width_nave, height_nave)), 90)

NAVE_AMARILLA_IMG =pg.image.load(os.path.join("archivos", "nave_amarilla.png"))
NAVE_AMARILLA = pg.transform.rotate(
    pg.transform.scale(NAVE_AMARILLA_IMG, (width_nave, height_nave)), 270)

FONDO_ESPACIAL = pg.transform.scale(pg.image.load(os.path.join("archivos", "espacio_3.png")), (WIDTH_WIN, HEIGHT_WIN))

BARRA_DEL_MEDIO = pg.Rect(WIDTH_WIN//2, 0, 10, HEIGHT_WIN)
color_barra = (0, 26, 26)
#---------------------------------------------V
    # Ganadores
winner_font = pg.font.SysFont("Rockwell", 75)
color_winner = (191, 191, 191)

def winner(text):
    MENSAJE = winner_font.render(text, 1, color_winner)
    WIN.blit(MENSAJE, (WIDTH_WIN//2-MENSAJE.get_width()//2, HEIGHT_WIN//2 - MENSAJE.get_height()//2))
    pg.display.update()
    pg.time.delay(3000)# Esto hace que, al ganar uno, el mensaje se muestre por 3 SEGUNDOS y luego reiniciar el juego
#---------------------------------------------V
    # Sonidos
MUSICA = pg.mixer.Sound("archivos/fondo.mp3")
MUSICA.play() 

DISPARO = pg.mixer.Sound('archivos/shoot.mp3')
COLICION = pg.mixer.Sound('archivos/explocion.mp3')

#---------------------------------------------V
    # BALAS
balas_velocidad = 9
COLOR_ROJO = (255, 51, 0)
COLOR_AMARILLO = (255, 255, 26)
MAX_BALAS = 7
ROJO_COLICION = pg.USEREVENT + 1 #El "+1" y "+2" son identificadores para cada evento
AMARILLO_COLICION = pg.USEREVENT + 2

def balas_control(ROJA_RECT,AMARILLA_RECT,balas_rojo,balas_amarillo): #Manejar movimiento, coliciones y eliminacion de las balas
    for BALA in balas_rojo: #Controlar si el rojo acertó un disparo al amarillo
        BALA.x += balas_velocidad
        if AMARILLA_RECT.colliderect(BALA):
            pg.event.post(pg.event.Event(AMARILLO_COLICION))
            balas_rojo.remove(BALA)
        elif BALA.x > WIDTH_WIN:
            balas_rojo.remove(BALA)

    for BALA in balas_amarillo: #Controlar si el amarillo acertó un disparo al rojo
        BALA.x -= balas_velocidad
        if ROJA_RECT.colliderect(BALA):
            pg.event.post(pg.event.Event(ROJO_COLICION))
            balas_amarillo.remove(BALA)
        elif BALA.x < 0:
            balas_amarillo.remove(BALA)

#---------------------------------------------V
    # Main loop 

clock = pg.time.Clock()

def main():
    ROJA_RECT = pg.Rect(100,250, width_nave, height_nave)
    AMARILLA_RECT = pg.Rect(1000, 250, width_nave, height_nave)
    VIDAS_ROJO = 10
    VIDAS_AMARILLO = 10
    balas_rojo = []
    balas_amarillo = []

    while True:
        KEY_PRESSED = pg.key.get_pressed()

        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break
    # Balas--------------------V
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LCTRL and len(balas_rojo) < MAX_BALAS:
                    BALA = pg.Rect(ROJA_RECT.x + ROJA_RECT.width + 5, ROJA_RECT.y + ROJA_RECT.height//2 - 8, 10, 6)
                    balas_rojo.append(BALA)
                    DISPARO.play()

                if event.key == pg.K_SPACE and len(balas_amarillo) < MAX_BALAS:
                    BALA = pg.Rect(AMARILLA_RECT.x - 5, AMARILLA_RECT.y + AMARILLA_RECT.height//2 - 8, 10, 6)
                    balas_amarillo.append(BALA)
                    DISPARO.play()
    # Coliciones
            if event.type == ROJO_COLICION:
                VIDAS_ROJO -= 1
                COLICION.play()
            if event.type == AMARILLO_COLICION:
                VIDAS_AMARILLO -= 1
                COLICION.play()

        txt_win=""
        if VIDAS_ROJO == 0:
            txt_win = "LA NAVE AMARILLA HA GANADO"              
        if VIDAS_AMARILLO == 0:
            txt_win = "LA NAVE ROJA HA GANADO"
        if txt_win != "":
            winner(txt_win)
            break
            


        movimiento_roja(KEY_PRESSED, ROJA_RECT)
        movimiento_amarilla(KEY_PRESSED, AMARILLA_RECT)
        drawWindow(ROJA_RECT, NAVE_ROJA, AMARILLA_RECT, NAVE_AMARILLA,VIDAS_ROJO ,VIDAS_AMARILLO, balas_rojo, balas_amarillo)
        balas_control(ROJA_RECT,AMARILLA_RECT,balas_rojo,balas_amarillo)
    main()
#---------------------------------------------V
if __name__ == "__main__":
    main()
import pygame as pg
import os
pg.mixer.init()
#---------------------------------------------V
WIDTH_WIN, HEIGHT_WIN = 1200, 600
WIN = pg.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
#---------------------------------------------V

def drawWindow(ROJA_RECT, NAVE_ROJA, AMARILLA_RECT, NAVE_AMARILLA):
    WIN.blit(FONDO_ESPACIAL, (0,0)) # Fondo del juego
    WIN.blit(NAVE_ROJA, (ROJA_RECT.x, ROJA_RECT.y)) 
    WIN.blit(NAVE_AMARILLA, (AMARILLA_RECT.x, AMARILLA_RECT.y))
    pg.draw.rect(WIN, color_barra ,BARRA_DEL_MEDIO)

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

FONDO_ESPACIAL = pg.transform.scale(pg.image.load(os.path.join("archivos", "espacio_fondo.png")), (WIDTH_WIN, HEIGHT_WIN))

BARRA_DEL_MEDIO = pg.Rect(WIDTH_WIN//2, 0, 10, HEIGHT_WIN)
color_barra = (153, 38, 0)
#---------------------------------------------V
    # Sonidos
MUSICA = pg.mixer.Sound("archivos/fondo.mp3")
MUSICA.play() 

#---------------------------------------------V
    # Main loop 

clock = pg.time.Clock()

def main():
    ROJA_RECT = pg.Rect(100,250, width_nave, height_nave)
    AMARILLA_RECT = pg.Rect(1000, 250, width_nave, height_nave)

    while True:
        KEY_PRESSED = pg.key.get_pressed()

        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

        movimiento_roja(KEY_PRESSED, ROJA_RECT)
        movimiento_amarilla(KEY_PRESSED, AMARILLA_RECT)
        drawWindow(ROJA_RECT, NAVE_ROJA, AMARILLA_RECT, NAVE_AMARILLA)
#---------------------------------------------V
main()
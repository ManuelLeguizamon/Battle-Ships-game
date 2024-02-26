import pygame as pg
import os
#---------------------------------------------
WIDTH_WIN, HEIGHT_WIN = 1200, 600
WIN = pg.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
#---------------------------------------------
def drawWindow(NAVE_RECT, NAVE_1):
    WIN.fill((0,0,0))
    WIN.blit(NAVE_1, (NAVE_RECT.x, NAVE_RECT.y))


    pg.display.update()
#---------------------------------------------}
MOVE = 5
def movimiento_1(KEY_PRESSED, NAVE_RECT):
    if KEY_PRESSED[pg.K_w]:
        NAVE_RECT.y -= MOVE
    if KEY_PRESSED[pg.K_s] and NAVE_RECT.y + MOVE < HEIGHT_WIN:
        NAVE_RECT.y += MOVE


    
#---------------------------------------------}
width_nave, height_nave = 70, 70
NAVE_IMG= pg.image.load(os.path.join("archivos","nave_pija_roja.png"))
NAVE_1 = pg.transform.rotate(pg.transform.scale(NAVE_IMG, (width_nave, height_nave)), 90)



#---------------------------------------------
clock = pg.time.Clock()
def main():
    KEY_PRESSED = pg.key.get_pressed()
    NAVE_RECT = pg.Rect(100,300, width_nave, height_nave)

    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

        movimiento_1(KEY_PRESSED, NAVE_RECT)
        drawWindow(NAVE_RECT, NAVE_1)
#---------------------------------------------
main()
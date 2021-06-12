import pygame as pg
import os

WIDTH=800
HEIGHT=800
COLOR_SCREEN = (127,127,127)
SPACESHIP_SIZE=(50,50)
FPS=60
VEL=5
sprite_folder="sprites"

pg.init()
screen = pg.display.set_mode([800, 800])


def load_sprite(sprite):
    return pg.image.load(os.path.join(sprite_folder,sprite))


SPACESHIP_IMAGE=load_sprite("ufodark.png")
SPACESHIP=pg.transform.scale(SPACESHIP_IMAGE,SPACESHIP_SIZE)


def draw_screen(circle):
    screen.fill(COLOR_SCREEN)
    screen.blit(SPACESHIP,(circle.x,circle.y))
    pg.display.update()


ufo=pg.Rect((WIDTH/2, HEIGHT/2),SPACESHIP_SIZE)
clock=pg.time.Clock()

running=True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type== pg.QUIT:
            running=False
    keys_pressed=pg.key.get_pressed()
    if keys_pressed[pg.K_LEFT]:
        ufo.x-=VEL
    if keys_pressed[pg.K_RIGHT]:
        ufo.x+=VEL
    if keys_pressed[pg.K_UP]:
        ufo.y-=VEL
    if keys_pressed[pg.K_DOWN]:
        ufo.y+=VEL
    
    draw_screen(ufo)

pg.quit()
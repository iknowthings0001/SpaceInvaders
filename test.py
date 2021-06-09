import pygame as pg


WIDTH=800
HEIGHT=800
color_screen = (127,127,127)
cradius=75 
FPS=60


pg.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])


def draw_screen(circle):
    screen.fill(color_screen)
    pg.draw.circle(screen,(0,0,255),(circle.x,circle.y),cradius)
    pg.display.update()


circle=pg.Rect(WIDTH/2, HEIGHT/2,cradius,cradius)
clock=pg.time.Clock()

running=True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type== pg.QUIT:
            running=False
    draw_screen(circle)
    circle.x+=1
pg.quit()
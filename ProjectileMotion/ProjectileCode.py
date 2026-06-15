'''
    14/06/26
    Projectile Motion project. This will be my second project in python now so I should have a better idea of what I am doing.
    I planned to make a game sort of thing using the projectile motion physics so it should not be hard at all. I will use no AI for this project.
    *Also i most likely won't use matplotlib cause its hard and a very big package to run for demo.
    *update on what game actually is
'''

#imports
import sys
import numpy as np
import pygame
import pygame as pg
from pygame.examples.music_drop_fade import VOLUME_CHANGE_AMOUNT

#sys and pygame setup
pygame.init()
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = 60
clock = pygame.time.Clock()
dt = clock.tick(fps) / 1000.0
t = 0
VarChoice = True
Shoot = False

#colours
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)
Yellow = (255, 255, 0)

#math vars
g = 9.81
Vo = 0
#Vpres
thetao = 0
#thetapres
x1 = 200
y1 = 500
xpres = Vo*np.cos(thetao)*t + x1
ypres = (Vo*np.sin(thetao)) -(0.5)*(g)*(t*t) + y1
distancepres = Vo*np.cos(thetao)*t
distancefin = 2*((Vo*np.sin(thetao))/g)*Vo*np.cos(thetao)
heightpres = (Vo*np.sin(thetao)) -(0.5)*(g)*(t*t)
heightmax = (Vo*np.sin(thetao))*((Vo*np.sin(thetao))/(g)) - (0.5)*(g)*(((Vo*np.sin(thetao))/g)**2)
t += dt
'''x2t = f"X position relative to centre = {x2fake:.2f}"
    y2t = f"Y position relative to centre = {y2fake:.2f}"
    Vot = f"Vo = {Vo:.2f} (885 ≈ equilibrium)"
    Rt = f"R length = {R:.1f}"
    θt = f"radians = {θ:.2f}"

    def doText():
        text_surfaceθ = my_font.render(θt, True, (0, 0, 0))
        text_surfaceVo = my_font.render(Vot, True, (0, 0, 0))
        text_surfaceRt = my_font.render(Rt, True, (0, 0, 0))
        text_surfacex2 = my_font.render(x2t, True, (0, 0, 0))
        text_surfacey2 = my_font.render(y2t, True, (0, 0, 0))

        screen.blit(text_surfaceVo, (10, 10))
        screen.blit(text_surfaceθ, (10, 50))
        screen.blit(text_surfaceRt, (10, 90))
        screen.blit(text_surfacex2, (800, 10))
        screen.blit(text_surfacey2, (800, 50))
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(window, color, rectangle)'''
#make text
my_font = pg.font.SysFont(pg.font.get_default_font(), 30)
my_fontinc = pg.font.SysFont(pg.font.get_default_font(), 50)
gt = f'Gravity Value = {g:5f}'
Vot = f'Initial Velocity = {Vo:2f}'
thetaot = f'Launch Angle = {thetao:2f}'

p = "+"
m = "-"
#functions
def TextMake():
    #make text
    TextSurfaceG = my_font.render(gt, True, Black)
    TextSurfaceVo = my_font.render(Vot, True, Black)
    TextSurfaceThetao = my_font.render(thetaot, True, Black)

    pt = my_fontinc.render(p, True, Black)
    mt = my_fontinc.render(m, True, Black)

    #drawtext
    screen.blit(TextSurfaceG, (10, 10))
    screen.blit(TextSurfaceVo, (10, 70))
    screen.blit(TextSurfaceThetao, (10, 130))

    screen.blit(pt, (25, 30))
    screen.blit(pt, (25, 90))
    screen.blit(pt, (25, 150))
    screen.blit(mt, (89, 32))
    screen.blit(mt, (89, 92))
    screen.blit(mt, (89, 152))

def buttons():
    #create Rects
    VoButtonp = pg.Rect(10, 30, 50, 40)
    gButtonp = pg.Rect(10, 90, 50, 40)
    ThetaoButtonp = pg.Rect(10, 150, 50, 40)

    VoButtonm = pg.Rect(70, 30, 50, 40)
    gButtonm = pg.Rect(70, 90, 50, 40)
    ThetaoButtonm = pg.Rect(70, 150, 50, 40)

    #draw rects
    pg.draw.rect(screen, Green, VoButtonp)
    pg.draw.rect(screen, Green, gButtonp)
    pg.draw.rect(screen, Green, ThetaoButtonp)
    pg.draw.rect(screen, Red, VoButtonm)
    pg.draw.rect(screen, Red, gButtonm)
    pg.draw.rect(screen, Red, ThetaoButtonm)
#loops
while VarChoice:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            VarChoice = False
            pg.quit()
            sys.exit()
    screen.fill(White)

    #input
    keys = pg.key.get_pressed()
    if pg.mouse.get_pressed()[0]:
        pos = pg.mouse.get_pos()
    if keys[pg.K_s]:
        VarChoice = False
        Shoot = True
    #draw
    buttons()#BUTTONS HAVE TO BE DRAWN BEFORE TEXT so plus and minus are drawn on top
    TextMake()
    pg.display.flip()
while Shoot:
    dt = clock.tick(fps) / 1000.0
    if dt > 0.1:
        dt = 0.1

    t += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            VarChoice = False
            pg.quit()
            sys.exit()

    screen.fill(White)
    pg.draw.circle(screen, Black, (x1,y1), 5)
    pg.draw.line(screen, Black, (x1,y1), (x1 + 500,y1), 5)
    pg.draw.line(screen, Black, (x1,y1), (x1,y1 - 300), 5)





    clock.tick(fps)
    pg.display.flip()
pygame.quit()
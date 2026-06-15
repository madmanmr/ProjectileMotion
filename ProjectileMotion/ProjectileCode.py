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
prevMouseClick = False

#colours
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)
darkGreen = (0,200,0)
darkRed = (200,0,0)
darkBlue = (0,0,200)

#math vars
g = 0
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
    gt = f'Gravity Value = {g:5f}'
    Vot = f'Initial Velocity = {Vo:2f}'
    thetaot = f'Launch Angle = {thetao:2f}'

    p = "+"
    m = "-"
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

#create Rects
gButtonp = pg.Rect(10, 30, 50, 40)
VoButtonp = pg.Rect(10, 90, 50, 40)
ThetaoButtonp = pg.Rect(10, 150, 50, 40)

gButtonm = pg.Rect(70, 30, 50, 40)
VoButtonm = pg.Rect(70, 90, 50, 40)
ThetaoButtonm = pg.Rect(70, 150, 50, 40)

StartButton = pg.Rect(10, 250, 100, 100)

#loops
while VarChoice:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            VarChoice = False
            pg.quit()
            sys.exit()
    screen.fill(White)
    #mouse stuff
    mousePos = pg.mouse.get_pos()
    mouseClick = pg.mouse.get_pressed()
    mousePress = mouseClick and not prevMouseClick
    prevMouseClick = mouseClick
    #buttons

    def handle_buttonG(rect, action):
        color = Green
        if rect.collidepoint(mousePos):
            color = darkGreen
            if mousePress:
                action()
        pg.draw.rect(screen, color, rect)
    def handle_buttonR(rect, action):
        color = Red
        if rect.collidepoint(mousePos):
            color = darkRed
            if mousePress:
                action()
        pg.draw.rect(screen, color, rect)
    def handle_buttonS(rect, action):
        color = Blue
        if rect.collidepoint(mousePos):
            color = darkBlue
            if mousePress:
                action()
        pg.draw.rect(screen, color, rect)
    #input
    keys = pg.key.get_pressed()
    #funcs
    def Fire():
        VarChoice = False
        Shoot = True
    def Vop():
        global Vo
        Vo += 1
    def Vom():
        global Vo
        Vo -= 1
    def Gp():
        global g
        g += 1
    def Gm():
        global g
        g -= 1
    def thetaop():
        global thetao
        thetao += 1
    def thetaom():
        global thetao
        thetao -= 1
    #draw
    handle_buttonG(VoButtonp, Vop)
    handle_buttonG(gButtonp, Gp)
    handle_buttonG(ThetaoButtonp, thetaop)

    handle_buttonR(VoButtonm, Vom)
    handle_buttonR(gButtonm, Gm)
    handle_buttonR(ThetaoButtonm, thetaom)

    handle_buttonS(StartButton, Fire)
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
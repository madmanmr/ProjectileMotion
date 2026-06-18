'''
    14/06/26
    Projectile Motion project. This will be my second project in python now so I should have a better idea of what I am doing.
    I planned to make a game sort of thing using the projectile motion physics so it should not be hard at all. I will use no AI for this project.
    *Also i most likely won't use matplotlib cause its hard and a very big package to run for demo.
    Have nearly completed physics now but I just want to make sure the timing is right, then I might make a game out of it.
    Completed physics and timing and everything else is good so now im gonna start with the game, idea is to have a target in a random position
    with set parameters then give points based on where projectile hits
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
t = 0
running = True
VarChoice = True
Shoot = False
End = False
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
Yellow = (255,200,40)

#math vars
SCALE = 10# 10 pixels=1m
g = 9.81
Vo = 20
thetao = np.radians(45)
thetapres = 0
x1 = 200
y1 = 500
xpres = x1
ypres = y1
distancepres = Vo*np.cos(thetao)*t
heightpres = 0
heightmax = 0
speed = 0

#game vars
points = 0
pointsold = 0
Ellx = np.random.randint(400, 1000)
Elly = y1 - 17.5

#make text
my_font = pg.font.SysFont(pg.font.get_default_font(), 30)
my_fontinc = pg.font.SysFont(pg.font.get_default_font(), 50)

#functions
def TextMake():
    heightmax = (Vo * np.sin(thetao)) ** 2 / (2 * g)
    gt = f"Gravity Value = {g:.2f}"
    Vot = f"Initial Velocity = {Vo:.1f} m/s"
    thetaot = f"Launch Angle = {np.degrees(thetao):.1f}°"

    distanceprest = f"Distance = {distancepres:.2f} m"
    heightprest = f"Height = {heightpres:.2f} m"
    thetaprest = f"Angle of travel = {thetapres:.1f}°"
    heightmaxt = f"Maximum Height= {heightmax:.2f} m"
    timet = f"Flight Time = {t:.2f} s"
    Speed = f"Speed = {speed:.2f} m/s"
    pointst = f"points = {points:.0f}"

    start = "Start"
    restart = "Restart"

    p = "+"
    m = "-"
    #make text
    TextSurfaceG = my_font.render(gt, True, Black)
    TextSurfaceVo = my_font.render(Vot, True, Black)
    TextSurfaceThetao = my_font.render(thetaot, True, Black)
    TextSurfacedPres = my_font.render(distanceprest, True, Black)
    TextSurfacehPres = my_font.render(heightprest, True, Black)
    TextSurfaceThetaprest = my_font.render(thetaprest, True, Black)
    TextSurfaceheightmaxt = my_font.render(heightmaxt, True, Black)
    TextSurfacett = my_font.render(timet, True, Black)
    TextSurfacespeed = my_font.render(Speed, True, Black)
    TextSurfacepointst = my_font.render(pointst, True, Yellow)

    TextSurfaceStart = my_font.render(start, True, Green)
    TextSurfaceRestart = my_font.render(restart, True, Red)

    pt = my_fontinc.render(p, True, Black)
    mt = my_fontinc.render(m, True, Black)

    #drawtext
    screen.blit(TextSurfaceG, (10, 10))
    screen.blit(TextSurfaceVo, (10, 70))
    screen.blit(TextSurfaceThetao, (10, 130))
    screen.blit(TextSurfacedPres, (500,10))
    screen.blit(TextSurfacehPres, (500, 50))
    screen.blit(TextSurfaceThetaprest, (500, 90))
    screen.blit(TextSurfaceheightmaxt, (800, 10))
    screen.blit(TextSurfacett, (500, 170))
    screen.blit(TextSurfacespeed, (500, 130))
    screen.blit(TextSurfacepointst, (800, 50))

    screen.blit(TextSurfaceStart, (10, 220))
    screen.blit(TextSurfaceRestart, (10, 370))

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
EndButton = pg.Rect(10, 400, 100, 100)
#funcs
def Fire():
    global VarChoice, Shoot, t, ypres, xpres
    t = 0
    ypres = y1
    xpres = x1
    VarChoice = False
    Shoot = True
def Vop():
    global Vo
    Vo = min(40, Vo +1)
def Vom():
    global Vo
    Vo = max(1, Vo - 1)
def Gp():
    global g
    g = min(20, g + 0.1)
def Gm():
    global g
    g = max(0.1, g - 0.1)
def thetaop():
    global thetao
    thetao = min(np.radians(89), thetao + np.radians(1))
def thetaom():
    global thetao
    thetao = max(np.radians(1), thetao - np.radians(1))
def elCreato():
    pg.draw.line(screen, Black, (x1, y1), (x1 + 1000, y1), 5)
    pg.draw.line(screen, Black, (x1, y1), (x1, y1 - 300), 5)

    pg.draw.rect(screen, Green, VoButtonp)
    pg.draw.rect(screen, Green, ThetaoButtonp)
    pg.draw.rect(screen, Green, gButtonp)

    pg.draw.rect(screen, Red, VoButtonm)
    pg.draw.rect(screen, Red, ThetaoButtonm)
    pg.draw.rect(screen, Red, gButtonm)

    pg.draw.rect(screen, Blue, StartButton)
    pg.draw.rect(screen, Blue, EndButton)
def Target():
    ellipse_rect3 = pg.Rect(Ellx, Elly, 200, 35)
    ellipse_rect2 = pg.Rect(Ellx + 30, Elly + 7.5, 140, 20)
    ellipse_rect1 = pg.Rect(Ellx + 50, Elly + 12.5, 100, 10)

    pg.draw.ellipse(screen, Red, ellipse_rect3)
    pg.draw.ellipse(screen, White, ellipse_rect2)
    pg.draw.ellipse(screen, Red, ellipse_rect1)

    return ellipse_rect1, ellipse_rect2, ellipse_rect3
def splash(ellipse_rect1, ellipse_rect2, ellipse_rect3):
    global points, pointsold
    Splashfx = pg.Rect(xpres - 25, ypres, 50, 5)
    pg.draw.ellipse(screen, Yellow, Splashfx)

    if ellipse_rect1.colliderect(Splashfx) and points == pointsold:
        points += 50
    elif ellipse_rect2.colliderect(Splashfx) and points == pointsold:
        points += 30
    elif ellipse_rect3.colliderect(Splashfx) and points == pointsold:
        points += 10
def angleLine():
    l = 100
    y3 = y1 - (l * np.sin(thetao))
    x3 = x1 + (l * np.cos(thetao))

    pg.draw.line(screen, darkGreen, (x1, y1), (x3, y3), 4)

while running:
    #loops
    while VarChoice:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                VarChoice = False
                Shoot = False
                End = False
        screen.fill(White)
        #mouse stuff
        mousePos = pg.mouse.get_pos()
        mouseClick = pg.mouse.get_pressed()[0]
        mousePress = mouseClick and not prevMouseClick
        prevMouseClick = mouseClick
        #reset vars
        t = 2 * (Vo*np.sin(thetao)/g)
        xpres = x1
        ypres = y1
        distancepres = (Vo**2 * np.sin(2 * thetao)) / g
        heightpres = 0
        thetapres = np.degrees(thetao)
        heightmax = 0

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

        #draw
        handle_buttonG(VoButtonp, Vop)
        handle_buttonG(gButtonp, Gp)
        handle_buttonG(ThetaoButtonp, thetaop)

        handle_buttonR(VoButtonm, Vom)
        handle_buttonR(gButtonm, Gm)
        handle_buttonR(ThetaoButtonm, thetaom)

        angleLine()

        pg.draw.line(screen, Black, (x1, y1), (x1 + 1000, y1), 5)
        pg.draw.line(screen, Black, (x1, y1), (x1, y1 - 300), 5)
        pg.draw.circle(screen, Yellow, (int(xpres), int(ypres)), 10)

        pg.draw.rect(screen, Blue, EndButton)

        Target()

        handle_buttonS(StartButton, Fire)
        TextMake()
        pg.display.flip()
    while Shoot:
        dt = clock.tick(fps) / 1000.0
        if dt > 0.1:
            dt = 0.1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                VarChoice = False
                Shoot = False
                End = False

        screen.fill(White)

        # physics
        vx = Vo * np.cos(thetao)
        vy = Vo * np.sin(thetao) - g * t

        xpres = x1 + SCALE * vx * t
        ypres = y1 - SCALE * (Vo * np.sin(thetao) * t - 0.5 * g * t**2)

        speed = np.hypot(vx, vy)#np to save the day
        thetapres = np.degrees(np.arctan2(vy, vx))

        distancepres = vx * t
        heightpres = (y1 - ypres) / SCALE

        elCreato()
        Target()
        angleLine()
        pg.draw.circle(screen, Yellow, (int(xpres), int(ypres)), 10)
        TextMake()

        # better landing condition
        if ypres >= y1 and t > 0:
            range_total = Vo**2 * np.sin(2 * thetao) / g
            xpres = x1 + SCALE * range_total
            ypres = y1
            Shoot = False
            End = True

        t += dt
        pg.display.flip()
    while End:
        mousePos = pg.mouse.get_pos()
        mouseClick = pg.mouse.get_pressed()[0]
        mousePress = mouseClick and not prevMouseClick
        prevMouseClick = mouseClick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                VarChoice = False
                Shoot = False
                End = False

        screen.fill(White)
        def handle_buttonS(rect, action):
            color = Blue
            if rect.collidepoint(mousePos):
                color = darkBlue
                if mousePress:
                    action()
            pg.draw.rect(screen, color, rect)

        def New():
            global End, VarChoice, t, Ellx, points, pointsold
            VarChoice = True
            End = False
            t = 0
            Ellx = np.random.randint(400, 1000)
            pointsold = points

        #making variables what they should be cause i cant think of a way to handle collision without delay
        t = 2 * (Vo*np.sin(thetao)/g)
        speed = Vo
        distancepres = (Vo**2 * np.sin(2 * thetao)) / g

        heightpres = int(np.round((y1 - ypres) / SCALE))
        thetapres = int(np.round(thetapres))

        elCreato()
        ellipse_rect1, ellipse_rect2, ellipse_rect3 = Target()
        splash(ellipse_rect1, ellipse_rect2, ellipse_rect3)
        pg.draw.circle(screen, Yellow, (int(xpres), int(ypres)), 5)

        pg.draw.rect(screen, Blue, EndButton)
        handle_buttonS(EndButton, New)
        TextMake()

        pg.display.flip()
pygame.quit()
sys.exit()
'''
    14/06/26
    Projectile Motion project. This will be my second project in python now so I should have a better idea of what I am doing.
    I planned to make a game sort of thing using the projectile motion physics so it should not be hard at all. I will use no AI for this project.
    *Also i most likely won't use matplotlib cause its hard and a very big package to run for demo.
    Have nearly completed physics now but I just want to make sure the timing is right, then I might make a game out of it.
    Completed physics and timing and everything else is good so now im gonna start with the game, idea is to have a target in a random position
    with set parameters then give points based on where projectile hits.
    I think the game is basically done now. I have a target now that moves and I have the points based system. blah blah bored of typing you can see for yourself
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
cheats = False
GameOver = False
pg.display.set_caption("Projectile Motion Game")
#colours
Red = (220, 70, 80)
Green = (80, 190, 130)
Blue = (65, 125, 215)
White = (242, 246, 250)
Black = (25, 30, 40)
darkGreen = (45, 145, 95)
darkRed = (170, 45, 55)
darkBlue = (40, 85, 165)
Yellow = (255, 205, 65)
darkYellow = (210, 155, 30)
StartGreen = (60, 200, 110)
StartGreenDark = (40, 160, 85)
CheatGrey = (110, 120, 140)
CheatGreyDark = (80, 90, 110)
cheatbcol = CheatGrey

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
count = 1
shots = 5

#restart button
size = [500,200]

#make text
my_font = pg.font.SysFont(pg.font.get_default_font(), 30)
my_fontinc = pg.font.SysFont(pg.font.get_default_font(), 50)
my_fontbig = pg.font.SysFont(pg.font.get_default_font(), 80)

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
    cheatst = f"Aim Assist (half points) = {cheats:}"
    shotst = f"Shots Left = {shots:.0f}"

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
    TextSurfacepointst = my_fontinc.render(pointst, True, Yellow)

    TextSurfaceStart = my_font.render(start, True, White)
    TextSurfaceRestart = my_font.render(restart, True, White)
    TextSurfacecheat = my_font.render(cheatst, True, White)
    TextSurfaceshots = my_fontinc.render(shotst, True, Yellow)

    pt = my_fontinc.render(p, True, Black)
    mt = my_fontinc.render(m, True, Black)

    #drawtext
    screen.blit(TextSurfaceG, (25, 25))
    screen.blit(TextSurfaceVo, (25, 95))
    screen.blit(TextSurfaceThetao, (25, 165))

    screen.blit(TextSurfacedPres, (430, 20))
    screen.blit(TextSurfacehPres, (430, 55))
    screen.blit(TextSurfaceThetaprest, (430, 90))
    screen.blit(TextSurfaceheightmaxt, (430, 125))
    screen.blit(TextSurfacespeed, (430, 160))
    screen.blit(TextSurfacett, (430, 195))

    screen.blit(TextSurfacepointst, (1030, 25))
    screen.blit(TextSurfaceshots, (1030, 85))

    screen.blit(TextSurfaceStart, (75, 314))
    screen.blit(TextSurfaceRestart, (63, 390))
    screen.blit(TextSurfacecheat, (37, 627))

    screen.blit(pt, (37, 52))
    screen.blit(mt, (97, 54))

    screen.blit(pt, (37, 122))
    screen.blit(mt, (97, 124))

    screen.blit(pt, (37, 192))
    screen.blit(mt, (97, 194))


#create Rects
gButtonp = pg.Rect(25, 55, 45, 35)
gButtonm = pg.Rect(80, 55, 45, 35)

VoButtonp = pg.Rect(25, 125, 45, 35)
VoButtonm = pg.Rect(80, 125, 45, 35)

ThetaoButtonp = pg.Rect(25, 195, 45, 35)
ThetaoButtonm = pg.Rect(80, 195, 45, 35)

StartButton = pg.Rect(25, 295, 150, 60)
EndButton = pg.Rect(25, 370, 150, 60)

cheatButton = pg.Rect(25, 610, 340, 55)

Newgamebutton = pg.Rect(SCREEN_WIDTH/2 - size[0]/2, SCREEN_HEIGHT/2 - size[1]/2 + 100, size[0], size[1])
#funcs
def Fire():
    global VarChoice, Shoot, t, ypres, xpres, shots
    if shots > 0:
        t = 0
        ypres = y1
        xpres = x1
        VarChoice = False
        Shoot = True
        shots -= 1
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
        if cheats == True:
            points += 25
        else:
            points += 50
    elif ellipse_rect2.colliderect(Splashfx) and points == pointsold:
        if cheats == True:
            points += 15
        else:
            points += 30
    elif ellipse_rect3.colliderect(Splashfx) and points == pointsold:
        if cheats == True:
            points += 5
        else:
            points += 10
def angleLine():
    l = 200
    y3 = y1 - (l * np.sin(thetao))
    x3 = x1 + (l * np.cos(thetao))

    pg.draw.line(screen, darkGreen, (x1, y1), (x3, y3), 4)
def parabola():
    if cheats == True:
        points = []
        range_pixels = int((Vo ** 2 * np.sin(2 * thetao) / g) * SCALE)

        for x in range(range_pixels):
            x_m = x / SCALE
            y_m = (
                 x_m * np.tan(thetao)
                - (g * x_m ** 2)
                / (2 * Vo ** 2 * np.cos(thetao) ** 2)
            )
            screen_x = x1 + x
            screen_y = y1 - y_m * SCALE

            points.append((screen_x, screen_y))
        if len(points) > 1:
            pg.draw.lines(screen, darkRed, False, points, 3)
def CheatsFunc():
    global cheats, cheatbcol
    cheats = True
    cheatbcol = Green
def PlayAgainfunc():
    global VarChoice, GameOver, shots, points, pointsold, cheats, cheatbcol, Ellx, t, g, Vo, thetao, speed

    GameOver = False
    VarChoice = True

    shots = 5
    points = 0
    pointsold = 0
    cheats = False
    cheatbcol = CheatGrey
    Ellx = np.random.randint(400, 1000)
    t = 0
    g = 9.81
    Vo = 20
    thetao = np.radians(45)
    speed = 0
def Playagaintext():
    gameovert = "Game Over!"
    playagaint = "Play Again"
    finalscore = f"Final Score: {points}"

    textSurfacegameover = my_fontbig.render(gameovert, True, Black)
    textSurfaceplayagain = my_fontbig.render(playagaint, True, White)
    textSurfacefinalscore = my_fontbig.render(finalscore, True, darkYellow)

    # centered positions
    gameover_rect = textSurfacegameover.get_rect(center=(SCREEN_WIDTH // 2, 140))
    score_rect = textSurfacefinalscore.get_rect(center=(SCREEN_WIDTH // 2, 260))
    playagain_rect = textSurfaceplayagain.get_rect(center=Newgamebutton.center)

    screen.blit(textSurfacegameover, gameover_rect)
    screen.blit(textSurfacefinalscore, score_rect)
    screen.blit(textSurfaceplayagain, playagain_rect)

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
        if shots == 0:
            VarChoice = False
            Shoot = False
            End = False
            GameOver = True
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
        def handle_start(rect, action):
            color = StartGreen
            if rect.collidepoint(mousePos):
                color = StartGreenDark
                if mousePress:
                    action()
            pg.draw.rect(screen, color, rect, border_radius=12)
        def handle_cheat(rect, action):
            global cheats, cheatbcol
            if cheats == True:
                cheatbcol = Green
            else:
                cheatbcol = CheatGrey
            color = cheatbcol
            if rect.collidepoint(mousePos):
                color = Green
                if mousePress:
                    action()
            pg.draw.rect(screen, color, rect, border_radius=12)

        #draw
        handle_buttonG(VoButtonp, Vop)
        handle_buttonG(gButtonp, Gp)
        handle_buttonG(ThetaoButtonp, thetaop)

        handle_buttonR(VoButtonm, Vom)
        handle_buttonR(gButtonm, Gm)
        handle_buttonR(ThetaoButtonm, thetaom)

        handle_cheat(cheatButton, CheatsFunc)

        pg.draw.line(screen, Black, (x1, y1), (x1 + 1000, y1), 5)
        pg.draw.line(screen, Black, (x1, y1), (x1, y1 - 300), 5)
        angleLine()
        pg.draw.circle(screen, Yellow, (int(xpres), int(ypres)), 10)

        pg.draw.rect(screen, Blue, EndButton)

        Target()

        parabola()

        handle_start(StartButton, Fire)
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
        pg.draw.rect(screen, Blue, StartButton)
        pg.draw.rect(screen, Blue, EndButton)
        pg.draw.rect(screen, cheatbcol, cheatButton, border_radius=12)
        Target()
        angleLine()
        parabola()
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
        def handle_restart(rect, action):
            color = StartGreen
            if rect.collidepoint(mousePos):
                color = StartGreenDark
                if mousePress:
                    action()
            pg.draw.rect(screen, color, rect, border_radius=12)
        def New():
            global End, VarChoice, t, Ellx, points, pointsold, cheats
            VarChoice = True
            End = False
            cheats = False
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
        parabola()
        pg.draw.circle(screen, Yellow, (int(xpres), int(ypres)), 5)

        handle_restart(EndButton, New)
        pg.draw.rect(screen, Blue, StartButton)
        pg.draw.rect(screen, StartGreen, EndButton, border_radius=12)
        pg.draw.rect(screen, cheatbcol, cheatButton, border_radius=12)
        TextMake()

        pg.display.flip()

    while GameOver:
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
                GameOver = False

        screen.fill(White)

        def handleAgain(rect, action):
            color = StartGreen
            if rect.collidepoint(mousePos):
                color = StartGreenDark
                if mousePress:
                    action()
            pg.draw.rect(screen, color, rect, border_radius=20)


        handleAgain(Newgamebutton, PlayAgainfunc)
        Playagaintext()


        pg.display.flip()
pygame.quit()
sys.exit()
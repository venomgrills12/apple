import pygame, random, sys, os, time

pygame.init()

FPS = 30
clock = pygame.time.Clock()

#rbg #defining the colors.

RED = (255,0,0)
GREEN = (127,255,0)
BLACK = (5,5,5)
PURPLE= (178,58,238)

#length and positions of sprites

screenHEIGHT = 600
screenWIDTH = 500

x_axis1 = 300
y_axis1 = 425

x_axis2 = random.randrange(0,screenWIDTH)
y_axis2 = 10

x_axis3 = random.randrange(0,screenWIDTH)
y_axis3 = 10

x_axis4 = random.randrange(0,screenWIDTH)
y_axis4 = 10

x_axis5 = random.randrange(0,screenWIDTH)
y_axis5 = 10

velocity = 50
speed = 30

score = 0
level = 1
time = 60


backgroundfile = "bg.png"

background_x = 15
background_y = 15

pygame.key.set_repeat(100,30)

#for text

font = pygame.font.SysFont(None, 55)

#WINDOW LENGTH AND CAPTION OF WINDOW

screen = pygame.display.set_mode((screenHEIGHT,screenWIDTH))
caption = pygame.display.set_caption("Newton Under Apple")


#FALSE STATEMENTS

Closescreen = False
game_over = False

#defining the text on screen

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])
with open("hiscore.txt", "r") as f:
        hiscore = f.read()

#TIMING

clock.tick(30)

#MAIN LOOP FOR THE MOVEMENTS , SCORE AND COLLISION...

while not Closescreen:
    if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            screen.fill(PURPLE)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Closescreen = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and x_axis1 < 600 - 50 - (velocity+5):
                x_axis1 += velocity
            if event.key == pygame.K_LEFT and x_axis1 > velocity:
                x_axis1 -= velocity + 10
            if event.key == pygame.K_ESCAPE :
                Closescreen = True
        if score>int(hiscore):
            hiscore = score
    if y_axis2 > screenWIDTH:
        x_axis2 = random.randrange(0,screenHEIGHT)
        y_axis2 = 10
        score += 10
        print(score)
    y_axis2 += 10
    if y_axis3 > screenWIDTH:
        x_axis3 = random.randrange(0,screenHEIGHT)
        y_axis3 = 10
        score += 10
        print(score)
    y_axis3 += 15
    if y_axis4 > screenWIDTH:
        x_axis4 = random.randrange(0,screenHEIGHT)
        y_axis4 = 10
        score += 10
        print(score)
    y_axis4 += 12
    if y_axis5 > screenWIDTH:
        x_axis5 = random.randrange(0,screenHEIGHT)
        y_axis5 = 10
        score += 10
        print(score)
    y_axis5 += 11
    if abs(x_axis1 - x_axis2)<55 and abs(y_axis1 - y_axis2)<55:
                Closescreen = True
    if abs(x_axis1 - x_axis3)<55 and abs(y_axis1 - y_axis3)<55:
                Closescreen = True
    if abs(x_axis1 - x_axis4)<55 and abs(y_axis1 - y_axis4)<55:
                Closescreen =True
    if abs(x_axis1 - x_axis5)<55 and abs(y_axis1 - y_axis5)<55:
                Closescreen =True

    screen.fill(PURPLE)
#sprites for the game
    pygame.draw.rect(screen, BLACK, (x_axis5, y_axis5, 50,50))
    pygame.draw.rect(screen, BLACK, (x_axis4, y_axis4, 50,50))
    pygame.draw.rect(screen, BLACK, (x_axis3, y_axis3, 50,50))
    pygame.draw.rect(screen, BLACK, (x_axis2, y_axis2, 50,50))
    pygame.draw.rect(screen, RED,    (x_axis1,y_axis1, 50,50))

    pygame.display.update()

    text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), RED, 5, 5)


#screen update after every second. FPS = FRAME PER SECOND.
    pygame.display.update()
    clock.tick(FPS)

#QUIT THE WINDOW


quit()

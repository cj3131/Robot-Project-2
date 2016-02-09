import pygame
import time
import random

displayWidth = 800
displayHeight = 600

#colour definition
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
brightRed = (255,0,0)
brightBlue = (0,0,255)
brightGreen = (0,255,0)

#Initialise screen
pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("This is the window's title")
clock = pygame.time.Clock()

#Load player character images
eastImg = pygame.image.load('eastfacing.png')
eastLeftImg = pygame.image.load('eastfacingleft.png')
eastRightImg = pygame.image.load('eastfacingright.png')

westImg = pygame.image.load('westfacing.png')
westLeftImg = pygame.image.load('westfacingleft.png')
westRightImg = pygame.image.load('westfacingright.png')

northImg = pygame.image.load('northfacing.png')
northLeftImg = pygame.image.load('northfacingleft.png')
northRightImg = pygame.image.load('northfacingright.png')

southImg = pygame.image.load('southfacing.png')
southLeftImg = pygame.image.load('southfacingleft.png')
southRightImg = pygame.image.load('southfacingright.png')


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y + 50 > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render(msg, 1, (10,10,10))
    textRect = text.get_rect()
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(text, textRect)

def quitGame():
    pygame.quit()
    quit()

def writeText(text,fontType,fontSize,x,y):
    font = pygame.font.Font(fontType, fontSize)
    text = font.render(text, 1, (10,10,10))
    textRect = text.get_rect()
    textRect.center = (x,y)
    gameDisplay.blit(text, textRect)

def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(white)
            writeText('Game Title','freesansbold.ttf',100,(displayWidth/2),(displayHeight/2))
            button("Start",150,450,100,50,green,brightGreen,gameLoop)
            button("Exit",550,450,100,50,red,brightRed,quitGame)
            pygame.display.update()
            clock.tick(15)

def move(img,xcoords,ycoords):
    position = img.get_rect()
    t = 0
    if img == westImg:
        imgOne = westLeftImg
        imgTwo = westRightImg
        xChange = -1
        yChange = 0
    elif img == eastImg:
        imgOne = eastLeftImg
        imgTwo = eastRightImg
        xChange = 1
        yChange = 0
    elif img == southImg:
        imgOne = southLeftImg
        imgTwo = southRightImg
        xChange = 0
        yChange = 1
    else:
        imgOne = northLeftImg
        imgTwo = northRightImg
        xChange = 0
        yChange = -1
    while t < 31:
        for i in range(4):
            xcoords += xChange
            ycoords += yChange
            gameDisplay.fill(white)
            gameDisplay.blit(imgOne, (xcoords,ycoords))
            pygame.display.update()
            time.sleep(0.05)
            t += 1
        for i in range(4):
            xcoords += xChange
            ycoords += yChange
            gameDisplay.fill(white)
            gameDisplay.blit(img, (xcoords,ycoords))
            pygame.display.update()
            time.sleep(0.05)
            t += 1
        for i in range(4):
            xcoords += xChange
            ycoords += yChange
            gameDisplay.fill(white)
            gameDisplay.blit(imgTwo, (xcoords,ycoords))
            pygame.display.update()
            time.sleep(0.05)
            t += 1
        for i in range (4):
            xcoords += xChange
            ycoords += yChange
            gameDisplay.fill(white)
            gameDisplay.blit(img, (xcoords,ycoords))
            pygame.display.update()
            time.sleep(0.05)
            t += 1
    return xcoords,ycoords
        
def gameLoop():
    facing = southImg
    moving = None
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    facing = westImg
                    moving = True
                if event.key == pygame.K_RIGHT:
                    facing = eastImg
                    moving = True                        
                if event.key == pygame.K_UP:
                    facing = northImg
                    moving = True
                if event.key == pygame.K_DOWN:
                    facing = southImg
                    moving = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    moving = None
                    
        gameDisplay.fill(white)
        if moving == True and facing == westImg:
            move(westImg,x,y)
            x -= 32
        if moving == True and facing == eastImg:
            move(eastImg,x,y)
            x += 32
        if moving == True and facing == northImg:
            move(northImg,x,y)
            y -= 32
        if moving == True and facing == southImg:
            move(southImg,x,y)
            y += 32
        elif moving == None:
            gameDisplay.blit(facing, (x,y))
            pygame.display.update()

gameIntro()
gameLoop()
pygame.quit()
quit()
        

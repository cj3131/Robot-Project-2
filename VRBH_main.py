import pygame
import time
import random
from pygame import *

displayWidth = 800
displayHeight = 600
halfWidth = 400
halfHeight = 300

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
fps = 60
spriteGroup = pygame.sprite.Group()

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
mapImg = pygame.image.load('mainMap.png')

class Camera(object):
    def __init__(self, cameraFunc, width, height):
        self.cameraFunc = cameraFunc
        self.state = pygame.rect.Rect((0, 0, width, height))

    def apply(self, target):

        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.cameraFunc(self.state, target.rect)

##class Entity(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("walking.wav")
        self.xchange = 0
        self.ychange = 0

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def setImage(self, filename):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

    def playSound(self):
        self.sound.play()

    def move(self, direction):
        t = 0
        xtemp = 0
        ytemp = 0
        if direction == "west":
            imgOne = westImg
            imgTwo = westLeftImg
            imgThree = westRightImg
            xChange = -1
            yChange = 0
        elif direction == "east":
            imgOne = eastImg
            imgTwo = eastLeftImg
            imgThree = eastRightImg
            xChange = 1
            yChange = 0
        elif direction == "south":
            imgOne = southImg
            imgTwo = southLeftImg
            imgThree = southRightImg
            xChange = 0
            yChange = 1
        else:
            imgOne = northImg
            imgTwo = northLeftImg
            imgThree = northRightImg
            xChange = 0
            yChange = -1
        if (self.rect.x + xChange) < 65 or (self.rect.x + xChange) > 704 or (self.rect.y + yChange) < 65 or (self.rect.y + yChange) > 833:
            print("collided")
            self.image = imgOne
            gameDisplay.fill(white)
            gameDisplay.blit(mapImg,(0,0))
            spriteGroup.draw(gameDisplay)
            pygame.display.update()
        else:
            while t < 31:
                for i in range(4):
                    self.rect.x += xChange
                    self.rect.y += yChange
                    xtemp = self.rect.x
                    ytemp = self.rect.y
                    self.image = imgTwo
                    self.rect.x = xtemp
                    self.rect.y = ytemp
                    gameDisplay.fill(white)
                    gameDisplay.blit(mapImg,(0,0))
                    spriteGroup.draw(gameDisplay)
                    pygame.display.update()
                    pygame.time.delay(30)
                    t += 1
                #self.playSound()
                for i in range(4):
                    self.rect.x += xChange
                    self.rect.y += yChange
                    xtemp = self.rect.x
                    ytemp = self.rect.y
                    self.image = imgOne
                    self.rect.x = xtemp
                    self.rect.y = ytemp
                    gameDisplay.fill(white)
                    gameDisplay.blit(mapImg,(0,0))
                    spriteGroup.draw(gameDisplay)
                    pygame.display.update()
                    pygame.time.delay(30)
                    t += 1
                for i in range(4):
                    self.rect.x += xChange
                    self.rect.y += yChange
                    xtemp = self.rect.x
                    ytemp = self.rect.y
                    self.image = imgThree
                    self.rect.x = xtemp
                    self.rect.y = ytemp
                    gameDisplay.fill(white)
                    gameDisplay.blit(mapImg,(0,0))
                    spriteGroup.draw(gameDisplay)
                    pygame.display.update()
                    pygame.time.delay(30)
                    t += 1
                for i in range (4):
                    self.rect.x += xChange
                    self.rect.y += yChange
                    xtemp = self.rect.x
                    ytemp = self.rect.y
                    self.image = imgOne
                    self.rect.x = xtemp
                    self.rect.y = ytemp
                    gameDisplay.fill(white)
                    gameDisplay.blit(mapImg,(0,0))
                    spriteGroup.draw(gameDisplay)
                    pygame.display.update()
                    pygame.time.delay(30)
                    t += 1

def simpleCamera(camera, targetRect):
    l, t, _, _ = targetRect
    _, _, w, h = camera
    return pygame.Rect(-1 + halfWidth, -t + halfHeight, w, h)
                

        
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

        
def gameLoop():
    pc = Player()
    pc.setImage("southfacing.png")
    pc.setPosition(193,97)
    
    spriteGroup.add(pc)
    spriteGroup.draw(gameDisplay)
    
    facing = southImg
    moving = None
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)
    #camera = Camera(simpleCamera, displayWidth, displayHeight)
    gameDisplay.blit(mapImg,(0,0))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    facing = westImg
                    moving = True
                    pc.move("west")
                if event.key == pygame.K_RIGHT:
                    facing = eastImg
                    moving = True
                    pc.move("east")
                if event.key == pygame.K_UP:
                    facing = northImg
                    moving = True
                    pc.move("north")
                if event.key == pygame.K_DOWN:
                    facing = southImg
                    moving = True
                    pc.move("south")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    moving = None
                    
        #gameDisplay.fill(white)
##        if moving == True and facing == westImg:
##            move(westImg,x,y,camera)
##            x -= 32
##        if moving == True and facing == eastImg:
##            move(eastImg,x,y,camera)
##            x += 32
##        if moving == True and facing == northImg:
##            move(northImg,x,y,camera)
##            y -= 32
##        if moving == True and facing == southImg:
##            move(southImg,x,y,camera)
##            y += 32
        if moving == None:
            spriteGroup.draw(gameDisplay)
            #gameDisplay.blit(facing, (x,y))
            pygame.display.update()

        clock.tick(fps)
        #window.fill(white)
        pygame.display.update
        
gameIntro()
gameLoop()
pygame.quit()
quit()
        

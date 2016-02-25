import pygame
import time
import random
from pygame import *

displayWidth = 800
displayHeight = 600
halfWidth = 400
halfHeight = 300
quadOne = (0,0)
quadTwo = (-800,0)
quadThree = (0,-352)
quadFour = (-800,-352)

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
pygame.display.set_caption("Bargain Hunter!")
clock = pygame.time.Clock()
fps = 60

spriteGroup = pygame.sprite.Group()
coinGroup = pygame.sprite.Group()
currentCoinGroup = pygame.sprite.Group()
currentSpriteGroup = pygame.sprite.Group()


#f = open("E:\\Python scripts\\mainVRBH\\images\\mainmap.png")

#Load player character, map, menu, and other interface images
eastImg = pygame.image.load('images/eastfacing.png')
eastLeftImg = pygame.image.load('images/eastfacingleft.png')
eastRightImg = pygame.image.load('images/eastfacingright.png')

westImg = pygame.image.load('images/westfacing.png')
westLeftImg = pygame.image.load('images/westfacingleft.png')
westRightImg = pygame.image.load('images/westfacingright.png')

northImg = pygame.image.load('images/northfacing.png')
northLeftImg = pygame.image.load('images/northfacingleft.png')
northRightImg = pygame.image.load('images/northfacingright.png')

southImg = pygame.image.load('images/southfacing.png')
southLeftImg = pygame.image.load('images/southfacingleft.png')
southRightImg = pygame.image.load('images/southfacingright.png')

#mapImg = pygame.image.load('mainmap.png')
mapImg = pygame.image.load("images/mainmap.png")
shopImg = pygame.image.load('images/shopinteriorone.png')
startImg = pygame.image.load('images/startmenu.png')
scrollImg = pygame.image.load('images/scrollhorizontal.png')
coinImg = pygame.image.load('images/coinone.png')

#Not currently used
class Level:
    
    def __init__(self):

        self.image = pygame.Surface((1600,960))
        self.rect = self.image.get_rect()
        self.worldShiftx = 0
        self.leftViewbox = halfWidth - displayWidth/8
        self.rightViewbox = halfWidth + displayWidth/8

    def shiftWorld(self, shiftx):

        self.worldShiftx += shiftx
        self.rect.x += shiftx
        gameDisplay.blit(mapImg,(self.rect.x,0))

#Not currently used
class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((800,600))
        self.rect = self.image.get_rect()

#Will probably need to be used to move the NPC character in shops around.
class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.xchange = 0
        self.ychange = 0

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect()

    def setImage(self, filename):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

    def setPosition(self,x,y):
        self.rect.x = x
        self.rect.y = y
        

#Deals with the player character's movement, and changing of map quadrants
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        #self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.xchange = 0
        self.ychange = 0
        #self.sound = pygame.mixer.Sound("walking.wav")
        self.sector = "topleft"
        self.collided = False
        self.quadrant = (0,0)
        self.coins = 0
        self.collected = []

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
            

        if self.sector == "topleft":
            if (self.rect.x + xChange) < 65 or (self.rect.y + yChange) < 65:
                print("collided")
                self.collided = True
                self.quadrant = (0,0)
                

            elif (self.rect.x + xChange) > 769:
                self.sector = "topright"
                self.rect.x = -31
                self.collided = False
            elif (self.rect.y + yChange) > 577:
                self.sector = "bottomleft"
                self.rect.y = 225
                self.collided = False
            elif (self.rect.x > 350) and (self.rect.y > 350):
                #check that coin is not in collected. if it is, pass. if it isn't,
                #add it to collected and currentSpriteGroup.  increase self.coins
                self.collected.append(c1)
                print(self.collected)
            else:
                self.collided = False
                
        elif self.sector == "topright":
            if (self.rect.x + xChange) > 705 or (self.rect.y + yChange) < 97:
                print("collided")
                self.collided = True
                self.quadrant = (-800,0)

            elif (self.rect.x + xChange) < 1:
                self.sector = "topleft"
                self.rect.x = 801
                self.collided = False
            elif (self.rect.y + yChange) > 577:
                self.sector = "bottomright"
                self.rect.y = 1
                self.collided = False
            else:
                self.collided = False

        elif self.sector == "bottomleft":
            if (self.rect.x + xChange) < 65 or (self.rect.y + yChange) > 481:
                print("collided")
                self.collided = True
                self.quadrant = (0,-352)

            elif self.rect.x == 161 or self.rect.x == 193:
                if 417 < self.rect.y + yChange < 449:
                    #Needs copying to other sectors
                    shopInterior(imgOne,shopImg)
                    self.rect.x, self.rect.y = 161, 449
                    yChange = 1

            elif (self.rect.x + xChange) > 768:
                self.sector = "bottomright"
                self.rect.x = 1
                self.collided = False
            elif (self.rect.y + yChange) < 1:
                self.sector = "topleft"
                self.rect.y = 353
                self.collided = False
            else:
                self.collided = False

        elif self.sector == "bottomright":
            if (self.rect.x + xChange) > 705 or (self.rect.y + yChange) > 473:
                print("collided")
                self.collided = True
                self.quadrant = (-800,-352)

            elif (self.rect.x + xChange) < 1:
                self.sector = "bottomleft"
                self.rect.x = 801
                self.collided = False
            elif (self.rect.y + yChange) < 1:
                self.sector = "topright"
                self.rect.y = 369
                self.collided = False
            else:
                self.collided = False


        if self.collided == True:
            self.image = imgOne
            gameDisplay.fill(white)
            gameDisplay.blit(mapImg,(self.quadrant))
            spriteGroup.draw(gameDisplay)
            pygame.display.update()
        else:
            while t < 31:

                for i in range(4):
                    self.image = imgTwo
                    self.rect.x, self.rect.y = update(self.rect.x, self.rect.y, xChange, yChange, spriteGroup, self.sector, mapImg, currentSpriteGroup)
                    pygame.time.delay(5)
                    t += 1

                for i in range(4):
                    self.image = imgOne
                    self.rect.x, self.rect.y = update(self.rect.x, self.rect.y, xChange, yChange, spriteGroup, self.sector, mapImg, currentSpriteGroup)
                    pygame.time.delay(5)
                    t += 1

                for i in range(4):
                    self.image = imgThree
                    self.rect.x, self.rect.y = update(self.rect.x, self.rect.y, xChange, yChange, spriteGroup, self.sector, mapImg, currentSpriteGroup)
                    pygame.time.delay(5)
                    t += 1

                for i in range (4):
                    self.image = imgOne
                    self.rect.x, self.rect.y = update(self.rect.x, self.rect.y, xChange, yChange, spriteGroup, self.sector, mapImg, currentSpriteGroup)
                    pygame.time.delay(5)
                    t += 1
            xChange = 0
            yChange = 0
            print(self.rect)

#This function should be called every time something happens, i.e when the character moves.
def update(posx, posy, xChange, yChange, spriteGroup, sect, img, currentSpriteGroup):
    posx += xChange
    posy += yChange
    gameDisplay.fill(white)
    #currentspriteGroup needs pc added
    currentSpriteGroup.add(pc,c1,c2,c3)

    if sect == "topleft":
        gameDisplay.blit(img, (0,0))        
    elif sect == "topright":
        gameDisplay.blit(img, (-800,0))
    elif sect == "bottomleft":
        gameDisplay.blit(img, (0,-352))
    elif sect == "bottomright":
        gameDisplay.blit(img, (-800,-352))

    #spriteGroup.draw(gameDisplay)
    currentSpriteGroup.draw(gameDisplay)
    pygame.display.update()

    return posx, posy

#This function should run when entering a shop. 
def shopInterior(player, shopBackground):
    inside = True
    pc.rect.x = 416
    pc.rect.y = 544
    gameDisplay.fill(white)
    gameDisplay.blit(shopBackground, (0,0))
    gameDisplay.blit(scrollImg, (80,0))
    spriteGroup.draw(gameDisplay)
    writeText("Hello. How long do you", "freesansbold.ttf", 36, 160,80)
    writeText("want me to search for?", "freesansbold.ttf", 36, 160,110)
    writeText("1 minute", "freesansbold.ttf", 24, 160, 300)
    writeText("2 minutes", "freesansbold.ttf", 24, 270, 300)
    writeText("3 minutes", "freesansbold.ttf", 24, 380, 300)
    writeText("Exit", "freesansbold.ttf", 24, 500, 300)
    writeText("(costs 1 coin)", "freesansbold.ttf", 24, 160, 340)
    writeText("(costs 2 coins)", "freesansbold.ttf", 24, 270, 340)
    writeText("(costs 3 coins)", "freesansbold.ttf", 24, 380, 340)
    pygame.display.update()

    #Here we check the user's option choice
    while inside == True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)
        pygame.time.delay(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if click[0] == 1:
                if 100 <= mouse[0] <= 250 and 500 <= mouse[1] <= 600:
                    print("START PATHFINDING STUFF HERE. ABOVE BUTTON CO-ORDINATES NEED TO BE CHANGED")

#If the user clicks within the given co-ords, the passed function will run
def button(x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + 48 > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()

def quitGame():
    pygame.quit()
    quit()

#Guess what this does
def writeText(text,fontType,fontSize,x,y):
    font = pygame.font.Font(fontType, fontSize)
    text = font.render(text, 1, (10,10,10))
    textRect = text.get_rect()
    textRect = (x,y)
    gameDisplay.blit(text, textRect)

#Main menu function
def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(white)    
            gameDisplay.blit (startImg, (0,0))
            button (5,526,105,48,gameLoop)
            button (438,526,105,48,quitGame)
            pygame.display.update()
            clock.tick(15)


def gameLoop():
    #background = Level()
    gameDisplay.fill(white)
    
    pc.setImage("images/southfacing.png")
    pc.setPosition(193,97)
    spriteGroup.add(pc)


    
    
    for i in currentCoinGroup:
        i.setImage("images/coinone.png")

    for i in currentCoinGroup:
        i.setPosition(350, 350)
    
    facing = southImg
    moving = None
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)
    gameDisplay.blit(mapImg,(0,0))
##    gameDisplay.blit(coinImg, (385, 97))
##    gameDisplay.blit(coinImg, (673, 97))
##    gameDisplay.blit(coinImg, (545, 289))
    spriteGroup.draw(gameDisplay)
    currentCoinGroup.draw(gameDisplay)
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
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

        # if moving == None:
        #     spriteGroup.draw(gameDisplay)
        #     pygame.display.update()

        clock.tick(fps)
        
pc = Player()
c1,c2,c3,c4,c5,c6,c7,c8,c9 = Coin(),Coin(),Coin(),Coin(),Coin(),Coin(),Coin(),Coin(),Coin()
coinGroup.add(c1,c2,c3,c4,c5,c6,c7,c8,c9)
currentCoinGroup.add(c1,c2,c3)
gameIntro()
pygame.quit()
quit()

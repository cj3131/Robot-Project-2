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

#Load player character, NPC, map, menu, and other interface images
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


shopkeepEastImg = pygame.image.load('images/shopkeepeastfacing.png') 
shopkeepEastLeftImg = pygame.image.load('images/shopkeepeastfacingleft.png') 
shopkeepEastRightImg = pygame.image.load('images/shopkeepeastfacingright.png') 

shopkeepWestImg = pygame.image.load('images/shopkeepwestfacing.png')
shopkeepWestLeftImg = pygame.image.load('images/shopkeepwestfacingleft.png') 
shopkeepWestRightImg = pygame.image.load('images/shopkeepwestfacingright.png') 

shopkeepNorthImg = pygame.image.load('images/shopkeepnorthfacing.png') 
shopkeepNorthLeftImg = pygame.image.load('images/shopkeepnorthfacingleft.png') 
shopkeepNorthRightImg = pygame.image.load('images/shopkeepnorthfacingright.png') 

shopkeepSouthImg = pygame.image.load('images/shopkeepsouthfacing.png') 
shopkeepSouthLeftImg = pygame.image.load('images/shopkeepsouthfacingleft.png') 
shopkeepSouthRightImg = pygame.image.load('images/shopkeepsouthfacingright.png') 


mapImg = pygame.image.load("images/mainmap.png")
shopImg = pygame.image.load('images/shopinteriorone.png')
startImg = pygame.image.load('images/startmenu.png')
scrollImg = pygame.image.load('images/scrollhorizontal.png')
coinImg = pygame.image.load('images/coinone.png')

#Not currently used
# class Level:
    
#     def __init__(self):

#         self.image = pygame.Surface((1600,960))
#         self.rect = self.image.get_rect()
#         self.worldShiftx = 0
#         self.leftViewbox = halfWidth - displayWidth/8
#         self.rightViewbox = halfWidth + displayWidth/8

#     def shiftWorld(self, shiftx):

#         self.worldShiftx += shiftx
#         self.rect.x += shiftx
#         gameDisplay.blit(mapImg,(self.rect.x,0))

# #Not currently used
# class Shop(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((800,600))
#         self.rect = self.image.get_rect()

#Will probably need to be used to move the NPC character in shops around.
class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.xchange = 0
        self.ychange = 0

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def setImage(self,filename):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()


#A sprite to be used in detecting when the player character picks up a coin. (Not implemented yet)
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
            elif (self.rect.x == 545) and (self.rect.y == 289):
                #check that coin is not in collected. if it is, pass. if it isn't,
                #add it to collected and currentSpriteGroup.  increase self.coins. 
                #not yet implemented
                print("you got a coin")
                self.collected.append(c1)
                print(self.collected)
            else:
                self.collided = False
                
        elif self.sector == "topright":
            if (self.rect.x + xChange) > 705 or (self.rect.y + yChange) < 65:
                print("collided")
                self.collided = True
                self.quadrant = (-800,0)

            elif ( (self.rect.x == 609) and (193 < self.rect.y + yChange < 225) ) or ( (self.rect.x == 641) and (193 < self.rect.y + yChange < 225) ):
                shopInterior(imgOne,shopImg)
                self.rect.x, self.rect.y = 641,193
                yChange = 1

            elif (self.rect.x + xChange) < 1:
                self.sector = "topleft"
                self.rect.x = 801
                self.collided = False
            elif (self.rect.y + yChange) > 577:
                self.sector = "bottomright"
                self.rect.y = 225
                self.collided = False
            else:
                self.collided = False

        elif self.sector == "bottomleft":
            if (self.rect.x + xChange) < 65 or (self.rect.y + yChange) > 481:
                print("collided")
                self.collided = True
                self.quadrant = (0,-352)

            elif ( (self.rect.x == 161) and (417 < self.rect.y + yChange < 449) ) or ( (self.rect.x == 193) and (417 < self.rect.y + yChange < 449) ):
                shopInterior(imgOne,shopImg)
                self.rect.x, self.rect.y = 161, 449
                yChange = 1

            elif (self.rect.x + xChange) > 768:
                self.sector = "bottomright"
                self.rect.x = -31
                self.collided = False
            elif (self.rect.y + yChange) < 1:
                self.sector = "topleft"
                self.rect.y = 353
                self.collided = False
            else:
                self.collided = False

        elif self.sector == "bottomright":
            if (self.rect.x + xChange) > 705 or (self.rect.y + yChange) > 481:
                print("collided")
                self.collided = True
                self.quadrant = (-800,-352)

            elif ((self.rect.x == 545) and (417 < self.rect.y + yChange < 449)) or ((self.rect.x == 577) and (417 < self.rect.y + yChange < 449)):
                shopInterior(imgOne,shopImg)
                self.rect.x, self.rect.y = 577,449
                yChange = 1

            elif (self.rect.x + xChange) < 1:
                self.sector = "bottomleft"
                self.rect.x = 801
                self.collided = False
            elif (self.rect.y + yChange) < 1:
                self.sector = "topright"
                self.rect.y = 353
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
    result = False
    pc.rect.x = 417
    pc.rect.y = 545
    gameDisplay.fill(white)
    gameDisplay.blit(shopBackground, (0,0))
    gameDisplay.blit(scrollImg, (80,0))
    shopkeeper = NPC()
    shopkeeper.setImage("images/shopkeepsouthfacing.png")
    shopkeeper.setPosition(416, 481)
    spriteGroup.add(shopkeeper)
    spriteGroup.draw(gameDisplay)
    writeText("Hello. How long do you", "freesansbold.ttf", 36, 160,80)
    writeText("want me to search for?", "freesansbold.ttf", 36, 160,120)
    writeText("1 minute", "freesansbold.ttf", 24, 160, 300)
    writeText("2 minutes", "freesansbold.ttf", 24, 290, 300)
    writeText("3 minutes", "freesansbold.ttf", 24, 425, 300)
    writeText("Exit", "freesansbold.ttf", 24, 565, 300)
    writeText("(costs 1 coin)", "freesansbold.ttf", 16, 160, 325)
    writeText("(costs 2 coins)", "freesansbold.ttf", 16, 290, 325)
    writeText("(costs 3 coins)", "freesansbold.ttf", 16, 425, 325)
    pygame.display.update()

    #Here we check the user's option choice
    while inside == True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            result = button (160, 300, 110, 50, result)
            if result == True:
                print("1 minute")
            result = button(290, 300, 110, 50, result)
            if result == True:
                print("2 minutes")
            result = button(425, 300, 110, 50, result)
            if result == True:
                print("3 minutes")
            result = button(565, 300, 110, 25, result)
            if result == True:
                print("Exit")
                shopkeeper.remove(spriteGroup)
                return

#If the user clicks within the given co-ords, the passed function will run
def button(x,y,w,h,chosen):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    chosen = False
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1:
            chosen = True
    return chosen

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
    result = False
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.fill(white)    
            gameDisplay.blit (startImg, (0,0))
            result = button (5,526,105,48,result)
            if result == True:
                return
            result = button (438,526,105,48,result)
            if result == True:
                pygame.quit()
                quit()
            pygame.display.update()
            clock.tick(15)


def gameLoop():
    #background = Level()
    gameDisplay.fill(white)
    pc.setImage("images/southfacing.png")
    pc.setPosition(193, 97)
    spriteGroup.add(pc)
    for i in currentCoinGroup:
        i.setImage("images/coinone.png")

    # for i in currentCoinGroup:
    #     i.setPosition(350, 350)
    
    facing = southImg
    moving = None
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)
    gameDisplay.blit(mapImg,(0,0))
##    gameDisplay.blit(coinImg, (385, 97))
##    gameDisplay.blit(coinImg, (673, 97))
##    gameDisplay.blit(coinImg, (545, 289))
    spriteGroup.draw(gameDisplay)
    c1.setPosition(545, 289)
    c2.setPosition(673, 97)
    c3.setPosition(385, 97)
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
gameLoop()
pygame.quit()
quit()

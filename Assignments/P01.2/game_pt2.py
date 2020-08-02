import pygame
import random
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('RedRight.png')]
walkLeft = [pygame.image.load('RedLeft.png')]
walkUp = [pygame.image.load('RedUp.png')]
walkDown = [pygame.image.load('RedDown.png')]
char = pygame.image.load('RedRight.png')
screenRefresh = True

clock = pygame.time.Clock()

class Background():
    def __init__(self):
        self.dimensions = 0

    def setTiles(self,tiles):
        if type(tiles) is str:
            self.tiles = [[pygame.image.load(tiles)]]
            self.dimensions = 0
        elif type(tiles[0]) is str:
            self.tiles = [[pygame.image.load(i) for i in tiles],None]
            self.dimensions = 1
        else:
            self.tiles = [ [pygame.image.load(i) for i in row] for row in tiles]
            self.dimensions = 2
        self.stagePosX = 0
        self.stagePosY = 0
        self.tileWidth = self.tiles[0][0].get_width()
        self.tileHeight = self.tiles[0][0].get_height()
        win.blit(self.tiles[0][0],[0,0])
        self.surface = win.copy()

    def scroll(self,x,y):
        self.stagePosX -= x
        self.stagePosY -= y
        col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        xOff = (0 - self.stagePosX%self.tileWidth)
        row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
        yOff = (0 - self.stagePosY % self.tileHeight)

        col2 = ((self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        row2 = ((self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
        win.blit(self.tiles[row][col], [xOff, yOff])
        win.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
        win.blit(self.tiles[row2][col], [xOff, yOff+self.tileHeight])
        win.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])

        self.surface = win.copy()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False 
        self.up = False
        self.down = False
        self.walkCount = 0

    def draw(self,win):
        if self.walkCount + 1 >= 15:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[0], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[0], (self.x,self.y))
            self.walkCount += 1
        elif self.up:
            win.blit(walkUp[0], (self.x,self.y))
            self.walkCount += 1
        elif self.down:
            win.blit(walkDown[0], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))

class Orb(object):
    floating = [pygame.image.load('Orb1.png'), pygame.image.load('Orb2.png'), pygame.image.load('Orb3.png'), pygame.image.load('Orb4.png'), pygame.image.load('Orb5.png')]
    
    def __init__(self):
        self.x = random.randrange(0,500)
        self.y = random.randrange(0,500)
        self.orbNum = random.randrange(0,5)

    def draw(self,win):
        win.blit(self.floating[self.orbNum], (self.x, self.y))

def redrawGameWindow():
    # win.blit(background, (0,0))
    player.draw(win)
    orb1.draw(win)
    orb2.draw(win)
    orb3.draw(win)
    orb4.draw(win)
    orb5.draw(win)
    pygame.display.update()

def scrollBackground(x,y):
    global background
    background.scroll(x,y)

def setAutoUpdate(val):
    global screenRefresh
    screenRefresh = val

def setBackgroundImage(img):
    global bgSurface, backgroundImage
    surf = pygame.image.load(img)
    backgroundImage = surf
    win.blit(surf, [0, 0])
    bgSurface = win.copy()
    if screenRefresh:
        pygame.display.update()
    global background
    background = Background()
    background.setTiles(img)

#Main Loop
player = Player(300, 410, 64, 64)
orb1 = Orb()
orb2 = Orb()
orb3 = Orb()
orb4 = Orb()
orb5 = Orb()
setBackgroundImage( "background.png" )
setAutoUpdate(False)



run = True
while run:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.vel:
        #player.x -= player.vel
        scrollBackground(5,0)
        player.left = True
        player.right = False
        player.up = False
        player.down = False

    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
        #player.x += player.vel
        scrollBackground(-5,0)
        player.left = False
        player.right = True
        player.up = False
        player.down = False

    elif keys[pygame.K_UP] and player.y > player.vel:
        #player.y -= player.vel
        scrollBackground(0,5)
        player.left = False
        player.right = False
        player.up = True
        player.down = False

    elif keys[pygame.K_DOWN] and player.y < 500 - player.height - player.vel:
        #player.y += player.vel
        scrollBackground(0,-5)
        player.left = False
        player.right = False
        player.up = False
        player.down = True

    else:
        player.left = False
        player.right = False
        player.up = False
        player.down = False
        player.walkCount = 0
    
    redrawGameWindow()

pygame.quit()
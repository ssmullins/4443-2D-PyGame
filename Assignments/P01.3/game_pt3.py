import pygame
import random
pygame.init()

gameWidth = 500
gameHeight = 500

win = pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('Images/Frame1r.png'), pygame.image.load('Images/Frame2r.png'), pygame.image.load('Images/Frame3r.png'), pygame.image.load('Images/Frame4r.png'), pygame.image.load('Images/Frame5r.png'), pygame.image.load('Images/Frame6r.png'), pygame.image.load('Images/Frame7r.png'), pygame.image.load('Images/Frame8r.png')]
walkLeft = [pygame.image.load('Images/Frame1l.png'), pygame.image.load('Images/Frame2l.png'), pygame.image.load('Images/Frame3l.png'), pygame.image.load('Images/Frame4l.png'), pygame.image.load('Images/Frame5l.png'), pygame.image.load('Images/Frame6l.png'), pygame.image.load('Images/Frame7l.png'), pygame.image.load('Images/Frame8l.png')]
walkUp = [pygame.image.load('Images/Frame1u.png'), pygame.image.load('Images/Frame2u.png'), pygame.image.load('Images/Frame3u.png'), pygame.image.load('Images/Frame4u.png'), pygame.image.load('Images/Frame5u.png'), pygame.image.load('Images/Frame6u.png'), pygame.image.load('Images/Frame7u.png'), pygame.image.load('Images/Frame8u.png')]
walkDown = [pygame.image.load('Images/Frame1d.png'), pygame.image.load('Images/Frame2d.png'), pygame.image.load('Images/Frame3d.png'), pygame.image.load('Images/Frame4d.png'), pygame.image.load('Images/Frame5d.png'), pygame.image.load('Images/Frame6d.png'), pygame.image.load('Images/Frame7d.png'), pygame.image.load('Images/Frame8d.png')]
char = pygame.image.load('Images/Frame1r.png')
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
        self.vel = 20
        self.left = False
        self.right = False 
        self.up = False
        self.down = False
        self.walkCount = 0

    def draw(self,win):
        global walkCount
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 4], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 4], (self.x,self.y))
            self.walkCount += 1
        elif self.up:
            win.blit(walkUp[self.walkCount // 4], (self.x,self.y))
            self.walkCount += 1
        elif self.down:
            win.blit(walkDown[self.walkCount // 4], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))

class Orb(object):
    floating = [pygame.image.load('Images/Orb1.png'), pygame.image.load('Images/Orb2.png'), pygame.image.load('Images/Orb3.png'), pygame.image.load('Images/Orb4.png'), pygame.image.load('Images/Orb5.png')]
    
    def __init__(self):
        self.x = random.randrange(0,gameWidth)
        self.y = random.randrange(0,gameHeight)
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
player = Player(gameWidth // 2, gameHeight // 2, 64, 64)
orb1 = Orb()
orb2 = Orb()
orb3 = Orb()
orb4 = Orb()
orb5 = Orb()
setBackgroundImage( "Images/background.png" )
setAutoUpdate(False)



run = True
while run:
    clock.tick(33)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.vel:
        # player.x -= player.vel
        scrollBackground(5,0)
        player.left = True
        player.right = False
        player.up = False
        player.down = False

    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
        # player.x += player.vel
        scrollBackground(-5,0)
        player.left = False
        player.right = True
        player.up = False
        player.down = False

    elif keys[pygame.K_UP] and player.y > player.vel:
        # player.y -= player.vel
        scrollBackground(0,5)
        player.left = False
        player.right = False
        player.up = True
        player.down = False

    elif keys[pygame.K_DOWN] and player.y < 500 - player.height - player.vel:
        # player.y += player.vel
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
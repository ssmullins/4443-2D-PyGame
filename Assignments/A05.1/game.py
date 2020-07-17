import pygame
import random
import os
import sys
import math
import pprint
import json

# Tells OS where to open the window
os.environ['SDL_VIDEO_WINDOW_POS'] = str(300) + "," + str(100)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

from helper_module import load_colors
from helper_module import mykwargs
from helper_module import straightDistance

colors = load_colors('colors.json')
FPS = 120

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(os.path.join(img_folder, "bg_shroom.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image = pygame.transform.scale(self.image, (int(kwargs['pwidth']), int(kwargs['pheight'])))
        self.image.set_colorkey((colors['black']['rgb']))
        self.rect = self.image.get_rect()
        self.rect.center = (int(int(kwargs['width']) / 2), int(int(kwargs['height']) /2))
        self.y_speed = 5

    def update(self):
            self.vx, self.vy = 0,0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP] and self.check_collisions == (False,False):
                self.vy = -5
            if keystate[pygame.K_DOWN]:
                self.vy = 5
            if keystate[pygame.K_LEFT]:
                self.vx = -5
            if keystate[pygame.K_RIGHT]:
                self.vx = 5
            if self.vx != 0 and self.vy !=0:
                self.vx /= 1.414
                self.vy /= 1.414

            self.rect.x += self.vx
            self.rect.y += self.vy

    def check_collisions(self):
        hit_xbounds = False
        hit_ybounds = False

        if self.rect.right >= int(kwargs['width']) or self.rect.left <= 0:
            hit_xbounds = True

        if self.rect.top <= 0 or self.rect.bottom >= int(kwargs['height']):
            hit_ybounds = True

        return hit_xbounds, hit_ybounds

def main(**kwargs):
    pygame.init()
    pygame.mixer.init()

    width = int(kwargs['width'])
    height = int(kwargs['height'])

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(kwargs['title'])
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    BackGround = Background('background_image.png', [0,0])

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Update
        all_sprites.update()
        # Draw / render
        screen.fill([255,255,255])
        screen.blit(BackGround.image, BackGround.rect)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

def usage():
    # Params in square brackets are optional
    # The kwargs function script needs key=value to NOT have spaces
    print("Usage: python basic.py title=string img_path=string width=int height=int [jsonfile=string]")
    print("Example:\n\n\t python basic.py title='Game 1' img_path=./sprite.png width=640 height=480 \n")
    sys.exit()

if __name__=='__main__':
    """
    This example has 4 required parameters, so after stripping the file name out of
    the list argv, I can test the len() of argv to see if it has 4 params in it.
    """
    argv = sys.argv[1:]

    if len(argv) < 6:
        print(len(argv))
        usage()

    args,kwargs = mykwargs(argv)

    # here you have a dictionary with all your parameters in it
    print("Printing dictionary from name == main:")
    pprint.pprint(kwargs)

    # you could send all of them to a main function
    main(**kwargs)
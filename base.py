import pygame, sys
from pygame.locals import *

sp_val = 1
speed = [1, 1]
width = 500
height = 300
size = (width, height)
up = [0, -sp_val]
down = [0, sp_val]
left = [-sp_val, 0]
right = [sp_val, 0]
black = (0, 0, 0)
# ball = pygame.image.load('ball.jpeg')
# ball_rect = ball.get_rect()
screen = pygame.display.set_mode(size)


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super(Snake, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.rect = self.surf.get_rect()
        self.surf.fill((255, 255, 255))
        self.direction = right

    # overriding the update() function  to update the sprites position
    def update(self, direction):
        self.direction = direction


class Food(pygame.sprite.Sprite):

    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface(10, 10)
        self.rect = self.surf.get_rect()


segs = pygame.sprite.Group()

# this function will create a segment and assign its position on the snake
def create_seg():
    seg = Snake()
    segs.add(seg)


# this function is supposed to update the position of all the segments
def update_segs(direction):
    for seg in segs:
        seg.update(direction)


# this function ensures that the snake remains within the screen
def constraint(object):
    if object.right> width:
        object.right = 0
    if object.top > height:
        object.top = 0


if __name__ == '__main__':
    # initialise the game
    pygame.init()
    create_seg()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # check for events then change the direction attribute for the snake
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    update_segs(down)
                if event.key == K_UP:
                    update_segs(up)
                if event.key == K_RIGHT:
                    update_segs(right)
                if event.key == K_LEFT:
                    update_segs(left)

            # erase the screen by rewriting with black color
            screen.fill(black)
            for seg in segs:
                constraint(seg)
                screen.blit(seg.surf, seg.rect)
            pygame.display.flip()



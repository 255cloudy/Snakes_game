import pygame, sys
import random
from pygame.locals import *

sp_val = 1
speed = [1, 1]
width = 800
height = 400
food_color = [255, 100, 100]
size = (width, height)
up = [0, -sp_val]
down = [0, sp_val]
left = [-sp_val, 0]
right = [sp_val, 0]
black = (100, 100, 100)
direct = right
# ball = pygame.image.load('ball.jpeg')
# ball_rect = ball.get_rect()
screen = pygame.display.set_mode(size)


class Segment(pygame.sprite.Sprite):

    def __init__(self):
        super(Segment, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.rect = self.surf.get_rect()
        self.surf.fill((255, 255, 255))
        self.right = self.rect.right
        self.left = self.rect.left
        self.top = self.rect.right
        self.bottom = self.rect.bottom
        self.direction = direct

    # overriding the update() function  to update the sprites direction
    def update(self, direction):
        self.direction = direction
        self.move()
        contsr(self)

    # function changes the position of a segment of the snake
    def move(self):
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]


class Food(pygame.sprite.Sprite):

    def __init__(self):
        super(Food, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill(food_color)
        self.rect = self.surf.get_rect()
        self.rect.x = random.randint(1, width)
        self.rect.y = random.randint(1, height)


segs = pygame.sprite.Group()
foods = pygame.sprite.Group()


# this function will create a segment and assign its position on the snake
def create_seg():
    seg = Segment()
    segs.add(seg)


# this function helps us create a food object
def create_food():
    food = Food()
    foods.add(food)


# function checks to ensure that the segments are within the window
def contsr(seg):
    if seg.rect.x > width:
        seg.rect.x = 0
    if seg.rect.x < 0:
        seg.rect.x = width
    if seg.rect.y > height:
        seg.rect.y = 0
    if seg.rect.y < 0:
        seg.rect.y = height


if __name__ == '__main__':
    # initialise the game
    pygame.init()
    create_seg()
    food = Food()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # check for events then change the direction attribute for the snake
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    direct = down
                if event.key == K_UP:
                    direct = up
                if event.key == K_RIGHT:
                    direct = right
                if event.key == K_LEFT:
                    direct = left

        segs.update(direct)
        # erase the screen by rewriting with black color
        screen.fill(black)
        for seg in segs:
            screen.blit(seg.surf, seg.rect)
        screen.blit(food.surf, food.rect)
        pygame.display.flip()



import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game!!')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BORDER_WIDTH = 10
BORDER = pygame.Rect((WIDTH//2)-(BORDER_WIDTH//2), 0, BORDER_WIDTH, HEIGHT)

# sound effects when shooting and getting hit
BULLET_HIT_SOUND = pygame.mixer.Sound('sprint1_game/Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('sprint1_game/Assets/Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('calibri', 30, bold=True)
WINNER_FONT = pygame.font.SysFont('calibri', 80, bold=True)
TOTAL_WINS_FONT = pygame.font.SysFont('calibri', 30, bold=True)
TOTAL_PLAY_FONT = pygame.font.SysFont('calibri', 20, bold=True)


FPS = 60
# moving speed of spaceships and bullets
VEL = 5
BULLET_VEL = 10
MAX_BULLETS = 3
PUSH_OPPONENT = 20
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# define the width and height, loading images of the spaceships and rotate them to the right facing direction
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('sprint1_game/Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('sprint1_game/Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('sprint1_game/Assets', 'space.jpg')), (WIDTH, HEIGHT))

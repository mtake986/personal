import pygame
import os
pygame.font.init()
pygame.mixer.init()

# todo: separate functions and main function if possible

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
BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 30, bold=True)
WINNER_FONT = pygame.font.SysFont('sans', 80, bold=True)

FPS = 60
# moving speed of spaceships and bullets
VEL = 5
BULLET_VEL = 10
MAX_BULLETS = 5 
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# loading images of the spaceships and rotate them to the right facing direction
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

# handle both yellow and red and bullet movements
def yellow_handle_movement(keys_pressed, yellow):
  if keys_pressed[pygame.K_1] and yellow.x - VEL > 10: # Left
  # if keys_pressed[pygame.K_a] and yellow.x >= 0: # Left
    yellow.x -= VEL
  if keys_pressed[pygame.K_2] and yellow.y - VEL > 10: # UP
  # if keys_pressed[pygame.K_w] and yellow.y >= 0: # UP
    yellow.y -= VEL
  if keys_pressed[pygame.K_3] and yellow.y + VEL + yellow.height < HEIGHT - 25: # DOWN
  # if keys_pressed[pygame.K_s] and yellow.y <= HEIGHT - SPACESHIP_HEIGHT - 20: # DOWN
    yellow.y += VEL
  if keys_pressed[pygame.K_4] and yellow.x + VEL + yellow.width < BORDER.x: # Right
  # if keys_pressed[pygame.K_d] and yellow.x <= (((WIDTH/2)-(BORDER_WIDTH/2))-SPACESHIP_WIDTH): # Right
    yellow.x += VEL
def red_handle_movement(keys_pressed, red):
  if keys_pressed[pygame.K_7] and red.x - VEL > BORDER.x + BORDER.width + 10: # Left
    red.x -= VEL
  if keys_pressed[pygame.K_8] and red.y - VEL > 10: # UP
    red.y -= VEL
  if keys_pressed[pygame.K_9] and red.y + VEL + red.height < HEIGHT - 25: # DOWN
    red.y += VEL
  if keys_pressed[pygame.K_0] and red.x + VEL + red.width < WIDTH: # Right
    red.x += VEL
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
  for bullet in yellow_bullets:
    bullet.x += BULLET_VEL # Because yellow is on the left side and the direction of its bullets needs to move right (+pxl)
    if red.colliderect(bullet):
      pygame.event.post(pygame.event.Event(RED_HIT))
      # when a spaceship can hit the opponent, reload one bullet so they can shoot again
      yellow_bullets.remove(bullet)
    if bullet.x > WIDTH:
      # remove one bullet from yellow_bullets list, so the spaceship can shoot again
      yellow_bullets.remove(bullet)
  for bullet in red_bullets:
    bullet.x -= BULLET_VEL # Because red is on the right side and the direction of its bullets needs to move left (-pxl)
    if yellow.colliderect(bullet):
      pygame.event.post(pygame.event.Event(YELLOW_HIT))
      red_bullets.remove(bullet)  
    if bullet.x > WIDTH:
      red_bullets.remove(bullet)

# draw stuff on the surface
def draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health): 
  # WIN.fill(WHITE)
  WIN.blit(SPACE, (0, 0))
  pygame.draw.rect(WIN, BLACK, BORDER)

  # start: draw health text
  red_health_text = HEALTH_FONT.render("Health:" + str(red_health), 1, WHITE)
  yellow_health_text = HEALTH_FONT.render("Health:" + str(yellow_health), 1, WHITE) # ("text_to_display", 1, COLOR)
  WIN.blit(red_health_text, (WIDTH -  red_health_text.get_width() - 10, 10)) 
  WIN.blit(yellow_health_text, (10, 10))
  # blit(thing_to_display, (where_x, where_y))

  # start: draw two spaceships
  WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
  WIN.blit(RED_SPACESHIP, (red.x, red.y))

  for bullet in red_bullets:
    pygame.draw.rect(WIN, RED, bullet)
  for bullet in yellow_bullets:
    pygame.draw.rect(WIN, YELLOW, bullet)
  pygame.display.update()

# when someone wins
def draw_winner(text):
  draw_text = WINNER_FONT.render(text, 1, WHITE)
  WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
  pygame.display.update()
  pygame.time.delay(5000)

# LEFT_CENTER = WIDTH//4-SPACESHIP_WIDTH//2
HEIGHT_CENTER = HEIGHT//2-SPACESHIP_HEIGHT//2

def main():
  yellow = pygame.Rect(200, HEIGHT_CENTER, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
  red = pygame.Rect(WIDTH-200-SPACESHIP_WIDTH, HEIGHT_CENTER, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

  # this is for limiting the maximum number users can shoot 
  red_bullets = []
  yellow_bullets = []

  red_health = 10
  yellow_health = 10

  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        # pygame.display.quit()
        pygame.quit()
        exit()
      # shoot bullet
      if event.type == pygame.KEYDOWN:
        # when the yellow player shoot
        if event.key == pygame.K_5 and len(yellow_bullets) < MAX_BULLETS:
          bullet = pygame.Rect(
            yellow.x + yellow.width, yellow.y + yellow.height//2 + 5, 10, 5) # Rect(where_x, where_x, bulllet_length, bullet_width)
          yellow_bullets.append(bullet)
          BULLET_FIRE_SOUND.play()
        # when the red play shoot
        if event.key == pygame.K_6 and len(red_bullets) < MAX_BULLETS:
          bullet = pygame.Rect(
            red.x, red.y + red.height//2 + 5, 10, 5)
          red_bullets.append(bullet) # Rect(where_x, where_x, bulllet_length, bullet_width)
          BULLET_FIRE_SOUND.play()
      if event.type == RED_HIT:
        red_health -= 1
        BULLET_HIT_SOUND.play()
      if event.type == YELLOW_HIT:
        yellow_health -= 1
        BULLET_HIT_SOUND.play()

    # define winner_text and change the value depending on who the winner is 
    winner_text = ''
    if red_health <= 0:
      winner_text = 'Yellow Wins!'
    elif yellow_health <= 0:
      winner_text = "Red Wins!"

    if winner_text != "": 
      draw_winner(winner_text)
      break

    keys_pressed = pygame.key.get_pressed()
    yellow_handle_movement(keys_pressed, yellow)
    red_handle_movement(keys_pressed, red)

    handle_bullets(yellow_bullets, red_bullets, yellow, red)
    draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health)
    
  # Instead of closing the window, restart the game
  main()
  # pygame.display.quit()
  # pygame.quit()
  # exit()


if __name__ == "__main__":
  main()
from variables import *
from main import *
import pygame
import os
pygame.font.init()
pygame.mixer.init()


# handle both yellow and red movements and bullet  #####################################
def yellow_handle_movement(keys_pressed, yellow):
  if keys_pressed[pygame.K_1] and yellow.x - VEL > PADDING:  # Left
    # if keys_pressed[pygame.K_a] and yellow.x >= 0: # Left
    yellow.x -= VEL
  if keys_pressed[pygame.K_2] and yellow.y - VEL > PADDING:  # UP
    # if keys_pressed[pygame.K_w] and yellow.y >= 0: # UP
    yellow.y -= VEL
  if keys_pressed[pygame.K_3] and yellow.y + VEL + yellow.height < HEIGHT - 25:  # DOWN
    # if keys_pressed[pygame.K_s] and yellow.y <= HEIGHT - SPACESHIP_HEIGHT - 20: # DOWN
    yellow.y += VEL
  if keys_pressed[pygame.K_4] and yellow.x + VEL + yellow.width < BORDER.x:  # Right
    # if keys_pressed[pygame.K_d] and yellow.x <= (((WIDTH/2)-(BORDER_WIDTH/2))-SPACESHIP_WIDTH): # Right
    yellow.x += VEL
def red_handle_movement(keys_pressed, red):
  if keys_pressed[pygame.K_7] and red.x - VEL > BORDER.x + BORDER.width + PADDING:  # Left
    red.x -= VEL
  if keys_pressed[pygame.K_8] and red.y - VEL > PADDING:  # UP
    red.y -= VEL
  if keys_pressed[pygame.K_9] and red.y + VEL + red.height < HEIGHT - 25:  # DOWN
    red.y += VEL
  if keys_pressed[pygame.K_0] and red.x + VEL + red.width < WIDTH:  # Right
    red.x += VEL
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
  for bullet in yellow_bullets:
    # Because yellow is on the left side and the direction of its bullets needs to move right (+pxl)
    bullet.x += BULLET_VEL
    if red.colliderect(bullet):
      pygame.event.post(pygame.event.Event(RED_HIT))
      # when a spaceship can hit the opponent, reload one bullet so they can shoot again
      yellow_bullets.remove(bullet)
    if bullet.x > WIDTH:
      # remove one bullet from yellow_bullets list, so the spaceship can shoot again
      yellow_bullets.remove(bullet)
  for bullet in red_bullets:
    # Because red is on the right side and the direction of its bullets needs to move left (-pxl)
    bullet.x -= BULLET_VEL
    if yellow.colliderect(bullet):
      pygame.event.post(pygame.event.Event(YELLOW_HIT))
      red_bullets.remove(bullet)
    if bullet.x > WIDTH:
      red_bullets.remove(bullet)

# draw hp, total wins, total play #########################################################################
def draw_hp(yellow_health, red_health, origin_health):
  # start: draw health text => "Health"
  HEALTH_TEXT = HEALTH_FONT.render("Health:", 1, WHITE)
  HEALTH_TEXT_WIDTH = HEALTH_TEXT.get_width()
  
  def yellow_actual_hp(color, yellow_health):
    actual_hp_text = HEALTH_FONT.render(str(yellow_health), 1, color)
    WIN.blit(HEALTH_TEXT, (10, 10))
    WIN.blit(actual_hp_text, (HEALTH_TEXT_WIDTH+PADDING, 10))
  def red_actual_hp(color, red_health):
    actual_hp_text = HEALTH_FONT.render(str(red_health), 1, color)
    ACTUAL_HP_WIDTH = actual_hp_text.get_width()
    WIN.blit(HEALTH_TEXT, (WIDTH - (HEALTH_TEXT_WIDTH + ACTUAL_HP_WIDTH + 10), 10))
    WIN.blit(actual_hp_text, (WIDTH - (ACTUAL_HP_WIDTH + PADDING), 10))
    
  # todo: yellow_health_text で一文で表示してるけど、分ける。yellow_health_textの横にhealthを置く。yellow_health_text.get_width()で長さ取得
  if yellow_health <= origin_health*.3:
    # yellow_health_under_thirty = HEALTH_FONT.render(
    # str(yellow_health), 1, RED)
    # WIN.blit(yellow_health_under_thirty, (HEALTH_TEXT_WIDTH+PADDING, 10))
    yellow_actual_hp(RED, yellow_health)
  elif yellow_health <= origin_health*.7:
    yellow_actual_hp(YELLOW, yellow_health)
  else:
    yellow_actual_hp(WHITE, yellow_health)
  if red_health <= origin_health*.3:
    red_actual_hp(RED, red_health)
  elif red_health <= origin_health*.7:
    red_actual_hp(YELLOW, red_health)
  else:
    red_actual_hp(WHITE, red_health)
def draw_total_wins(yellow_total_win_so_far, red_total_win_so_far):
  # drawing both texts of total win and define where
  yellow_total_win_text = TOTAL_WINS_FONT.render(
    'Wins:' + str(yellow_total_win_so_far), 1, WHITE)
  red_total_win_text = TOTAL_WINS_FONT.render(
    'Wins:' + str(red_total_win_so_far), 1, WHITE)
  WIN.blit(yellow_total_win_text, (
    (WIDTH//2 - yellow_total_win_text.get_width() - (BORDER_WIDTH//2))-10, 10))
  WIN.blit(red_total_win_text, ((WIDTH//2 + BORDER_WIDTH//2)+10, 10))
def draw_total_play(ttl_play, yellow_bullets, red_bullets):
  # define total amount of play
  total_play_text = TOTAL_PLAY_FONT.render(
    "Total Plays:" + str(ttl_play), 1, WHITE)
  WIN.blit(total_play_text, (10, HEIGHT-total_play_text.get_height()-10))
  for bullet in red_bullets:
    pygame.draw.rect(WIN, RED, bullet)
  for bullet in yellow_bullets:
    pygame.draw.rect(WIN, YELLOW, bullet)

# draw stuff on the surface #################################
def draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health, origin_health,  yellow_total_win_so_far, red_total_win_so_far, ttl_play):
  # WIN.fill(WHITE)
  WIN.blit(SPACE, (0, 0))
  pygame.draw.rect(WIN, BLACK, BORDER)
  # draw two spaceships
  WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
  WIN.blit(RED_SPACESHIP, (red.x, red.y))
  
  # call draw_hp()
  draw_hp(yellow_health, red_health, origin_health)
  # Call draw_total_wins()
  draw_total_wins(yellow_total_win_so_far, red_total_win_so_far)
  # Call draw_total_play()
  draw_total_play(ttl_play, yellow_bullets, red_bullets)
  
  pygame.display.update()

# when someone wins
def draw_winner(text, yellow, red, yellow_bullets, red_bullets, yellow_health, red_health, winner):
  if winner == "yellow":
    draw_text = WINNER_FONT.render(text, 1, YELLOW)
  else:
    draw_text = WINNER_FONT.render(text, 1, RED)
  WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
  pygame.display.update()
  pygame.time.delay(5000)
  # Disable shooting during 5 seconds. 
  MAX_BULLETS = 0
  for event in pygame.event.get():
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
      # decrease the health, play the sound, push the opponent
      red_health -= 1
      BULLET_HIT_SOUND.play()
      if red.x+SPACESHIP_WIDTH + PUSH_OPPONENT <= WIDTH-10:
        # print(red.x)
        red.x += PUSH_OPPONENT
    if event.type == YELLOW_HIT:
      yellow_health -= 1
      BULLET_HIT_SOUND.play()
      if yellow.x - PUSH_OPPONENT >= 10:
        # print(yellow.x)
        yellow.x -= PUSH_OPPONENT



# LEFT_CENTER = WIDTH//4-SPACESHIP_WIDTH//2
HEIGHT_CENTER = HEIGHT//2-SPACESHIP_HEIGHT//2

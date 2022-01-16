import pygame
import os
pygame.font.init()
pygame.mixer.init()

from main import *
from variables import *

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
def draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health, yellow_total_wins_so_far, red_total_wins_so_far, ttl_play): 
  # WIN.fill(WHITE)
  WIN.blit(SPACE, (0, 0))
  pygame.draw.rect(WIN, BLACK, BORDER)

  # start: draw health text
  # ("text_to_display", 1, COLOR)
  yellow_health_text = HEALTH_FONT.render("Health:" + str(yellow_health), 1, WHITE) 
  red_health_text = HEALTH_FONT.render("Health:" + str(red_health), 1, WHITE)
  # blit(thing_to_display, (where_x, where_y))
  WIN.blit(yellow_health_text, (10, 10))
  WIN.blit(red_health_text, (WIDTH -  red_health_text.get_width() - 10, 10)) 

  # drawing both texts of total win and define where
  yellow_total_wins_text = TOTAL_WINS_FONT.render('Wins:' + str(yellow_total_wins_so_far), 1, WHITE)
  red_total_wins_text = TOTAL_WINS_FONT.render('Wins:' + str(red_total_wins_so_far), 1, WHITE)
  WIN.blit(yellow_total_wins_text, ((WIDTH//2 - yellow_total_wins_text.get_width() - (BORDER_WIDTH//2))-10, 10))
  WIN.blit(red_total_wins_text, ((WIDTH//2 + BORDER_WIDTH//2)+10, 10))

  # draw two spaceships
  WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
  WIN.blit(RED_SPACESHIP, (red.x, red.y))

  # define total amount of play
  total_play_text = TOTAL_PLAY_FONT.render("Total Amount of Play:" + str(ttl_play), 1, WHITE)
  WIN.blit(total_play_text, (10, HEIGHT-total_play_text.get_height()-10))
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


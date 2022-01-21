
yellow_total_win_so_far = 0
red_total_win_so_far = 0
total_amount_of_play = 0
origin_health = 10
# from xml.dom.expatbuilder import parseString
from functions import *

def main(origin_health, yellow_ttl_win, red_ttl_win, ttl_play):
  yellow = pygame.Rect(200, HEIGHT_CENTER, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
  red = pygame.Rect(WIDTH-200-SPACESHIP_WIDTH, HEIGHT_CENTER, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
  
  MAX_BULLETS = 3
  # this is for limiting the maximum number users can shoot 
  red_bullets = []
  yellow_bullets = []

  red_health = origin_health
  yellow_health = origin_health

  yellow_total_win_so_far = yellow_ttl_win
  red_total_win_so_far = red_ttl_win

  total_amount_of_play = ttl_play
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
          # print(f'Max bullets => {MAX_BULLETS}, pressed => {event.key}, len(yellow_bullets) => {yellow_bullets}')
        # when the red play shoot
        if event.key == pygame.K_6 and len(red_bullets) < MAX_BULLETS:
          bullet = pygame.Rect(
            red.x, red.y + red.height//2 + 5, 10, 5)
          red_bullets.append(bullet) # Rect(where_x, where_x, bulllet_length, bullet_width)
          BULLET_FIRE_SOUND.play()
          # print(f'Max bullets => {MAX_BULLETS}, pressed => {event.key}, len(red_bullets) => {red_bullets}')
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

    keys_pressed = pygame.key.get_pressed()
    yellow_handle_movement(keys_pressed, yellow)
    red_handle_movement(keys_pressed, red)
    
    handle_bullets(yellow_bullets, red_bullets, yellow, red)
    draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health, origin_health, yellow_total_win_so_far, red_total_win_so_far, ttl_play)
    
    # define winner_text and change the value depending on who the winner is 
    winner_text = ''
    winner = ''
    if red_health <= 0:
      winner_text = 'Yellow Wins!'
      yellow_total_win_so_far += 1
      winner = "yellow"
    elif yellow_health <= 0:
      winner_text = "Red Wins!"
      red_total_win_so_far += 1
      winner = "red"

    if winner_text != "": 
      draw_winner(winner_text, yellow, red, yellow_bullets, red_bullets, yellow_health, red_health, winner)
      break
      # Instead of closing the window, restart the game
  main(origin_health, yellow_total_win_so_far, red_total_win_so_far, total_amount_of_play+1)


if __name__ == "__main__":
  main(origin_health, yellow_total_win_so_far, red_total_win_so_far, total_amount_of_play)
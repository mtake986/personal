
``` python
# functions.py

# ("text_to_display", 1, COLOR)
yellow_health_text = HEALTH_FONT.render("Health:" + str(yellow_health), 1, WHITE) 
# blit(thing_to_display, (where_x, where_y))
WIN.blit(yellow_health_text, (10, 10))


# main.py

# Instead of closing the window, restart the game
main(yellow_total_win_so_far, red_total_win_so_far, total_amount_of_play+1)
# pygame.display.quit()
# pygame.quit()
# exit()
```
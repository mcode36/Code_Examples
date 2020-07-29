'''

  Python_Alien.pdf -- Upto page_242.

  Section Title: Setting the Background Color

'''

import sys
import pygame
import time

def run_game():
    
    ## Set the background color.
    bg_color = (230, 230, 230)
    white = (255,255,255)
    red = (255,0,0)
    blue = (0,0,255)

    screen_w = 800
    screen_h = 600
    ball_x = 20
    ball_y = 20
    ball_r = 10
    paddle_w = 80
    paddle_h = 10
    paddle_x = 0
    paddle_y = screen_h-paddle_h
    speed_x = 2
    speed_y = 2

    ## Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("Bouncing Ball")
    pygame.key.set_repeat(10, 10)

    ## Sound effect
    hit = pygame.mixer.Sound('sms-alert-1-daniel_simon.wav')
    
    ## Start the main loop for the game.
    while True:
        ## Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RIGHT:
                paddle_x = paddle_x + 3
              if event.key == pygame.K_LEFT:
                paddle_x = paddle_x - 3
        ## Redraw the screen during each pass through the loop.
        screen.fill(bg_color)

        ## Adjust FPS
        clock = pygame.time.Clock()
        dt = clock.tick(180)

        
        ## Draw circle
        ball_x = ball_x + speed_x
        ball_y = ball_y + speed_y
        if ((ball_x + 20) >= screen_w) or ((ball_x - 20) <= 0):
          speed_x = 0 - speed_x
        if (ball_y - 20) <= 0:
          speed_y = 0 - speed_y
        if ((ball_y + 20) >= paddle_y) and (ball_x >= paddle_x) and (ball_x <= paddle_x+paddle_w):
          speed_y = 0 - speed_y
          hit.play()        
        pygame.draw.circle(screen, red, (ball_x,ball_y), ball_r)
        
        ## Draw paddle
        pygame.draw.rect(screen, blue, (paddle_x,paddle_y,paddle_w,paddle_h))

        ## Refresh the entire screen
        pygame.display.flip()
        #time.sleep(0.01)

run_game()

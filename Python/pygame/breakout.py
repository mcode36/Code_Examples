# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 19:46:07 2018
github: https://github.com/scidan/Breakout.git
Youtube: https://www.youtube.com/watch?v=julpd5m1hbM
@author: daniel
"""

import pygame
import sys
pygame.init()

# Setup colors
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)

# Sound Effect
hit = pygame.mixer.Sound('sms-alert-1-daniel_simon.wav')



# Setup the main display
display_width = 600
display_height = 600
display_res = (display_width, display_height)
display = pygame.display.set_mode(display_res)
display_color = (0, 0, 0)
display.fill(display_color)

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf = largeText.render(text, True, red)
    TextRect = TextSurf.get_rect()
    TextRect.center = (int(display_width/2),int(display_height/2))
    display.blit(TextSurf, TextRect)

# Setup the player controlled rectangle
player_width = 100
player_height = 20
player_size = (player_width, player_height)
player_surface = pygame.Surface(player_size)
player_rect = player_surface.get_rect()
rect_speed = 1
player_rect.x = 300
player_rect.y = display_height-60
player_color = (255, 255, 255)
player_surface.fill(player_color)

# Setup the bouncing ball
ball = pygame.image.load("PngItem_25193s.png")
# Image size: 40 x 40
ball_rect = ball.get_rect()
ball_rect.x = 300
ball_rect.y = player_rect.y - 50
ball_speed = [1, 1]

# Setup the target blocks
target_width = 50
target_height = 20
target_size = (target_width, target_height)
x_offs = 10
y_offs = 10
n_rows = 5
target_color = (0,255,0)
target_surf_list = []
target_rect_list = []
for target_col in range(int(display_width / (target_width+x_offs))):
    for target_row in range(n_rows):
        target_surf = pygame.Surface(target_size)
        target_rect = target_surf.get_rect()
        x_location = x_offs + x_offs * target_col + target_width * target_col
        y_location = y_offs + y_offs * target_row + target_height * target_row
        target_rect.x = x_location
        target_rect.y = y_location
        target_surf.fill(target_color)
        target_surf_list.append(target_surf)
        target_rect_list.append(target_rect)

game_status = 'start'
while 1:
    ## Adjust FPS
    clock = pygame.time.Clock()
    dt = clock.tick(180)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect = player_rect.move([-rect_speed, 0])
    if keys[pygame.K_RIGHT]:
        player_rect = player_rect.move([rect_speed, 0])
    if keys[pygame.K_q]:
        break

    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.left < 0 or ball_rect.right > display_width:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 :
        ball_speed[1] = -ball_speed[1]
    if ball_rect.bottom > display_height:
        ball_speed = [0, 0]
        game_status = 'over'

    if player_rect.colliderect(ball_rect):
        hit.play()  
        ball_speed[1] = -ball_speed[1]

    for idx, x in enumerate(target_rect_list):
        if x.colliderect(ball_rect):
            del target_rect_list[idx]
            del target_surf_list[idx]
            ball_speed[1] = -ball_speed[1]

    # Try text
    
    display.fill(display_color)
    display.blit(player_surface, player_rect)
    display.blit(ball, ball_rect)
    for x in range(len(target_surf_list)):
        display.blit(target_surf_list[x], target_rect_list[x])
    if game_status == 'over':
        message_display('Game Over')
    pygame.display.flip()

print("Bye")
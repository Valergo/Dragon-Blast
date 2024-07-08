''' More infos:
https://www.pygame.org/docs/ref/key.html
'''

#STOP bei: 1:51:28

import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dragon Blaster')
running = True
clock = pygame.time.Clock() # can control the frame rate

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('white')
px = 100
ex = 700
y = 50
player_direction = pygame.math.Vector2()
player_speed = 300

# importing an image # convert() for images with no transparent pixel, convert_alpha() if image has transparent pixel
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha() # if you are not in the project folder, use ../
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)) # frect for float. get_frect needs a decleration of the point position of the rect and then the coordinates

enemy_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha() # if you are not in the project folder, use ../
enemy_rect = enemy_surf.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

cloud_surf = pygame.image.load(join('images', 'cloud.png')).convert_alpha() # if you are not in the project folder, use ../
cloud_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(30)]

fire_surf = pygame.image.load(join('images', 'fire.png')).convert_alpha() # if you are not in the project folder, use ../
fire_rect = fire_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))


# import an image. put every image to a surface

## The display of a game window is a loop that updates the screen with all the data it contains.
while running:
    dt = clock.tick() / 500
    #print(clock.get_fps())
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        '''if event.type == pygame.MOUSEMOTION: #usefull: pygame.MOUSEMOTION --> event.pos -- it returns the position of the cursor
            player_rect.center = event.pos'''

    # input -- without the loop we can use a button continuously! not just once
    # print(pygame.mouse.get_rel() -- for the maouse speed
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) # K_... returns booleon. With int we return: True == 1 and False == 0 SMART!!!
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    # normalizing the vector because diagonal we are faster! So we keep th length of 1
    player_direction = player_direction.normalize() if player_direction  else player_direction
    player_rect.center += player_direction * player_speed * dt
    # print((player_direction * player_speed).magnitude())
    # print(player_direction)

    '''if keys[pygame.K_RIGHT]:
        player_direction.x = 1
    else:
        player_direction.x = 0'''




    # draw the game
    display_surface.fill('skyblue')
    for pos in cloud_pos:
        # what if i'd like to change now the position of the clouds?
        display_surface.blit(cloud_surf, pos)
    display_surface.blit(player_surf, player_rect)
    display_surface.blit(player_surf,  player_rect) #blit=block image transfer. The Pygame blit() method is one of the methods to place an image onto the screens of pygame applications. It intends to put an image on the screen. It just copies the pixels of an image from one surface to another surface just like that.
    display_surface.blit(enemy_surf, enemy_rect)
    display_surface.blit(fire_surf, fire_rect)

    # player movement
    '''if player_rect.bottom >= WINDOW_HEIGHT:
        player_rect.bottom = WINDOW_HEIGHT
        player_direction.y = -1 '''
    '''if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
        player_direction.y *= -1
    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1
    player_rect.center += player_direction * player_speed * dt'''




    pygame.display.update() # update: updates hole screen, flip: updates part of the window


 # The opposite of init. It is sometimes necessary for closing the game properly.
pygame.quit()

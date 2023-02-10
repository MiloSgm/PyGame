import pygame


"""
create a function game_loop() that will run your game
you will have to handle the events in this loop
for now just handle one events: close the game when we click on the cross
"""


def game_loop():
################################################################################
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
################################################################################


wn_width = 1600
wn_height = 900


pygame.init()

wn = pygame.display.set_mode((wn_width, wn_height))
game_loop()

pygame.quit()
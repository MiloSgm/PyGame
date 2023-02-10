import pygame

################################################################################
def draw_game():
    pygame.draw.rect(wn, (50, 150, 250), (0, 0, wn_width, wn_height))
    pygame.display.flip()
################################################################################


def game_loop():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False
        draw_game()


wn_width = 1600
wn_height = 900


pygame.init()

wn = pygame.display.set_mode((wn_width, wn_height))
game_loop()

pygame.quit()
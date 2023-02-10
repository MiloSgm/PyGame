import pygame


"""
Let's get started for real now and start coding the game
create a class Pad() that will have
-the following variables:
    x, y -> position
    width, height -> shape
    speed -> movement speed
    score -> (no comments)
    k_up, k_down -> bool that will be usefull for the inputs
-and the method draw() that will draw himself, you can just draw a white rectangle
"""


################################################################################
class Pad:
    def __init__(self, x) -> None:
        self.x = x
        self.y = wn_height / 2
        self.width = 20
        self.height = 100
        self.speed = 1
        self.score = 0
    
    def draw(self):
        pygame.draw.rect(wn, (250, 250, 250), (self.x-self.width, self.y - self.height, self.width*2, self.height*2))
################################################################################


def draw_game():
    pygame.draw.rect(wn, (0, 0, 0), (0, 0, wn_width, wn_height))
    p1.draw()
    p2.draw()
    pygame.display.flip()


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

p1 = Pad(0)
p2 = Pad(wn_width)

pygame.init()

wn = pygame.display.set_mode((wn_width, wn_height))
game_loop()

pygame.quit()
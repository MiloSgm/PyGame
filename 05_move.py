import pygame


################################################################################
class Pad:
    def __init__(self, x) -> None:
        self.x = x
        self.y = wn_height / 2
        self.width = 20
        self.height = 100
        self.speed = 1
        self.score = 0
        self.k_up = False
        self.k_down = False

    def move(self):
        if self.k_up:
            self.y -= self.speed
        if self.k_down:
            self.y += self.speed
        if self.y > wn_height - self.height:
            self.y = wn_height - self.height
        if self.y < self.height:
            self.y = self.height

    def draw(self):
        pygame.draw.rect(wn, (250, 250, 250), (self.x-self.width, self.y - self.height, self.width*2, self.height*2))


def pads_input(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            p2.k_up = True
        if event.key == pygame.K_DOWN:
            p2.k_down = True
        if event.key == pygame.K_z:
            p1.k_up = True
        if event.key == pygame.K_s:
            p1.k_down = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            p2.k_up = False
        if event.key == pygame.K_DOWN:
            p2.k_down = False
        if event.key == pygame.K_z:
            p1.k_up = False
        if event.key == pygame.K_s:
            p1.k_down = False
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
            pads_input(event)
        p1.move()
        p2.move()
        draw_game()


wn_width = 1600
wn_height = 900

p1 = Pad(0)
p2 = Pad(wn_width)

pygame.init()

wn = pygame.display.set_mode((wn_width, wn_height))
game_loop()

pygame.quit()
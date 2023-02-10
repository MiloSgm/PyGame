import pygame
import random


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


class Ball:
    def __init__(self) -> None:
        self.speed = 1
        self.x = wn_width / 2
        self.y = wn_height / 2
        self.radius = 20
        self.hspeed = 0
        self.vspeed = 0

    def reset(self):
        self.speed = 1
        self.x = wn_width / 2
        self.y = wn_height / 2
        self.hspeed = 0
        self.vspeed = 0

    def move(self):
        self.x += self.hspeed * self.speed
        self.y += self.vspeed * self.speed

        if (self.y <= self.radius or self.y >= wn_height - self.radius):
            self.vspeed *= -1

###################################################################################
        if (self.x <= p1.width + self.radius):
            self.speed += 0.1
            if (self.y >= p1.y - p1.height - self.radius and self.y <= p1.y + p1.height):
                self.hspeed *= -1
            else:
                p2.score += 1
                print("player 2 scored")
                self.reset()
        
        if (self.x >= wn_width - self.radius - p2.width):
            self.speed += 0.1
            if (self.y >= p2.y - p2.height - self.radius and self.y <= p2.y + p2.height):
                self.hspeed *= -1
            else:
                p1.score += 1
                print("player 1 scored")
                self.reset()
###################################################################################

    def draw(self):
        pygame.draw.circle(wn, (250, 250, 250), (self.x, self.y), self.radius)


def draw_game():
    pygame.draw.rect(wn, (0, 0, 0), (0, 0, wn_width, wn_height))
    pygame.draw.rect(wn, (250, 250, 250), (wn_width / 2 - 1, 0, 2, wn_height))
    p1.draw()
    p2.draw()
    ball.draw()
    pygame.display.flip()


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
        if (ball.hspeed == 0 and ball.vspeed == 0 and event.key == pygame.K_SPACE):
            ball.hspeed = random.choice([-1, 1])
            ball.vspeed = random.choice([-1, 1])
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            p2.k_up = False
        if event.key == pygame.K_DOWN:
            p2.k_down = False
        if event.key == pygame.K_z:
            p1.k_up = False
        if event.key == pygame.K_s:
            p1.k_down = False


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
        ball.move()
        draw_game()


wn_width = 1600
wn_height = 900

p1 = Pad(0)
p2 = Pad(wn_width)
ball = Ball()

pygame.init()

wn = pygame.display.set_mode((wn_width, wn_height))
game_loop()

pygame.quit()
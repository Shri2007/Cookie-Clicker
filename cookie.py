import pygame
import sys
from pygame import mixer
from pygame import K_SPACE
x = 0
y = 0
score = 0
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
icon = pygame.image.load('cookie.png')
pygame.display.set_icon(icon)
cookieImg = pygame.image.load('cookie.png')
pygame.display.set_caption('Cookie Clicker')

font = pygame.font.Font('freesansbold.ttf', 40)
score_value = 0
bg = pygame.image.load('background.jpg')
def draw_cookie():
    screen.blit(cookieImg, (210, 210))

def show_score():
    score = font.render('Score: {}'.format(score_value), True, (255, 0, 20))
    screen.blit(score, (x, y))
def secret_writing():
    figure_out = font.render('Try a key to gain points easier!', True, (255, 255, 0))
    screen.blit(figure_out, (0, 520))
def end():
    sys.setrecursionlimit(10**6)
    hi = font.render('Congrats! You won!', True, (255, 255, 0))
    screen.blit(hi, (0, 100))
    f = mixer.Sound('fortnite.wav')
    f.play()

while True:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            score_value += 1
            click = mixer.Sound('click.wav')
            click.play()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                score_value += 70
    if score_value > 1000:
        end()
    draw_cookie()
    show_score()
    secret_writing()
    pygame.display.update()
    clock.tick(120)


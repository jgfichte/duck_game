import pygame, sys
import random
from missile import Missile

def get_cloud_rects(qty):
    rects = []
    for i in range(qty):
        rects.append((random.randint(1, 1200), random.randint(1, 100)))
    return rects

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

bgnd = pygame.image.load('assets/Wood_BG.png')
water = pygame.image.load('assets/Water_BG.png')
duck = pygame.image.load('assets/duck.png')
cloud1 = pygame.image.load('assets/Cloud1.png')

duck_x = 100
duck_y = 540
duck_speed = 30
water_y = 600
water_range = [595, 605]
water_delta = -0.5

cloud_rects = get_cloud_rects(8)

NEW_MISSILE = pygame.USEREVENT + 0
pygame.time.set_timer(NEW_MISSILE, 2000)
missiles = []
score = 0

game_font = pygame.font.Font(None, 70)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == NEW_MISSILE:
            missiles.append(Missile(screen))
        if event.type == Missile.MISSILE_GOBBLED:
            score += 1

    # Handle the left / right keys to move the duck
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        duck_x -= duck_speed
    if keys[pygame.K_RIGHT]:
        duck_x += duck_speed

    # paint all the graphics on the screen
    screen.blit(bgnd, (0, 0))
    duck_rect = duck.get_rect(center = (duck_x, 560))
    screen.blit(duck, duck_rect)
    screen.blit(water, (0, water_y))
    for rect in cloud_rects:
        screen.blit(cloud1, rect)

    # Handle the up and down for the water
    water_y += water_delta
    if (water_y < water_range[0] or water_y > water_range[1]):
        water_delta = -1 * water_delta

    score_surface = game_font.render(str(score), True, (255,255,255))
    screen.blit(score_surface, (5, 5))

    # Boundaries for the duck
    if duck_x <= 0:
        duck_x = 0
    if duck_x >= 1200:
        duck_x = 1200

    for m in missiles:
        m.update(duck_rect)

    pygame.display.update()
    clock.tick(120)


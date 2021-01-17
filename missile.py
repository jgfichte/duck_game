import pygame, random
from constants import *


class Missile:

    MISSILE_GOBBLED = pygame.USEREVENT + 1

    def __init__(self, screen):
        self.screen = screen
        self.sprite = pygame.image.load('assets/berry.png')
        self.xpos = random.randrange(10, 1270)
        self.ypos = 0
        self.speed = 15
        self.gobbled = False
        self.gobble_sound = pygame.mixer.Sound('assets/gobble.wav')

    def update(self, duck_rect):
        if not self.gobbled:
            self.ypos += self.speed
            r = self.sprite.get_rect(center = (self.xpos, self.ypos))
            if duck_rect.colliderect(r):
                self.gobble()
            self.screen.blit(self.sprite, r)
    
    def gobble(self):
        self.gobbled = True
        pygame.mixer.Sound.play(self.gobble_sound)
        evt = pygame.event.Event(Missile.MISSILE_GOBBLED)
        pygame.event.post(evt)


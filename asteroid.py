from circleshape import *
from constants import *
import pygame #type: ignore
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20,50)
        vector1 = self.velocity.rotate(rand_angle)
        vector2 = self.velocity.rotate(-(rand_angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ## Creating two new asteroids that will split from destroyed astroid
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector1 * 1.2

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = vector2 * 1.2
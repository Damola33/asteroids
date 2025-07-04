from constants import *
from player import *
from asteroidfield import *
import pygame # type: ignore

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    ##creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    ##creating player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #using the new containers 
        for item in drawable:
            item.draw(screen)  

        updatable.update(dt)

        for asteroid in asteroids:
            if(player.collisions(asteroid)):
                print("Game Over!")
                sys.exit()


        pygame.display.flip()

        #limit the framerate to 60 fps
        dt = clock.tick(60) / 1000


   


if __name__ == "__main__":
    main()

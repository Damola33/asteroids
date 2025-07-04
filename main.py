from constants import *
from player import *
import pygame # type: ignore

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    ##creating update and draw groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable,drawable)

    ##creating player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #using the Player containers 
        for player in drawable:
            player.draw(screen)          
        updatable.update(dt)


        pygame.display.flip()

        #limit the framerate to 60 fps
        dt = clock.tick(60) / 1000


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()

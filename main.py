# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
color = (0,0,0)

running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with black color
    screen.fill(color)
    
    # Update display
    pygame.display.flip()
    
pygame.quit()
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
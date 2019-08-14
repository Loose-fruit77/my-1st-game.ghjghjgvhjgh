import pygame
from pygame.locals import *

pygame.int()

screen = pygame.display.set_mode((800, 600))

# Variable to keep our main loop running
running = True
# Our main Loop!
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == KEYDOWN

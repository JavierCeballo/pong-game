# Import libraries
import pygame

# Initialize pygame
pygame.init()

# Define the dimensions of the window
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)

# Display the window
screen = pygame.display.set_mode( size )



# Variable that to keep our game loop running
running = True

# Game loop
while running:
    
    # for loop through the event queue
    for event in pygame.event.get():
        
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
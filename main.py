# Import libraries
import pygame

# Initialize pygame
pygame.init()

# Colors: bacground
bg_color = (0, 255, 0)

# Define the dimensions of the window
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)

# Display the window
screen = pygame.display.set_mode( size )

# Icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon( icon )

# Title
pygame.display.set_caption("Pong Game")


# Variable that to keep our game loop running
running = True

# Game loop
while running:
    
    # Set the background color
    screen.fill(bg_color)
    
    # for loop through the event queue
    for event in pygame.event.get():
        
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
    
    # Update the window
    pygame.display.flip()
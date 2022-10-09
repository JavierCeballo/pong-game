# Import libraries
import pygame

# Initialize pygame
pygame.init()

# Colors: background
bg_color = (0, 255, 0)
players_color = (66, 51, 255)
ball_color = (255, 87, 51)

# Define dimensions of the window
screen_width = 800
screen_height = 600
size = (screen_width, screen_height)

# Define dimentions of the players
players_width = 15
players_height = 90

# Define player 1 coordinates
player_1_x = 50
player_1_y = 300 - (players_height/2)

# Define player 2 coordinates
player_2_x = 750 - players_width
player_2_y = player_1_y

# Define ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 20


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
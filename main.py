# Import libraries
from curses import KEY_DOWN
import pygame

# Initialize pygame
pygame.init()

# Colors: background
bg_color = (0, 255, 0)
players_color = (66, 51, 255)
ball_color = (255, 87, 51)
line_color = (255, 255, 255)

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
player_1_y_speed = 0

# Define player 2 coordinates
player_2_x = 750 - players_width
player_2_y = player_1_y
player_2_y_speed = 0

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
            
        # Players key controls
        
        # Cheks for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            
            # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = -1
                
            if event.key == pygame.K_s:
                player_1_y_speed = 1
                
            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -1
                
            if event.key == pygame.K_DOWN:
                player_2_y_speed = 1
                
                
        # Cheks for KEYUP event       
        if event.type == pygame.KEYUP:
            
            # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = 0
            
            if event.key == pygame.K_s:
                player_1_y_speed = 0
                
            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = 0
                
            if event.key == pygame.K_DOWN:
                player_2_y_speed = 0
            
    
    
    # Player movement
    player_1_y += player_1_y_speed
    player_2_y += player_2_y_speed
            
            
            
            
            
            
    # Drawing area
    
    # Draw the player 1 on the left
    player_1 = pygame.draw.rect(screen, players_color, (player_1_x, player_1_y, players_width, players_height))
    
    # Draw the player 2 on the right
    player_2 = pygame.draw.rect(screen, players_color, (player_2_x, player_2_y, players_width, players_height))
    
    # Draw the ball
    ball = pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    
    # Draw the center line
    pygame.draw.aaline(screen, line_color, (screen_width/2, 0), (screen_width/2, screen_height))
    
    
    # Update the window
    pygame.display.flip()
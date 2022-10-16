# Import libraries
from curses import KEY_DOWN
import pygame
import random as rd

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

ball_speed_x = 0.1
ball_speed_y = 0.1


# Display the window
screen = pygame.display.set_mode( size )

# Icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon( icon )

# Title
pygame.display.set_caption("Pong Game")

# Score variables
player_1_score = 0
player_2_score = 0

# Score font
score_font = pygame.font.Font("quantifier-font.ttf", 32)

# Score position in the screen - Player 1
player_1_score_x = 10
player_1_score_y = 10

# Score position in the screen - Player 2
player_2_score_x = screen_width - 165
player_2_score_y = 10

# Player 1 score function
def show_score_1(x, y):
    score1 = score_font.render("Player one: " + str( player_1_score), True, (0, 0, 0))
    screen.blit( score1, (x, y))
    
# Player 2 score function
def show_score_2(x, y):
    score2 = score_font.render("Player two: " + str( player_2_score), True, (0, 0, 0))
    screen.blit( score2, (x, y))

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
            
    
    
    # Players movement
    player_1_y += player_1_y_speed
    player_2_y += player_2_y_speed
            
    # Players boundaries
    
    # Player 1
    if player_1_y <= 0:
        player_1_y = 0
    
    elif player_1_y >= screen_height - players_height:
        player_1_y = screen_height - players_height
        
    # Player 2
    if player_2_y <= 0:
        player_2_y = 0
    
    elif player_2_y >= screen_height - players_height:
        player_2_y = screen_height - players_height
    
    
    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Ball boundaries: top or buttom
    if ball_y > (screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1
        
    # Ball boundaries: right or left
    if (ball_x > screen_width) or (ball_x < 0):
        
        ball_x = (screen_width/2)
        ball_y = (screen_height/2)
        ball_speed_x *= rd.choice( [-1, 1] )
             
                
    # Drawing area
    
    # Draw the player 1 on the left
    player_1 = pygame.draw.rect(screen, players_color, (player_1_x, player_1_y, players_width, players_height))
    
    # Draw the player 2 on the right
    player_2 = pygame.draw.rect(screen, players_color, (player_2_x, player_2_y, players_width, players_height))
    
    # Draw the center line
    pygame.draw.aaline(screen, line_color, (screen_width/2, 0), (screen_width/2, screen_height))
    
    # Draw the ball
    ball = pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    

    
    # Collitions
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
        
    # Call the show_score1 function
    show_score_1(player_1_score_x, player_1_score_y)
    show_score_2(player_2_score_x, player_2_score_y)
    
    # Update the window
    pygame.display.flip()
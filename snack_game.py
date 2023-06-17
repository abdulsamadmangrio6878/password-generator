import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the width and height of the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set the clock for the game
clock = pygame.time.Clock()

# Set the size of the snake's segments and the speed of the snake
segment_size = 20
segment_speed = 20

# Define fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Function to display the score on the screen
def display_score(score):
    text = score_font.render("Score: " + str(score), True, WHITE)
    window.blit(text, [10, 10])

# Function to draw the snake on the screen
def draw_snake(segment_size, snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(window, WHITE, [segment[0], segment[1], segment_size, segment_size])

# Function to run the Snake game
def snake_game():
    game_over = False
    game_exit = False

    # Initialize the starting position of the snake
    x = window_width / 2
    y = window_height / 2

    # Define initial movement direction
    x_change = 0
    y_change = 0

    # Create an empty list to store the segments of the snake
    snake_segments = []
    snake_length = 1

    # Generate the initial position of the food
    food_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
    food_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size

    while not game_exit:
        while game_over:
            # Display game over message and the final score
            window.fill(BLACK)
            game_over_message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            window.blit(game_over_message, [window_width / 6, window_height / 3])
            display_score(snake_length - 1)
            pygame.display.update()

            # Wait for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        snake_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -segment_speed
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = segment_speed
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -segment_speed
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = segment_speed

        # Update the position of the snake
        x += x_change
        y += y_change

        # Check for collisions with the boundaries of the window
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_over = True

        # Clear the window
        window.fill(BLACK)

        # Draw the food
        pygame.draw.rect(window, RED, [food_x, food_y, segment_size, segment_size])

        # Update the segments of the snake
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_segments.append(snake_head)

        # Remove the oldest segment if the snake is longer than its length
        if len(snake_segments) > snake_length:
            del snake_segments[0]

        # Check for collisions with the snake's own body
        for segment in snake_segments[:-1]:
            if segment == snake_head:
                game_over = True

        # Draw the snake
        draw_snake(segment_size, snake_segments)

        # Check for collisions with the food
        if x == food_x and y == food_y:
            # Generate a new position for the food
            food_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
            food_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size
            # Increase the length of the snake
            snake_length += 1

        # Display the score
        display_score(snake_length - 1)

        # Update the display
        pygame.display.update()

        # Set the frames per second
        clock.tick(15)

    pygame.quit()

# Run the Snake game
snake_game()
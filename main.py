import pygame
import random

# Initialize Pygame
pygame.init()

# Set up game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game with Background")

# Load background image
background_image = pygame.image.load("background.jpg")  # Replace with your image file path

# Colors
green = (0, 255, 0)

# Snake settings
snake_block = 20
snake_speed = 15
snake = [(window_width // 2, window_height // 2)]
snake_direction = "RIGHT"

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Change snake direction based on key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake_direction != "DOWN":
            snake_direction = "UP"
        if keys[pygame.K_DOWN] and snake_direction != "UP":
            snake_direction = "DOWN"
        if keys[pygame.K_LEFT] and snake_direction != "RIGHT":
            snake_direction = "LEFT"
        if keys[pygame.K_RIGHT] and snake_direction != "LEFT":
            snake_direction = "RIGHT"

    # Move the snake...
    # (Same code as before)

    # Clear the screen
    window.blit(background_image, (0, 0))

    # Draw snake...
    # (Same code as before)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(snake_speed)

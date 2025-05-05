import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Ball setup
ball_radius = 10
ball_color = (255, 0, 0)
ball_pos = [WIDTH // 2, HEIGHT // 2]  #(0, 0) is the top-left corner of the screen.
ball_vel = [1, -2]  # speed in x and y

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Bounce on walls
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= WIDTH:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
        ball_vel[1] = -ball_vel[1]

    # Draw ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
sys.exit()

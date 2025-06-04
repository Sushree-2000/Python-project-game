import pygame
import sys
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Spaceship Asteroid Avoider")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
# print(f"clock timing = {clock}")
# exit

# Spaceship
# ship = pygame.rec
ship = pygame.Rect(WIDTH//2 - 25, HEIGHT - 60, 50, 40)
ship_speed = 5

# Asteroids
asteroids = []
asteroid_speed = 5
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1000)  # Spawn every 1 sec

# Game Loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == SPAWN_EVENT:
            x_pos = random.randint(0, WIDTH - 30)
            asteroids.append(pygame.Rect(x_pos, 0, 30, 30))

    # Move spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship.left > 0:
        ship.x -= ship_speed
    if keys[pygame.K_RIGHT] and ship.right < WIDTH:
        ship.x += ship_speed

    # Move asteroids
    for asteroid in asteroids:
        asteroid.y += asteroid_speed

    # Collision detection
    for asteroid in asteroids:
        if ship.colliderect(asteroid):
            print("💥 Crash! Game Over!")
            pygame.quit()
            sys.exit()

    # Draw spaceship and asteroids
    pygame.draw.rect(screen, (0, 255, 255), ship)
    for asteroid in asteroids:
        pygame.draw.rect(screen, (255, 0, 0), asteroid)

    pygame.display.flip()
    clock.tick(60)

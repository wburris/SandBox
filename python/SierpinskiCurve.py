import pygame
import sys
import time
import os
from datetime import datetime

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
#WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sierpinski Curve")

#vertices = []
def draw_line(color, x1, y1, x2, y2):
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)
    #vertices.append((x1, y1))
    #pygame.event.pump()  # Process event queue
    #pygame.display.flip()
    #time.sleep(0.05)
    return x2, y2

def sierpinski(level):
    screen.fill(BLACK)
    total_length = 0.9 * min(WIDTH, HEIGHT)
    dist = total_length / (3 * 2 ** level - 1)
    x = (WIDTH - total_length) / 2
    y = (HEIGHT - total_length) / 2 + dist
    #vertices.clear()

    x, y = sierp_b(level, dist, x, y)
    x, y = draw_line(RED, x, y, x + dist, y + dist)
    x, y = sierp_c(level, dist, x, y)
    x, y = draw_line(RED, x, y, x + dist, y - dist)
    x, y = sierp_d(level, dist, x, y)
    x, y = draw_line(RED, x, y, x - dist, y - dist)
    x, y = sierp_a(level, dist, x, y)
    x, y = draw_line(RED, x, y, x - dist, y + dist)
    #pygame.draw.polygon(screen, GREEN, vertices, 1)

def sierp_b(level, dist, x, y):
    if level == 1:
        x, y = draw_line(ORANGE, x, y, x + dist, y + dist)
        x, y = draw_line(ORANGE, x, y, x, y + dist)
        x, y = draw_line(ORANGE, x, y, x - dist, y + dist)
    else:
        x, y = sierp_b(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x + dist, y + dist)
        x, y = sierp_c(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x, y + dist)
        x, y = sierp_a(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x - dist, y + dist)
        x, y = sierp_b(level - 1, dist, x, y)
    return x, y

def sierp_c(level, dist, x, y):
    if level == 1:
        x, y = draw_line(ORANGE, x, y, x + dist, y - dist)
        x, y = draw_line(ORANGE, x, y, x + dist, y)
        x, y = draw_line(ORANGE, x, y, x + dist, y + dist)
    else:
        x, y = sierp_c(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x + dist, y - dist)
        x, y = sierp_d(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x + dist, y)
        x, y = sierp_b(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x + dist, y + dist)
        x, y = sierp_c(level - 1, dist, x, y)
    return x, y

def sierp_d(level, dist, x, y):
    if level == 1:
        x, y = draw_line(ORANGE, x, y, x - dist, y - dist)
        x, y = draw_line(ORANGE, x, y, x, y - dist)
        x, y = draw_line(ORANGE, x, y, x + dist, y - dist)
    else:
        x, y = sierp_d(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x - dist, y - dist)
        x, y = sierp_a(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x, y - dist)
        x, y = sierp_c(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x + dist, y - dist)
        x, y = sierp_d(level - 1, dist, x, y)
    return x, y

def sierp_a(level, dist, x, y):
    if level == 1:
        x, y = draw_line(ORANGE, x, y, x - dist, y + dist)
        x, y = draw_line(ORANGE, x, y, x - dist, y)
        x, y = draw_line(ORANGE, x, y, x - dist, y - dist)
    else:
        x, y = sierp_a(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x - dist, y + dist)
        x, y = sierp_b(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x - dist, y)
        x, y = sierp_d(level - 1, dist, x, y)
        x, y = draw_line(GREEN, x, y, x - dist, y - dist)
        x, y = sierp_a(level - 1, dist, x, y)
    return x, y

def save_screen(screen):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    current_time = datetime.now()
    time_str = current_time.strftime("%Y%m%d%H%M%S")
    filename = f"screenshots/sierp_{time_str}.png"
    pygame.image.save(screen, filename)

def main():
    level = 2
    sierpinski(level)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    level = min(level + 1, 6)
                    sierpinski(level)
                elif event.key == pygame.K_DOWN:
                    level = max(level - 1, 1)
                    sierpinski(level)
                if event.key == pygame.K_s:
                    save_screen(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

import pygame
import sys
import os
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up the display
#WIDTH, HEIGHT = 800, 800
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hilbert Curve")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
line_color = GREEN

def hilbert(screen, level, dx, dy, start_x, start_y):
    if level > 0:
        start_x, start_y = hilbert(screen, level - 1, dy, dx, start_x, start_y)
        
        end_x = start_x + dx
        end_y = start_y + dy
        pygame.draw.line(screen, line_color, (start_x, start_y), (end_x, end_y), 2)
        start_x, start_y = end_x, end_y
        
        start_x, start_y = hilbert(screen, level - 1, dx, dy, start_x, start_y)
        
        end_x = start_x + dy
        end_y = start_y + dx
        pygame.draw.line(screen, line_color, (start_x, start_y), (end_x, end_y), 2)
        start_x, start_y = end_x, end_y
        
        start_x, start_y = hilbert(screen, level - 1, dx, dy, start_x, start_y)
        
        end_x = start_x - dx
        end_y = start_y - dy
        pygame.draw.line(screen, line_color, (start_x, start_y), (end_x, end_y), 2)
        start_x, start_y = end_x, end_y
        
        start_x, start_y = hilbert(screen, level - 1, -dy, -dx, start_x, start_y)
    
    return start_x, start_y

def draw_curve(screen, level, total_length):
    start_length = total_length // (2 ** level - 1)
    start_x = (WIDTH - total_length) // 2
    start_y = (HEIGHT - total_length) // 2
    screen.fill(BLACK)
    hilbert(screen, level, start_length, 0, start_x, start_y)

def save_screen(screen):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    current_time = datetime.now()
    time_str = current_time.strftime("%Y%m%d%H%M%S")
    filename = f"screenshots/hilbert_{time_str}.png"
    pygame.image.save(screen, filename)

def main():
    level = 4
    total_length = int(0.9 * min(WIDTH, HEIGHT))
    draw_curve(screen, level, total_length)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    level = min(level + 1, 8)
                    draw_curve(screen, level, total_length)
                elif event.key == pygame.K_DOWN:
                    level = max(level - 1, 1)
                    draw_curve(screen, level, total_length)
                elif event.key == pygame.K_s:
                    save_screen(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)

PURPLE = (128, 0, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

display_surface.fill(PURPLE)

CENTER = (300, 300)
RADIUS = 150
pygame.draw.circle(display_surface, BLACK, CENTER, RADIUS)

START = (100, 50)
END = (300, 400)
pygame.draw.line(display_surface, MAGENTA, START, END, 100)

TOP_LEFT_X = 100
TOP_LEFT_Y = 200
WIDTH = 75
HEIGHT = 150
DATA = (TOP_LEFT_X, TOP_LEFT_Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, CYAN, DATA)

TOP_LEFT_X = 100
TOP_LEFT_Y = 400
WIDTH = 400
HEIGHT = 100
DATA = (TOP_LEFT_X, TOP_LEFT_Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, CYAN, DATA)

START = (500, 70)
END = (300, 400)
pygame.draw.line(display_surface, MAGENTA, START, END, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
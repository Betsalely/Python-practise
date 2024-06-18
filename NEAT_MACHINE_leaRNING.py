import pygame
import numpy as np
import random

# Constants
WIDTH, HEIGHT = 480, 480  # Canvas size (10x scaling of 28x28)
PIXEL_SIZE = WIDTH // 16
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 40
SCREEN_WIDTH, SCREEN_HEIGHT = WIDTH, HEIGHT + BUTTON_HEIGHT
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 255)
BUTTON_TEXT_COLOR = WHITE
BRIGHTNESS_INCREMENT = 0.1

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("28x28 Pixel Canvas")

# Canvas data
canvas = np.zeros((16, 16), dtype=np.float32)

weights_layer1 = [random.uniform(-3.99, 3.99) for _ in range(265*16)]
weights_layer2 = [random.uniform(-3.99, 3.99) for _ in range(16*16)]
weights_layer3 = [random.uniform(-3.99, 3.99) for _ in range(16*10)]

hidden_layer1 = [0.00] * 16
hidden_layer2 = [0.00] * 16


def draw_grid():
    for x in range(0, WIDTH, PIXEL_SIZE):
        pygame.draw.line(screen, GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, PIXEL_SIZE):
        pygame.draw.line(screen, GREY, (0, y), (WIDTH, y))

# Draw canvas function
def draw_canvas():
    for y in range(16):
        for x in range(16):
            brightness = canvas[y, x] * 255  # Scale to 0-255 for display
            color = (brightness, brightness, brightness)
            pygame.draw.rect(screen, color, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

# Draw button function
def draw_button():
    button_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, HEIGHT + 10, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render('Predict', True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect

# Predict function
def predict(canvas):
    sum = 0
    for i in range(len(canvas)):
        for j in range(len(canvas)):
            weights_added = canvas[i][j] * weights_layer1[j]
            sum += weights_added
    print(sum)
    print(sigmoid(sum))
    

def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
            x, y = pygame.mouse.get_pos()
            if y < HEIGHT:
                grid_x, grid_y = x // PIXEL_SIZE, y // PIXEL_SIZE
                if 0 <= grid_x < 16 and 0 <= grid_y < 16:
                    canvas[grid_y, grid_x] = min(canvas[grid_y, grid_x] + BRIGHTNESS_INCREMENT, 1.0)  # Increase brightness

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button is clicked
            x, y = pygame.mouse.get_pos()
            button_rect = draw_button()
            if button_rect.collidepoint(x, y):
                predict(canvas)

    screen.fill(BLACK)
    draw_canvas()
    draw_grid()
    draw_button()
    pygame.display.flip()


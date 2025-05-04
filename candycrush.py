import pygame
import random
import time  # for adding a small delay

# Initialize Pygame
pygame.init()

# Constants
ROWS, COLS = 8, 8
TILE_SIZE = 50
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Match-3 Game")

# Colors (representing candies)
CANDY_COLORS = [
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (255, 165, 0),   # Orange
    (128, 0, 128)    # Purple
]

# Create board
def generate_board():
    return [[random.randint(0, len(CANDY_COLORS) - 1) for _ in range(COLS)] for _ in range(ROWS)]

board = generate_board()

# Swap tiles
def swap(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]

# Check for matches
def find_matches():
    matched = [[False] * COLS for _ in range(ROWS)]

    # Horizontal match
    for r in range(ROWS):
        for c in range(COLS - 2):
            if board[r][c] == board[r][c+1] == board[r][c+2]:
                matched[r][c] = matched[r][c+1] = matched[r][c+2] = True

    # Vertical match
    for c in range(COLS):
        for r in range(ROWS - 2):
            if board[r][c] == board[r+1][c] == board[r+2][c]:
                matched[r][c] = matched[r+1][c] = matched[r+2][c] = True

    return matched

# Remove matches and refill board
def remove_and_refill(matched):
    for c in range(COLS):
        col = [board[r][c] for r in range(ROWS) if not matched[r][c]]
        while len(col) < ROWS:
            col.insert(0, random.randint(0, len(CANDY_COLORS) - 1))
        for r in range(ROWS):
            board[r][c] = col[r]

# Draw board
def draw_board():
    for r in range(ROWS):
        for c in range(COLS):
            color = CANDY_COLORS[board[r][c]]
            pygame.draw.rect(SCREEN, color, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(SCREEN, (0, 0, 0), (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

# Main loop
running = True
first_click = None
clock = pygame.time.Clock()

while running:
    SCREEN.fill((50, 50, 50))
    draw_board()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // TILE_SIZE
            row = y // TILE_SIZE
            if first_click is None:
                first_click = (row, col)
            else:
                second_click = (row, col)
                # Check adjacency
                if abs(first_click[0] - second_click[0]) + abs(first_click[1] - second_click[1]) == 1:
                    swap(first_click, second_click)
                    matches = find_matches()
                    while any(any(row) for row in matches):  # Repeat while matches are found
                        remove_and_refill(matches)
                        matches = find_matches()  # Check for new matches after removal
                        draw_board()  # Redraw the board after each removal
                        pygame.display.update()
                        time.sleep(0.5)  # Add a small delay for better gameplay experience
                    else:
                        swap(first_click, second_click)  # swap back if no match
                first_click = None

    clock.tick(60)

pygame.quit()
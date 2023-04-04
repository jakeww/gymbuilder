import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Gym Builder")

# Set up the game variables
money = 100
floor_cost = 10
floor_width = 50
floor_height = 50

# Set up the grid
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

# Track whether the player is currently clicking and dragging to place tiles
dragging = False
start_pos = None
end_pos = None

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the player has enough money to place a floor tile
            if money >= floor_cost:
                # Start tracking the click and drag placement of the tile
                dragging = True
                start_pos = event.pos
                end_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            # End tracking the click and drag placement of the tile
            dragging = False
            # Get the start and end grid positions
            start_column = start_pos[0] // floor_width
            start_row = start_pos[1] // floor_height
            end_column = end_pos[0] // floor_width
            end_row = end_pos[1] // floor_height
            # Calculate the total cost of the floor tiles
            num_rows = abs(end_row - start_row) + 1
            num_columns = abs(end_column - start_column) + 1
            total_tiles = num_rows * num_columns
            total_cost = total_tiles * floor_cost
            # Check if the player has enough money to place the floor tiles
            if money >= total_cost:
                # Subtract the cost of the floor tiles from the player's money
                money -= total_cost
                # Place the floor tiles on the grid
                for row in range(start_row, end_row + 1):
                    for column in range(start_column, end_column + 1):
                        grid[row][column] = 1
        elif event.type == pygame.MOUSEMOTION:
            # If the player is currently dragging to place a tile, update the end position
            if dragging:
                end_pos = event.pos

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = BLACK
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [column * floor_width, row * floor_height, floor_width, floor_height])

    # Draw the player's money
    font = pygame.font.Font(None, 36)
    text = font.render("Money: $" + str(money), True, BLACK)
    screen.blit(text, [10, 10])

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()

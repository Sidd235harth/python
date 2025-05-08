import time
import os
import copy

# Define the dimensions of the grid
WIDTH = 20
HEIGHT = 20

# Create the initial state of the grid (you can randomize or hardcode it)
def create_grid():
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Glider pattern
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

    return grid

# Display the grid
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print("".join(['█' if cell else ' ' for cell in row]))

# Count live neighbors
def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
            count += grid[nx][ny]
    return count

# Update the grid based on the rules
def update_grid(grid):
    new_grid = copy.deepcopy(grid)
    for x in range(HEIGHT):
        for y in range(WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[x][y] = 0
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

# Main loop
def run_game():
    grid = create_grid()
    while True:
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.3)

if __name__ == "__main__":
    run_game()

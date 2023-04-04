import random

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def add_tile(grid, tile_type, cost):
    while True:
        x = int(input(f"Enter x-coordinate for {tile_type}: "))
        y = int(input(f"Enter y-coordinate for {tile_type}: "))
        if grid[y][x] == "E":
            grid[y][x] = tile_type
            return cost
        else:
            print("Tile already occupied. Please choose another position.")

def generate_customers():
    return random.randint(1, 20)

def calculate_revenue(customers, grid):
    revenue = 0
    for row in grid:
        revenue += row.count("C") * 5 * customers
        revenue += row.count("F") * 4 * customers
        revenue += row.count("S") * 3 * customers
    return revenue

def calculate_expenses(grid):
    expenses = 0
    for row in grid:
        expenses += row.count("C") * 3
        expenses += row.count("F") * 2
        expenses += row.count("S") * 1
    return expenses

grid = [["E" for _ in range(5)] for _ in range(5)]
balance = 100

tile_info = {
    "C": {"name": "Cardio", "cost": 10},
    "F": {"name": "Freeweights", "cost": 10},
    "S": {"name": "Fitness Studio", "cost": 10},
}

while True:
    print_grid(grid)
    print(f"Balance: ${balance}")
    action = input("Enter 'B' to buy a tile or 'Q' to quit: ").upper()
    if action == "B":
        tile = input("Enter 'C' for Cardio, 'F' for Freeweights, or 'S' for Fitness Studio: ").upper()
        if tile in tile_info and balance >= tile_info[tile]["cost"]:
            balance -= add_tile(grid, tile, tile_info[tile]["cost"])
        else:
            print("Invalid tile or insufficient funds.")
    elif action == "Q":
        break
    else:
        print("Invalid action.")

    customers = generate_customers()
    revenue = calculate_revenue(customers, grid)
    expenses = calculate_expenses(grid)
    balance += revenue - expenses

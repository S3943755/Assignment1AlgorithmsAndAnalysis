import random

# Scenario 2
size = 100  # Size of the grid (number of rows and columns)
output_file = "scenarioUpdatingValsLrg.txt"  # Output file name

with open(output_file, "w") as f:
    for i in range(500):
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        value = round(random.uniform(-10, 10), 1)
        f.write(f"U {row} {col} {value}\n")
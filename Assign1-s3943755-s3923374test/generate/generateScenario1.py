import random

# Scenario 1
size = 32  # Size of the grid (number of rows and columns)
output_file = "scenarioAppendRowsColsLow.txt"  # Output file name


with open(output_file, "w") as f:
    for i in range(100): # iRows
        row = random.randint(0, size - 1)
        f.write(f"IR {row}\n")
    for i in range(100): # iCols
        col = random.randint(0, size - 1)
        f.write(f"IR {col}\n")
    for i in range(100): # Rows
        f.write(f"R\n")
    for i in range(100): # Cols
        f.write(f"C\n")
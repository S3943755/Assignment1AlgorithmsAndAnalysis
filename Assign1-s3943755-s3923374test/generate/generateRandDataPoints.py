import random

# Input parameters
size = 100  # Size of the grid (number of rows and columns)
density = 0.5  # Density of random values
outputFile = "dataHMT3.txt"  # Output file name

numVals = int(size * size * density) # amount of values on the board that would contain the randomly generated values.  

with open(outputFile, "w") as f: # generate random values in the spreadsheet
    for i in range(numVals):
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        value = round(random.uniform(-10, 10), 1)
        f.write(f"{row} {col} {value}\n")
def probability_of_survival(N, x, y, n):
    if x < 0 or x >= N or y < 0 or y >= N:
#out of bounds
        return 0.0  
#safe
    if n == 0:
        return 1.0  

#N,E,W,S
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    

    probability = 0.0


    for dx, dy in directions:
        probability += 0.25 * probability_of_survival(N, x + dx, y + dy, n - 1)

    return probability

size = 10  # Size of the island (N*N matrix)
row = 3  # Starting position (row)
column = 4  # Starting position (column)
steps = 8  # Number of steps

result = probability_of_survival(size, row, column, steps)
print("Probability :", result)
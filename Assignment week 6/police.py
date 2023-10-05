import random
import numpy as np

def catchThieves(grid, k):
    rows, cols = len(grid), len(grid[0])
    policemen = []
    thieves = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'P':
                policemen.append((i, j))
            elif grid[i][j] == 'T':
                thieves.append((i, j))

    caught_thieves = set()
    num_thieves_caught = 0

    #euclidean distance

    for policeman in policemen:
        sorted_thieves = sorted(
            thieves, key=lambda thief: abs(thief[0] - policeman[0]) + abs(thief[1] - policeman[1])
        )

        for thief in sorted_thieves:
            if thief not in caught_thieves and (
                abs(thief[0] - policeman[0]) <= k or abs(thief[1] - policeman[1]) <= k
            ):
                caught_thieves.add(thief)
                num_thieves_caught += 1
                break

    return num_thieves_caught,len(thieves),len(policemen)

def random_grid_gen(m,n):
	def thing():
		p = random.randint(0,2)
		if p == 1:
			return "P"
		return "T"
	grid = [[thing() for _ in range(n)] for _ in range(m)]
	return grid

m = 5
n = 5

grid = random_grid_gen(m,n)
k = 1

number_thieves_caught, number_thieves, number_cops = catchThieves(grid,k)

arr = np.array(grid)

print(arr)

print("Total Number of Theives caught : ",number_thieves_caught)
print("Total Number of Theives : ",number_thieves)
print("Total Number of Cops : ",number_cops)


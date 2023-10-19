import random as rd

class knapsack:
	
	def knap(n,cap,profit,weight):

		matrix = [[-1 for _ in range(cap+1)] for _ in range(n+1)]

		for i in range(n+1):
			for j in range(cap+1):
				if i == 0 or cap == 0:
					matrix[i][j] = 0
				elif weight[i-1] <= j:
					matrix[i][j] = max(profit[i-1] + matrix[i-1][j - weight[i-1]],matrix[i-1][j])
				else:
					matrix[i][j] = matrix[i-1][j]

		return matrix[n][cap]



graph_caps = [3,10,100,200,300,500,700,1000,1200,1300]

profits = [[rd.randint(0,100) for _ in range(i)] for i in graph_caps]
weights = [[rd.randint(1,30) for _ in range(i)] for i in graph_caps]

obj = knapsack

result = []

for index,elements in enumerate(profits):
	profit = elements
	weight = weights[index]

	cap = 50
	n = len(elements)
	result.append(obj.knap(n,cap,profit,weight))


print(result)
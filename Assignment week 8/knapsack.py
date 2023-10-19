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



profits = [[60, 100, 120],[1, 2, 3, 10, 20],[10, 40, 30, 50]]
weights = [[10, 20, 30],[2, 3, 4, 5, 9],[5, 4, 6, 3]]
caps = [50,10,10]

obj = knapsack

result = []

for index,elements in enumerate(profits):
	profit = elements
	weight = weights[index]

	cap = caps[index]
	n = len(elements)
	result.append(obj.knap(n,cap,profit,weight))


print(result)
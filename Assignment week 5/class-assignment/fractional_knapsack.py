import time
import random

def knapsack(activities:dict,W):
	ratio_sort = dict(sorted(activities.items(),key=lambda item:item[0]/item[1],reverse = True))
	profit = 0

	for i in ratio_sort:
		if W-ratio_sort[i] > 0:
			profit+=i
			W-=ratio_sort[i]
		else:
			profit+=(W/ratio_sort[i])*i
			break
	return profit

example1 = {50:10,60:20,80:30}
W1 = 40

example2 = {10: 2,5: 3,15: 5,7: 7,6: 1}
W2 = 10

example3 = {100: 20,60: 10,120: 40,50: 30}
W3 = 50

things = [example1,example2,example3]
weights = [W1,W2,W3]

for i in range(len(weights)):
    profit = knapsack(things[i],weights[i])
    print(f"Profit for {things[i]} is {profit}")
import time
import random

activities = {50:10,60:20,80:30}

ratio_sort = dict(sorted(activities.items(),key=lambda item:item[0]/item[1],reverse = True))

W = 40
profit = 0

for i in ratio_sort:
	if W-ratio_sort[i] > 0:
		profit+=i
		W-=ratio_sort[i]
	else:
		profit+=(W/ratio_sort[i])*i
		break

print(profit)
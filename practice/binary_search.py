import time
#from threading import Threading yo

arr  = [i for i in range(10000)]

key = 9999

def bin_search(arr,i,j,key):
	if (i == j):
		if key == arr[i]:
			return i
		return -1
	else:
		mid = (i+j)//2
		if key == arr[mid]:
			return mid
		elif key < arr[mid]:
			return bin_search(arr,i,mid-1,key)
		else:
			return bin_search(arr,mid+1,j,key)

def normal_search(arr,key):
	for a,i in enumerate(arr):
		if i == key:
			return a

start = time.time()
index = bin_search(arr,0,len(arr)-1,key)
time.sleep(1)
end = time.time()
time_taken_bin = end-start

start = time.time()
index = normal_search(arr,key)
time.sleep(1)
end = time.time()
time_taken_normal = end-start

print(f"Time taken for normal : {time_taken_normal}")
print(f"Time taken for divide : {time_taken_bin}")




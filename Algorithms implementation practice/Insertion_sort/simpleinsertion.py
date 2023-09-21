import random as rd

arr = [8,7,6,5,4,3,2,1,0]

for j in range(1,len(arr)):
    key = arr[j]
    i = j-1
    
    while arr[i] > key and i>-1:
        arr[i+1] = arr[i]
        i-=1
    arr[i+1] = key
    
print(arr)
import random

li = [random.randint(1,1000) for i in range(10)]

class sorting:
	def __init__(self,arr):
		self.arr = arr
		self.b = [0]*len(arr)
		self._mergeSort(low = self.arr[0],high = self.arr[-1])
	def _mergeSort(self,low,high):
		if low<high:
			mid = (low+high)//2
			self._mergeSort(low,mid);
			self._mergeSort(mid+1,high)
			self._merge(low,mid,high)
	def _merge(self,low,mid,high):
		h = low
		i = low
		j = mid+1
		while h<=mid and j<=high:
			if self.arr[h]<=self.arr[j]:
				self.b[i] = self.arr[h]
				h+=1
			else:
				self.b[i] = a[j]
				j+=1
			i+=1
		if h >mid:
			for d in range(k,high+1):
				self.b[i] = self.arr[k]
				i+=1
		else:
			for d in range(h,mmid+1):
				self.b[i] = self.arr[k]
				i+=1
		for d in range(low,high+1):
			self.arr[k] = self.b[k]	

sorter = sorting(li)
print(sorter.b)
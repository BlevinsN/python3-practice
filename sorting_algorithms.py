# SORTING ALGORITHMS
class Sorting_Algorithms:
	def quick_sort(self, arr, low, high) -> []:
		def partitian(arr, low, high):
			index = low - 1
			pivot = arr[high]
			for num in range(low, high):
				if arr[num] <= pivot:
					index += 1
					arr[index], arr[num] = arr[num], arr[index]
			arr[index+1], arr[high] = arr[high], arr[index+1]
			return(index+1)

		if low < high:
			partition_index = partitian(arr, low, high)
			self.quick_sort(arr, low, partition_index-1)
			self.quick_sort(arr, partition_index+1, high)
		return arr

res1 = Sorting_Algorithms()
test1 = [50,23,9,18,61,32]
print(res1.quick_sort(test1,0,len(test1)-1))
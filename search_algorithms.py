# SEARCH ALGORITHMS
class Search_Algorithms:
	def binary_search(self, to_find:int, arr) -> int:
		def bin_search(arr, to_find, left, right):
			mid = int((left + right) / 2)
			if arr[mid] == to_find:
				return mid
			elif arr[mid] > to_find:
				return bin_search(arr, to_find, left, mid)
			elif arr[mid] < to_find:
				return bin_search(arr, to_find, mid, right)
			else:
				return -1
		return bin_search(arr, to_find, 0, len(arr)-1)

test1 = [1,2,3,4,5,6,7,8,9,10]
res1 = Search_Algorithms()
print(res1.binary_search(9, test1))
print(res1.binary_search(5, test1))
print(res1.binary_search(6, test1))
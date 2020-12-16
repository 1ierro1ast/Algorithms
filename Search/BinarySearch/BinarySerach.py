from timeit import timeit

def binarySearch(sortedList: list, item):
	"""
	O(log2(n))
	"""
	low = 0
	high = len(sortedList) - 1
	tryValue = 0
	while low <= high:
		mid = (low + high) // 2
		guess = sortedList[mid]
		tryValue += 1
		if guess < item:
			low = mid + 1
		elif guess > item:
			high = mid - 1
		else:
			print(tryValue)
			return mid
	return None

mySortedList = list(range(0, 1000000))
tryValue = 100
elapsedTime = timeit('binarySearch(mySortedList, 18)','from __main__ import mySortedList, binarySearch', number=tryValue)/tryValue
print(elapsedTime)

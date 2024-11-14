def binary_search(key, sequence):
	def helper(low, high): #use this function to compare if both are less or more
		if low > high:
			return False
		mid = (low + high) // 2 #get the middle, 0 + 10 // 2
		print(f' mid = {mid}') #in first iteration, it will return 5
		if key == sequence[mid]: #if 15 is == sequence[5] #(6), return true
			return True
		elif key < sequence[mid]: #else if 15 is < 6, return helper again with (0, and 5-1)
			return helper(low, mid-1)
		else:
			return helper(mid+1, high) #else return helper(5+1, 10)
	return helper(0, len(sequence)-1)


print(binary_search(15,[1,2,3,4,5,6,7,15,17,19,22]))


def selection_sort():
	a = [4,12,3,1,11]
	sort = []
	while a:
		smallest = a[0]
		for element in a:
			if element < smallest:
				smallest = element
		a.remove(smallest)
		sort.append(smallest)
		print(a)

def merge_sort(lst):
	if len(lst) > 2:
		return lst



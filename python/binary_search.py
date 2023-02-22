import math
def binary_search(start, end, nums, target):
	mid = math.floor((start + end)//2)
	if target == mid:
		return mid
	elif start == mid and end == mid:
		return "Not Found"
	
	if target > mid:
		return binary_search(mid + 1, len(nums)-1, nums, target)
	return  binary_search(0, mid-1, nums, target)


nums = [9,3,5,3,1,8]
nums.sort()
binary_search(0, len(nums) - 1, nums, 5)
	 
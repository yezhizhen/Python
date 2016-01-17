
def nextPermutation( nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	i = len(nums)-2
	while i>=0:
		if(nums[i]<nums[i+1]):
			break
		i-=1
	if i== -1:
		return nums.sort()
	for j in range(len(nums)-1,i,-1):
		if(nums[j]>nums[i]):
			nums[j],nums[i] = nums[i],nums[j]
			nums[i+1:]=reversed(nums[i+1:])
			break
	
	
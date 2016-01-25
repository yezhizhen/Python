class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = []
		self.permutes(nums, 0, res)
		return res
		
	def permutes(self, nums, start, res):
		def check(j):
			for i in range(start,j):
				if(nums[i] == nums[j] ):
					return	True
			return False
		
		if start == len(nums) - 1:
			res.append(nums[:])
			return
		for i in range(start, len(nums)):
			if check(i):
				continue
			nums[i], nums[start] = nums[start], nums[i]
			self.permutes(nums, start+1, res)
			nums[i], nums[start] = nums[start], nums[i]
	
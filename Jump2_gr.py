class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # you want to jump now
        step,near,far = 0,0,1
        # far represents [far-1] elements you can reach
        while far < len(nums):
            #next_far = max(i+j for i,j in zip(range(near,far), nums[near:far])) + 1
            # find next_far faster
            next_far = 0
            for i in range(near,far):
                next_far = max(next_far, i+nums[i]+1) 
            near,far,step = far, next_far, step+1 
        return step
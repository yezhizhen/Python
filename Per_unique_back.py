class Solution(object)
    def permute(self, nums)
        
        type nums List[int]
        rtype List[List[int]]
        
        mylist = []
        self.permutes(nums, 0,mylist)
        return mylist
        
    def permutes(self, nums, start, mylist)
        #swap nums start with nums[i]
        if start == len(nums)-1
            mylist.append(nums[])
            return
        for i in range(start, len(nums))
            nums[start], nums[i] = nums[i], nums[start]
            self.permutes(nums, start + 1, mylist)
            nums[i], nums[start] = nums[start],nums[i]
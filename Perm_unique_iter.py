class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            new_res = []
            for subset in res:
                for i in range(len(subset)+1):
                    new_res.append(subset[:i] + [num] + subset[i:])
            res = new_res
        return res
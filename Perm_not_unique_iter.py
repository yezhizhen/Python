class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for num in nums:
            new_ans =[]
            for subset in ans:
                for i in range(len(subset)+1):
                    new_ans.append(subset[:i] + [num] + subset[i:])
                    if (i < len(subset) and subset[i] == num):
                        break
            ans = new_ans
        return ans
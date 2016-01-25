def canJump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    m = len(nums)
    dp = [[-1 for a in range(m)] for _ in range(m)]
    return jum(nums,0,len(nums)-1, dp)    
    

def jum(nums, start, end, dp):
    #base case
    if start + nums[start] >= end:
        return True
    if dp[start][end] != -1:
        return dp[start][end]
    #intermediate steps taken
    k = start+nums[start]+1
    for i in range(start+1,min(k,end+1)):
        dp[start][end] = jum(nums,start,i,dp) and jum(nums,i,end,dp)
        if dp[start][end]:
            return True
        return False

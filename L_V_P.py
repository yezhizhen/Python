#https://leetcode.com/problems/longest-valid-parentheses/
class Solution(object):
    def lvp_stack(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        temp = [-1]
        for i in range(len(s)):
            if s[i] ==')' and temp[-1]>=0 and s[temp[-1]] =='(':
                temp.pop()
                longest = max(longest, i-temp[-1])
                
            else:
                temp.append(i)
        return longest
	
    def lvp_studpid_dp(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        dp = [0 for x in range(m)]
        longest = 0
        for i in range(1,m):
            if s[i] == '(':
                continue
            #find nearest
            else:
                if s[i-1] =='(':
                    if i - 2 >=0:
                            dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                #in this case, s[i-1] == ')'
                else:
                    temp = i-1-dp[i-1]
                    if temp<0:
                        continue
                    elif s[temp] ==')':
                        continue
                    elif s[temp] =='(':
                        # recursively plus
                        dp[i] = dp[i-1] +2 +dp[temp-1]
                            
                    
            longest = max(longest,dp[i])
        return longest
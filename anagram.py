# Hash Map. Make good use of keys.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        ans = []
        for ele in strs:
            temp = ''.join(sorted(ele))
            if dic.has_key(temp):
                dic[temp].append(ele)
            else:
                dic[temp] = [ele]
        #For every subset in the values set
        #memory efficient way to do this?
        for subset in dic.values():
            subset.sort()
            ans.append(subset)
        return ans
#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        mapping = {')':'(', ']':'[','}':'{'}
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char in mapping.values():
                    stack.append(char)
                else:
                     tem = stack.pop()
                     if tem != mapping[char]:
                         return False
        if len(stack) > 0:
            return False
        return True
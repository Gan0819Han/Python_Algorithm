class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = list()
        for i in s:
            if  stack and stack[-1]==i:
                stack.pop()
            else :
                stack.append(i)
        return "".join(stack)
    
EXM = Solution()
s = "abbaac"
print(f"结果是{EXM.removeDuplicates(s)}")
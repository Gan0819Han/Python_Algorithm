# 判断有效括号
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "{":
                stack.append("}")
            elif i == "[":
                stack.append("]")
            elif not stack or stack[-1]!= i:
                return False
            else:
                stack.pop()

        return True if not stack else False
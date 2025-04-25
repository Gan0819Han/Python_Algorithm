# 比较含退格的字符串
# class Solution(object):
#     def backspaceCompare(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         def build(s):
#             temp = list()
#             for char in s:
#                 if char != "#":
#                     temp.append(char)
#                 elif temp:
#                     temp.pop()
#             return "".join(temp)
        
#         return (build(s)==build(t))
    
# solution = Solution()
# s = "a#c"
# t = "b"
# print(solution.backspaceCompare(s,t))

##############################################

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        
        return True
    
solution = Solution()
s = "a#c"
t = "b"
print(solution.backspaceCompare(s,t))
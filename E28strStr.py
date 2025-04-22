class Solution(object):
    # 这道题为KMP算法以及NEXT数组的常规应用：“最长相等字串”问题
    def calculateNext(self,next,s):
        """
        lst(->str): 传入"模式串"用于求其Next数组
        """
        n = len(s)
        j = 0
        # 遍历模式串
        for i in range(1,n):
            # 定义next数组的起始数是0

            # 求解剩下部分的最小相等前缀
            while(s[j]!=s[i] and j > 0):
                j = next[j-1]
            if(s[j]==s[i]):
                j += 1
            next[i] = j
                
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        next = [0] * len(needle)
        self.calculateNext(next,needle)
        j = 0
        for i in range(len(haystack)):
            while(j>0 and haystack[i]!=needle[j]):
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
            
        return -1
    
EXM = Solution()
s = "abcabcabcabc"
print(EXM.strStr(s,"abc"))
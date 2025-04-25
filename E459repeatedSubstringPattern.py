class Solution:
    def repeatedSubstringPattern(self, s):  
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        # print(f"nxt[-1]={nxt[-1]} , len(s)%(len(s)-nxt[-1])= {len(s) % (len(s) - nxt[-1])} ")
        if nxt[-1] != 0 and len(s) % (len(s) - nxt[-1]) == 0:
            return True
        return False
    
    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt
    
EXM = Solution()
s = "ababab"
next = [0] * len(s)
print(EXM.getNext(next,s))
print(EXM.repeatedSubstringPattern(s))
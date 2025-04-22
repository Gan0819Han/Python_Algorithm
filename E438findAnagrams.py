# 哈希表
# 找到字符串中所有字母的异位词
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 先列哈希表记录p
        record_p = [0] * 26
        len_p = len(p)
        record_s = [0] * 26
        len_s = len(s)
        result=[]
        
        if(len_p > len_s):
            return result
        for i in p:
            record_p[ord(i)-ord("a")] += 1
            
        # 先比第一轮
        for i in range(len_p):
            record_s[ord(s[i])-ord("a")] += 1
            
        if(record_s==record_p):
            result.append(0)
            
        # 类比滑动窗口进行检索
        for i in range(len_s - len_p):
            record_s[ord(s[i])-ord("a")] -= 1
            record_s[ord(s[i+len_p])-ord("a")] += 1

            if(record_s==record_p):
                result.append(i+1)
                
        return result

exm = Solution()
s = "abcdabcabcdabc"
t = "abc"
print(exm.findAnagrams(s,t))
        
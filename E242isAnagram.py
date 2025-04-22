# 哈希表
# 有效的字母异位词
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = [0] * 26
        for i in s:
            # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            # ord 用于返回ASCII码，这里就是记录相对位置了
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                # record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True
    
solve = Solution()
s = "abcdefg"
t = "gfedcba"
print(solve.isAnagram(s,t))
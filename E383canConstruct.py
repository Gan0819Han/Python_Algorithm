# 哈希表
# 赎金信
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        record = [0]*26
        for i in magazine:
            record[ord(i)-ord("a")] += 1
            
        for j in ransomNote:
            record[ord(j)-ord("a")] -= 1  
            
        # 如果有下标 <0 说明用多了
        for k in range(26):
            if record[k]<0:
                return False
            
        return True
    
solve = Solution()
ransomNote = "abcdf"
magazine = "aabceff"
print(solve.canConstruct(ransomNote,magazine))
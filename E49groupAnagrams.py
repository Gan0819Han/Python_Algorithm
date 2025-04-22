class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        mp = defaultdict(list)
        
        # 一个单词一个单词的读
        for i in strs:
            record = [0] * 26
            # 遍历单词的字母并记录到字母哈希表里
            for j in i:
                record[ord(j) - ord("a")] += 1
            mp[tuple(record)].append(i)   
                
        return list(mp.values())
    
str1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
Exm = Solution()
print(Exm.groupAnagrams(str1))
            
             
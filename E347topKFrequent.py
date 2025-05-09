
from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        time_dict = defaultdict(int)
        for num in nums:
            time_dict[num] += 1
        
        # 更改字典，key为出现次数，value为相应的数字的集合
        index_dict = defaultdict(list)
        for key in time_dict:
            index_dict[time_dict[key]].append(key)
            
        # 排序
        key = list(index_dict.keys())
        key.sort()
        result = []
        cnt = 0
        
        # 获取前k项的值
        while key and cnt != k:
            result += index_dict[key[-1]]
            cnt += len(index_dict[key[-1]])
            key.pop()
            
        return result[0:k]
    
nums = [1,1,1,2,2,3]
k = 2
EXM = Solution()
print(EXM.topKFrequent(nums,k))
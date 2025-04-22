# 两数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = dict()
        for index,value in enumerate(nums):
            if (target - value) in record:
                return [record[target-value],index]
            record[value] = index
        return []
    
EXM = Solution()
nums = [1,2,3,4,5,6,7,8,9]
print(EXM.twoSum(nums,17))
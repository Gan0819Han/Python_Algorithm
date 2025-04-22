class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        # a = nums[i],b=nums[j],c=-(a+b)
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i > 0 and nums[i]==nums[i-1]:
                continue # 对a去重
            
            d = {}
            
            for j in range(i+1,len(nums)):
                if j > i + 2 and nums[j-1]==nums[j-2]:
                    continue # 对b去重
                c = 0 - (nums[i]+nums[j])
                if c in d:
                    result.append([nums[i],nums[j],c])
                    d.pop(c)
                else:
                    d[nums[j]]=j
                    
        return result
    
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 排序
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > target and nums[i] > 0 and target > 0:
                break
            if i > 0 and nums[i]==nums[i-1]:
                continue # 去重
            for j in range(i+1,n):
                if nums[i] + nums[j] > target and target>0:
                    break
                if j > i+1 and nums[j]==nums[j-1]:
                    continue # 去重
                left,right = j+1,n-1
                while left<right:
                    s = nums[i]+nums[j]+nums[left]+nums[right]
                    if s == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left]==nums[left+1]:
                            left += 1
                        while left < right and nums[right]==nums[right-1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                        
                    elif s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                        
        return result
                    
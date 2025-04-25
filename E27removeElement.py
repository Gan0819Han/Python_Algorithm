class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    
solution = Solution()

nums = [1,2,3,4,5,6,7,8,9]
val = 5

new_length = solution.removeElement(nums,val)

# 截取部分
processed_nums = nums[:new_length]
print(processed_nums)
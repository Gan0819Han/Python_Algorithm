# 长度最小的子数组

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start,end = 0,len(nums)
        min_len = float("inf")
        sum = 0
        for i in range(end):
            # print(f'第{i}轮')
            sum += nums[i]
            while(sum >= target):
                sum -= nums[start]                
                min_len = min(min_len,(i - start + 1) )
                # print(f"此时的i是{nums[i]},start是{nums[start]}")
                # print(f"此时的min_len是{min_len}")
                start += 1
            i += 1
    
        return min_len if min_len != float("inf") else 0

solution = Solution()
nums = [5,1,3,5,10,7,4,9,2,8]
print(solution.minSubArrayLen(15,nums))
                
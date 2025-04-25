class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 初始化慢指针 slow
        slow = 0
        
        # 遍历数组
        for fast in range(len(nums)):
            # 如果当前 fast 指针指向的元素不是零
            if nums[fast] != 0:
                # 将 fast 指针的值赋给 slow 指针的位置
                nums[slow] = nums[fast]
                # 如果 slow 和 fast 不在同一位置，将 fast 位置置为 0
                if slow != fast:
                    nums[fast] = 0
                # 慢指针向前移动
                slow += 1

# 测试代码
solution = Solution()
nums = [1, 2, 3, 4, 0, 0, 0, 0, 1, 2, 3, 4]
print(f"处理前: {nums}")
solution.moveZeroes(nums)
print(f"处理后: {nums}")
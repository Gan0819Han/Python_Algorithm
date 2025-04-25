class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        i = 0
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

# 创建算法实例
solution = Solution()

# 浏览记录列表
browse_records = [101, 101, 102, 103, 103, 103, 104, 104, 105]

# 调用算法方法，获取去重后的新长度
new_length = solution.removeDuplicates(browse_records)

# 截取去重后的部分
unique_browse_records = browse_records[:new_length]

# 打印结果
print("去重后的浏览记录：", unique_browse_records)
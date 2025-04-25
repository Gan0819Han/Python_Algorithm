class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(nums) and nums[left] == target else -1

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right if right >= 0 and nums[right] == target else -1

        start = find_first(nums, target)
        if start == -1:
            return [-1, -1]
        end = find_last(nums, target)
        return [start, end]

# 测试代码
solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))  # 输出: [3, 4]
print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))  # 输出: [-1, -1]
print(solution.searchRange([], 0))                   # 输出: [-1, -1]
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1

        return right

# 测试代码
solution = Solution()
print(solution.mySqrt(4))  
print(solution.mySqrt(8))  
print(solution.mySqrt(16)) 
print(solution.mySqrt(2147395599))
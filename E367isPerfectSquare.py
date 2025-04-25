# 有效的完全平方数
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        
        left,right = 1,num
        while (left<=right):
            mid = (left+right)//2
            if(mid*mid < num):
                left = mid + 1
            elif(mid*mid > num):
                right = mid -1
            elif (mid*mid == num):
                return True
        return False

solution = Solution()
print(solution.isPerfectSquare(0)) 
print(solution.isPerfectSquare(1)) 
print(solution.isPerfectSquare(2)) 
print(solution.isPerfectSquare(3)) 
print(solution.isPerfectSquare(4)) 
print(solution.isPerfectSquare(16)) 




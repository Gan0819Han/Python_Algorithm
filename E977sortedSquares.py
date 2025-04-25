# 有序数组的平方
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        start,end = 0,n-1
        k = n-1
        new = [0]*n
        while(start <= end):
            if (nums[start]**2 > nums[end]**2):
                new[k]=nums[start]**2
                start += 1
                k -= 1
            elif (nums[start]**2 < nums[end]**2):
                new[k]=nums[end]**2
                end-= 1
                k -= 1
            elif (nums[start]**2 == nums[end]**2):
                new[k]=nums[end]**2
                end-= 1
                k -= 1
        return new

solution=Solution()
list1 = [-8,-5,-4,-2,-1,0,3,6,7,9,10]
list2 = [-7,-3,2,3,11]
print(solution.sortedSquares(list1))
print(solution.sortedSquares(list2))

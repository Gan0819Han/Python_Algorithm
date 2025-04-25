# 第704题

class Solution:
    def search(self,nums,target):
        left,right = 0,len(nums)-1
        while(left <= right):
            middle = left + (right - left) // 2
            if(nums[middle] > target):
                right = middle - 1
            elif(nums[middle]< target):
                left = middle + 1
            else:
                return middle
        return -1

solution = Solution()
num = [1,3,4,5,6,7,8,123,332]
target = 45
result = solution.search(num,target)
print(f"目标值的索引是:{result}")
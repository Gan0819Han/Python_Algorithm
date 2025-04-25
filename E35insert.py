# 35题：搜索插入位置
class Solution():
    def insert(self,nums,target):
        left,right = 0,len(nums)-1
        while(left<=right):
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle -1
            else:
                return middle
            
        return right + 1
    
solution = Solution()
nums = [1,2,3,4,6,7,8,9,10]
target = 9
result = solution.insert(nums,target)
print(f"{target}在当前列表的位置是第{result + 1}个")
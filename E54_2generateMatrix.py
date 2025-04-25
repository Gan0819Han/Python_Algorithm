# 螺旋矩阵 —— 存数字
class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 初始化矩阵
        nums = [[0]*n for _ in range(n)]
        # 确定起始位置
        startx,starty = 0,0
        # 确定循环圈数与中间点
        loop,mid = n//2,n//2
        # 填充数
        count = 1

        for offset in range(1,loop+1):
            # 按顺序旋转并填写数字
            # 从左到右,左闭右开
            for i in range (starty,n-offset):
                nums[startx][i] = count
                count += 1
            # 从上到下,上闭下开
            for i in range(startx,n-offset):
                nums[i][n-offset] = count
                count += 1
            # 从右到左，右闭左开
            for i in range(n-offset,starty,-1):
                nums[n-offset][i] = count
                count += 1
            # 从下到上，下闭上开
            for i in range(n-offset,startx,-1):
                nums[i][starty]=count
                count += 1
            startx += 1
            starty += 1

        if n % 2 != 0: # n为奇数的时候，填充中心点
            nums[mid][mid] = count
        
        return nums
    
solution = Solution()
n = 6
print(f"n为{n}时,结果为\n{solution.generateMatrix(n)}")



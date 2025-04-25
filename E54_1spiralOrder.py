# 螺旋矩阵 —— 取数字
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        loop = min(m,n)//2
        start_row,start_col = 0,0
        ans = [0]*m*n
        count = 0
        offset = 0
        # 转圈圈
        for offset in range(1,loop+1):
            # 左右
            for i in range(start_col,n-offset):
                ans[count] = matrix[start_row][i]
                count += 1
            # 上下
            for i in range(start_row,m-offset):
                ans[count] = matrix[i][n-offset]
                count += 1
            # 右左
            for i in range(n-offset,start_col,-1):
                ans[count] = matrix[m-offset][i]
                count += 1
            # 下上
            for i in range(m-offset,start_row,-1):
                ans[count] = matrix[i][start_col]
                count += 1
            start_col += 1
            start_row += 1

        # 补充剩下的部分
        if n > m and m%2!=0: 
            for i in range(start_col,n-offset):
                ans[count] = matrix[start_row][i]
                count += 1
        elif n < m and n%2!=0:
            for i in range(start_row,m-offset):
                ans[count] = matrix[i][start_col]
                count += 1
        elif n == m and n%2!=0:
            ans[count] = matrix[start_row][start_col]
            count += 1

        return ans
    
solution = Solution()
matrix =[[2,5],[8,4],[0,-1]]
print(f"{solution.spiralOrder(matrix)}")


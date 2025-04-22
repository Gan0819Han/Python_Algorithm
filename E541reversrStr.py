class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 内置函数用于反转字符串，将题目拆分成两个部分：
        # 1、按规则切片
        # 2、反转需要的部分
        
        def reverse_str(str):
            left,right = 0,len(str)-1
            while(left<right):
                str[left],str[right]=str[right],str[left]
                left += 1
                right -= 1
            return str
        
        temp = list(s)
        
        for i in range(0,len(s),2*k): # 按步数做切片
            temp[i:i+k] = reverse_str(temp[i:i+k])
            
        return ''.join(temp)
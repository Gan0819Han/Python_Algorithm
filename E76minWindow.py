# 最小覆盖子串
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t) :
            return ""
        
        # 记录t中的字母 初始化count表
        count = defaultdict(int)
        for char in t:
            count[char] += 1
        
        # 记录t中不同字符的种类数
        m = len(count)

        # 初始化滑动窗口
        left = right = 0
        min_len = float("inf")
        ans = [-1,-1]

        # 遍历s字符串
        while(right < len(s)):
            char_right = s[right]
            if char_right in count:
                count[char_right] -= 1
                if count[char_right] == 0:
                    m -= 1
            # 条件字符都被满足的时候，记录当前窗口
            while(m==0):
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    ans = [left,right]

                # 移动左指针
                char_left = s[left]
                if char_left in count:
                    count[char_left] += 1
                    if count[char_left] > 0:
                        m += 1
                left += 1 # 已经记录了，所以继续往后找
            
            right += 1

        return s[ans[0]:ans[1]+1] if min_len!= float("inf") else ""
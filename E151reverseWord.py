class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = s.split()
        
        left,right = 0,len(st)-1
        while(left < right):
            st[left],st[right] = st[right],st[left]
            left += 1
            right -= 1
            
        result = str()
        for i in st:
            result = result + i
            result = result + ' '
        result = result[:-1]
        return result
            
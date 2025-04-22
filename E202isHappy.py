class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = []
        while(n not in record):
            record.append(n)
            sum = 0
            num = str(n)
            for i in num:
                sum += int(i)*int(i)
            if sum == 1:
                return True
            n = sum
        return False            
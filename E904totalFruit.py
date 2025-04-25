# 水果成篮
from collections import Counter

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = Counter()

        left = ans = 0
        for right, x in enumerate(fruits):
            count[x] += 1
            while(len(count)>2):
                count[fruits[left]] -= 1
                if count[fruits[left]]==0:
                    count.pop(fruits[left])
                left += 1
            ans = max(ans,right - left + 1)

        return ans

fruits = [3,3,3,1,2,1,1,2,3,3,4]
solution = Solution()
print(solution.totalFruit(fruits))
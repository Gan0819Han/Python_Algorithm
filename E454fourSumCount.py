# 四数之和
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import defaultdict

        # 计算 nums1 和 nums2 的所有两数之和及其出现次数
        sumAB = defaultdict(int)
        for a in nums1:
            for b in nums2:
                sumAB[a + b] += 1

        # 计算 nums3 和 nums4 的所有两数之和及其出现次数
        sumCD = defaultdict(int)
        for c in nums3:
            for d in nums4:
                sumCD[c + d] += 1

        count = 0
        # 遍历 sumCD，统计满足条件的组合数量
        for target in sumCD:
            if -target in sumAB:
                count += sumAB[-target] * sumCD[target]

        return count
    
EXM = Solution()
nums1 = [1,2]
nums2 = [-2,-1] 
nums3 = [-1,2]
nums4 = [0,2]
print(EXM.fourSumCount(nums1,nums2,nums3,nums4))
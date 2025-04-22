class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        record1 = [0] * 1001
        record2 = [0] * 1001
        result = []
        for i in nums1:
            record1[i] += 1
        # print(record1)
        
        for i in nums2:
            record2[i] += 1  
        # print(record2) 
        
        count = 0
        while(count<1001):
            if record1[count] and record2[count]:
                result.append(count)
            count += 1
            
        return result
            
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
EXM = Solution()
print(EXM.intersection(nums1,nums2))
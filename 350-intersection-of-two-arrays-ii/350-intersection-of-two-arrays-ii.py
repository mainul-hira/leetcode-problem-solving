class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        intersect_val = []
        for i in nums1:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        for j in nums2:
            if j in result and result[j]>0:
                result[j] -= 1
                intersect_val.append(j)
        return intersect_val
        
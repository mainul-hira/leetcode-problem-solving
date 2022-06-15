class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, current_sum = -inf , 0
        for i in nums:
            current_sum = max(i, current_sum+i)
            if max_sum<current_sum:
                max_sum = current_sum
        return max_sum
                
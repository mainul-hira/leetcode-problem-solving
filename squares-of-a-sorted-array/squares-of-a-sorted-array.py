class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_list = [0]*len(nums)
        l_p, r_p = 0, len(nums)-1
        
        while l_p<=r_p:
            left_val, right_val = abs(nums[l_p]), abs(nums[r_p])
            if left_val>right_val:
                sorted_list[r_p-l_p] = left_val*left_val
                l_p += 1
            else:
                sorted_list[r_p-l_p] = right_val*right_val
                r_p -= 1
        return sorted_list
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        result = 0
        for i in range(2, len(nums)):
            if nums[i] + nums[i-2] == nums[i-1] / 2:
                result += 1

        return result
    
sol = Solution()
print(sol.countSubarrays([1,2,1,4,1]))
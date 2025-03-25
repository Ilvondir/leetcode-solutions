from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_nums = 1

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[unique_nums] = nums[i]
                unique_nums += 1

        return unique_nums

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
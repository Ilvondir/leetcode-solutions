from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        zero_indexes = []

        for i in range(len(nums) - 1):

            if nums[i] == 0:
                zero_indexes.append(i)
                continue

            if nums[i] == nums[i+1]:
                if len(zero_indexes) > 0:
                    nums[zero_indexes.pop(0)] = nums[i] * 2
                    nums[i+1] = 0
                    nums[i] = 0
                    zero_indexes.append(i)
                else:
                    nums[i] = nums[i] * 2
                    nums[i+1] = 0
            else:
                if len(zero_indexes) > 0:
                    nums[zero_indexes.pop(0)] = nums[i]
                    nums[i] = 0
                    zero_indexes.append(i)

        if len(zero_indexes) > 0:
            nums[zero_indexes.pop(0)] = nums[-1]
            nums[-1] = 0

        return nums
    

sol = Solution()
nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]

print(sol.applyOperations(nums))
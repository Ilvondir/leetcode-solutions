from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ones = 0
        twos = 0

        i=0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                ones += 1
                twos += 1
            elif nums[i] == 1:
                nums.pop(i)
                nums.insert(ones, 1)
                ones += 1
                twos += 1
            else:
                nums.pop(i)
                nums.insert(twos, 2)
                twos += 1
            i+=1


sol = Solution()
nums = [0,1,0,1,2,2,2,2,0,0,1,2,2,1]
sol.sortColors(nums)
print(nums)
        
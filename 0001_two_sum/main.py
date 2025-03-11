from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            if nums[i] not in my_map.keys():
                my_map[nums[i]] = [i]
            else:
                my_map[nums[i]].append(i)

            if target - nums[i] in my_map.keys():
                if i != my_map[target - nums[i]][0]:
                    return [i, my_map[target - nums[i]][0]]
            

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_nums = []
        for i in range(len(nums)):
            if i == 0:
                my_nums.append(nums[i])
            else:
                my_nums.append(nums[i])
                for j in range(len(my_nums)):
                    if my_nums[j] + nums[i] == target and i != j:
                        return [i, j]
                    

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

sol = Solution()
print(sol.twoSum(nums=[12, 1, 3, 3, 2, 1], target=1))
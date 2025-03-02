from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        len_n1, len_n2 = len(nums1), len(nums2)
        dict = {}
        max_key = nums1[-1][0] if nums1[-1][0] > nums2[-1][0] else nums2[-1][0]
        max_len = len_n1 if len_n1 > len_n2 else len_n2
        result_array = []

        for i in range(max_len):

            if (len_n1 > i):
                if nums1[i][0] in dict.keys():
                    dict[nums1[i][0]] += nums1[i][1]
                else:
                    dict[nums1[i][0]] = nums1[i][1]

            if (len_n2 > i):
                if nums2[i][0] in dict.keys():
                    dict[nums2[i][0]] += nums2[i][1]
                else:
                    dict[nums2[i][0]] = nums2[i][1]

        keys = dict.keys()
        for key in range(max_key + 1):
            if key in keys:
                result_array.append([key, dict[key]])
        
        return result_array

        

sol = Solution()
nums1 = [[1,2],[2,3],[4,5], [5,1]]
nums2 = [[1,4],[3,2],[4,1]]
print(sol.mergeArrays(nums1, nums2))
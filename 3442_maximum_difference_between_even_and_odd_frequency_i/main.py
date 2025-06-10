class Solution:
    def maxDifference(self, s: str) -> int:
        frequency_dictionary = dict()

        for char in s:
            if char in frequency_dictionary.keys():
                frequency_dictionary[char] += 1
            else:
                frequency_dictionary[char] = 1

        max_odd = 0
        min_even = 100

        for value in frequency_dictionary.values():
            if value % 2 == 0:
                if value < min_even:
                    min_even = value
            else:
                if value > max_odd:
                    max_odd = value
            
    
        return max_odd - min_even

print(Solution().maxDifference('abcabcab'))
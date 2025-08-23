class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        
        pointer_1 = 0
        pointer_2 = 1
        max_len = 1

        while pointer_2 < len(s)+1:
            current_window = s[pointer_1:pointer_2]

            if len(set(current_window)) == (pointer_2 - pointer_1):
                pointer_2 += 1
                current_len = len(current_window)
                if (current_len > max_len):
                    max_len = current_len
            else:
                pointer_1 += 1

        return max_len
        
sol = Solution()
print(sol.lengthOfLongestSubstring('au'))
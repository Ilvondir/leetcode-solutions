from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        res = ''

        for i in range(len(strs[0])):
            if len(strs[-1]) > i:
                if strs[0][i] == strs[-1][i]:
                    res += strs[0][i]
                else:
                    break
            else:
                break

        return res

sol = Solution()
print(sol.longestCommonPrefix(['cat', 'catman', 'catty']))

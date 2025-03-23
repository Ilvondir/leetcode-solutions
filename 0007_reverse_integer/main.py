import time

class Solution:
    def reverse(self, x: int) -> int:
        is_minus = True if x < 0 else False
        x_str = str(-x) if is_minus else str(x)
        res = ''.join(x_str[-i] for i in range(1, len(x_str)+1, 1))

        if int(res) > 2**31:
            return 0

        return int(res) if not is_minus else int('-' + res)
    

sol = Solution()
print(sol.reverse(-123))
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reversed = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if len(stack) > 0:
                    if stack[-1] == reversed[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

sol = Solution()
print(sol.isValid(''))
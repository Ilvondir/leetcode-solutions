class Solution:
    def romanToInt(self, s: str) -> int:

        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        current_index = len(s)-1
        result = 0

        while True:
            if current_index < 0:
                break

            if s[current_index-1:current_index+1] in symbols:
                result += symbols[s[current_index-1:current_index+1]]
                current_index -= 2
            else:
                result += symbols[s[current_index]]
                current_index -= 1

        return result


        

sol = Solution()
print(sol.romanToInt('IV'))
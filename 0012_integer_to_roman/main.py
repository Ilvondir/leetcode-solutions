class Solution:
    def intToRoman(self, num: int) -> str:

        result = ''

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        current_index = 0

        while current_index < len(values):
            if num >= values[current_index]:
                result += symbols[current_index]
                num -= values[current_index]
            else:
                current_index += 1

        return result
        

sol = Solution()
print(sol.intToRoman(999))
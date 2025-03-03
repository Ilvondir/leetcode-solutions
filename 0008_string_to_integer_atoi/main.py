
class Solution:
    def myAtoi(self, s: str) -> int:

        legal_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
        numbers = []
        output = 0
        is_number_started = False
        is_positive = False
        is_sign_submitted = False

        for i in range(len(s)):

            if (is_number_started and s[i] not in legal_characters[:-2]) or (not is_number_started and s[i] not in legal_characters + [' ']) or (s[i] in legal_characters[-2:] and is_sign_submitted):
                break

            if s[i] in legal_characters[-2:] and not is_sign_submitted:
                is_number_started = True
                if not is_sign_submitted:
                    is_sign_submitted = True
                    is_positive = s[i] == '+'

            if s[i] in legal_characters[:-2]:
                
                if not is_number_started:
                    is_number_started = True

                    if not is_sign_submitted:
                        is_sign_submitted = True
                        is_positive = True
                
                numbers.append(int(s[i]))

        len_numbers = len(numbers)
        for i in range(len_numbers):
            output += numbers[len_numbers - i - 1] * 10 ** i

        output = output if is_positive else -output

        if output >= 2**31:
            output = 2**31 - 1
        elif output < -(2**31):
            output = -(2**31)

        return output


sol = Solution()
num = '+-12'

print(sol.myAtoi(num))
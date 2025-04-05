class Solution:
    def myAtoi(self, s: str) -> int:
        # T: O(n), S: O(1)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Read numeric characters
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Step 4: Handle overflow
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return sign * num
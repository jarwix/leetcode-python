class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        neg = 1
        while (i < len(s) and s[i] == ' '):
            i += 1
        while (i < len(s)) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                neg = -1
                if ((i != 0) and (s[i-1] == '-' or s[i-1] == '+')):
                    return 0
            if s[i] == '+':
                if ((i != 0) and (s[i-1] == '-' or s[i-1] == '+')):
                    return 0
            i += 1
        number = 0
        while (i < len(s)) and (s[i] >= '0' and s[i] <= '9'):
            number *= 10
            number += int(s[i])
            if (number > 2147483647):
                if (neg == -1):
                    return -2147483648
                else:
                    return 2147483647
            i += 1
        return number * neg
        

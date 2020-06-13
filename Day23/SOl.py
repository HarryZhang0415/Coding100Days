class Solution:
    def calculate(self, s: str) -> int:
        s += '+0'  ## for the last number of the loop
        
        stack, num, mark = [], 0, '+'
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * int(num) + int(s[i])
            elif not s[i].isdigit() and s[i] != ' ':
                if mark == '+': stack.append(num)
                if mark == '-': stack.append(-num)
                if mark == '*': stack.append(stack.pop(-1) * num)
                if mark == '/': stack.append(int(stack.pop(-1) / num))  ## using int() rather than // is because -3 // 2 = -2 and we need it to be -1
                mark = s[i]
                num = 0
        
        return sum(stack)
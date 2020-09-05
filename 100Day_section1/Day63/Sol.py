class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        
        s = '+' + s.replace(' ','') + '+'
        
        tmp_number = 0
        tmp_op = '+'
        
        idx = 0
        
        while idx < len(s):
            if s[idx].isdigit():
                
                tmp_number = tmp_number * 10 + int(s[idx])
                idx += 1
                
            elif s[idx] == '+':
                
                tmp_number = tmp_number if tmp_op == '+' else -tmp_number
                stack.append(tmp_number)
                tmp_number = 0
                tmp_op = '+'
                idx += 1
                
            elif s[idx] == '-':
                
                tmp_number = tmp_number if tmp_op == '+' else -tmp_number
                stack.append(tmp_number)
                tmp_number = 0
                tmp_op = '-'
                idx += 1
                
            elif s[idx] == '*':
                
                prev_number = tmp_number
                tmp_number = 0
                idx += 1
                while s[idx].isdigit():
                    tmp_number = 10 * tmp_number + int(s[idx])
                    idx += 1
                    
                tmp_number *= prev_number
                
            elif s[idx] == '/':
                
                prev_number = tmp_number
                tmp_number = 0
                idx += 1
                while s[idx].isdigit():
                    tmp_number = 10 * tmp_number + int(s[idx])
                    idx += 1
                    
                tmp_number = prev_number // tmp_number
            else:
                idx += 1
                
        return sum(stack)     
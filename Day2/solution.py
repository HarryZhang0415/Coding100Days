""" 
Using stack and queue
There are three stacks, stack for numbers, letter, and bracket

for stack of letter, add "" for initialization to avoid pure words error
(string like "leercode")

"""
class Solution:
    def decodeString(self, s: str) -> str:
        numbers = []
        letter = [""]
        bracket = []
        
        point = 0
        number = ''

        while point < len(s):
            if s[point] in [str(i) for i in range(10)]:
                number += s[point]
            elif s[point] == '[':
                letter.append('')
                if number:
                    numbers.append(number)
                else:
                    numbers.append('1')
                    
                number = ''
                bracket.append(s[point])
            elif s[point] == ']':
                n = int(numbers.pop())
                l = letter.pop()
                bracket.pop()
                if letter:
                    letter[-1] += n*l
                else:
                    letter.append(n*l)
            else:
                letter[-1] += s[point]

            point += 1
        
        return "".join(letter)



s = Solution()
print(s.decodeString("leetcode"))
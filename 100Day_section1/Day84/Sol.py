class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        self.stack = collections.deque()
        
        def generator(n,k,tmp_ans):
            if len(str(tmp_ans)) == n:
                if tmp_ans not in self.stack:
                    self.stack.append(tmp_ans)
                return
            else:
                prev = tmp_ans % 10
                if prev + k >= 0 and prev + k < 10:
                    generator(n,k,tmp_ans*10 + prev + k)
                    generator(n,-k,tmp_ans*10 + prev + k)
                else:
                    return
        for i in range(1,10):
            generator(N,K,i)
            generator(N,-K,i)
        
        if N == 1:
            self.stack.append(0)
            return self.stack
        return self.stack
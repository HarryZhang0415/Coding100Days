class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.l = collections.deque()
        def generator(characters, length, tmp_ans, idx):
            if len(tmp_ans) == length:
                self.l.append(tmp_ans)
                return
            if idx >= len(characters):
                return
            else:
                generator(characters, length, tmp_ans + characters[idx], idx + 1)
                generator(characters, length, tmp_ans, idx + 1)
        generator(characters, combinationLength, '', 0)
        
    def next(self) -> str:
        return self.l.popleft()
                
    def hasNext(self) -> bool:
        if self.l:
            return True
        else:
            return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
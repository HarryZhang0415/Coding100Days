## Sol 1  -- time limit exceed
import collections
from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = collections.deque()
        
    def match(self, w1, w2):
        idx = 0
        
        while idx < len(w1):
            if w1[idx] == '.':
                idx += 1
                continue
            if w1[idx] != w2[idx]:
                return False
            idx += 1
        
        return True
    
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if word not in self.que:
            self.que.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        for w2 in self.que:
            if len(word) != len(w2):
                continue
            if self.match(word, w2):
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Sol 2: 

class WordDictionary:
    def __init__(self):
        self.d = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        m = len(word)
        for dict_word in self.d[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False


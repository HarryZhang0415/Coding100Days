### sorted can use for multiple keys
import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        word_dict = collections.defaultdict(int)
        
        for w in words:
            word_dict[w] += 1
        
        w = [k for k, v in sorted(word_dict.items(), key=lambda item: (-item[1], item[0]))]

        return w[:k]
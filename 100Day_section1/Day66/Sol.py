class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(int)
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.dic[timestamp] += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        tmp_dic = {k:v for k, v in self.dic.items() if (timestamp >= k and timestamp - k < 300)}
        
        return sum(tmp_dic.values())
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
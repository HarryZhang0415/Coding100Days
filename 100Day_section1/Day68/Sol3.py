### 注意同一时间！ 注意 0 时刻！

import collections 

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = collections.defaultdict(lambda: -1)
        self.print_ts = collections.defaultdict(list)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        prev = self.ts[message]
        
        if timestamp in self.print_ts[message]:
            return False
        
        if prev < 0:
            self.ts[message] = timestamp
            self.print_ts[message].append(timestamp)
            return True
        elif timestamp - prev >= 10:
            self.ts[message] = timestamp
            self.print_ts[message].append(timestamp)
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
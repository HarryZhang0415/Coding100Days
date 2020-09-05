class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.values = []
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            idx = self.keys.index(key)
            self.values[idx] = value
            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.keys:
            return -1
        
        return self.values[self.keys.index(key)]
        
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key not in self.keys:
            return
        
        else:
            idx = self.keys.index(key)
            
            self.keys.pop(idx)
            self.values.pop(idx)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
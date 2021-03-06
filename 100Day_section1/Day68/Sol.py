class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for p in paths:
            tmp = p.split(' ')
            dir = tmp[0]
            
            for file in tmp[1:]:
                content = file[file.index('(') + 1:-1]
                f_name = file[:file.index('(')]
                ans[content].append(dir+ '/' + f_name)
        
        return [v for k,v in ans.items() if len(v) > 1]



'''BFS vs DFS
BFS explores neigbours first. This means that files which are located close to each other are also accessed one after another. This is great for space locality and that's why BFS is expected to be faster. Also, BFS is easier to parellelize.

Very large files and false positives
For very large files we should do the following comparisons in this order:

compare sizes, if not equal, then files are different and stop here!
hash them with a fast algorithm e.g. MD5 or use SHA256 (no collisions found yet), if not equal then stop here!
compare byte by byte to avoid false positives due to collisions.
Have you used an IDE in remote development mode?
For example, CLion has some options on how to compare the local files with the remote server files and then decides to synchronize or not.

Complexity
Runtime - Worst case (which is very unlikely to happen): O(N^2 * L) where L is the size of the maximum bytes that need to be compared
Space - Worst case: all files are hashed and inserted in the hashmap, so O(H^2*L), H is the hash code size and L is the filename size'''
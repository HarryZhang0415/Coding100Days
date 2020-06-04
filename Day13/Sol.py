## not accepted

import collections

class Solution:
    def leastInterval(self, tasks, n):
        
        def sort_tasks(tasks):
            counts = collections.Counter(tasks)
            new_list = sorted(tasks, key=counts.get, reverse=True)
            return new_list
        
        tasks = sort_tasks(tasks)
        
        task_index = {}
        idx = 0
        idx_list = []
        max_length = 0

        for t in range(len(tasks)):
            task = tasks[t]
            if task not in task_index:
                while idx in idx_list:
                    idx += 1
                task_index[task] = idx
                idx_list.append(task_index[task])
                idx += 1
            else:
                task_index[task] = task_index[task] + n + 1
                idx_list.append(task_index[task])
            
            max_length = max(max_length, task_index[task])
        
        res = [''] * (max_length+1)
        for i in range(len(tasks)):
            _ = idx_list[i]
            res[_] = tasks[i]
        
        ttt = tasks
        
        return max_length + 1


L = ["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"]
n = 2

s = Solution()
s.leastInterval(L,n)
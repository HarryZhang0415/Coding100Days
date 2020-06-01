class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.ans = []

        def search(candidates, target, tmp_list):
            if sum(tmp_list) > target:
                return 
            
            elif sum(tmp_list) == target and sorted(tmp_list) not in self.ans:
                self.ans.append(sorted(tmp_list))
                return

            else:
                for cand in candidates:
                    if cand > target:
                        continue
                    search(candidates, target, tmp_list + [cand])
        
        search(candidates, target, [])
        
        return self.ans


## A better way -- tarck the index of the search algorithm to accelerate the speed

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.ans = []

        def search(candidates, target, tmp_list,index_tracker):
            if sum(tmp_list) > target:
                return 
            
            elif sum(tmp_list) == target and sorted(tmp_list) not in self.ans:
                self.ans.append(sorted(tmp_list))
                return

            else:
                for idx in range(index_tracker,len(candidates)):
                    if candidates[idx] > target:
                        continue
                    search(candidates, target, tmp_list + [candidates[idx]], idx)
        
        search(candidates, target, [], 0)
        
        return self.ans

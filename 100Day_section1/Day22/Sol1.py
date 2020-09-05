#Partially true
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True
        
        from collections import defaultdict
        self.d = defaultdict(list)
        
        for pre in prerequisites:
            self.d[pre[0]] = pre[1]
        
        def search(course, tmp_list, numCourses):
            if course not in self.d.keys():
                return True

            else:
                if self.d[course] in tmp_list:
                    return False
                else:
                    return search(self.d[course], tmp_list + [course], numCourses)
        
        for key in self.d.keys():
            if search(key, [], numCourses):
                return True
        
        return False
            
        
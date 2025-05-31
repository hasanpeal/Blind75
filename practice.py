from typing import List

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i : [] for i in range(numCourses)}
        for c, p in prerequisites:
            preq[c].append(p)
        visited = set()

        def dfsCycleDetect(c):
            if c in visited:
                return False
            if preq[c] == []:
                return True
            visited.add(c)
            for pre in preq[c]:
                if not dfsCycleDetect(pre):
                    return False
            visited.remove(c)
            preq[c] = []
            return True
        
        for p in range(numCourses):
            if not dfsCycleDetect(p):
                return False
        return True
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white = 1
        gray = 2
        black = 3

        # O(V) space complexity
        color = {c: white for c in range(numCourses)}
        
        # O(V + E) space complexity since we store the vertices on the key and values the edges
        must_take = defaultdict(list)
        for a, b in prerequisites:
            must_take[b].append(a)

        # o(E) time complexity
        def dfs(node):

            color[node] = gray
            for pre in must_take[node]:
                if color[pre] == white:
                    if dfs(pre):
                        return True
                elif color[pre] == gray:
                    return True
                    
            color[node] = black

        # o(V) time complexity
        # so total time complexity will be o(V + E)
        for node in range(numCourses):
            if color[node] == white:
                if dfs(node):
                    return False
            
        return True
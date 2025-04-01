#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        def dfs_helper(node):
            visited[node] = True
            traversal.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_helper(neighbor)
        
        V = len(adj)
        visited = [False] * V
        traversal = []
        dfs_helper(0)
        return traversal
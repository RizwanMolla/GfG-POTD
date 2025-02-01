class Solution:
    def isWordExist(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or mat[i][j] != word[index]:
                return False
            visited[i][j] = True
            if (dfs(i + 1, j, index + 1) or
                dfs(i - 1, j, index + 1) or
                dfs(i, j + 1, index + 1) or
                dfs(i, j - 1, index + 1)):
                return True
            visited[i][j] = False
            return False
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
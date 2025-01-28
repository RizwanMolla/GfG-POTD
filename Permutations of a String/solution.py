class Solution:
    def findPermutation(self, s):
        # Sort the string to handle duplicates
        s = sorted(s)
        results = []
        visited = [False] * len(s)

        def backtrack(path):
            # If the path length matches the string length, it's a valid permutation
            if len(path) == len(s):
                results.append("".join(path))
                return
            
            for i in range(len(s)):
                # Skip duplicates or already visited characters
                if visited[i] or (i > 0 and s[i] == s[i - 1] and not visited[i - 1]):
                    continue
                
                # Mark as visited
                visited[i] = True
                # Add to the current path
                backtrack(path + [s[i]])
                # Backtrack (unmark the visited)
                visited[i] = False

        backtrack([])
        return results

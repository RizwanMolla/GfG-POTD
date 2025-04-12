class Solution:
    def floodFill(self, image, sr, sc, newColor):
        originalColor = image[sr][sc]
        if originalColor == newColor:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != originalColor:
                return

            image[r][c] = newColor

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
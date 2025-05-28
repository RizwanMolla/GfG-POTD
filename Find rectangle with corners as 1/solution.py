class Solution:
    def ValidCorner(self, mat):
        n = len(mat)
        if n == 0:
            return False
        m = len(mat[0])
        
        seen = set()
        
        for row in mat:
            for i in range(m):
                if row[i] == 1:
                    for j in range(i + 1, m):
                        if row[j] == 1:
                            # We found a pair of columns with 1s in this row
                            pair = (i, j)
                            if pair in seen:
                                return True
                            seen.add(pair)
        return False

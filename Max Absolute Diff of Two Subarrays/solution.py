class Solution:
    def maxDiffSubArrays(self, a):
        n = len(a)
        if n < 2:
            return 0

        lmx = [0] * n
        lmn = [0] * n
        rmx = [0] * n
        rmn = [0] * n

        cmx = cmn = bmx = bmn = a[0]
        lmx[0] = lmn[0] = a[0]

        for i in range(1, n):
            cmx = max(a[i], cmx + a[i])
            bmx = max(bmx, cmx)
            lmx[i] = bmx

            cmn = min(a[i], cmn + a[i])
            bmn = min(bmn, cmn)
            lmn[i] = bmn

        cmx = cmn = bmx = bmn = a[-1]
        rmx[-1] = rmn[-1] = a[-1]

        for i in range(n - 2, -1, -1):
            cmx = max(a[i], cmx + a[i])
            bmx = max(bmx, cmx)
            rmx[i] = bmx

            cmn = min(a[i], cmn + a[i])
            bmn = min(bmn, cmn)
            rmn[i] = bmn

        ans = 0
        for i in range(n - 1):
            ans = max(
                ans,
                abs(lmx[i] - rmn[i + 1]),
                abs(rmx[i + 1] - lmn[i])
            )

        return ans
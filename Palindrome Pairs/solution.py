class Solution:
    def palindromePair(self, arr):
        arr.sort(key=lambda w: len(w))

        fwd = {}
        bwd = {}

        for w in arr:
            lth = len(w)

            if len(fwd) >= 1:

                cur = bwd

                for ix in range(lth):
                    c = w[ix]

                    if c not in cur:
                        break

                    cur = cur[c]

                if '' in cur:
                    if w[ix:] == w[ix:][::-1]:
                        return True

                cur = fwd

                for ix in range(1, lth + 1):
                    c = w[-ix]

                    if c not in cur:
                        break

                    cur = cur[c]

                if '' in cur:
                    if w[:-ix + 1] == w[:-ix + 1][::-1]:
                        return True

            cur = fwd

            for c in w:
                if c not in cur:
                    cur[c] = {}

                cur = cur[c]

            cur[''] = 1

            cur = bwd

            for c in w[::-1]:
                if c not in cur:
                    cur[c] = {}

                cur = cur[c]

            cur[''] = 1

        return False

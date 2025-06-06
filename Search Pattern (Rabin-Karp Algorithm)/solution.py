class Solution:
    def search(self, pat, txt):
        d = 26  # Number of characters in the input alphabet (lowercase letters)
        q = 101  # A prime number for modulo in hashing

        M = len(pat)
        N = len(txt)
        p = 0  # hash value for pattern
        t = 0  # hash value for text
        h = 1
        result = []

        # The value of h would be "pow(d, M-1)%q"
        for i in range(M - 1):
            h = (h * d) % q

        # Calculate the hash value of pattern and first window of text
        for i in range(M):
            p = (d * p + ord(pat[i]) - ord('a')) % q
            t = (d * t + ord(txt[i]) - ord('a')) % q

        # Slide the pattern over text one by one
        for i in range(N - M + 1):
            # Check the hash values of current window of text and pattern
            if p == t:
                # If the hash values match, then only check characters one by one
                if txt[i:i + M] == pat:
                    result.append(i + 1)  # Using 1-based indexing

            if i < N - M:
                t = (d * (t - (ord(txt[i]) - ord('a')) * h) + (ord(txt[i + M]) - ord('a'))) % q

                if t < 0:
                    t += q

        return result

class Solution:
    def longestValidWord(self, words):
        word_set = set(words)
        words.sort(key=lambda w: (-len(w), w))
        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            if valid:
                return word
        return ""
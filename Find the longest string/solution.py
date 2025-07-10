class Solution():
    def longestString(self, arr):
        word_set = set(arr)
        arr.sort()
        arr.sort(key=len)
        
        valid_words = set()
        longest = ""

        for word in arr:
            if len(word) == 1:
                if word in word_set:
                    valid_words.add(word)
                    if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                        longest = word
            else:
                if word[:-1] in valid_words and word in word_set:
                    valid_words.add(word)
                    if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                        longest = word

        return longest

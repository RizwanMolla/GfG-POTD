# Print Anagrams Together

class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        anagram_map = {}
        for word in arr:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]
        
        return list(anagram_map.values())


"""
Explanation:

The function groups words that are anagrams by sorting each word to determine its canonical form. Words that share the same canonical form are grouped together. A dictionary is used to map the sorted form of words to their corresponding groups, ensuring an efficient O(n . m log m) time complexity, where n is the number of words and m is the average length of the words.
"""
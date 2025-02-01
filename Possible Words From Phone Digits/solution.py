class Solution:
    def possibleWords(self, numbers):
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        result = []
        
        def backtrack(index, current_word):
            if index == len(numbers):
                result.append(current_word)
                return
            current_digit = str(numbers[index])
            for letter in digit_to_letters[current_digit]:
                backtrack(index + 1, current_word + letter)
        
        backtrack(0, "")
        return result
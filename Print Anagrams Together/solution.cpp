#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
  public:
    vector<vector<string>> anagrams(vector<string>& arr) {
        unordered_map<string, vector<string>> anagram_map;
        
        for (const string& word : arr) {
            string sorted_word = word;
            sort(sorted_word.begin(), sorted_word.end());
            anagram_map[sorted_word].push_back(word);
        }
        
        vector<vector<string>> result;
        for (auto& pair : anagram_map) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};
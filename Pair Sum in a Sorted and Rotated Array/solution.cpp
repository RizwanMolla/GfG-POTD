#include <vector>
using namespace std;

class Solution {
public:
    bool pairInSortedRotated(vector<int>& arr, int target) {
        int n = arr.size();
        int i;
        
        for (i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1])
                break;
        }
        
        int l = (i + 1) % n;
        int r = i;

        while (l != r) {
            int current_sum = arr[l] + arr[r];
            if (current_sum == target)
                return true;
            if (current_sum < target)
                l = (l + 1) % n;
            else
                r = (r - 1 + n) % n;
            
            if (l == (r + 1) % n)
                break;
        }

        return false;
    }
};

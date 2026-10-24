''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)

    def merge(self, arr, left, mid, right):
        temp = []
        i, j = left, mid + 1
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
                inv_count += mid - i + 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        arr[left:right + 1] = temp
        return inv_count

    def mergeSort(self, arr, left, right):
        inv_count = 0

        if left < right:
            mid = left + (right - left) // 2
            inv_count += self.mergeSort(arr, left, mid)
            inv_count += self.mergeSort(arr, mid + 1, right)
            inv_count += self.merge(arr, left, mid, right)

        return inv_count

    def pairsViolatingBST(self, root):
        arr = []
        self.inorder(root, arr)
        return self.mergeSort(arr, 0, len(arr) - 1)
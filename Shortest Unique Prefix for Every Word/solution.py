class TrieNode:
    def __init__(self):
        self.arr=[None]*26
        self.freq=0

class Trie:
    def __init__(self):
        self.t=TrieNode()
    
    def insert(self,s):
        node=self.t
        for item in s:
            idx=ord(item)-ord("a")
            if node.arr[idx] is None:
                node.arr[idx]=TrieNode()
            node=node.arr[idx]
            node.freq+=1

class Solution:
    def findPrefixes(self, arr):
        t=Trie()
        for item in arr:
            t.insert(item)
        ans=[]
        for s in arr:
            node=t.t
            curr=""
            for item in s:
                curr+=item
                idx=ord(item)-ord("a")
                node=node.arr[idx]
                if node.freq==1:
                    break
            ans.append(curr)
        return ans
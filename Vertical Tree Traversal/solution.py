'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import defaultdict

class Solution:
    def DFS(self, node, horizontal_distance, min_distance, node_map):
        if node is None:
            return
        
        if horizontal_distance not in node_map:
            node_map[horizontal_distance] = []
        node_map[horizontal_distance].append(node.data)
        
        min_distance[0] = min(min_distance[0], horizontal_distance)
        
        self.DFS(node.left, horizontal_distance - 1, min_distance, node_map)
        self.DFS(node.right, horizontal_distance + 1, min_distance, node_map)

    def verticalOrder(self, root):
        node_map = {}
        min_distance = [0]
        self.DFS(root, 0, min_distance, node_map)
        
        traversal_result = []
        horizontal_distance = min_distance[0]
        
        while horizontal_distance in node_map:
            traversal_result.append(node_map[horizontal_distance])
            horizontal_distance += 1
        
        return traversal_result
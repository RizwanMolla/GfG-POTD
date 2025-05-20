from collections import deque, defaultdict

class Solution:
    def minTime(self, root, target):
        # Step 1: Build parent mapping and find the target node
        parent_map = {}
        target_node = None

        def map_parents(node, parent=None):
            nonlocal target_node
            if not node:
                return
            if node.data == target:
                target_node = node
            if parent:
                parent_map[node] = parent
            map_parents(node.left, node)
            map_parents(node.right, node)

        map_parents(root)

        # Step 2: BFS from target node
        visited = set()
        q = deque()
        q.append(target_node)
        visited.add(target_node)

        time = -1  # we start with -1 because 1st level is time 0

        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                # Check all 3 directions: left, right, and parent
                for neighbor in (curr.left, curr.right, parent_map.get(curr)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            time += 1

        return time
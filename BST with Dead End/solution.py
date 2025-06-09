class Solution:
    def isDeadEnd(self, root):
        """
        Single-pass solution that checks dead end condition
        while traversing with min/max bounds.
        """
        if not root:
            return False
        
        all_nodes = set()
        self._collect_nodes(root, all_nodes)
        
        return self._is_dead_end_helper(root, 1, float('inf'), all_nodes)
    
    def _collect_nodes(self, node, node_set):
        if not node:
            return
        node_set.add(node.data)
        self._collect_nodes(node.left, node_set)
        self._collect_nodes(node.right, node_set)
    
    def _is_dead_end_helper(self, node, min_val, max_val, all_nodes):
        if not node:
            return False
        
        # Check if leaf node is dead end
        if not node.left and not node.right:
            # Check if we can insert node.data-1 or node.data+1
            can_insert_left = (node.data - 1 >= min_val and 
                             node.data - 1 not in all_nodes)
            can_insert_right = (node.data + 1 <= max_val and 
                              node.data + 1 not in all_nodes)
            
            # Dead end if we can't insert either
            if not can_insert_left and not can_insert_right:
                return True
        
        # Recurse with updated bounds
        return (self._is_dead_end_helper(node.left, min_val, node.data - 1, all_nodes) or
                self._is_dead_end_helper(node.right, node.data + 1, max_val, all_nodes))

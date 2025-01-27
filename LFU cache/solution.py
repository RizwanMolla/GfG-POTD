#User function Template for python3

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict


@dataclass
class CacheNode:
    key: int
    value: int
    count: int


class LFUCache:
    def __init__(self, cap: int):
        #code here
        self.cap = cap
        self.key_to_node_map: Dict[int, CacheNode] = {}
        self.count_to_nodes_map: Dict[int, Dict[int, CacheNode]] = defaultdict(dict)
        self.min_count = 0

    def get(self, key: int) -> int:
        #code here
        if key not in self.key_to_node_map:
            return -1

        node = self.key_to_node_map[key]
        del self.count_to_nodes_map[node.count][key]

        node.count += 1
        self.count_to_nodes_map[node.count][key] = node
        if not self.count_to_nodes_map[self.min_count]:
            self.min_count += 1

        return node.value

    def put(self, key: int, value: int) -> None:
        #code here
        if self.cap == 0:
            return

        if key in self.key_to_node_map:
            self.key_to_node_map[key].value = value
            self.get(key)
            return

        if len(self.key_to_node_map) == self.cap:
            lru_key = -1
            for k in self.count_to_nodes_map[self.min_count].keys():
                lru_key = k
                break
            del self.count_to_nodes_map[self.min_count][lru_key]
            del self.key_to_node_map[lru_key]

        new_node = CacheNode(key, value, 1)
        self.count_to_nodes_map[1][key] = self.key_to_node_map[key] = new_node
        self.min_count = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(cap)
# param_1 = obj.get(key)
# obj.put(key,value)